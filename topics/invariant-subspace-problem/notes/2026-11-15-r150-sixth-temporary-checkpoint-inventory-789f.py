#!/usr/bin/env python3
"""Read-only inventory of actual temporary R150 sixth checkpoints.
Never decompresses a matrix or starts any mathematical computation.
SHA256 is streamed from existing files; no file contents are printed.
"""
import argparse
import hashlib
import json
import os
from pathlib import Path
import signal
import time

STOP=False
def stop(signum,frame):
    global STOP
    STOP=True

def file_hash(path,deadline):
    h=hashlib.sha256();n=0
    with path.open("rb") as f:
        while True:
            if STOP or time.monotonic()>=deadline:
                return None,n
            b=f.read(1024*1024)
            if not b: return h.hexdigest(),n
            h.update(b);n+=len(b)

def main():
    p=argparse.ArgumentParser()
    p.add_argument("--checkpoint-dir",required=True)
    p.add_argument("--prepared-cochain-dir")
    p.add_argument("--out",required=True)
    p.add_argument("--remaining-seconds",type=float,default=10.0)
    a=p.parse_args()
    if not a.remaining_seconds>0: raise ValueError("Positive shared time")
    started=time.monotonic();deadline=started+a.remaining_seconds
    signal.signal(signal.SIGALRM,stop);signal.setitimer(signal.ITIMER_REAL,a.remaining_seconds)
    roots=[("sixth",Path(a.checkpoint_dir),"sixth-checkpoint.json")]
    if a.prepared_cochain_dir:
        roots.append(("paid-fifth",Path(a.prepared_cochain_dir),
                      "fifth-joint-high-low-checkpoint.json"))
    result={"format":"r150-sixth-temporary-read-only-inventory-v1",
            "status":"completed","parameters":{
                "sharedSeconds":a.remaining_seconds,
                "noMathematicalComputation":True,
                "noMatrixPayloadDecompressed":True,
                "noExistingFilesModified":True,
                "directories":[]}}
    for label,directory,manifestname in roots:
        entry={"label":label,"directory":str(directory),"exists":directory.is_dir(),
               "manifest":None,"files":[]}
        result["parameters"]["directories"].append(entry)
        if not directory.is_dir(): continue
        claims={}
        manifest=directory/manifestname
        if manifest.is_file() and not manifest.is_symlink():
            size=manifest.stat().st_size
            info={"file":manifestname,"bytes":size}
            entry["manifest"]=info
            if size<=100000:
                raw=manifest.read_bytes()
                info["sha256"]=hashlib.sha256(raw).hexdigest()
                obj=json.loads(raw)
                info["format"]=obj.get("format")
                info["binding"]=obj.get("binding")
                info["temporaryOnly"]=obj.get("temporaryOnly")
                info["phases"]={}
                for phase,e in obj.get("phases",{}).items():
                    keep={k:e[k] for k in ("file","bytes","sha256","matrixSHA256",
                                          "shape","verified") if k in e}
                    info["phases"][phase]=keep
                    claims[e.get("file")]=(phase,e)
            else:
                info["notReadBecauseOversized"]=True
        for file in sorted(directory.iterdir(),key=lambda x:x.name):
            if not file.is_file() or file.is_symlink(): continue
            size=file.stat().st_size
            f={"file":file.name,"bytes":size}
            if file.name in claims:
                phase,e=claims[file.name]
                f["manifestPhase"]=phase
                f["manifestReportedVerified"]=e.get("verified")
                f["manifestSHA256Claim"]=e.get("sha256")
                f["manifestByteCountMatches"]=(size==e.get("bytes"))
            digest,n=file_hash(file,deadline)
            f["sha256"]=digest;f["bytesHashed"]=n
            if digest is None:
                f["hashIncomplete"]=True;result["status"]="incomplete"
            elif file.name in claims:
                f["manifestSHA256Matches"]=(digest==claims[file.name][1].get("sha256"))
            entry["files"].append(f)
            if STOP or time.monotonic()>=deadline:
                result["status"]="incomplete";break
        if STOP or time.monotonic()>=deadline: break
    signal.setitimer(signal.ITIMER_REAL,0)
    result["elapsedSeconds"]=time.monotonic()-started
    result["scriptSHA256"]=hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    raw=json.dumps(result,sort_keys=True,indent=2).encode()
    if len(raw)>=100000: raise ValueError("Small inventory receipt limit")
    out=Path(a.out);out.parent.mkdir(parents=True,exist_ok=True)
    tmp=out.with_name(out.name+".tmp");tmp.write_bytes(raw);os.replace(tmp,out)
    print(json.dumps({"status":result["status"],"receipt":str(out),
                      "receiptBytes":len(raw),
                      "receiptSHA256":hashlib.sha256(raw).hexdigest(),
                      "elapsedSeconds":result["elapsedSeconds"]}),flush=True)

if __name__=="__main__":
    main()
