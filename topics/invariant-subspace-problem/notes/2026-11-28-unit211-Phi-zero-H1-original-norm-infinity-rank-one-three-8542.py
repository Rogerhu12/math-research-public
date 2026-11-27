#!/usr/bin/env python3
"""NEW exact infinity rank-one/rank-three model for the fixed original H1 norm.
Reconstruct only the two original QQ lambda-six input cofactors from the
0ea9 necessary prefix, never its modular norms or F6/NV tails.
t=1/u,q=t^2 Q gives g_infty(0,q)=q(q^3-3q^2+13q-12).
Construct the actual QQ Hensel simple branch and monic cubic by complete
truncated products. The two full fixed Sylvester regular matrices have
orders 12 and 36. Laurent coefficient orders give complete assignment
duals; a constant QQ left-kernel replacement of determinant one and exact
t division pays any remaining valuation within retained precision.
No parameter pivot is inverted, no infinite component is dropped, and
incomplete precision is reported as a bound, not an exact degree.
120s /1GiB, 2026-11-28 Asia/Taipei. No coefficient payload or old norm replay.
"""
import os,time,json,hashlib,signal,resource,contextlib,io
from pathlib import Path
from flint import fmpq,fmpq_poly,fmpq_mat
started=time.perf_counter();deadline=started+120
signal.alarm(120);resource.setrlimit(resource.RLIMIT_AS,(1024**3,1024**3))
PREC=192;prime=1009
def say(stage,**kw):
 kw.update(stage=stage,seconds=time.perf_counter()-started)
 print(json.dumps(kw,separators=(",",":")),flush=True)
path=Path(os.environ.get("ISP_H1_POLYNOMIAL_V_SOURCE",
 str(Path(__file__).with_name("2026-11-28-unit211-Phi-zero-H1-polynomial-v-source-scaled-matrices-fixed-norm-input-8542.py"))))
raw=path.read_bytes()
assert hashlib.sha256(raw).hexdigest()=="5f6ba628dd4a660a7cedc7bb338a7cebc9cdc1ac3b6d6958a36409cb578b00ef"
text=raw.decode()
driver="\nall_projections=[];all_names=[];all_modular_returns=[];common=None"
assert text.count(driver)==1
text=text.split(driver,1)[0]
a=text.index("\n DD=ell*A2-Tr*Tr;B3=")
b=text.index("\n return cleared,extras,units",a)+len("\n return cleared,extras,units")
text=text[:a]+"\n return cleared,[],units"+text[b:]
text=text.replace('  headNorm= pdigest(polynomial_norm(head)),\n',"")
ns={"__file__":str(path),"__name__":"__two_original_lambda_six_inputs_for_NEW_infinity_model__"}
with contextlib.redirect_stdout(io.StringIO()):
 exec(compile(text,str(path)+"::<new-infinity-only>","exec"),ns)
 gen=ns["whole_polynomial_module"]()
 projections,names=next(gen)
assert len(projections)==2 and [f.degree() for f in projections]==[6,6]
defs=[ns["pprofile"](ns["UtoP"](f)) for f in projections]
assert [d["sha256"] for d in defs]==[
 "1a9c37f94927e25028b2ee69e87821c9b2c2c00c449f4ac9d02ca84f9696b1d7",
 "acec51cd259279242643603b882ee30cecd9dfdea4e7ae3ddd301ed686a5f7ef"]
signal.setitimer(signal.ITIMER_REAL,max(.001,deadline-time.perf_counter()))
def pol(v=()):
 if isinstance(v,fmpq_poly):return v
 if isinstance(v,(int,fmpq)):v=[v]
 return fmpq_poly([fmpq(c) for c in v])
zero=pol();one=pol(1);tt=pol([0,1])
def trunc(p,n):return pol(p.coeffs()[:n])
def prod(a,b,n=PREC):return trunc(a*b,n)
def series_inverse(a,n):
 assert a[0]
 b=pol(1/a[0]);k=1
 while k<n:
  k=min(2*k,n);b=trunc(b*(2-a*b),k)
 assert trunc(a*b,n)==one
 return b
def evaluate(coeffs,v,n):
 out=zero
 for c in reversed(coeffs):out=trunc(out*v+c,n)
 return out
