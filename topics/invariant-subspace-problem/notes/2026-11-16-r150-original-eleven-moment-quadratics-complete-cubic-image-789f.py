#!/usr/bin/env python3
"""Exact original constant leading relations after all twelve gradient NFs.

Author: Astra-ISP-789f / normal_annihilator.
AI-assisted: GPT-6 Astra Pro. Date: 2026-11-16.
Read the complete paid original NF files without reconstructing their
large parameter algebra. Verify the six constant w-quadratic forms,
then form EVERY u-multiple of all eleven original leading quadratics.
Finite-field units only certify nonzero fixed E-minors; no parameter
is specialized, and a ten-generator conclusion is not called free.
"""
import argparse,gzip,hashlib,itertools,json,os,resource,signal,sys,time
from pathlib import Path
from flint import fmpq

FORMAT="r150-original-eleven-moment-quadratics-complete-cubic-image-v1"
PARENT={"bytes":1921,"sha256":"ca4c3d98675ab404cb2b8e05c8ddacd32c02d936f751cf05fe572eb57d510e48",
"logicalSha256":"d58cf0f99c7d2fee7087ca76297d30e70dd4b8ba830ab7b42709b7ab8c6ccc52",
"binding":"8fb21996da88d9abaa7d8a0c96208129603808d7c5c1e03b9acf6caa1dca6545"}
MATCHED=[52565262336,6080833024,-43931504,3725]
PRIMES=[127,131,137,139,149,151,157,163,167,173,179,181,191]
CROSS=list(itertools.combinations(range(5),2))
def need(b,s):
    if not b:raise ValueError(s)
def sha(b):return hashlib.sha256(b).hexdigest()
def canon(x):return json.dumps(x,sort_keys=True,separators=(",",":")).encode()
def key(t):
    e=[0]*5
    for i in t:e[i]+=1
    return tuple(e)
def mons(d):return [key(t) for t in itertools.combinations_with_replacement(range(5),d)]
M2=mons(2);M3=mons(3);M3I={e:i for i,e in enumerate(M3)}
LOW=[(0,)*5]+[key([i]) for i in range(5)]+[key(z) for z in CROSS]
def load_gz(p,desc,binding):
    raw=p.read_bytes();need(len(raw)==desc["bytes"] and sha(raw)==desc["sha256"],"whole original file "+p.name)
    data=gzip.decompress(raw);need(sha(data)==desc["logicalSha256"],"whole original logical file "+p.name)
    x=json.loads(data);need(x["binding"]==binding,"same original source binding "+p.name)
    return x["data"]
def save_json(p,x):
    b=json.dumps(x,sort_keys=True,indent=2).encode();t=p.with_name(p.name+".tmp");t.write_bytes(b);os.replace(t,p)
    return {"path":p.name,"bytes":len(b),"sha256":sha(b)}
def save_gz(p,x):
    b=canon(x);z=gzip.compress(b,compresslevel=1,mtime=0);t=p.with_name(p.name+".tmp");t.write_bytes(z);os.replace(t,p)
    return {"path":p.name,"bytes":len(z),"sha256":sha(z),"logicalBytes":len(b),"logicalSha256":sha(b)}
def cfield(v):
    a=[fmpq(0)]*3
    for e,c in v:
        need(len(e)==18 and 0<=e[0]<3 and not any(e[1:]),"actual fixed matched-field w-quadratic coefficient")
        a[e[0]]+=fmpq(c)
    return a
def rank(A,p):
    a=[list(r) for r in A];nr=len(a);nc=len(a[0]);k=0;piv=[]
    for j in range(nc):
        i=next((i for i in range(k,nr) if a[i][j]%p),None)
        if i is None:continue
        a[k],a[i]=a[i],a[k];v=pow(a[k][j]%p,-1,p);a[k]=[x*v%p for x in a[k]]
        for i in range(k+1,nr):
            z=a[i][j]%p
            if z:a[i]=[(x-z*y)%p for x,y in zip(a[i],a[k])]
        piv.append(j);k+=1
        if k==nr:break
    return k,piv
