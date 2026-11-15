#!/usr/bin/env python3
"""Restore historical byte identities from freshly recomputed temporary phases.

Author: Astra-ISP-789f / root. AI-assisted: GPT-6 Astra Pro.
This never downloads mathematical arrays or changes mathematical entries.
It restores only the gzip timestamp and, for complete-rref, the historical
elapsedSeconds explicitly present in the already published receipt. Acceptance
requires the entire recovered file to match its historical byte count and SHA.
Both original and reconstructed arrays remain temporary in this job.
"""
import argparse,datetime,gzip,hashlib,io,json,os,resource,struct,time
from pathlib import Path

FORMAT="r150-recomputed-temporary-byte-recovery-v1"
def need(ok,msg):
    if not ok:raise AssertionError(msg)
def digest(raw):return hashlib.sha256(raw).hexdigest()
def read(path):return json.loads(Path(path).read_bytes())
def inner(x):return x.get("result",x)
def params(x):return inner(x)["parameters"]
def phases(p):
    for key in ("checkpointPhases","temporaryPhaseFiles","temporaryPhases"):
        if key in p:return p[key]
    raise AssertionError("No complete temporary phase descriptors")
def binding(p):
    for key in ("checkpointBinding","semanticBinding","binding"):
        if key in p:return p[key]
    raise AssertionError("Missing semantic binding")
def name(root,item):
    need(Path(item["file"]).name==item["file"],"Temporary file must be a basename")
    return root/item["file"]
def header_size(raw):
    need(raw[:3]==b"\x1f\x8b\x08","Single gzip deflate stream required")
    flags=raw[3];need(flags&~8==0,"Expected simple gzip FNAME header only")
    return raw.index(b"\x00",10)+1 if flags&8 else 10
def rref_metadata(raw,old):
    o=json.loads(gzip.decompress(raw));need(o["phase"]=="complete-rref","RREF phase")
    events=inner(old).get("events",[])
    values=[e["seconds"] for e in events if "RREF" in e.get("phase","") and "seconds" in e]
    need(len(values)==1,"Historical RREF duration must be an actual unique receipt event")
    need("elapsedSeconds" in o["data"],"Exact RREF duration metadata")
    o["data"]["elapsedSeconds"]=values[0]
    # Match the original gzip.open(...,"wt") buffering and close sequence.
    # TextIOWrapper flushes the gzip stream before its final close.
    output=io.BytesIO()
    with gzip.GzipFile(fileobj=output,filename="",mode="wb",compresslevel=1,mtime=0) as compressed:
        with io.TextIOWrapper(compressed,encoding="utf-8") as text:
            json.dump(o,text,sort_keys=True,separators=(",",":"),ensure_ascii=True)
    rebuilt=output.getvalue()
    return raw[:header_size(raw)]+rebuilt[header_size(rebuilt):]
def timestamp_range(old):
    stamps=[int(datetime.datetime.strptime(p["utc"],"%Y-%m-%d %H:%M:%S UTC").replace(tzinfo=datetime.timezone.utc).timestamp()) for p in old["pulls"]]
    need(len(stamps)>=2,"Actual before/after pull times required")
    lo,hi=min(stamps)-10,max(stamps)+10
    need(0<=hi-lo<=3600,"Bounded historical timestamp interval")
    return lo,hi
