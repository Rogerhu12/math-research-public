#!/usr/bin/env python3
"""Independent original P31 jet ranks and integer T/S Smith audit.
Author: ChatGPT (AI), root. Date: 2026-11-16.
No projection producer, polynomial core, Schur routine, or HNF audit is imported.
All mathematical matrices and receipts stay temporary.
"""
import argparse,gzip,hashlib,itertools,json,math,resource,signal,time
from pathlib import Path
from flint import nmod_mat,fmpz_mat
P=31;N=5
PRIMITIVE=(65159,"44350c49f9f60c61427b7278bf7f3d24b6cb2e6583848a113b03bb109516d4fe")
DECODED=(158741,"fa2e5d80e9fbd47e1e237ae60c548900a15922a0543e02be77fc972dc52944b3")
RAW={1:(6740,"4ca163bbc3084bc2c05dab47a60a96dcfe8c90d242d2bc68cb63d1c66521e4b9"),2:(7828,"9acb3368250f9efeeed1b358036f3ee6620846ba48fb176f6b2011a94c00e2a4")}
COORD={1:(662,"2598ebf23851c2bd48e2c32049dc5adb9a660984c336698bccd36215ead5fc55"),2:(16797,"46cb736d61e85daf6af0a4476ffa857c98b06f84d8c6e149b6180ce054d14a5c")}
AUDIT=(2013,"1ac4cfed2d998f11b9c382f814287d46f5a02e4be64e7b2db856839482a2b8f9")
def require(ok,msg):
 if not ok:raise ValueError(msg)
def canonical(x):return (json.dumps(x,sort_keys=True,separators=(",",":"),ensure_ascii=True)+"\n").encode()
def sha(b):return hashlib.sha256(b).hexdigest()
def identity(p):
 b=Path(p).read_bytes();return {"bytes":len(b),"sha256":sha(b)}
def pin(p,e):
 b=Path(p).read_bytes();require((len(b),sha(b))==e,"Full input "+str(p));return b
def jet(q,c):
 return [sum(int(q[d])*math.comb(d,k)*pow(c,d-k,P) for d in range(k,len(q)))%P for k in range(N)]
def zero(r,c):return nmod_mat([[0]*c for _ in range(r)],P)
def matseries_product(A,B,r,c):
 out=[]
 for n in range(N):
  z=zero(r,c)
  for k in range(n+1):z+=A[k]*B[n-k]
  out.append(z)
 return out
def reconstruct(equations,center,rec):
 pairs=list(itertools.combinations_with_replacement(range(11),2))
 half=pow(2,-1,P)
 TT=[nmod_mat([[math.comb(i,j)*math.comb(i-j,k)*pow(center,i-j-k,P)%P if i-j>=k else 0 for j in range(11)] for i in range(11)],P) for k in range(N)]
 require(int(TT[0].det())==1,"Original full binomial coordinate change")
 fields=[]
 for row in equations:
  coeff=[jet(q,center) for q in row]
  LL=[nmod_mat([[coeff[i][k] for i in range(11)]],P) for k in range(N)]
  QQ=[]
  for k in range(N):
   Q=[[0]*11 for _ in range(11)]
   for (i,j),v in zip(pairs,coeff[11:]):
    Q[i][j]=v[k] if i==j else v[k]*half%P;Q[j][i]=Q[i][j]
   QQ.append(nmod_mat(Q,P))
  L=matseries_product(LL,TT,1,11)
  QT=matseries_product(QQ,TT,11,11)
  B=matseries_product([T.transpose() for T in TT],QT,11,11)
  f={}
  for i in range(11):
   v=[int(L[k][0,i]) for k in range(N)]
   if any(v):f[(i,)]=v
  for i,j in pairs:
   v=[int(B[k][i,j])*(1 if i==j else 2)%P for k in range(N)]
   if any(v):f[(i,j)]=v
  fields.append(f)
 pc=[tuple([0]*i+[1]*(n-i)) for n in range(1,6) for i in range(n+1)]
 nc=[tuple([0]*i+[1]*(n-i)+[j]) for n in range(5) for i in range(n+1) for j in range(2,11)]
 targets=pc+nc;ti={m:i for i,m in enumerate(targets)}
 require(len(targets)==155,"Complete original projected target dictionary")
 multipliers=[m for n in range(4) for m in itertools.combinations_with_replacement(range(11),n)]
 rows=[];labels=[];counts=[0]*4
 for eq,f in enumerate(fields):
  for m in multipliers:
   v={}
   for fm,q in f.items():
    j=ti.get(tuple(sorted(m+fm)))
    if j is not None:
     old=v.get(j,[0]*N);v[j]=[(a+b)%P for a,b in zip(old,q)]
   v={j:q for j,q in v.items() if any(q)}
   nd=sum(i>=2 for i in m);counts[nd]+=1;labels.append([eq,list(m)])
   if nd>=2:require(not v,"Every high-normal original projected row has zero jet")
   else:rows.append(v)
 con=rec["parameters"]["originalConstruction"]
 require(counts==[170,918,2295,2805] and len(rows)==1088,"Complete source coverage")
 require(sha(canonical(labels))==con["sourceDictionaryLogicalSha256"],"Complete original source order")
 require(sha(canonical(targets))==con["targetDictionaryLogicalSha256"],"Complete original output order")
 return rows