def ord0(p,n):
 for i in range(min(len(p.coeffs()),n)):
  if p[i]:return i
 return n
# g_infty=t^8*g(1/t,q/t^2); every exponent is nonnegative.
ginfty=[]
for j,c in enumerate(ns["g"]):
 out=[fmpq(0)]*(9-2*j)
 for k,co in enumerate(c.coeffs()):
  exponent=8-2*j-k;assert exponent>=0
  out[exponent]+=co
 ginfty.append(pol(out))
assert [g[0] for g in ginfty]==[0,-12,13,-3,1]
N0=PREC+2
q0=zero;k=1
while k<N0:
 k=min(2*k,N0)
 value=evaluate(ginfty,q0,k)
 derivative=evaluate([(j+1)*ginfty[j+1] for j in range(4)],q0,k)
 q0=trunc(q0-value*series_inverse(derivative,k),k)
 assert not evaluate(ginfty,q0,k)
assert q0[0]==0 and q0[1]==0 and q0[2]==fmpq(4,3)
cubic=[zero,zero,zero,one]
for j in range(3,0,-1):cubic[j-1]=trunc(ginfty[j]+q0*cubic[j],N0)
assert trunc(ginfty[0]+q0*cubic[0],N0)==zero
for j in range(1,4):
 assert trunc(cubic[j-1]-q0*cubic[j]-ginfty[j],N0)==zero
assert cubic[3]==one
assert [c[0] for c in cubic]==[-12,13,-3,1]
Qsmall=pol(q0.coeffs()[2:])
assert Qsmall[0]==fmpq(4,3)
say("new_H1_complete_QQ_infinity_rank_one_three_model",
 retainedCoefficientPrecision=PREC,
 actualSimpleRootHenselProductsReturned=True,
 actualMonicCubicDivisionProductsReturned=True,
 completeInitialFactors="q and q^3-3q^2+13q-12",
 simpleBranchQConstant="4/3",cubicDiscriminant=-4027,
 firstResultantInputs=defs,oldModularNormTailExecuted=False,
 bothInfinityComponentsAndAllThreeCubicEmbeddingsRetained=True)
def regular_cubic(vv):
 def reduce_q(cc):
  cc=list(cc)
  while len(cc)<3:cc.append(zero)
  original=cc[:];quot=[zero for _ in range(max(0,len(cc)-3))]
  for j in range(len(cc)-1,2,-1):
   co=cc[j];quot[j-3]=trunc(quot[j-3]+co,PREC)
   for h in range(3):cc[j-3+h]=trunc(cc[j-3+h]-co*cubic[h],PREC)
   cc[j]=zero
  returned=cc[:]
  for j,co in enumerate(quot):
   for h in range(4):returned[j+h]=trunc(returned[j+h]+co*cubic[h],PREC)
  assert all(trunc(a-b,PREC)==zero for a,b in zip(returned,original))
  return cc[:3]
 cols=[reduce_q([zero]*j+vv[:]) for j in range(3)]
 return [[cols[j][i] for j in range(3)] for i in range(3)]
def coefficient_model(a,branch):
 assert a.d==one
 if not a:return None
 if branch=="small":
  D=max(int(n.degree()) for n in a.n if n)
  powers=[one,Qsmall,prod(Qsmall,Qsmall),prod(prod(Qsmall,Qsmall),Qsmall)]
  value=zero
  for j,nn in enumerate(a.n):
   pp=[fmpq(0)]*(D+1)
   for k,c in enumerate(nn.coeffs()):pp[D-k]+=c
   value=trunc(value+pol(pp)*powers[j],PREC)
  return ([[value]],D)
 D=max(int(nn.degree())+2*j for j,nn in enumerate(a.n) if nn)
 vv=[zero,zero,zero]
 for j,nn in enumerate(a.n):
  pp=[fmpq(0)]*(D+1)
  for k,c in enumerate(nn.coeffs()):
   exponent=D-k-2*j;assert exponent>=0
   pp[exponent]+=c
  pp=pol(pp)
  if j<3:vv[j]=trunc(vv[j]+pp,PREC)
  else:
   for h in range(3):vv[h]=trunc(vv[h]-pp*cubic[h],PREC)
 return (regular_cubic(vv),D)
