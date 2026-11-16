#!/usr/bin/env python3
"""Exact original symmetric pencil for the complete rank-three mean exception.
Author: Astra-ISP-789f / normal_annihilator. AI-assisted: GPT-6 Astra Pro.
Date: 2026-11-16. Only fixed E constants are changed; all pencil parameters remain.
"""
import argparse,gzip,hashlib,itertools,json,math,os,resource,signal,sys,time
from pathlib import Path
from flint import fmpq,fmpq_poly,fmpq_mat,fmpz_mat
sys.set_int_max_str_digits(0)
FORMAT="r150-original-mean-rank-three-exact-pencil-v1"
PIN={"bytes":2208219,"sha256":"1928d85c9cb6a40cbbf038e39d65bd0b72dffe900d0da6c600070966444acc12","logicalBytes":4478284,"logicalSha256":"7c37ad0846331a5ad9bf96d7c0086e2c65d65fe8831081dc34c778365592197d","binding":"2c120983a234d63f52e19d0f81a8f486b3d5dad5ca010f1ad74ebe9c7045e7f0"}
F=[52565262336,6080833024,-43931504,3725]
MOD=fmpq_poly([fmpq(x,F[-1]) for x in F]);ZERO=fmpq_poly();ONE=fmpq_poly([1]);P=127;ROOT=100
def need(b,s):
 if not b:raise ValueError(s)
def sha(b):return hashlib.sha256(b).hexdigest()
def canon(x):return json.dumps(x,sort_keys=True,separators=(",",":")).encode()
def save(p,x,gz=False):
 b=canon(x) if gz else json.dumps(x,sort_keys=True,indent=2).encode()
 z=gzip.compress(b,compresslevel=1,mtime=0) if gz else b
 q=p.with_name(p.name+".tmp");q.write_bytes(z);os.replace(q,p)
 d={"path":p.name,"bytes":len(z),"sha256":sha(z)}
 if gz:d.update(logicalBytes=len(b),logicalSha256=sha(b))
 return d
def fv(x):return [str(x[k]) for k in range(3)]
def reduceq(q):
 need(int(q.denom())%P!=0,"every original coefficient has a127-unit denominator")
 return int(q.numer())%P*pow(int(q.denom())%P,-1,P)%P
def residue(x):return sum(reduceq(x[k])*pow(ROOT,k,P) for k in range(3))%P
def height(x):
 return max([abs(int(x[k].numer())).bit_length() for k in range(3)]+[int(x[k].denom()).bit_length() for k in range(3)])
def rank(rows):
 a=[r[:] for r in rows];r=0
 for c in range(len(a[0]) if a else 0):
  p=next((j for j in range(r,len(a)) if a[j][c]),None)
  if p is None:continue
  a[r],a[p]=a[p],a[r];v=pow(a[r][c],-1,P);a[r]=[x*v%P for x in a[r]]
  for i in range(len(a)):
   if i!=r:
    v=a[i][c]
    if v:a[i]=[(x-v*y)%P for x,y in zip(a[i],a[r])]
  r+=1
 return r
def determinant_field(a):
 a=[r[:] for r in a];ans=1
 for k in range(len(a)):
  j=next((i for i in range(k,len(a)) if a[i][k]),None)
  if j is None:return 0
  if j!=k:a[k],a[j]=a[j],a[k];ans=-ans
  q=a[k][k];ans=ans*q%P
  inv=pow(q,-1,P)
  for i in range(k+1,len(a)):
   f=a[i][k]*inv%P
   for j in range(k+1,len(a)):a[i][j]=(a[i][j]-f*a[k][j])%P
 return ans%P
