#!/usr/bin/env python3
"""Explicit Rabin certificate for an original full-degree sextic pencil line.
Author: Astra-ISP-789f / normal_annihilator. AI-assisted: GPT-6 Astra Pro.
Date: 2026-11-16. Only a positive irreducible full-degree line certifies the
original homogeneous polynomial; failure of the finite list is inconclusive.
"""
import argparse,gzip,hashlib,itertools,json,os,resource,signal,time
from pathlib import Path
P=127
FORMAT="r150-original-sextic-pencil-rabin-certificate-v1"
PIN={"path":"complete-original-pencil-sextic127-factorization.json.gz","bytes":1403,"sha256":"9c92e8d2dd0452d27e0eedbf2ffe8c246aebd6aea3f89a66bbd97ca6b9ba3935","logicalBytes":3245,"logicalSha256":"9fffbc82778c464c4e9e60c65a8a104f4385ec003cbe5ea37c9b311f91536b8a","binding":"d73ed9dc675a00081cea88a34f47fcc617db89aba1c7df5e56427f9168c641ba"}
def need(b,s):
 if not b:raise ValueError(s)
def sha(b):return hashlib.sha256(b).hexdigest()
def canon(x):return json.dumps(x,sort_keys=True,separators=(",",":")).encode()
def tr(a):
 a=[x%P for x in a]
 while a and a[-1]==0:a.pop()
 return a
def add(a,b):
 c=[0]*max(len(a),len(b))
 for i,x in enumerate(a):c[i]+=x
 for i,x in enumerate(b):c[i]+=x
 return tr(c)
def neg(a):return tr([-x for x in a])
def mul(a,b):
 if not a or not b:return []
 c=[0]*(len(a)+len(b)-1)
 for i,x in enumerate(a):
  for j,y in enumerate(b):c[i+j]=(c[i+j]+x*y)%P
 return tr(c)
def divmodp(a,b):
 need(bool(b),"nonzero polynomial divisor");a=tr(a);q=[0]*max(0,len(a)-len(b)+1);inv=pow(b[-1],-1,P)
 while len(a)>=len(b):
  e=len(a)-len(b);v=a[-1]*inv%P;q[e]=v
  for i,x in enumerate(b):a[e+i]=(a[e+i]-v*x)%P
  a=tr(a)
 return tr(q),a
def power(a,n,f):
 r=[1]
 while n:
  if n&1:r=divmodp(mul(r,a),f)[1]
  a=divmodp(mul(a,a),f)[1];n//=2
 return r
def xgcd(a,b):
 oldr,r=a,b;olds,s=[1],[];oldt,t=[],[1]
 while r:
  q,z=divmodp(oldr,r);oldr,r=r,z;olds,s=s,add(olds,neg(mul(q,s)));oldt,t=t,add(oldt,neg(mul(q,t)))
 if not oldr:return [],[],[]
 z=pow(oldr[-1],-1,P);return tr([v*z for v in oldr]),tr([v*z for v in olds]),tr([v*z for v in oldt])
def save(p,x,gz=False):
 b=canon(x) if gz else json.dumps(x,sort_keys=True,indent=2).encode();z=gzip.compress(b,compresslevel=1,mtime=0) if gz else b
 q=p.with_name(p.name+".tmp");q.write_bytes(z);os.replace(q,p);d={"path":p.name,"bytes":len(z),"sha256":sha(z)}
 if gz:d.update(logicalBytes=len(b),logicalSha256=sha(b))
 return d