def main():
    ap=argparse.ArgumentParser()
    for k in ("paid-receipt","paid-receipt-sha256","new-receipt","temporary-root","out"):
        ap.add_argument("--"+k,required=True)
    ap.add_argument("--manifest")
    ap.add_argument("--manifest-style",choices=("fifth","projection","complete"))
    ap.add_argument("--remaining-seconds",type=float,default=180)
    ap.add_argument("--memory-mib",type=int,default=2048)
    a=ap.parse_args();start=time.monotonic()
    need(0<a.remaining_seconds<=600 and 512<=a.memory_mib<=4096,"Bounded recovery resources")
    resource.setrlimit(resource.RLIMIT_AS,(a.memory_mib*1024**2,)*2)
    need(digest(Path(a.paid_receipt).read_bytes())==a.paid_receipt_sha256,"Exact published historical receipt")
    old=read(a.paid_receipt);new=read(a.new_receipt)
    need(inner(old)["status"]==inner(new)["status"]=="completed","Both actual calculations completed")
    op,np=params(old),params(new)
    need(binding(op)==binding(np),"Freshly recomputed exact source and input binding")
    def script(x):
        r=inner(x);p=r["parameters"]
        return r.get("scriptSHA256",p.get("selfSHA256",p.get("checkpointInputBytes",{}).get("script")))
    need(script(old) is not None and script(old)==script(new),"Unmodified mathematical executable")
    oldph,newph=phases(op),phases(np)
    need(set(oldph)==set(newph),"The same complete mathematical phases")
    root=Path(a.temporary_root).resolve();need(root.is_dir(),"Existing fresh temporary root")
    lo,hi=timestamp_range(old);items=[]
    report={"format":FORMAT,"status":"running","parameters":{"author":"Astra-ISP-789f / root",
        "aiAssisted":"GPT-6 Astra Pro","paidReceiptSHA256":a.paid_receipt_sha256,
        "freshReceiptSHA256":digest(Path(a.new_receipt).read_bytes()),"binding":binding(op),
        "temporaryOnly":True,"largeDataUploadedOrCommitted":False,"mathematicalEntriesModified":False,
        "historicalTimestampRange":[lo,hi],"recoveredPhases":items}}
    def save():
        report["elapsedSeconds"]=time.monotonic()-start
        raw=(json.dumps(report,sort_keys=True,indent=2)+"\n").encode()
        need(len(raw)<95000,"Small recovery receipt")
        out=Path(a.out);out.parent.mkdir(parents=True,exist_ok=True);out.write_bytes(raw)
    try:
        for phase in sorted(oldph):
            need(time.monotonic()-start<a.remaining_seconds,"Recovery budget")
            target=oldph[phase];actual=newph[phase];p=name(root,actual);raw=p.read_bytes()
            need(len(raw)==actual["bytes"] and digest(raw)==actual["sha256"],"Actual new complete phase bytes")
            payload=json.loads(gzip.decompress(raw))
            need(payload["complete"] is True and payload["phase"]==phase and payload["binding"]==binding(op),"Full new phase identity")
            metadata_restored=False
            if phase=="complete-rref":
                raw=rref_metadata(raw,old);metadata_restored=True
            need(len(raw)==target["bytes"],"Recomputed historical compressed byte count: "+phase)
            recovered=None;mtime=None;tries=0
            if digest(raw)==target["sha256"]:recovered=raw;mtime=struct.unpack("<I",raw[4:8])[0]
            else:
                buf=bytearray(raw)
                for stamp in range(hi,lo-1,-1):
                    need(time.monotonic()-start<a.remaining_seconds,"Timestamp recovery budget")
                    struct.pack_into("<I",buf,4,stamp);tries+=1
                    if digest(buf)==target["sha256"]:
                        recovered=bytes(buf);mtime=stamp;break
            need(recovered is not None,"Full historical SHA mismatch: "+phase)
            need(len(recovered)==target["bytes"] and digest(recovered)==target["sha256"],"Full recovered identity")
            dest=name(root,target)
            if dest.exists():need(dest.read_bytes()==recovered,"Never overwrite a different existing checkpoint")
            else:
                temp=dest.with_name(dest.name+".recovery-tmp");temp.write_bytes(recovered);os.replace(temp,dest)
            items.append({"phase":phase,"bytes":target["bytes"],"sha256":target["sha256"],
                "gzipMtime":mtime,"timestampAttempts":tries,"historicalRrefDurationRestored":metadata_restored,
                "allFileBytesMatchHistoricalSHA256":True})
            save()
        if a.manifest:
            need(Path(a.manifest).name==a.manifest and a.manifest_style,"Explicit temporary manifest style")
            path=root/a.manifest;fresh=read(path)
            need(fresh["binding"]==binding(op) and fresh["phases"]==newph and fresh["temporaryOnly"] is True,"Fresh actual complete manifest")
            historical=dict(fresh);historical["phases"]=oldph
            if a.manifest_style=="fifth":
                raw=json.dumps(historical,sort_keys=True,indent=2).encode()
                expected=op["checkpointManifestSHA256"]
            elif a.manifest_style=="projection":
                raw=(json.dumps(historical,sort_keys=True,indent=2)+"\n").encode()
                expected=op["temporaryManifestSHA256"]
            else:
                raw=json.dumps(historical,sort_keys=True,separators=(",",":"),ensure_ascii=True).encode("ascii")
                expected=op["temporaryManifestSHA256"]
            need(digest(raw)==expected,"Every historical manifest byte matches its published hash")
            freshcopy=path.with_name(path.name+".fresh-"+digest(path.read_bytes()))
            if not freshcopy.exists():freshcopy.write_bytes(path.read_bytes())
            path.write_bytes(raw)
            report["parameters"]["recoveredManifest"]={"bytes":len(raw),"sha256":expected,"allPhasesMaterialized":True}
        report["status"]="completed";report["outcome"]="fresh-original-calculations-match-all-historical-temporary-bytes";save()
    except BaseException as e:
        report["status"]="failed";report["error"]=type(e).__name__+": "+str(e);save();raise
    print(json.dumps({"status":report["status"],"phases":len(items),"receipt":a.out,"elapsedSeconds":report["elapsedSeconds"]}),flush=True)
if __name__=="__main__":main()