def main():
 ap=argparse.ArgumentParser();ap.add_argument("--six-out",required=True);ap.add_argument("--out",required=True)
 ap.add_argument("--seconds",type=float,default=180);ap.add_argument("--memory-mib",type=int,default=768)
 a=ap.parse_args();need(0<a.seconds<=600 and 256<=a.memory_mib<=2048,"bounded exact pencil parameters")
 resource.setrlimit(resource.RLIMIT_AS,(a.memory_mib*1024**2,)*2)
 out=Path(a.out);out.mkdir(parents=True,exist_ok=True);start=time.monotonic()
 source=sha(Path(__file__).read_bytes());binding=sha(canon({"format":FORMAT,"source":source,"pin":PIN}))
 rec={"format":FORMAT,"binding":binding,"sourceSha256":source,"parameters":{"seconds":a.seconds,"memoryMiB":a.memory_mib}}
 def event(n):
  rec["parameters"]["lastCompletedPhase"]=n
  print(json.dumps({"phase":n,"elapsedSeconds":time.monotonic()-start,"maxResidentKiB":resource.getrusage(resource.RUSAGE_SELF).ru_maxrss}),flush=True)
 def timeout(s,f):raise TimeoutError("bounded full-original pencil computation")
 signal.signal(signal.SIGALRM,timeout);signal.setitimer(signal.ITIMER_REAL,a.seconds);code=1
 try:
  raw=(Path(a.six_out)/"complete-original-four-mean-quadratic-matrices.json.gz").read_bytes()
  need(len(raw)==PIN["bytes"] and sha(raw)==PIN["sha256"],"complete original tensor compressed bytes")
  z=gzip.decompress(raw);need(len(z)==PIN["logicalBytes"] and sha(z)==PIN["logicalSha256"],"complete original tensor logical bytes")
  x=json.loads(z);need(x["binding"]==PIN["binding"],"same original tensor binding");d=x["data"]
  T=[[[fmpq_poly([fmpq(v) for v in x]) for x in row] for row in t] for t in d["matrices"]]
  need(len(T)==4 and all(len(t)==6 and all(len(row)==6 for row in t) for t in T),"all4 original6square matrices")
  for t in T:
   for i in range(6):
    for j in range(6):need(t[i][j]==t[j][i],"all144 original symmetric entries")
  need(sum(F[i]*pow(ROOT,i,P) for i in range(4))%P==0,"same legal matched127 embedding")
  coords=list(itertools.combinations_with_replacement(range(6),2))
  A=[[T[k][i][j] for k in range(4)] for i,j in coords]
  Ap=[[residue(x) for x in row] for row in A]
  selected=[]
  for i in range(21):
   if rank([Ap[j] for j in selected+[i]])>len(selected):selected.append(i)
   if len(selected)==4:break
  need(len(selected)==4,"complete four-dimensional original symmetric pencil")
  U=[A[i] for i in selected];q=fmpq_mat(12,12);rhs=fmpq_mat(12,4)
  for i in range(4):
   for j in range(4):
    for k in range(3):
     z=U[i][j]*fmpq_poly([0]*k+[1])%MOD
     for l in range(3):q[3*i+l,3*j+k]=z[l]
  for i in range(4):rhs[3*i,i]=1
  t=time.monotonic();sol=q.solve(rhs,algorithm="dixon");rec["parameters"]["constantSolveSeconds"]=time.monotonic()-t
  V=[[fmpq_poly([sol[3*i+l,j] for l in range(3)]) for j in range(4)] for i in range(4)]
  cand=save(out/"complete-original-pencil-constant-inverse-candidate.json.gz",{"format":FORMAT+"-candidate","binding":binding,"data":{
   "originalSymmetricCoordinates":coords,"selectedOriginalCoordinateRows":selected,"unit":[[fv(x) for x in row] for row in U],
   "inverse":[[fv(x) for x in row] for row in V],"savedBeforeVerification":True}},True)
  rec["parameters"]["inverseCandidate"]=cand;event("complete-original-pencil-unit-candidates-saved")
  invcount=0
  for B,C in [(U,V),(V,U)]:
   for i in range(4):
    for j in range(4):
     need(sum((B[i][k]*C[k][j] for k in range(4)),ZERO)%MOD==fmpq_poly([int(i==j)]),"all32 complete original constant inverse products");invcount+=1
  N=[[sum((A[i][k]*V[k][j] for k in range(4)),ZERO)%MOD for j in range(4)] for i in range(21)]
  check=0
  for i in range(21):
   for j in range(4):
    need(sum((N[i][k]*U[k][j] for k in range(4)),ZERO)%MOD==A[i][j],"all84 original full pencil coordinates multiply back");check+=1
  for i in range(4):
   need(N[selected[i]]==[fmpq_poly([int(i==j)]) for j in range(4)],"all16 canonical original coordinate values")
  oldheight=max(height(x) for row in A for x in row);newheight=max(height(x) for row in N for x in row)
  Mp=[[[ZERO for j in range(6)] for i in range(6)] for k in range(4)]
  for aij,(i,j) in enumerate(coords):
   for k in range(4):Mp[k][i][j]=Mp[k][j][i]=N[aij][k]
  normalized=save(out/"complete-original-canonical-four-matrix-pencil.json.gz",{"format":FORMAT+"-canonical","binding":binding,"data":{
   "originalTensor":PIN,"matchedCubic":F,"selectedOriginalCoordinateRows":selected,"selectedOriginalMatrixEntries":[coords[i] for i in selected],
   "canonicalParameterToOriginalParameter":[[fv(v) for v in row] for row in V],
   "originalParameterToCanonicalParameter":[[fv(v) for v in row] for row in U],
   "allFourCanonicalMatrices":[[[fv(v) for v in row] for row in m] for m in Mp],
   "all32OriginalInverseProductsVerified":invcount==32,"all84OriginalCoordinateProductsVerified":check==84,
   "maximumOriginalCoefficientBits":oldheight,"maximumCanonicalCoefficientBits":newheight,
   "parameterIdentity":"lambda_original=V*mu; T_original(lambda)=sum(mu_i*Tcanonical_i)"}},True)
  rec["parameters"].update({"canonicalPencil":normalized,"selectedOriginalMatrixEntries":[coords[i] for i in selected],"all32ConstantInverseProductsVerified":True,
    "all84OriginalPencilCoordinateProductsVerified":True,"maximumOriginalCoefficientBits":oldheight,"maximumCanonicalCoefficientBits":newheight})
  event("complete-original-canonical-pencil-verified")
  dp={0:{(0,0,0,0):ONE}};termops=0
  for r in range(6):
   nxt={}
   for mask,poly in dp.items():
    for j in range(6):
     if mask>>j&1:continue
     sign=-1 if (mask>>(j+1)).bit_count()%2 else 1
     target=nxt.setdefault(mask|1<<j,{})
     for e,c in poly.items():
      for k in range(4):
       v=Mp[k][r][j]
       if not v:continue
       ee=list(e);ee[k]+=1;ee=tuple(ee)
       z=(c*v)%MOD
       if sign<0:z=-z
       target[ee]=(target.get(ee,ZERO)+z)%MOD
       if not target[ee]:target.pop(ee)
       termops+=1
   dp=nxt
   event("complete-original-sextic-determinant-row-"+str(r+1))
  det=dp[(1<<6)-1];need(det and all(sum(e)==6 for e in det),"full nonzero homogeneous sextic determinant")
  # Independent finite-field values audit the exact DP signs and coordinate order.
  pts=[[int(i==j) for i in range(4)] for j in range(4)]+[[1,1,1,1],[1,2,3,4],[2,3,5,7]]
  for point in pts:
   mv=[[sum(point[k]*residue(Mp[k][i][j]) for k in range(4))%P for j in range(6)] for i in range(6)]
   direct=determinant_field(mv)
   value=sum(residue(c)*math.prod(pow(point[k],e[k],P) for k in range(4)) for e,c in det.items())%P
   need(value==direct,"independent full6 field determinant and exact polynomial evaluation")
  final=save(out/"complete-original-rank-three-pencil-sextic.json.gz",{"format":FORMAT+"-complete-sextic","binding":binding,"data":{
   "canonicalPencil":normalized,"matchedCubic":F,"variables":["mu0","mu1","mu2","mu3"],"fullDeterminant":[[e,fv(c)] for e,c in sorted(det.items())],
   "homogeneousDegree":6,"completeOriginalMatrixColumnsRetained":True,"parameterToOriginalIncludedInCanonicalPencil":True,
   "allSevenIndependentFieldDeterminantValuesVerified":True,"exactDeterminantAlgorithm":"full subset permutation dynamic program, no parameter specialization",
   "rankThreeIncidence":"Tcanonical(mu)*y=0 with y!=0,mu!=0; use all6 equations and the complete original M rank>=3",
   "kernelDimensionAtSingularPencilAssumed":False,"irreducibilityClaimed":False,"criticalIdealEmptyClaimed":False}},True)
  rec["parameters"].update({"sextic":final,"sexticNonzeroTerms":len(det),"sexticMaximumCoefficientBits":max(height(c) for c in det.values()),
   "completePolynomialTermProducts":termops,"allSevenIndependentFieldDeterminantValuesVerified":True,
   "criticalIdealEmptyClaimed":False,"irreducibilityClaimed":False})
  rec["status"]="completed";code=0;event("complete-original-rank-three-pencil-sextic")
 except BaseException as e:
  rec["status"]="budget-checkpoint" if isinstance(e,TimeoutError) else "failed";rec["parameters"]["error"]={"type":type(e).__name__,"message":str(e)}
  code=75 if isinstance(e,TimeoutError) else 1
 finally:
  signal.setitimer(signal.ITIMER_REAL,0);rec["elapsedSeconds"]=time.monotonic()-start;rec["maxResidentKiB"]=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
  desc=save(out/"original-mean-rank-three-exact-pencil-receipt.json",rec)
  print(json.dumps({"exitCode":code,"receipt":desc,**rec},sort_keys=True),flush=True)
 return code
if __name__=="__main__":sys.exit(main())