def ranks(rows):
 out=[];nr=len(rows);nc=155
 for length in range(1,N+1):
  block=[[0]*(length*nc) for _ in range(length*nr)]
  for k in range(length):
   for j in range(k+1):
    order=k-j
    for ri,row in enumerate(rows):
     dest=block[k*nr+ri]
     for ci,coeff in row.items():dest[j*nc+ci]=coeff[order]
  out.append(int(nmod_mat(block,P).rank()))
 return out
def vp(n):
 n=abs(int(n));require(n>0,"Full finite relation rank");v=0
 while n%P==0:n//=P;v+=1
 require(n==1,"Pure coefficient-prime invariant factor")
 return v
def quotient_snf(path,pin_value):
 d=json.loads(pin(path,pin_value));E=d["ambientExponents"];A=d["coordinateRows"];n=len(E)
 require(len(A)==n,"Original torsion coordinate shape")
 relations=[[P**E[j] if i==j else 0 for i in range(n)] for j in range(n)]
 relations += [list(c) for c in zip(*A)]
 S=fmpz_mat(relations).snf()
 vals=[vp(S[i,i]) for i in range(n)]
 return [v for v in vals if v]
def main():
 ap=argparse.ArgumentParser()
 for name in ("primitive","w31-dir","root1","root2","out"):ap.add_argument("--"+name,type=Path,required=True)
 a=ap.parse_args();start=time.monotonic()
 resource.setrlimit(resource.RLIMIT_AS,(768<<20,768<<20))
 signal.signal(signal.SIGALRM,lambda *_:(_ for _ in ()).throw(TimeoutError("Root ninety-second audit budget")))
 signal.setitimer(signal.ITIMER_REAL,90)
 result={"format":"r150-root-independent-original-p31-block-jet-and-quotient-snf-v1","status":"started","source":identity(__file__),"parameters":{"prime":P,"jetLengths":[1,2,3,4,5],"seconds":90,"memoryMiB":768}}
 code=1
 try:
  b=gzip.decompress(pin(a.primitive,PRIMITIVE));require((len(b),sha(b))==DECODED,"Complete decoded original")
  primitive=json.loads(b);eqs=primitive["equations"]
  require(len(eqs)==17 and all(len(r)==77 for r in eqs),"Complete original17 by77 equations")
  require(int(primitive["denominator"])%P and all(int(z)%P for z in primitive["contents"]),"All18 normalization units")
  results=[]
  for center in (1,2):
   rp=a.w31_dir/("actual-root"+str(center))/"original-projection-field31-local-smith-receipt.json"
   rec=json.loads(pin(rp,RAW[center]))
   require(rec["status"]=="completed" and rec["exitCode"]==0,"Completed original projection")
   require(sha(canonical(rec["parameters"]["bindingInput"]))==rec["binding"],"Complete projection binding")
   desc=rec["parameters"]["temporaryData"];datap=Path(desc["path"])
   data=json.loads(pin(datap,(desc["bytes"],desc["sha256"])))
   require(data["binding"]==rec["binding"],"All temporary-data binding")
   rows=reconstruct(eqs,center,rec);rr=ranks(rows);delta=[rr[0]]+[rr[i]-rr[i-1] for i in range(1,N)]
   require(all(delta[i]<=delta[i+1] for i in range(N-1)) and delta[-1]==142,"Complete independent rank increments")
   exponents=[i for i in range(1,N) for _ in range(delta[i]-delta[i-1])]
   s=rec["parameters"]["actualSmith"]
   require(s["constantRank"]==delta[0] and s["positiveExponents"]==exponents,"Independent complete original jet spectrum")
   results.append({"center":center,"receipt":identity(rp),"binding":rec["binding"],"data":identity(datap),"all6188RowsAccountedFor":True,"blockJetRanks":rr,"rankIncrements":delta,"constantRank":delta[0],"positiveExponents":exponents,"genericRankPaidUpperAndActualLastIncrement":142})
  qraw=a.w31_dir/"whole-w31-remaining-torsion-quotient-audit.json";q=json.loads(pin(qraw,AUDIT))
  q1=quotient_snf(a.root1,COORD[1]);q2=quotient_snf(a.root2,COORD[2])
  require(q1==q["rootOneTOverS"]["exponents"] and q2==q["rootTwoTOverS"]["exponents"],"Independent complete integer SNF matches HNF")
  result.update(status="completed",projectionResults=results,quotientSNF={"rootOne":q1,"rootTwo":q2,"rootOneInput":identity(a.root1),"rootTwoInput":identity(a.root2),"comparedAudit":identity(qraw)},method="symmetric-quadratic-form-Taylor-congruence-and-original-1088-row-block-Toeplitz-ranks; direct-integer-SNF",mathematicalArraysTemporaryOnly=True)
  code=0
 except Exception as ex:result.update(status="failed",error={"type":type(ex).__name__,"message":str(ex)})
 finally:
  signal.setitimer(signal.ITIMER_REAL,0);result["elapsedSeconds"]=time.monotonic()-start;result["peakRssKiB"]=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss;result["exitCode"]=code
  a.out.write_bytes(canonical(result));print(canonical(result).decode(),end="")
 return code
if __name__=="__main__":raise SystemExit(main())
