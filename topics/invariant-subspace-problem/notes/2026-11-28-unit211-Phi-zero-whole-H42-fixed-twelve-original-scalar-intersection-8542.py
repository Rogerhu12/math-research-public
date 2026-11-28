#!/usr/bin/env python3
"""NEW whole-H42 original fixed12 scalar-intersection witness.
Use the already-paid whole-Phi C6 and the saved original P6 with
P6*D in I4. Define the fixed6/6 Sylvester determinant G universally,
without expanding it over QQ. At the FIRST H42 point eligible only
by original weight units and the P6 leading coefficient, compute
the actual12 determinant and lambda Bezout. If nonzero, p-Gauss
and the already-paid QQ irreducibility of H42 imply H42 does not
divide G, hence the entire H42 physical-D-nonzero weight set is
finite. All H19-zero fibers remain in the universal G condition.
No old cofactor/factor/rank/norm/projective gate is repeated.
120 seconds /1 GiB inclusive of necessary source prefixes.
2026-11-28 Asia/Taipei.
"""
import os,time,json,hashlib,zlib,base64,signal,resource,contextlib,io,math
from pathlib import Path
from flint import fmpq,nmod_poly
START=time.perf_counter();DEADLINE=START+120
signal.setitimer(signal.ITIMER_REAL,120)
resource.setrlimit(resource.RLIMIT_AS,(1024**3,1024**3))
def say(stage,**kw):
 kw.update(stage=stage,seconds=time.perf_counter()-START)
 print(json.dumps(kw,separators=(",",":")),flush=True)
name="2026-11-28-unit211-Phi-zero-centered-original-NSPS-cofactor-content-and-leading-support-8542.py"
path=Path(os.environ.get("ISP_PHI_CENTERED_NSPS_SOURCE",str(Path(__file__).with_name(name))))
raw=path.read_bytes()
assert hashlib.sha256(raw).hexdigest()=="baaac1d2cb05437b6c771856aea8991692cad5ff62276e6bce12584d15da8ca6"
mark=b"\nfor j in range(3):\n rhs=R(primitive) if j==0 else R()\n"
assert raw.count(mark)==1
prefix=raw.split(mark)[0];assert len(prefix)==6125
assert hashlib.sha256(prefix).hexdigest()=="4b152304c41026c94b93147d1360644217c5f15fff88e30264d2e7b02ae6b31d"
sc={"__file__":str(path),"__name__":"new_whole_H42_two_original_scalar_definitions"}
oa=signal.alarm;ot=signal.setitimer
def bounded_timer(which,seconds,interval=0):
 if which!=signal.ITIMER_REAL:return ot(which,seconds,interval)
 left=max(.001,DEADLINE-time.perf_counter())
 return ot(which,min(left,float(seconds) if seconds>0 else left),0)
def bounded_alarm(seconds):return math.ceil(bounded_timer(signal.ITIMER_REAL,seconds)[0])
signal.alarm=bounded_alarm;signal.setitimer=bounded_timer
try:
 with contextlib.redirect_stdout(io.StringIO()):
  exec(compile(prefix,str(path)+":only-original-C6-definition","exec"),sc)
finally:
 signal.alarm=oa;signal.setitimer=ot
 ot(signal.ITIMER_REAL,max(.001,DEADLINE-time.perf_counter()))
ctx,zero,geo,profile,C6=[sc[x] for x in ["ctx","zero","geo","profile","primitive"]]
def lcoeff(poly):
 out=[zero for _ in range(7)]
 for ex,c in poly.to_dict().items():
  assert not ex[3] and not ex[4] and 0<=ex[2]<=6
  out[int(ex[2])]+=ctx.from_dict({(int(ex[0]),int(ex[1]),0,0,0):c})
 return out