def inverse(A,p):
    n=len(A);B=[list(row)+[int(i==j) for j in range(n)] for i,row in enumerate(A)];det=1
    for j in range(n):
        i=next((i for i in range(j,n) if B[i][j]%p),None);need(i is not None,"actual selected constant field unit")
        if i!=j:B[j],B[i]=B[i],B[j];det=-det
        t=B[j][j]%p;det=det*t%p;v=pow(t,-1,p);B[j]=[x*v%p for x in B[j]]
        for i in range(n):
            if i==j:continue
            a=B[i][j]%p
            if a:B[i]=[(x-a*y)%p for x,y in zip(B[i],B[j])]
    V=[row[n:] for row in B]
    for i in range(n):
        for j in range(n):
            need(sum(A[i][k]*V[k][j] for k in range(n))%p==int(i==j),"all original unit right inverse products")
            need(sum(V[i][k]*A[k][j] for k in range(n))%p==int(i==j),"all original unit left inverse products")
    return V,det%p
def field_value(v,p,d):
    z=0
    for k,c in enumerate(v):
        den=int(c.denom()%p);need(den!=0,"chosen prime is a unit for every actual rational coefficient")
        z=(z+int(c.numer()%p)*pow(den,-1,p)*pow(d,k,p))%p
    return z
