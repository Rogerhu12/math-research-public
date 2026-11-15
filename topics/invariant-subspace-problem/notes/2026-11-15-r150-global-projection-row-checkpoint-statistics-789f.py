#!/usr/bin/env python3
"""Read-only statistics of an actual R150 polynomial-row-module checkpoint.
AI (ChatGPT / literature_audit), 2026-11-15 UTC.
No FLINT import, polynomial reduction, new original product, or mutation of parent.
"""
import argparse
import gzip
import hashlib
import json
import os
from pathlib import Path
import resource
import signal
import sys
import time

BINDING="ce358eac629541da0c9d35fd29c66424fa0d89ded97cfec93f324cf56e9d16ba"
MANIFEST_SHA="c43828673dc6513c43042e4452c91d146e78a26a15b3b82aa3f9e8a87ff49aa9"
STATE_SHA="42d998c95906cf0ad9e8cef8660b115027e4ad671b332ca6493bb025f237ff41"
STATE_BYTES=72400441
PAYLOAD_SHA="52d7d5f3b735ab0b3da8465f888485b0a29168b49502cfadb9770313f7c8dd4f"

def require(ok,msg):
    if not ok:
        raise AssertionError(msg)

def canonical(x):
    return json.dumps(x,ensure_ascii=True,sort_keys=True,separators=(",",":")).encode()

def identity(path):
    h=hashlib.sha256();n=0
    with Path(path).open("rb") as f:
        for b in iter(lambda:f.read(1<<20),b""):
            h.update(b);n+=len(b)
    return {"bytes":n,"sha256":h.hexdigest()}

def larger(a,b):
    a=a.lstrip("-").lstrip("0") or "0"
    b=b.lstrip("-").lstrip("0") or "0"
    return a if (len(a),a)>(len(b),b) else b

def summarize(rows,label):
    maxnum="0";maxden="1";degree=-1;npoly=0;ncoeff=0;chars=0
    perrow=[];hist={}
    for i,row in enumerate(rows):
        if row is None:
            continue
        rn="0";rd="1";rdegree=-1;rp=0;rc=0;rchars=0
        lead=None
        for j,p in enumerate(row):
            if not p:
                continue
            require(p[-1]!="0","Canonical polynomial trailing coefficient")
            rp+=1;rc+=len(p);rdegree=max(rdegree,len(p)-1)
            hist[str(len(p)-1)]=hist.get(str(len(p)-1),0)+1
            candidate=(len(p)-1,j)
            if lead is None or candidate>lead:
                lead=candidate
            for v in p:
                require(isinstance(v,str),"Rational coefficient text")
                a,sep,b=v.partition("/")
                if not sep:
                    b="1"
                require(a.lstrip("-").isdigit() and b.isdigit() and int(b[:1])>=0,
                        "Canonical rational coefficient syntax")
                require(b!="0","Nonzero denominator")
                rn=larger(rn,a);rd=larger(rd,b)
                rchars+=len(v)
        maxnum=larger(maxnum,rn);maxden=larger(maxden,rd)
        degree=max(degree,rdegree);npoly+=rp;ncoeff+=rc;chars+=rchars
        perrow.append({"slot":i,"columns":len(row),"nonzeroPolynomials":rp,
                       "maximumDegree":rdegree,"coefficientCount":rc,
                       "rationalTextCharacters":rchars,
                       "maximumNumeratorBits":int(rn).bit_length(),
                       "maximumDenominatorBits":int(rd).bit_length(),
                       "leadingPosition":None if lead is None else lead[1],
                       "leadingDegree":None if lead is None else lead[0]})
    return {"label":label,"nonemptyRows":len(perrow),"nonzeroPolynomials":npoly,
            "coefficientCount":ncoeff,"rationalTextCharacters":chars,
            "maximumDegree":degree,"maximumNumeratorBits":int(maxnum).bit_length(),
            "maximumDenominatorBits":int(maxden).bit_length(),
            "degreeHistogram":hist,"rows":perrow}