cc=lcoeff(C6);assert cc[6]
H42,paid,removed=geo["strip_paid"](cc[6],False)
assert H42*paid==cc[6]
assert profile(H42)["sha256"]=="1988b732b97dfdded9386c97d261774e6cc4d7e8db659f211faa54961c67a8e7"
# Historical coefficients are read only in the runner. No payload is
# printed, copied into this source, or written to repository files.
saved_name="2026-11-27-unit211-Phi-zero-first-quadratic-head-actual-D-core-exact-input-8542.json"
saved_path=Path(os.environ.get("ISP_PHI_SAVED_P6_JSON",str(Path(__file__).with_name(saved_name))))
saved_raw=saved_path.read_bytes()
assert hashlib.sha256(saved_raw).hexdigest()=="7cc9dcf4c8f716055518324966cf8c156c961c5204dfb156ede054f63568765b"
record=json.loads(saved_raw)["polynomial"]
payload=zlib.decompress(base64.b64decode(record["data"]))
assert len(payload)==record["uncompressedBytes"]==86039
assert hashlib.sha256(payload).hexdigest()==record["payloadSha256"]=="9e50cc2a30cf8500b7bef25f8e579334c2b46f8d896662759cdc0ec85f35542c"
obj=json.loads(payload)
assert obj["variables"]==["u","Q","lambda"] and len(obj["terms"])==3101
terms={}
for ex,c in obj["terms"]:
 e=tuple(map(int,ex))+(0,0);assert e not in terms
 terms[e]=fmpq(c)
P6=ctx.from_dict(terms);pc=lcoeff(P6)
assert int(P6.degrees()[2])==6 and pc[6]
p=1009
assert all(p%d for d in range(2,math.isqrt(p)+1))
def pair(q):
 ab=str(q).split("/")
 return int(ab[0]),int(ab[1]) if len(ab)>1 else 1
def vp(a):
 if not a:return 10**9
 a=abs(a);v=0
 while a%p==0:a//=p;v+=1
 return v
pv=min(vp(pair(x)[0])-vp(pair(x)[1]) for x in H42.to_dict().values() if x)
scale=fmpq(p**(-pv)) if pv<=0 else fmpq(1,p**pv)
HG=H42*scale
def qmod(q):
 a,b=pair(q);assert b%p
 return (a%p)*pow(b%p,-1,p)%p
# True integral coefficients of the entire fixed Sylvester input.
for poly in [P6,C6,HG]:
 for x in poly.to_dict().values():qmod(x)
assert any(qmod(x) for x in HG.to_dict().values())
def value(poly,u,q):
 ans=0
 for ex,c in poly.to_dict().items():
  assert not any(ex[2:])
  ans=(ans+qmod(c)*pow(u,int(ex[0]),p)*pow(q,int(ex[1]),p))%p
 return ans
# Fixed Sylvester columns: lambda^j P6,lambda^j C6,0<=j<6.
# Compute a complete total-degree assignment bound, without a QQ
# determinant expansion. Zero coefficients are genuinely absent.
N=12
coeff=[[zero for _ in range(N)] for _ in range(N)]
for j in range(6):
 for k in range(7):
  coeff[k+j][j]=pc[k];coeff[k+j][6+j]=cc[k]
weights=[[int(x.total_degree()) if x else -1 for x in row] for row in coeff]
BIG=10**8
cost=[[(-w if w>=0 else BIG) for w in row] for row in weights]
aa=[0]*(N+1);bb=[0]*(N+1);match=[0]*(N+1);way=[0]*(N+1)
for i in range(1,N+1):
 match[0]=i;j0=0;minv=[BIG*10]*(N+1);used=[False]*(N+1)
 while True:
  used[j0]=True;i0=match[j0];delta=BIG*10;j1=0
  for j in range(1,N+1):
   if not used[j]:
    cur=cost[i0-1][j-1]-aa[i0]-bb[j]
    if cur<minv[j]:minv[j]=cur;way[j]=j0
    if minv[j]<delta:delta=minv[j];j1=j
  assert j1
  for j in range(N+1):
   if used[j]:aa[match[j]]+=delta;bb[j]-=delta
   else:minv[j]-=delta
  j0=j1
  if not match[j0]:break
 while True:
  j1=way[j0];match[j0]=match[j1];j0=j1
  if not j0:break
perm=[None]*N
for j in range(1,N+1):perm[match[j]-1]=j-1
rows=[-aa[i+1] for i in range(N)];cols=[-bb[j+1] for j in range(N)]
upper=sum(rows)+sum(cols)
assert all(weights[i][perm[i]]>=0 for i in range(N))
assert upper==sum(weights[i][perm[i]] for i in range(N))
for i in range(N):
 for j in range(N):
  if weights[i][j]>=0:assert weights[i][j]<=rows[i]+cols[j]
say("new_whole_H42_fixed_original12_definition",
 H42=profile(H42),H42pGaussConstantExponent=-pv,
 wholeP6=profile(P6),wholeC6=profile(C6),
 fixedLambdaDegrees=[6,6],fixedSylvesterSize=12,
 trueQQTotalDegreeUpperBound=upper,
 totalDegreeAssignment=perm,totalDegreeDualRows=rows,totalDegreeDualColumns=cols,
 allGlobalQQCoefficients1009Integral=True,
 QQH42IrreducibilityAlreadyPaidNotRecomputed=True,
 universalOriginalIdentity="D*G in I10, since P6*D in I4 and C6 in I10",
 originalP6CofactorNotReplayed=True)
