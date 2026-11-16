#!/usr/bin/env python3
"""Verify all saved original cubic-border sources without repeating Dixon.

Author: Astra-ISP-789f / normal_annihilator.
AI-assisted: GPT-6 Astra Pro. Date: 2026-11-16.
Rebuild the exact original E35 unit, read all16 actual saved candidates,
clear rational denominators by one positive integer per row/column,
and multiply back all105x16 original rational coordinates.
The old budget-checkpoint receipt and candidates are never modified.
"""
import argparse,gzip,hashlib,json,math,os,resource,signal,sys,time
from pathlib import Path
from flint import fmpq,fmpq_poly,fmpq_mat,fmpz_mat
FORMAT="r150-original-sixteen-cubic-border-integer-product-verification-v1"
PARENT={"bytes":1653920,"sha256":"005484500176a294a3a14788843f1ad50031f2e2bce3e599c512e45ac5dacbb6",
"logicalSha256":"da5839f34930081d56df84d9d803daf2b226ac98de8364135463f6f94b6db1d2",
"binding":"41ee91c353da2b8a33bbb631d46bc48e11709dcf42e131ebf4d417c7a3e98b63"}
CANDIDATE_BINDING="883430390f24f79cf127df1df44645f091b345372ef2b36915c212c1787ae35e"
CHECKPOINT={"bytes":5041,"sha256":"c477bbb0acc38c651a011f76cd0433273825cf14e51883de51f857a933714dfb"}
RECEIPT={"bytes":7450,"sha256":"58c7b7686a7334aa966e0b0efcf4b62e2bbc3814f75d1da8624f278313971cc4"}
MATCHED=[52565262336,6080833024,-43931504,3725]
FMOD=fmpq_poly([fmpq(x,MATCHED[-1]) for x in MATCHED])
def need(b,s):
    if not b:raise ValueError(s)
def canon(x):return json.dumps(x,sort_keys=True,separators=(",",":")).encode()
def sha(x):return hashlib.sha256(x).hexdigest()
def raw_read(p,desc):
    b=p.read_bytes();need(len(b)==desc["bytes"] and sha(b)==desc["sha256"],"whole actual input bytes: "+p.name);return b
def read_gz(p,desc):
    b=gzip.decompress(raw_read(p,desc));need(sha(b)==desc["logicalSha256"],"whole actual logical input: "+p.name);return json.loads(b)
def save_json(p,x):
    b=json.dumps(x,sort_keys=True,indent=2).encode();t=p.with_name(p.name+".tmp");t.write_bytes(b);os.replace(t,p)
    return {"path":p.name,"bytes":len(b),"sha256":sha(b)}
def save_gz(p,x):
    b=canon(x);z=gzip.compress(b,compresslevel=1,mtime=0);t=p.with_name(p.name+".tmp");t.write_bytes(z);os.replace(t,p)
    return {"path":p.name,"bytes":len(z),"sha256":sha(z),"logicalBytes":len(b),"logicalSha256":sha(b)}
