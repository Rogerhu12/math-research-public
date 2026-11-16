#!/usr/bin/env python3
"""Complete degree-six Jacobian gate for the original residual five-moment cubic.

Author: Astra-ISP-789f / normal_annihilator.
AI-assisted: GPT-6 Astra Pro. Date: 2026-11-16.
The source is the exact restriction of original R3 in the verified global
Bell coordinates.  All 350 quartic multiples of all five quadratic partials
and all 210 sextic outputs are retained over the matched cubic field.
A rational regular representation gives 630 x 1050 coordinates.  Every
column is independently scaled by a nonzero rational constant, with all
coefficient products checked, before the one fixed finite-field rank.
Full row rank proves the characteristic-zero gate; smaller field rank is
only an unfinished gate, not a negative characteristic-zero conclusion.
"""
import argparse,gzip,hashlib,itertools,json,math,os
from pathlib import Path
import resource,signal,sys,time
from flint import fmpq,fmpq_poly,nmod_mat

FORMAT="r150-original-five-moment-cubic-complete-jacobian-gate-v1"
MODEL_BYTES=1777288
MODEL_SHA="46537ffbe520ff47df2f18448541a3d2608578ca067a0c865b43e8c44ab55fdc"
MODEL_LOGICAL="5a10a784f9d9ee9455f97bdd8a077ff32f1d75eefba392e5c58e5cd6f5de5ee3"
MODEL_BINDING="d939c3506ce8276d82c662f382ae4ffe5c93163929ec1931c2174ecf001c1a8f"
MATCHED=[52565262336,6080833024,-43931504,3725]
PRIME=127

def need(b,s):
    if not b:raise ValueError(s)
def canon(x):return json.dumps(x,sort_keys=True,separators=(",",":")).encode()
def sha(x):return hashlib.sha256(x).hexdigest()
def save_json(p,x):
    b=json.dumps(x,sort_keys=True,indent=2).encode()
    t=p.with_name(p.name+".tmp");t.write_bytes(b);os.replace(t,p)
    return {"path":p.name,"bytes":len(b),"sha256":sha(b)}
def save_gz(p,x):
    b=canon(x);z=gzip.compress(b,compresslevel=1,mtime=0)
    t=p.with_name(p.name+".tmp");t.write_bytes(z);os.replace(t,p)
    return {"path":p.name,"bytes":len(z),"sha256":sha(z),"logicalBytes":len(b),"logicalSha256":sha(b)}
def mons(n):
    out=[]
    for key in itertools.combinations_with_replacement(range(5),n):
        e=[0]*5
        for i in key:e[i]+=1
        out.append(tuple(e))
    return out