def max_assignment(weights):
 n=len(weights);BIG=10**8
 costs=[[BIG if d is None else -d for d in row] for row in weights]
 pu=[0]*(n+1);pv=[0]*(n+1);matching=[0]*(n+1);way=[0]*(n+1)
 for i in range(1,n+1):
  matching[0]=i;j0=0;dist=[BIG*n]*(n+1);seen=[False]*(n+1)
  while True:
   seen[j0]=True;i0=matching[j0];best=BIG*n;j1=0
   for j in range(1,n+1):
    if not seen[j]:
     cur=costs[i0-1][j-1]-pu[i0]-pv[j]
     if cur<dist[j]:dist[j]=cur;way[j]=j0
     if dist[j]<best:best=dist[j];j1=j
   for j in range(n+1):
    if seen[j]:pu[matching[j]]+=best;pv[j]-=best
    else:dist[j]-=best
   j0=j1
   if matching[j0]==0:break
  while True:
   j1=way[j0];matching[j0]=matching[j1];j0=j1
   if not j0:break
 assignment=[0]*n
 for j in range(1,n+1):assignment[matching[j]-1]=j-1
 if any(weights[i][assignment[i]] is None for i in range(n)):
  return None
 r=[-pu[i] for i in range(1,n+1)];c=[-pv[j] for j in range(1,n+1)]
 bound=sum(r)+sum(c)
 assert bound==sum(weights[i][assignment[i]] for i in range(n))
 assert all(w is None or r[i]+c[j]>=w for i,row in enumerate(weights) for j,w in enumerate(row))
 return bound,r,c