def main():
    p=argparse.ArgumentParser()
    p.add_argument("--checkpoint-dir",required=True)
    p.add_argument("--out",required=True)
    p.add_argument("--remaining-seconds",type=float,default=60)
    a=p.parse_args()
    require(a.remaining_seconds>0,"Positive budget")
    resource.setrlimit(resource.RLIMIT_AS,(4096*1024**2,4096*1024**2))
    sys.set_int_max_str_digits(0)
    signal.signal(signal.SIGALRM,lambda sig,frame: (_ for _ in ()).throw(TimeoutError("Read-only diagnostic time")))
    signal.setitimer(signal.ITIMER_REAL,a.remaining_seconds)
    started=time.monotonic()
    result={"format":"r150-row-module-checkpoint-read-only-statistics-v1","status":"started",
            "parameters":{"binding":BINDING,"parentMathematicsUnchanged":True,
                          "doesNotVerifyOrAdvanceCandidateBasis":True,
                          "memoryMiB":4096,"remainingSeconds":a.remaining_seconds}}
    try:
        root=Path(a.checkpoint_dir)
        manifest_path=root/"checkpoint-manifest.json"
        mid=identity(manifest_path)
        require(mid["sha256"]==MANIFEST_SHA,"Exact actual parent manifest")
        manifest=json.loads(manifest_path.read_text())
        require(manifest["binding"]==BINDING,"Actual parent binding")
        record=manifest["phases"]["row-module-state"]
        require(record["bytes"]==STATE_BYTES and record["sha256"]==STATE_SHA and
                record["payloadSha256"]==PAYLOAD_SHA,"Actual source checkpoint identities")
        state_path=root/record["file"]
        t=time.monotonic();sid=identity(state_path)
        require(sid=={"bytes":STATE_BYTES,"sha256":STATE_SHA},"Actual state bytes")
        checksum_seconds=time.monotonic()-t
        t=time.monotonic()
        with gzip.open(state_path,"rb") as f:
            raw=f.read()
        decompress_seconds=time.monotonic()-t
        require(hashlib.sha256(raw).hexdigest()==PAYLOAD_SHA,"Actual canonical payload SHA")
        rawsize=len(raw)
        t=time.monotonic();obj=json.loads(raw);del raw
        parse_seconds=time.monotonic()-t
        require(obj["binding"]==BINDING and obj["phase"]=="row-module-state",
                "Actual payload binding")
        state=obj["payload"]
        t=time.monotonic()
        stats=[summarize(state["basis"],"basis"),
               summarize(state["provenance"],"basisProvenance"),
               summarize([state["current"]],"current"),
               summarize([state["currentProvenance"]],"currentProvenance")]
        scan_seconds=time.monotonic()-t
        pending=any(state["current"])
        result["status"]="completed"
        result["parameters"].update({
            "manifest":mid,"stateFile":sid,"canonicalPayloadBytes":rawsize,
            "canonicalPayloadSha256":PAYLOAD_SHA,
            "inputRowsStarted":state["nextInputRow"],
            "completedInputRows":state["nextInputRow"]-int(pending),
            "hasPendingNonzeroInputRow":pending,
            "operations":state["operations"],"sections":stats,
            "readStageSeconds":{"fileChecksum":checksum_seconds,
                               "decompress":decompress_seconds,"parse":parse_seconds,
                               "coefficientScan":scan_seconds},
            "candidateOnly":True,"newRowOperations":0,"newOriginalProducts":0})
    except BaseException as e:
        result["status"]="failed"
        result["error"]={"type":type(e).__name__,"message":str(e)}
    finally:
        signal.setitimer(signal.ITIMER_REAL,0)
        result["elapsedSeconds"]=time.monotonic()-started
        out=Path(a.out);out.mkdir(parents=True,exist_ok=True)
        data=canonical(result)
        require(len(data)<40000,"Small statistics receipt")
        target=out/"row-module-checkpoint-statistics.json"
        tmp=target.with_name(target.name+".tmp-"+str(os.getpid()))
        tmp.write_bytes(data);os.replace(tmp,target)
        print(data.decode(),flush=True)
    return 0 if result["status"]=="completed" else 1

if __name__=="__main__":
    raise SystemExit(main())
