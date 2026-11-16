#!/usr/bin/env python3
"""Sixteen exact original cubic-border source columns over the matched field.

Author: Astra-ISP-789f / normal_annihilator.
AI-assisted: GPT-6 Astra Pro. Date: 2026-11-16.
Use the actual35 original leading source columns and only16 needed
cubic right-hand sides. Represent E^35 faithfully as Q^105, solve the
fixed constant unit by exact Dixon, save every complete candidate
before verification, then verify all105x16 original products.
No lower-parameter remainder or border commutator is asserted here.
"""
import argparse,gzip,hashlib,itertools,json,os,resource,signal,sys,time
from pathlib import Path
from flint import fmpq,fmpq_poly,fmpq_mat

FORMAT="r150-original-sixteen-cubic-border-constant-source-solve-v1"
PARENT={"bytes":1653920,"sha256":"005484500176a294a3a14788843f1ad50031f2e2bce3e599c512e45ac5dacbb6",
"logicalSha256":"da5839f34930081d56df84d9d803daf2b226ac98de8364135463f6f94b6db1d2",
"binding":"41ee91c353da2b8a33bbb631d46bc48e11709dcf42e131ebf4d417c7a3e98b63"}
MATCHED=[52565262336,6080833024,-43931504,3725]
FMOD=fmpq_poly([fmpq(x,MATCHED[-1]) for x in MATCHED])
def need(b,s):
    if not b:raise ValueError(s)
def canon(x):return json.dumps(x,sort_keys=True,separators=(",",":")).encode()
def sha(x):return hashlib.sha256(x).hexdigest()
def save_json(p,x):
    b=json.dumps(x,sort_keys=True,indent=2).encode();t=p.with_name(p.name+".tmp");t.write_bytes(b);os.replace(t,p)
    return {"path":p.name,"bytes":len(b),"sha256":sha(b)}
def save_gz(p,x):
    b=canon(x);z=gzip.compress(b,compresslevel=1,mtime=0);t=p.with_name(p.name+".tmp");t.write_bytes(z);os.replace(t,p)
    return {"path":p.name,"bytes":len(z),"sha256":sha(z),"logicalBytes":len(b),"logicalSha256":sha(b)}
def key(t):
    e=[0]*5
    for i in t:e[i]+=1
    return tuple(e)