def branch_matrix(branch):
 rank=1 if branch=="small" else 3
 f,h=projections;m=f.degree();n=h.degree();size=rank*(m+n)
 caches=[[coefficient_model(a,branch) for a in pp.c] for pp in projections]
 blocks=[]
 for which,ff,shifts in [(0,f,n),(1,h,m)]:
  for shift in range(shifts):
   blocks.append([caches[which][k-shift] if 0<=k-shift<=ff.degree() else None for k in range(m+n)])
 entries=[];weights=[]
 for i in range(size):
  er=[];wr=[]
  for j in range(size):
   mm=blocks[j//rank][i//rank]
   if mm is None:er.append(None);wr.append(None);continue
   poly=mm[0][i%rank][j%rank];D=mm[1]
   er.append((poly,D));wr.append(D-ord0(poly,PREC))
  entries.append(er);weights.append(wr)
 result=max_assignment(weights)
 if result is None:
  say("accurate_new_H1_infinity_structural_singular_branch",branch=branch,exactDegreePaid=False)
  return None
 bound,rd,cd=result
 precision=min(PREC+rd[i]+cd[j]-e[1]
               for i,row in enumerate(entries) for j,e in enumerate(row) if e is not None)
 if precision<=0:
  say("accurate_new_H1_infinity_insufficient_entry_precision",branch=branch,
      LaurentPoleUpperBound=bound,retainedPrecision=precision,exactDegreePaid=False)
  return None
 matrix=[]
 for i,row in enumerate(entries):
  rr=[]
  for j,e in enumerate(row):
   if e is None:rr.append(zero);continue
   poly,D=e;shift=rd[i]+cd[j]-D
   if shift>=0:value=pol([0]*shift+poly.coeffs())
   else:
    assert all(poly[k]==0 for k in range(-shift))
    value=pol(poly.coeffs()[-shift:])
   rr.append(trunc(value,precision))
  matrix.append(rr)
 say("new_H1_infinity_branch_complete_dual_normalization",
     branch=branch,fullFixedMatrixOrder=size,LaurentPoleUpperBound=bound,
     rowDual=rd,columnDual=cd,retainedUniformPrecision=precision,
     completeAssignmentDualAndEntryDivisionsReturned=True,
     noBranchOrEmbeddingDropped=True)
 return matrix,precision,bound
def constant_matrix(matrix):
 return fmpq_mat([[p[0] for p in row] for row in matrix])
def extract_valuation(branch,matrix,precision,bound):
 n=len(matrix);E=0;rounds=0;history=[]
 while precision>0:
  c0=constant_matrix(matrix);det=c0.det()
  if det:
   den=int(det.denominator)%prime
   residue=(int(det.numerator)%prime*pow(den,-1,prime)%prime) if den else None
   raw=str(det).encode()
   answer=dict(branch=branch,matrixOrder=n,initialLaurentPoleBound=bound,
     exactExtractedOrder=E,exactInfinityPoleDegree=bound-E,
     remainingPrecision=precision,constantKernelRounds=rounds,
     exactLeadingCoefficientIdentity=dict(bytes=len(raw),sha256=hashlib.sha256(raw).hexdigest()),
     leadingCoefficientIntegralAt1009=bool(den),
     leadingCoefficientMod1009=residue,
     exactDegreePaid=True,allDeterminantOneRowTransformsAndDivisionsReturned=True)
   say("new_H1_infinity_branch_exact_characteristic_zero_return",**answer)
   return answer
  transpose=fmpq_mat([[matrix[j][i][0] for j in range(n)] for i in range(n)])
  reduced,rank=transpose.rref()
  pivots=[]
  for i in range(rank):
   j=next(j for j in range(n) if reduced[i,j])
   assert reduced[i,j]==1;pivots.append(j)
  free=[j for j in range(n) if j not in pivots]
  assert len(free)==n-rank and free
  if precision<=1:
   say("accurate_new_H1_infinity_precision_exhausted",branch=branch,
     extractedOrderLowerBound=E+len(free),remainingPoleUpperBound=bound-E-len(free),
     exactDegreePaid=False)
   return dict(branch=branch,exactDegreePaid=False)
  N=[[fmpq(0) for _ in range(n)] for _ in range(n)]
  kernels=[]
  for j in free:
   vec=[fmpq(0) for _ in range(n)];vec[j]=1
   for k,i in enumerate(pivots):vec[i]=-reduced[k,j];N[j][i]=vec[i]
   assert all(sum((vec[i]*matrix[i][k][0] for i in range(n)),fmpq(0))==0 for k in range(n))
   kernels.append((j,vec))
  nn=fmpq_mat(N);eye=fmpq_mat([[1 if i==j else 0 for j in range(n)] for i in range(n)])
  assert nn*nn==fmpq_mat(n,n)
  assert (eye+nn)*(eye-nn)==eye
  updated=[row[:] for row in matrix]
  for j,vec in kernels:
   updated[j]=[sum((matrix[i][k]*vec[i] for i in range(n) if vec[i]),zero) for k in range(n)]
   assert all(not c[0] for c in updated[j])
   updated[j]=[pol(c.coeffs()[1:]) for c in updated[j]]
  precision-=1
  matrix=[[trunc(p,precision) for p in row] for row in updated]
  E+=len(free);rounds+=1
  history.append(dict(nullity=len(free),extractedOrder=E,precision=precision))
  say("new_H1_infinity_actual_constant_kernel_extraction",
   branch=branch,round=rounds,constantRank=int(rank),actualZeroRows=len(free),
   exactExtractedOrder=E,uniformPrecision=precision,
   completeLeftKernelProductsReturned=True,
   rowTransformIsIdentityPlusSquareZero=True,
   determinantExactlyOne=True,allEntryDivisionsByTActuallyReturned=True)
 return dict(branch=branch,exactDegreePaid=False)
answers=[]
for branch in ["small","large"]:
 data=branch_matrix(branch)
 if data is None:answers.append(dict(branch=branch,exactDegreePaid=False));continue
 answers.append(extract_valuation(branch,*data))
complete=all(x["exactDegreePaid"] for x in answers)
degree=sum(x["exactInfinityPoleDegree"] for x in answers) if complete else None
same=complete and degree==3179 and all(x["leadingCoefficientMod1009"] not in (None,0) for x in answers)
say("new_H1_original_fixed_norm_exact_infinity_finished",
 sourceSHA256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
 exactRankOneRankThreeSplittingReturned=True,branches=answers,
 completeQQNormDegreePaid=complete,exactQQNormDegree=degree,
 previouslyActualMod1009Degree=3179,
 fullQQDegree3179AndModularLeadingKept=same,
 firstFixedOriginalNormOnly=True,oldFullNormComputationReplayed=False,
 P201CoefficientsKnown=False,newP201ExclusionClaim=False,
 coefficientPayloadTransmitted=False,encodedOrSplitPayload=False,
 ordinaryISPClaim=False,
 peakRSSKiB=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
signal.alarm(0)
