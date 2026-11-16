#!/usr/bin/env python3
"""Complete original pencil minor gates at the fixed legal127 coefficient place.
Author: Astra-ISP-789f / normal_annihilator. AI-assisted: GPT-6 Astra Pro.
Date: 2026-11-16. All225 fourth minors and all21 symmetric cofactors retained.
Only constant coefficient units lift to E; no finite-field point exclusion lifts.
"""
import argparse,functools,gzip,hashlib,itertools,json,os,resource,signal,sys,time
from pathlib import Path
from flint import fmpq,nmod_mpoly_ctx
sys.set_int_max_str_digits(0)
FORMAT="r150-original-pencil-complete-minor-coefficient-gates-v2"
P=127;ROOT=100
BIND="39e2ef818d36588618292515fabf94615f3e7a64f1d047ea25c218e3987c9038"
PINS={
"canonical":{"path":"complete-original-canonical-four-matrix-pencil.json.gz","bytes":2265268,"sha256":"60e60c1683607569b8f58a62071f7e86f61ee2e9bdfc205e98a5d4108b3185d5","logicalBytes":4595018,"logicalSha256":"75c485c490d5f8f1918f241c734e49600d1ce8298a8631ac77151a9b1902ffff"},
"sextic":{"path":"complete-original-rank-three-pencil-sextic.json.gz","bytes":7775547,"sha256":"3fc2d9553563143a17032b2b432c81bf15a6dafe780424fe2d58232c883a6e5c","logicalBytes":15633428,"logicalSha256":"685cc84281d7e01abbd0302912437a5aab6ce997ed075a51201370df744ec354"}}
def need(b,s):
 if not b:raise ValueError(s)
def sha(b):return hashlib.sha256(b).hexdigest()
def canon(x):return json.dumps(x,sort_keys=True,separators=(",",":")).encode()
def save(p,x,gz=False):
 b=canon(x) if gz else json.dumps(x,sort_keys=True,indent=2).encode();z=gzip.compress(b,compresslevel=1,mtime=0) if gz else b
 q=p.with_name(p.name+".tmp");q.write_bytes(z);os.replace(q,p);d={"path":p.name,"bytes":len(z),"sha256":sha(z)}
 if gz:d.update(logicalBytes=len(b),logicalSha256=sha(b))
 return d
def load(root,key):
 pin=PINS[key];z=(root/pin["path"]).read_bytes();need(len(z)==pin["bytes"] and sha(z)==pin["sha256"],"complete original compressed "+key)
 b=gzip.decompress(z);need(len(b)==pin["logicalBytes"] and sha(b)==pin["logicalSha256"],"complete original logical "+key)
 d=json.loads(b);need(d["binding"]==BIND,"complete same original E binding");return d["data"]
def residue(x):
 ans=0
 for k,v in enumerate(x):
  q=fmpq(v);den=int(q.denom()%P);need(den,"all actual original E coefficients legal at127")
  ans=(ans+int(q.numer()%P)*pow(den,-1,P)*pow(ROOT,k,P))%P
 return ans
def mons(n,d):
 out=[]
 for ii in itertools.combinations_with_replacement(range(n),d):
  e=[0]*n
  for k in ii:e[k]+=1
  out.append(tuple(e))
 return sorted(out)
def inv(a):
 n=len(a);z=[row[:]+[int(i==j) for j in range(n)] for i,row in enumerate(a)];det=1
 for c in range(n):
  k=next((i for i in range(c,n) if z[i][c]),None)
  if k is None:return None,None
  if k!=c:z[c],z[k]=z[k],z[c];det=-det
  p=z[c][c];det=det*p%P;u=pow(p,-1,P);z[c]=[x*u%P for x in z[c]]
  for i in range(n):
   if i!=c:
    u=z[i][c]
    if u:z[i]=[(x-u*y)%P for x,y in zip(z[i],z[c])]
 v=[r[n:] for r in z]
 for B,C in [(a,v),(v,a)]:
  for i in range(n):
   for j in range(n):need(sum(B[i][k]*C[k][j] for k in range(n))%P==int(i==j),"all original coefficient unit inverse products")
 return v,det%P