def main():
    ap=argparse.ArgumentParser();ap.add_argument("--low-out",required=True);ap.add_argument("--out",required=True)
    ap.add_argument("--seconds",type=float,default=120);ap.add_argument("--memory-mib",type=int,default=1024);a=ap.parse_args()
    need(0<a.seconds<=300 and 512<=a.memory_mib<=4096,"bounded complete original leading-image budget")
    resource.setrlimit(resource.RLIMIT_AS,(a.memory_mib*1024**2,)*2);out=Path(a.out);out.mkdir(parents=True,exist_ok=True)
    src=sha(Path(__file__).read_bytes());binding=sha(canon({"format":FORMAT,"sourceSha256":src,"parent":PARENT,"primes":PRIMES}))
    rec={"format":FORMAT,"binding":binding,"sourceSha256":src,"parameters":{"seconds":a.seconds,"memoryMiB":a.memory_mib}}
    start=time.monotonic();code=1
    def timeout(sig,fr):raise TimeoutError("bounded original eleven-quadratic/cubic-image consumer")
    signal.signal(signal.SIGALRM,timeout);signal.setitimer(signal.ITIMER_REAL,a.seconds)
    try:
        base=Path(a.low_out);m=load_gz(base/"complete-original-twelve-gradient-low-normal-forms.json.gz",PARENT,PARENT["binding"])
        need(m["matchedCubic"]==MATCHED and len(m["completeVerifiedNormalFormRows"])==12,"complete original twelve-row index")
        f=load_gz(base/m["fiveGradientModel"]["path"],m["fiveGradientModel"],PARENT["binding"])
        need(f["lowStandardMonomials16"]==[list(e) for e in LOW],"actual low squarefree dictionary")
        q=[{tuple(e):[fmpq(z) for z in c] for e,c in row} for row in f["sameFiveTopQuadratics"]]
        need(len(q)==5 and all(set(row).issubset(M2) for row in q),"all five complete original leading quadratics")
        del f
        W=[];rowDescriptors=[]
        for row in range(6,12):
            desc=m["completeVerifiedNormalFormRows"][row];d=load_gz(base/desc["path"],desc,PARENT["binding"])
            need(d["row"]==row and d["gradient"]=="dw%d"%(row-6) and d["completeOriginalPolynomialSourceIdentityVerified"],"actual original w derivative row")
            need(len(d["normalFormCoefficients"])==16 and len(d["originalFiveGradientSourceCoefficients"])==5,"all original row coordinates")
            W.append([cfield(v) for v in d["normalFormCoefficients"][6:]])
            rowDescriptors.append(desc);del d
        for row in W:q.append({key(c):v for c,v in zip(CROSS,row)})
        need(len(q)==11,"five u plus six w original leading quadratics")
        C=[[None for _ in range(55)] for _ in M3]
        for i in range(len(M3)):
            for j in range(55):C[i][j]=[fmpq(0)]*3
        columns=[]
        for g,row in enumerate(q):
            for j in range(5):
                col=5*g+j;columns.append({"gradient":"du%d"%g if g<5 else "NFdw%d"%(g-5),"multiplierU":j})
                for e,v in row.items():
                    t=list(e);t[j]+=1;idx=M3I[tuple(t)]
                    C[idx][col]=[x+y for x,y in zip(C[idx][col],v)]
        allCoefficients=[v for row in W for v in row]+[v for row in C for v in row]
        attempts=[];chosen=None
        for p in PRIMES:
            if any(int(z.denom()%p)==0 for v in allCoefficients for z in v):
                attempts.append({"prime":p,"coefficientUnit":False});continue
            roots=[d for d in range(p) if sum(c*pow(d,i,p) for i,c in enumerate(MATCHED))%p==0]
            for d in roots:
                WF=[[field_value(v,p,d) for v in row] for row in W]
                CF=[[field_value(v,p,d) for v in row] for row in C]
                rw,pw=rank(WF,p);rc,pc=rank(CF,p)
                attempts.append({"prime":p,"root":d,"allCoefficientDenominatorsUnits":True,"wQuadraticRank":rw,"completeCubicImageRank":rc})
                if rw==6 and rc==35:
                    chosen=(p,d,WF,CF,pw,pc);break
            if chosen:break
        rec["parameters"]["actualPrimeRootAttempts"]=attempts
        if chosen:
            p,d,WF,CF,pw,pc=chosen
            UW=[[row[j] for j in pw] for row in WF];UC=[[row[j] for j in pc] for row in CF]
            IW,dw=inverse(UW,p);IC,dc=inverse(UC,p)
            remaining=[i for i in range(10) if i not in pw]
            fielddata={"prime":p,"root":d,"matchedCubic":MATCHED,
              "wQuadraticSelectedColumns":pw,"wQuadraticUnit":UW,"wQuadraticUnitInverse":IW,"wQuadraticUnitDeterminant":dw,
              "completeCubicSelectedOriginalColumns":pc,"completeCubicUnit":UC,"completeCubicUnitInverse":IC,"completeCubicUnitDeterminant":dc}
            model={"parentBinding":PARENT["binding"],"matchedCubic":MATCHED,
              "allElevenLeadingQuadratics":[[[list(e),[str(c) for c in v]] for e,v in sorted(row.items())] for row in q],
              "all55OriginalCubicSourceColumns":columns,"all35CubicOutputMonomials":[list(e) for e in M3],
              "actualFieldCertificate":fielddata,
              "tenOriginalGeneratingMonomials":[list(e) for e in LOW[:6]]+[list(key(CROSS[i])) for i in remaining],
              "sixOriginalWRowDescriptors":rowDescriptors,
              "exactOperatorDefinition":"Use the same original E minors and their adjugate/determinant inverses; all determinants are fixed E constants, not parameter polynomials.",
              "freenessOfTenGeneratorsClaimed":False}
            md=save_gz(out/"complete-original-eleven-quadratic-leading-model.json.gz",{"format":FORMAT+"-model","binding":binding,"data":model})
            rec["parameters"].update({"model":md,"wQuadraticExactRank":6,"completeCubicImageExactRank":35,
              "selectedOriginalWQuadraticColumns":pw,"selectedOriginalCubicColumns":pc,
              "remainingOriginalMixedQuadraticColumns":remaining,
              "all72WUnitInverseCoordinatesVerified":True,"all2450CubicUnitInverseCoordinatesVerified":True,
              "all55OriginalSourceColumnsRetained":True,"all35OriginalCubicOutputCoordinatesRetained":True,
              "completeOriginalMomentIdealHasTenParameterModuleGenerators":True,"freenessOfTenGeneratorsClaimed":False,
              "noMeanOrMomentParameterSpecialized":True,"noParameterDenominatorIntroduced":True})
            rec["status"]="completed";code=0
        else:
            rec["status"]="completed-bounded-field-profile";code=0
    except BaseException as e:
        rec["status"]="budget-checkpoint" if isinstance(e,TimeoutError) else "failed"
        rec["parameters"]["error"]={"type":type(e).__name__,"message":str(e)}
        code=75 if isinstance(e,TimeoutError) else 1
    finally:
        signal.setitimer(signal.ITIMER_REAL,0);rec["elapsedSeconds"]=time.monotonic()-start
        rec["maxResidentKiB"]=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
        desc=save_json(out/"original-eleven-quadratic-leading-image-receipt.json",rec)
        print(json.dumps({"status":rec["status"],"exitCode":code,"binding":binding,"elapsedSeconds":rec["elapsedSeconds"],"receipt":desc,"parameters":rec["parameters"]},sort_keys=True),flush=True)
    return code
if __name__=="__main__":sys.exit(main())