def main():
    ap=argparse.ArgumentParser();ap.add_argument("--leading-out",required=True);ap.add_argument("--candidate-out",required=True)
    ap.add_argument("--out",required=True);ap.add_argument("--seconds",type=float,default=180);ap.add_argument("--memory-mib",type=int,default=4096);a=ap.parse_args()
    need(0<a.seconds<=300 and 512<=a.memory_mib<=8192,"bounded exact source verification")
    resource.setrlimit(resource.RLIMIT_AS,(a.memory_mib*1024**2,)*2);out=Path(a.out);out.mkdir(parents=True,exist_ok=True)
    start=time.monotonic();source_sha=sha(Path(__file__).read_bytes())
    binding=sha(canon({"format":FORMAT,"sourceSha256":source_sha,"parent":PARENT,"candidateBinding":CANDIDATE_BINDING,"candidateCheckpoint":CHECKPOINT,"candidateReceipt":RECEIPT}))
    rec={"format":FORMAT,"binding":binding,"sourceSha256":source_sha,"parameters":{"seconds":a.seconds,"memoryMiB":a.memory_mib}}
    def event(phase):
        rec["parameters"]["lastCompletedPhase"]=phase;print(json.dumps({"phase":phase,"elapsedSeconds":time.monotonic()-start}),flush=True)
    def timeout(sig,fr):raise TimeoutError("bounded complete original integer-product verification")
    signal.signal(signal.SIGALRM,timeout);signal.setitimer(signal.ITIMER_REAL,a.seconds);code=1
    try:
        candidate_out=Path(a.candidate_out)
        cp=json.loads(raw_read(candidate_out/"original-cubic-source-candidate-checkpoint.json",CHECKPOINT))
        oldrec=json.loads(raw_read(candidate_out/"original-cubic-border-source-solve-receipt.json",RECEIPT))
        need(cp["binding"]==oldrec["binding"]==CANDIDATE_BINDING,"same actual saved candidate binding")
        need(oldrec["status"]=="budget-checkpoint" and oldrec["parameters"]["lastCompletedPhase"]=="all16-complete-original-E-columns-saved","accurate old verified scope")
        descriptors=cp["completeCandidates"];need(len(descriptors)==16 and descriptors==oldrec["parameters"]["completeCandidateColumns"],"all16 complete actual candidate descriptors")
        model=read_gz(Path(a.leading_out)/"complete-original-eleven-quadratic-leading-model.json.gz",PARENT)
        need(model["binding"]==PARENT["binding"],"same original source parent binding");d=model["data"]
        need(d["matchedCubic"]==MATCHED,"same matched cubic field")
        q=[{tuple(e):fmpq_poly([fmpq(x) for x in v]) for e,v in row} for row in d["allElevenLeadingQuadratics"]]
        mons=[tuple(e) for e in d["all35CubicOutputMonomials"]];need(len(mons)==35 and len(set(mons))==35,"all35 original outputs")
        ix={e:i for i,e in enumerate(mons)};cols=d["actualFieldCertificate"]["completeCubicSelectedOriginalColumns"];need(cols==list(range(35)),"actual paid original unit selection")
        labels=d["all55OriginalCubicSourceColumns"];need(len(labels)==55,"complete original source dictionary")
        A=[[fmpq_poly() for _ in range(35)] for _ in range(35)]
        for j,c in enumerate(cols):
            g,k=divmod(c,5);need(labels[c]=={"gradient":"du%d"%g if g<5 else "NFdw%d"%(g-5),"multiplierU":k},"original selected source label")
            for e,v in q[g].items():
                t=list(e);t[k]+=1;A[ix[tuple(t)]][j]+=v
        border=set()
        for v in d["tenOriginalGeneratingMonomials"][6:]:
            for k in range(5):
                t=list(v);t[k]+=1;border.add(tuple(t))
        targets=[e for e in mons if e in border];need(len(targets)==16,"complete16 distinct border targets")
        Q=fmpq_mat(105,105)
        for i in range(35):
            for j in range(35):
                for k in range(3):
                    v=(A[i][j]*fmpq_poly([0]*k+[1]))%FMOD
                    for l in range(3):Q[3*i+l,3*j+k]=v[l]
        X=fmpq_mat(105,16)
        for j,desc in enumerate(descriptors):
            o=read_gz(candidate_out/desc["path"],desc);need(o["binding"]==CANDIDATE_BINDING,"actual candidate binding")
            c=o["data"];need(c["targetIndex"]==j and c["targetMonomial"]==list(targets[j]) and c["selectedOriginalSourceColumns"]==cols,"complete candidate original target/source coordinates")
            need(c["savedBeforeOriginalProductVerification"] is True,"no old verification claim")
            co=c["completeEFieldSourceCoefficients"];need(len(co)==35 and all(len(v)==3 for v in co),"complete35 original E source coordinates")
            for i in range(35):
                for k in range(3):X[3*i+k,j]=fmpq(co[i][k])
        event("complete-original-unit-and-all16-candidates-rebuilt")
        rowD=[math.lcm(*(int(Q[i,j].denom()) for j in range(105))) for i in range(105)]
        colD=[math.lcm(*(int(X[i,j].denom()) for i in range(105))) for j in range(16)]
        need(all(v>0 for v in rowD+colD),"positive exact rational scale factors")
        U=fmpz_mat(105,105);N=fmpz_mat(105,16)
        for i in range(105):
            for j in range(105):
                v=Q[i,j]*rowD[i];need(v.denom()==1,"whole original unit row scaling");U[i,j]=v.numer()
        for i in range(105):
            for j in range(16):
                v=X[i,j]*colD[j];need(v.denom()==1,"whole original candidate column scaling");N[i,j]=v.numer()
        del Q,X
        event("all-row-and-column-rational-scale-identities-verified")
        product=U*N;verified=0
        for i in range(105):
            for j,e in enumerate(targets):
                expect=rowD[i]*colD[j] if i==3*ix[e] else 0
                need(product[i,j]==expect,"full original rational cubic source product via positive integer scales");verified+=1
        need(verified==1680,"all1680 complete original rational products")
        verifiedModel=save_gz(out/"complete-verified-original-cubic-border-sources.json.gz",{"format":FORMAT+"-verified-model","binding":binding,"data":{
            "parentBinding":PARENT["binding"],"candidateBinding":CANDIDATE_BINDING,"candidateCheckpoint":CHECKPOINT,"candidateReceipt":RECEIPT,
            "matchedCubic":MATCHED,"selectedOriginalSourceColumns":cols,"selectedOriginalSourceLabels":[labels[c] for c in cols],
            "all35OriginalCubicOutputMonomials":[list(e) for e in mons],"all16OriginalBorderMonomials":[list(e) for e in targets],
            "completeVerifiedSourceColumns":descriptors,"all1680OriginalRationalProductsVerified":True,"all560OriginalEProductsVerified":True,
            "identity":"borderMonomial_j=sum_i source_ij*(u_k*originalLeadingQuadratic_g)",
            "fullParameterBorderRemaindersComputed":False}})
        rec["parameters"].update({"model":verifiedModel,"all16ActualCandidateByteAndLogicalHashesVerified":True,"sameCompleteOriginalUnitRebuilt":True,
            "all11025OriginalUnitRowScaleIdentitiesVerified":True,"all1680OriginalSourceColumnScaleIdentitiesVerified":True,
            "all1680OriginalRationalProductsVerified":True,"all560OriginalEProductsVerified":True,"completeOriginalProducts":verified,
            "all35OriginalOutputCoordinatesRetained":True,"all16OriginalBorderTargetsRetained":True,"dixonRepeated":False,
            "maximumRowDenominatorBits":max(v.bit_length() for v in rowD),"maximumColumnDenominatorBits":max(v.bit_length() for v in colD),
            "noParameterSpecializedOrInverted":True,"fullParameterBorderRemaindersComputed":False})
        rec["status"]="completed";code=0;event("all16-complete-original-cubic-source-certificates-verified")
    except BaseException as e:
        rec["status"]="budget-checkpoint" if isinstance(e,TimeoutError) else "failed";rec["parameters"]["error"]={"type":type(e).__name__,"message":str(e)}
        code=75 if isinstance(e,TimeoutError) else 1
    finally:
        signal.setitimer(signal.ITIMER_REAL,0);rec["elapsedSeconds"]=time.monotonic()-start;rec["maxResidentKiB"]=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
        desc=save_json(out/"original-cubic-border-source-verification-receipt.json",rec)
        print(json.dumps({"status":rec["status"],"exitCode":code,"binding":binding,"elapsedSeconds":rec["elapsedSeconds"],"receipt":desc,"parameters":rec["parameters"]},sort_keys=True),flush=True)
    return code
if __name__=="__main__":sys.exit(main())