def main():
 ap=argparse.ArgumentParser();ap.add_argument("--minor-out",required=True);ap.add_argument("--out",required=True);a=ap.parse_args()
 resource.setrlimit(resource.RLIMIT_AS,(256*1024**2,)*2);out=Path(a.out);out.mkdir(parents=True,exist_ok=True)
 start=time.monotonic();source=sha(Path(__file__).read_bytes());binding=sha(canon({"format":FORMAT,"source":source,"pin":PIN,"trialGrid":[8,8]}))
 rec={"format":FORMAT,"binding":binding,"sourceSha256":source,"parameters":{}};code=1
 def timeout(s,f):raise TimeoutError("sixty-second original Rabin certificate budget")
 signal.signal(signal.SIGALRM,timeout);signal.setitimer(signal.ITIMER_REAL,60)
 try:
  raw=(Path(a.minor_out)/PIN["path"]).read_bytes();need(len(raw)==PIN["bytes"] and sha(raw)==PIN["sha256"],"complete original sextic field output")
  data=gzip.decompress(raw);need(len(data)==PIN["logicalBytes"] and sha(data)==PIN["logicalSha256"],"complete original sextic field logical bytes")
  d=json.loads(data);need(d["binding"]==PIN["binding"],"same original pencil/minor binding");F=d["data"]["entireOriginalSextic"]
  need(all(sum(e)==6 for e,c in F),"entire original sextic is homogeneous")
  dd={tuple(e):c for e,c in F};axes=[j for j in range(4) if dd.get(tuple(6*int(i==j) for i in range(4)),0)]
  need(axes,"actual nonzero pure sixth coefficient");free=axes[-1];other=[j for j in range(4) if j!=free];found=None;trials=0
  for aa,bb in itertools.product(range(8),repeat=2):
   point=[0]*4;point[other[0]]=1;point[other[1]]=aa;point[other[2]]=bb
   f=[0]*7
   for e,c in F:
    z=c
    for i in other:z=z*pow(point[i],e[i],P)%P
    f[e[free]]=(f[e[free]]+z)%P
   need(f[-1]!=0,"actual full degree-six specialization preserves the homogeneous leading unit")
   original=f[:];lead=f[-1];f=[x*pow(lead,-1,P)%P for x in f]
   chain=[];v=[0,1]
   for k in range(1,7):
    v=power(v,P,f);chain.append(v)
   tests=[];ok=chain[-1]==[0,1]
   for k in [2,3]:
    r=add(chain[k-1],[0,-1]);g,u,w=xgcd(f,r)
    need(add(mul(u,f),mul(w,r))==g,"entire original Bezout product")
    tests.append({"frobeniusPower":k,"difference":r,"gcd":g,"bezoutF":u,"bezoutDifference":w})
    if g!=[1]:ok=False
   trials+=1
   if ok:
    found={"variableIndex":free,"fixedOtherCoordinates":{str(i):point[i] for i in other},"originalUnivariateCoefficients":original,
     "leadingUnit":lead,"monicUnivariate":f,"completeFrobeniusChainPowers1Through6":chain,"twoBezoutCertificates":tests,
     "allExactBezoutProductsVerified":True,"xPower127ToSixEqualsX":True,"degreePreserved":6,
     "criterion":"prime divisors of degree6 are2,3; gcd(x^(127^3)-x,f)=gcd(x^(127^2)-x,f)=1 and x^(127^6)=x mod f",
     "entireOriginalFieldSextic":F,"originalPureSixthCoefficient":dd[tuple(6*int(i==free) for i in range(4))]}
    break
  rec["parameters"].update({"trials":trials,"fullDegreeIrreducibleLineFound":found is not None})
  if found is not None:
   desc=save(out/"complete-original-sextic-irreducible-line-rabin-certificate.json.gz",{"format":FORMAT+"-complete","binding":binding,"data":found},True)
   rec["parameters"].update({"certificate":desc,"irreducibleOriginalHomogeneousFieldSexticCertified":True})
  rec["status"]="completed" if found is not None else "finite-search-inconclusive";code=0
 except BaseException as e:
  rec["status"]="failed";rec["parameters"]["error"]={"type":type(e).__name__,"message":str(e)}
 finally:
  signal.setitimer(signal.ITIMER_REAL,0);rec["elapsedSeconds"]=time.monotonic()-start
  desc=save(out/"original-sextic-pencil-rabin-certificate-receipt.json",rec);print(json.dumps({"exitCode":code,"receipt":desc,**rec},sort_keys=True),flush=True)
 return code
if __name__=="__main__":raise SystemExit(main())