def main():
    ap=argparse.ArgumentParser();ap.add_argument("--leading-out",required=True);ap.add_argument("--out",required=True)
    ap.add_argument("--seconds",type=float,default=180);ap.add_argument("--memory-mib",type=int,default=4096);a=ap.parse_args()
    need(0<a.seconds<=600 and 1024<=a.memory_mib<=8192,"bounded exact cubic constant-source solve")
    resource.setrlimit(resource.RLIMIT_AS,(a.memory_mib*1024**2,)*2);out=Path(a.out);out.mkdir(parents=True,exist_ok=True)
    start=time.monotonic();ss=sha(Path(__file__).read_bytes());binding=sha(canon({"format":FORMAT,"sourceSha256":ss,"parent":PARENT,"matchedCubic":MATCHED,"algorithm":"dixon"}))
    rec={"format":FORMAT,"binding":binding,"sourceSha256":ss,"parameters":{"seconds":a.seconds,"memoryMiB":a.memory_mib}}
    def event(phase):
        rec["parameters"]["lastCompletedPhase"]=phase;print(json.dumps({"phase":phase,"elapsedSeconds":time.monotonic()-start}),flush=True)
    def timeout(sig,fr):raise TimeoutError("bounded original constant cubic source solve")
    signal.signal(signal.SIGALRM,timeout);signal.setitimer(signal.ITIMER_REAL,a.seconds);code=1
    try:
        path=Path(a.leading_out)/"complete-original-eleven-quadratic-leading-model.json.gz";z=path.read_bytes()
        need(len(z)==PARENT["bytes"] and sha(z)==PARENT["sha256"],"whole original leading source file")
        raw=gzip.decompress(z);need(sha(raw)==PARENT["logicalSha256"],"whole original leading logical file")
        p=json.loads(raw);need(p["binding"]==PARENT["binding"],"same original leading-source binding");d=p["data"]
        need(d["matchedCubic"]==MATCHED,"same complete matched field")
        q=[{tuple(e):fmpq_poly([fmpq(x) for x in v]) for e,v in row} for row in d["allElevenLeadingQuadratics"]]
        mons=[tuple(e) for e in d["all35CubicOutputMonomials"]];need(len(mons)==35 and len(set(mons))==35,"all original cubic outputs")
        ix={e:i for i,e in enumerate(mons)};cols=d["actualFieldCertificate"]["completeCubicSelectedOriginalColumns"]
        need(len(cols)==35 and len(set(cols))==35,"actual original35 source unit columns")
        sourceLabels=d["all55OriginalCubicSourceColumns"];need(len(sourceLabels)==55,"complete parent original source dictionary")
        A=[[fmpq_poly() for _ in cols] for _ in mons]
        for j,c in enumerate(cols):
            g,k=divmod(c,5);label=sourceLabels[c]
            need(label=={"gradient":"du%d"%g if g<5 else "NFdw%d"%(g-5),"multiplierU":k},"exact original source label")
            for e,v in q[g].items():
                t=list(e);t[k]+=1;A[ix[tuple(t)]][j]+=v
        border=set()
        for v in d["tenOriginalGeneratingMonomials"][6:]:
            for k in range(5):
                t=list(v);t[k]+=1;border.add(tuple(t))
        targets=[e for e in mons if e in border];need(len(targets)==16,"all16 distinct original cubic border monomials")
        Q=fmpq_mat(105,105);R=fmpq_mat(105,16)
        multiplicationCoordinates=0
        for i in range(35):
            for j in range(35):
                for k in range(3):
                    product=(A[i][j]*fmpq_poly([0]*k+[1]))%FMOD
                    for l in range(3):Q[3*i+l,3*j+k]=product[l];multiplicationCoordinates+=1
        for j,e in enumerate(targets):R[3*ix[e],j]=1
        rec["parameters"].update({"regularRepresentationShape":[105,105],"rightHandSides":16,
            "all11025OriginalFieldMultiplicationCoordinatesConstructed":multiplicationCoordinates==11025,
            "selectedOriginalSourceColumns":cols,"targetMonomials":[list(e) for e in targets]})
        event("complete-original-constant-unit-and-sixteen-right-hand-sides")
        ts=time.monotonic();X=Q.solve(R,algorithm="dixon");solveSeconds=time.monotonic()-ts
        need(X.nrows()==105 and X.ncols()==16,"all complete exact source coordinates returned")
        rec["parameters"]["dixonSolveSeconds"]=solveSeconds;event("complete-exact-dixon-candidates-returned")
        candidates=[]
        for j,e in enumerate(targets):
            col=[[str(X[3*i+k,j]) for k in range(3)] for i in range(35)]
            desc=save_gz(out/("complete-original-border-source-%02d.json.gz"%(j+1)),
                {"format":FORMAT+"-complete-candidate","binding":binding,
                 "data":{"targetIndex":j,"targetMonomial":list(e),"selectedOriginalSourceColumns":cols,
                         "completeEFieldSourceCoefficients":col,"savedBeforeOriginalProductVerification":True}})
            candidates.append(desc)
            save_json(out/"original-cubic-source-candidate-checkpoint.json",{"format":FORMAT+"-candidate-checkpoint","binding":binding,"completeCandidates":candidates})
        rec["parameters"]["completeCandidateColumns"]=candidates;event("all16-complete-original-E-columns-saved")
        product=Q*X
        verified=0
        for i in range(105):
            for j in range(16):
                need(product[i,j]==R[i,j],"all1680 exact original regular-coordinate cubic products");verified+=1
        need(verified==1680,"complete original cubic source verification")
        verifiedModel=save_gz(out/"complete-verified-original-cubic-border-sources.json.gz",
            {"format":FORMAT+"-verified-model","binding":binding,"data":{
                "parentBinding":PARENT["binding"],"matchedCubic":MATCHED,
                "selectedOriginalSourceColumns":cols,"selectedOriginalSourceLabels":[sourceLabels[c] for c in cols],
                "all35OriginalCubicOutputMonomials":[list(e) for e in mons],
                "all16OriginalBorderMonomials":[list(e) for e in targets],"completeVerifiedSourceColumns":candidates,
                "all1680OriginalRationalProductsVerified":True,"all560OriginalEProductsVerified":True,
                "identity":"borderMonomial_j=sum_i source_ij * (u_k * originalLeadingQuadratic_g)",
                "fullParameterBorderRemaindersComputed":False}})
        rec["parameters"].update({"model":verifiedModel,"all1680OriginalRationalProductsVerified":True,
           "all560OriginalEProductsVerified":True,"all16CompleteCandidateColumnsSavedBeforeVerification":True,
           "all35OriginalOutputCoordinatesRetained":True,"allOriginalConstantSourceLabelsRetained":True,
           "noParameterSpecializedOrInverted":True,"fullParameterBorderRemaindersComputed":False})
        rec["status"]="completed";code=0
    except BaseException as e:
        rec["status"]="budget-checkpoint" if isinstance(e,TimeoutError) else "failed";rec["parameters"]["error"]={"type":type(e).__name__,"message":str(e)}
        code=75 if isinstance(e,TimeoutError) else 1
    finally:
        signal.setitimer(signal.ITIMER_REAL,0);rec["elapsedSeconds"]=time.monotonic()-start;rec["maxResidentKiB"]=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
        desc=save_json(out/"original-cubic-border-source-solve-receipt.json",rec)
        print(json.dumps({"status":rec["status"],"exitCode":code,"binding":binding,"elapsedSeconds":rec["elapsedSeconds"],"receipt":desc,"parameters":rec["parameters"]},sort_keys=True),flush=True)
    return code
if __name__=="__main__":sys.exit(main())