# A first H42 point is selected by input units only. No rank,
# resultant or gcd value is considered during point selection.
chosen=None;hroots=0;bad_counts={}
for u0 in range(3,33):
 qco=[0]*(int(HG.degrees()[1])+1)
 for ex,c in HG.to_dict().items():
  qco[int(ex[1])]=(qco[int(ex[1])]+qmod(c)*pow(u0,int(ex[0]),p))%p
 if not any(qco):
  bad_counts["whole_H42_mod_vertical_slice"]=bad_counts.get("whole_H42_mod_vertical_slice",0)+1
  continue
 for q0 in range(p):
  hh=0
  for x in reversed(qco):hh=(hh*q0+x)%p
  if hh:continue
  hroots+=1;bad=[]
  for label,poly in geo["paid"]:
   if not value(poly,u0,q0):bad.append("old_unit:"+label)
  if not value(pc[6],u0,q0):bad.append("P6_lambda6_head")
  if bad:
   for k in bad:bad_counts[k]=bad_counts.get(k,0)+1
   continue
  chosen=(u0,q0);break
 if chosen is not None:break
if chosen is None:
 say("new_whole_H42_no_eligible_fixed_input_point",
     prime=p,testedU=[3,32],H42RootsEncountered=hroots,
     rejectedInputCounts=bad_counts,noIntersectionClaim=True,
     wholeH42ZeroRetained=True,wholePhiExcluded=False)
 signal.setitimer(signal.ITIMER_REAL,0);raise SystemExit(0)
u0,q0=chosen
f=nmod_poly([value(x,u0,q0) for x in pc],p)
g=nmod_poly([value(x,u0,q0) for x in cc],p)
assert value(HG,u0,q0)==0 and int(f.degree())==6 and int(g.degree())<=5
gd,s,t=f.xgcd(g)
assert s*f+t*g==gd
S=[[value(coeff[i][j],u0,q0) for j in range(N)] for i in range(N)]
A=[row[:] for row in S];det=1;rank=0
for j in range(N):
 k=next((i for i in range(j,N) if A[i][j]),None)
 if k is None:det=0;break
 if k!=j:A[k],A[j]=A[j],A[k];det=-det
 v=A[j][j];det=det*v%p;iv=pow(v,-1,p);rank+=1
 for i in range(j+1,N):
  mul=A[i][j]*iv%p
  if mul:
   for k in range(j,N):A[i][k]=(A[i][k]-mul*A[j][k])%p
det%=p
assert bool(det)==(int(gd.degree())==0)
proved=bool(det)
def modprofile(poly):
 c=[int(x) for x in poly.coeffs()]
 return dict(degree=int(poly.degree()),sha256=hashlib.sha256(json.dumps(c,separators=(",",":")).encode()).hexdigest())
say("new_whole_H42_true_original_fixed12_point_return",
 prime=p,point=[u0,q0],H42ModValue=0,
 oldWeightUnitsAndP6HeadCheckedBeforeTest=True,
 H42RootsEncounteredBeforeChoice=hroots,rejectedInputCounts=bad_counts,
 actualP6Degree=int(f.degree()),actualC6Degree=int(g.degree()),
 originalLambdaGCD=modprofile(gd),
 originalBezoutMultipliers=[modprofile(s),modprofile(t)],
 completeLambdaBezoutReturned=True,
 fixed12EliminationPivotsBeforeStop=rank,fixed12SylvesterDeterminant=det,
 H42DoesNotDivideOriginalQQGProved=proved,
 QQH42AndOriginalGCoprimeProved=proved,
 entireH42PhysicalWeightSupportFiniteProved=proved,
 entireH42DifferentComplexWeightPointUpperBound=42*upper if proved else None,
 globalQQGTotalDegreeUpperBound=upper,
 wholeH19ZeroFibersIncludedInUniversalCondition=True,
 noFpFactorIdentifiedAsQQBranch=True,
 originalDNotInvertedInComputation=True,
 noNewPhysicalWeightParameterUnit=True,
 wholePhiExcluded=False,ordinaryISPClaim=False,
 noRecomputablePolynomialOrMatrixPayloadSaved=True,
 peakRSSKiB=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
signal.setitimer(signal.ITIMER_REAL,0)