def profile(cols):
 piv={};ids=[]
 for j,col in enumerate(cols):
  v=col[:]
  for k,w in piv.items():
   t=v[k]
   if t:v=[(x-t*y)%P for x,y in zip(v,w)]
  k=next((i for i,x in enumerate(v) if x),None)
  if k is not None:
   t=pow(v[k],-1,P);piv[k]=[x*t%P for x in v];ids.append(j)
 return ids
def packed(poly):return [[[int(v) for v in e],int(c)] for e,c in sorted(poly.to_dict().items())]
def main():
 ap=argparse.ArgumentParser();ap.add_argument("--pencil-out",required=True);ap.add_argument("--out",required=True)
 ap.add_argument("--seconds",type=float,default=90);ap.add_argument("--memory-mib",type=int,default=768)
 a=ap.parse_args();need(0<a.seconds<=300 and 256<=a.memory_mib<=2048,"bounded complete coefficient gates")
 resource.setrlimit(resource.RLIMIT_AS,(a.memory_mib*1024**2,)*2)
 out=Path(a.out);out.mkdir(parents=True,exist_ok=True);start=time.monotonic();source=sha(Path(__file__).read_bytes())
 binding=sha(canon({"format":FORMAT,"source":source,"parentBinding":BIND,"inputs":PINS,"prime":P,"root":ROOT}))
 rec={"format":FORMAT,"binding":binding,"sourceSha256":source,"parameters":{"seconds":a.seconds,"memoryMiB":a.memory_mib}}
 def event(n):
  rec["parameters"]["lastCompletedPhase"]=n;print(json.dumps({"phase":n,"elapsedSeconds":time.monotonic()-start}),flush=True)
 def timeout(s,f):raise TimeoutError("complete original minor coefficient budget")
 signal.signal(signal.SIGALRM,timeout);signal.setitimer(signal.ITIMER_REAL,a.seconds);code=1
 try:
  d=load(Path(a.pencil_out),"canonical");T=[[[residue(v) for v in row] for row in t] for t in d["allFourCanonicalMatrices"]]
  ctx=nmod_mpoly_ctx.get(("mu0","mu1","mu2","mu3"),P,"lex");variables=ctx.gens();zero=ctx.constant(0);one=ctx.constant(1)
  A=[[sum((T[k][i][j]*variables[k] for k in range(4)),zero) for j in range(6)] for i in range(6)]
  @functools.lru_cache(None)
  def minor(rows,cols):
   if not rows:return one
   ans=zero
   for k,c in enumerate(cols):
    term=A[rows[0]][c]*minor(rows[1:],cols[:k]+cols[k+1:])
    ans=ans-term if k%2 else ans+term
   return ans
  m4=mons(4,4);comb=list(itertools.combinations(range(6),4));labels=[];polys=[];cols=[]
  for rows in comb:
   for cc in comb:
    v=minor(rows,cc);dd=v.to_dict();need(all(sum(e)==4 for e in dd),"complete fourth minors homogeneous4")
    labels.append({"rows":rows,"columns":cc});polys.append(packed(v));cols.append([int(dd.get(e,0)) for e in m4])
  selected=profile(cols);U=[[cols[j][i] for j in selected] for i in range(len(m4))]
  fourth={"all225OriginalMinorLabels":labels,"all225CompletePolynomials":polys,"all35OutputMonomials":m4,"selectedOriginalColumns":selected,"actualRank":len(selected)}
  if len(selected)==35:
   inverse,det=inv(U);need(inverse is not None,"actual complete fourth coefficient unit")
   fourth.update({"unit":U,"inverse":inverse,"unitDeterminant127":det,"all2450UnitProductsVerified":True,"originalEIdealContainsAllFourthMonomials":True})
  fourthdesc=save(out/"complete-original225-fourth-pencil-minor-coefficients.json.gz",{"format":FORMAT+"-fourth","binding":binding,"data":fourth},True)
  rec["parameters"].update({"fourth":fourthdesc,"completeFourthCoefficientRank":len(selected)});event("all225-original-fourth-pencil-minors")
  cofactorlabels=list(itertools.combinations_with_replacement(range(6),2));cof=[]
  for i,j in cofactorlabels:
   v=minor(tuple(k for k in range(6) if k!=i),tuple(k for k in range(6) if k!=j))
   if (i+j)%2:v=-v
   cof.append(v)
  m3=mons(3,5)
  # Fixed first hyperplane mu0=0; no other plane is silently substituted.
  C=[[int(p.to_dict().get((0,)+e,0)) for p in cof] for e in m3]
  selected5=profile([[C[i][j] for i in range(21)] for j in range(21)])
  fifth={"all21OriginalSymmetricCofactorLabels":cofactorlabels,"all21CompleteCofactors":[packed(p) for p in cof],
   "hyperplane":"mu0=0","all21OriginalThreeVariableQuinticMonomials":m3,"coefficientMatrix":C,"actualRank":len(selected5)}
  if len(selected5)==21:
   inverse,det=inv(C);need(inverse is not None,"all21 actual original plane coefficient unit")
   fifth.update({"inverse":inverse,"unitDeterminant127":det,"all882UnitProductsVerified":True,"originalEProjectiveCorankTwoLocusAvoidsThisHyperplane":True,
    "affineCoordinateAlgebraGeneratedByAtMost35Monomials":True,"free35Claimed":False})
  fifthdesc=save(out/"complete-original21-pencil-cofactors-plane-coefficients.json.gz",{"format":FORMAT+"-fifth","binding":binding,"data":fifth},True)
  rec["parameters"].update({"fifth":fifthdesc,"completePlaneFifthCoefficientRank":len(selected5)});event("all21-original-symmetric-cofactors-plane")
  sextic=load(Path(a.pencil_out),"sextic")
  s=ctx.from_dict({tuple(e):residue(c) for e,c in sextic["fullDeterminant"]})
  direct=minor(tuple(range(6)),tuple(range(6)))
  need(s==direct and s.total_degree()==6,"entire original E sextic reduces to the complete original field determinant")
  content,factors=s.factor();product=ctx.constant(int(content))
  for f,e in factors:product*=f**e
  need(product==s,"entire reported finite-field factorization multiplies back")
  fac=save(out/"complete-original-pencil-sextic127-factorization.json.gz",{"format":FORMAT+"-factor","binding":binding,"data":{
   "parentExactSextic":PINS["sextic"],"prime":P,"root":ROOT,"entireOriginalSextic":packed(s),
   "content":int(content),"factors":[{"polynomial":packed(f),"exponent":int(e),"degree":int(f.total_degree())} for f,e in factors],
   "completeOriginalDeterminantReductionVerified":True,"completeFactorProductVerified":True,
   "characteristicZeroFactorizationClaimed":False}},True)
  rec["parameters"].update({"factorization":fac,"factorDegreesAndExponents":[[int(f.total_degree()),int(e)] for f,e in factors],
   "all84OriginalSexticCoefficientReductionsVerified":True,"completeDeterminantReductionAndFactorProductVerified":True,
   "rankThreeIncidenceAllKernelDirectionsStillRetained":True,"criticalIdealEmptyClaimed":False})
  event("complete-original-pencil-minor-and-factor-gates");rec["status"]="completed";code=0
 except BaseException as e:
  rec["status"]="budget-checkpoint" if isinstance(e,TimeoutError) else "failed";rec["parameters"]["error"]={"type":type(e).__name__,"message":str(e)};code=75 if isinstance(e,TimeoutError) else 1
 finally:
  signal.setitimer(signal.ITIMER_REAL,0);rec["elapsedSeconds"]=time.monotonic()-start;rec["maxResidentKiB"]=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
  desc=save(out/"original-pencil-complete-minor-coefficient-gates-receipt.json",rec);print(json.dumps({"exitCode":code,"receipt":desc,**rec},sort_keys=True),flush=True)
 return code
if __name__=="__main__":sys.exit(main())