def rational_column_to_primitive(entries):
    den=1
    for x in entries.values():den=math.lcm(den,int(x.denom()))
    nums={i:int(x.numer())*(den//int(x.denom())) for i,x in entries.items() if x}
    content=0
    for n in nums.values():content=math.gcd(content,abs(n))
    need(content!=0,"all original Jacobian source columns nonzero")
    prim={i:n//content for i,n in nums.items()}
    scale=fmpq(den,content)
    need(all(fmpq(prim[i])==entries[i]*scale for i in nums),"every original primitive column scaling product")
    return prim,scale,len(nums)
def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--model",required=True);ap.add_argument("--out",required=True)
    ap.add_argument("--seconds",type=float,default=60);ap.add_argument("--memory-mib",type=int,default=1024)
    a=ap.parse_args();need(0<a.seconds<=180 and 512<=a.memory_mib<=2048,"bounded fixed five-moment gate")
    out=Path(a.out);out.mkdir(parents=True,exist_ok=True)
    resource.setrlimit(resource.RLIMIT_AS,(a.memory_mib*1024**2,)*2)
    started=time.monotonic();ss=sha(Path(__file__).read_bytes())
    binding=sha(canon({"format":FORMAT,"sourceSha256":ss,"parentBinding":MODEL_BINDING,
                      "modelSha256":MODEL_SHA,"prime":PRIME,"fullSourceDegree":6}))
    rec={"format":FORMAT,"binding":binding,"sourceSha256":ss,"status":"started",
         "parameters":{"seconds":a.seconds,"memoryMiB":a.memory_mib,"prime":PRIME}}
    def timeout(signum,frame):raise TimeoutError("bounded complete five-moment Jacobian gate")
    signal.signal(signal.SIGALRM,timeout);signal.setitimer(signal.ITIMER_REAL,a.seconds);code=1
    try:
        raw=Path(a.model).read_bytes();need(len(raw)==MODEL_BYTES and sha(raw)==MODEL_SHA,"complete original hyperbolic model bytes")
        logical=gzip.decompress(raw);need(sha(logical)==MODEL_LOGICAL,"complete original model logical bytes")
        p=json.loads(logical);need(p["binding"]==MODEL_BINDING,"same exact original transport binding")
        m=p["data"];need(m["matchedCubic"]==MATCHED and m["pureRemainingCubicEssentialRank"]==5,
                        "same unchanged matched cubic and actual pure cubic")
        f=fmpq_poly([fmpq(c,MATCHED[-1]) for c in MATCHED])
        basis=[fmpq_poly([1]),fmpq_poly([0,1]),fmpq_poly([0,0,1])]
        C={}
        for exp,q in m["pureRemainingFiveMomentCubic"]:
            need(len(exp)==18 and exp[0]<3 and not any(exp[1:13]) and sum(exp[13:])==3,
                 "all original pure-cubic coordinate positions")
            e=tuple(exp[13:]);v=C.setdefault(e,[fmpq(0)]*3);v[exp[0]]+=fmpq(q)
        C={e:fmpq_poly(v) for e,v in C.items()}
        need(len(C)==35,"all35 original pure-cubic monomials retained")
        Q=[]
        for j in range(5):
            row={}
            for e,c in C.items():
                if e[j]:
                    ee=list(e);ee[j]-=1;row[tuple(ee)]=c*e[j]
            Q.append(row)
        # Rebuild the entire polar matrix retained by the parent, not just rank5.
        quadratic=mons(2)
        parent=m["pureRemainingCubicPolarMatrix"]
        for j in range(5):
            for k,e in enumerate(quadratic):
                actual=Q[j].get(e,fmpq_poly())
                need([str(actual[t]) for t in range(3)]==parent[j][k],
                     "all225 original five-moment polar coordinates")
        inputs=mons(4);outputs=mons(6);need(len(inputs)==70 and len(outputs)==210,"complete quartic/sextic dictionaries")
        pos={e:i for i,e in enumerate(outputs)}
        cols=[];scales=[];dictionary=[];checks=0;maxbits=0
        for j in range(5):
            for a0 in inputs:
                for t in range(3):
                    col={}
                    for e,c in Q[j].items():
                        dest=pos[tuple(x+y for x,y in zip(a0,e))]
                        v=c*basis[t]%f
                        for k in range(3):
                            if v[k]:col[3*dest+k]=v[k]
                    prim,scale,nchecked=rational_column_to_primitive(col)
                    checks+=nchecked;maxbits=max(maxbits,max(abs(x).bit_length() for x in prim.values()))
                    v=[0]*630
                    for i,x in prim.items():v[i]=x%PRIME
                    cols.append(v);scales.append(str(scale));dictionary.append([j,list(a0),t])
        need(len(cols)==1050,"all1050 original rational-representation source columns")
        A=nmod_mat([[cols[j][i] for j in range(1050)] for i in range(630)],PRIME)
        rank=int(A.rank())
        full=rank==630
        model={"parentBinding":MODEL_BINDING,"matchedCubic":MATCHED,
               "pureCubic":[[list(e),[str(c[i]) for i in range(3)]] for e,c in sorted(C.items())],
               "allFiveQuadraticPartials":[[[list(e),[str(c[i]) for i in range(3)]] for e,c in sorted(q.items())] for q in Q],
               "completeOriginalSourceDictionary":dictionary,
               "completeOriginalSexticOutputDictionary":[list(e) for e in outputs],
               "originalRationalColumnToPrimitiveScales":scales,
               "prime":PRIME,"fullFieldRank":rank,
               "fieldMatrixColumnMajorSha256":sha(bytes(x for c in cols for x in c))}
        desc=save_gz(out/"complete-five-moment-jacobian-gate.json.gz",
                     {"format":FORMAT+"-model","binding":binding,"data":model})
        rec["parameters"].update({"parentModelSha256":MODEL_SHA,"model":desc,
            "matchedFieldSourceShape":[210,350],"rationalRepresentationShape":[630,1050],
            "actualFixedFieldRank":rank,"all225OriginalPolarCoordinatesVerified":True,
            "allOriginalSourceAndOutputMonomialsRetained":True,
            "allRationalColumnPrimitiveProductsVerified":True,"originalNonzeroScalingProducts":checks,
            "maximumPrimitiveCoefficientBits":maxbits,
            "originalSourceDictionarySha256":sha(canon(dictionary)),
            "originalOutputDictionarySha256":sha(canon([list(e) for e in outputs])),
            "fieldMatrixColumnMajorSha256":model["fieldMatrixColumnMajorSha256"],
            "characteristicZeroFullSexticImageProved":full,
            "projectivePureCubicCriticalLocusEmptyProved":full,
            "finiteFreeRank32InterfacePaid":full,
            "smallerFieldRankNeverCalledCharacteristicZeroNonregular":True})
        rec["status"]="completed";code=0
    except BaseException as e:
        rec["status"]="budget-checkpoint" if isinstance(e,TimeoutError) else "failed"
        rec["parameters"]["error"]={"type":type(e).__name__,"message":str(e)}
        code=75 if isinstance(e,TimeoutError) else 1
    finally:
        signal.setitimer(signal.ITIMER_REAL,0);rec["elapsedSeconds"]=time.monotonic()-started
        desc=save_json(out/"original-five-moment-cubic-jacobian-gate-receipt.json",rec)
        print(json.dumps({"status":rec["status"],"exitCode":code,"binding":binding,
              "elapsedSeconds":rec["elapsedSeconds"],"receipt":desc,"parameters":rec["parameters"]},sort_keys=True),flush=True)
    return code
if __name__=="__main__":sys.exit(main())
