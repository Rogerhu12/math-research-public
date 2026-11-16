#!/usr/bin/env python3
"""Read-only diagnosis and exact compact completion of the failed E8 receipt.

Astra-ISP-789f / literature_audit; AI-assisted GPT-6 Astra Pro,2026-11-16.
The frozen mathematical compute function is replayed only when its verified
complete cochain already exists. All phase writes and new RREF are forbidden.
"""
import argparse
import gzip
import hashlib
import importlib.util
import json
from pathlib import Path
import resource
import signal
import sys
import time

FORMAT="r150-critical-e8-readonly-complete-pack-recovery-v1"
FIRST_SHA="4938d26273a72b16185af28c185ea304771a4c91cea0054b1a538de1ef0993ad"
FAILED_SHA="1bbd8ff2cdb5e734e5d294d8510c01b0b47bc505a2ff693c059f5e65e6ffbfde"
FAILED_BYTES=6141
OLD_BINDING="60419855f26164ad652d38a00de0f467bc69722e9a558020611cc7ecc7b6e2d2"

def require(ok,message):
    if not ok:raise AssertionError(message)
def canonical(x):
    return json.dumps(x,sort_keys=True,separators=(",",":")).encode()
def sha_file(p):
    h=hashlib.sha256()
    with open(p,"rb") as f:
        for b in iter(lambda:f.read(1048576),b""):h.update(b)
    return h.hexdigest()
def module_at(name,path):
    spec=importlib.util.spec_from_file_location(name,path)
    m=importlib.util.module_from_spec(spec);sys.modules[name]=m;spec.loader.exec_module(m)
    return m

class BudgetStop(Exception):
    pass

class ReadOnlyReplay:
    def __init__(self,inner):
        self.inner=inner;self.manifest=inner.manifest;self.checkedWrites=0
    def get(self,name):
        require(name in self.manifest["stages"],"No new mathematical phase is allowed: "+name)
        return self.inner.get(name)
    def put(self,name,obj,verified):
        require(name in self.manifest["stages"],"No new mathematical phase is allowed: "+name)
        r=self.manifest["stages"][name]
        require(r["verified"]==bool(verified) and self.inner.get(name)==obj,
                "Frozen computation regenerates exactly the already completed phase: "+name)
        self.checkedWrites+=1
        return r

def main():
    ap=argparse.ArgumentParser()
    for name in ("generator","jet-actions","low-generator","field-helper","weak-driver",
                 "cubic-helper","high-driver","first-driver","parent-out","parent-receipt",
                 "high-out","high-receipt","high-receipt-sha","failed-out","failed-outer",
                 "step-log","out"):
        ap.add_argument("--"+name,required=True)
    ap.add_argument("--high-receipt-bytes",type=int,required=True)
    ap.add_argument("--field",choices=("e8",),default="e8")
    ap.add_argument("--remaining-seconds",type=float,default=120)
    ap.add_argument("--memory-mib",type=int,default=2048)
    a=ap.parse_args()
    require(0<a.remaining_seconds<=600 and 512<=a.memory_mib<=4096,"Explicit resources")
    resource.setrlimit(resource.RLIMIT_AS,(a.memory_mib*1024**2,)*2)
    if hasattr(sys,"set_int_max_str_digits"):sys.set_int_max_str_digits(0)
    output=Path(a.out);output.mkdir(parents=True,exist_ok=True)
    require(output.resolve() not in {Path(p).resolve() for p in
      (a.failed_out,a.parent_out,a.high_out)},"Every old mathematical directory is read only")
    receipt=output/"critical-e8-readonly-completion-receipt.json"
    start=time.monotonic()
    result={"format":FORMAT,"status":"started","scriptSHA256":sha_file(__file__),
      "parameters":{"field":"e8","originalMathematicalSourceSHA256":FIRST_SHA,
        "originalMathematicalBinding":OLD_BINDING,"allMathematicalDirectoriesReadOnly":True,
        "noNewRREF":True,"oldFailureNotReclassifiedWithoutFullVerification":True,
        "remainingSeconds":a.remaining_seconds,"memoryMiB":a.memory_mib}}
    def save():
        result["elapsedSeconds"]=time.monotonic()-start
        raw=canonical(result);require(len(raw)<85000,"Small diagnosis / complete recovery receipt")
        tmp=receipt.with_name(receipt.name+".tmp");tmp.write_bytes(raw);tmp.replace(receipt)
    def stop(signum,frame):raise BudgetStop("Read-only complete-pack revalidation budget")
    signal.signal(signal.SIGALRM,stop);signal.signal(signal.SIGTERM,stop)
    signal.setitimer(signal.ITIMER_REAL,a.remaining_seconds)
    code=1
    try:
        pp=result["parameters"];f=Path(a.failed_outer)
        require(f.stat().st_size==FAILED_BYTES and sha_file(f)==FAILED_SHA,
                "Exact actually failed outer identity")
        failed=json.loads(f.read_text())
        require(failed["exitCode"]==1 and failed["result"]["binding"]==OLD_BINDING
                and failed["result"]["scriptSHA256"]==FIRST_SHA,
                "The actual failed mathematical attempt")
        rawp=Path(a.failed_out)/"critical-complete-first-exit-receipt.json"
        require(rawp.stat().st_size==failed["fullTemporaryReceiptBytes"] and
                sha_file(rawp)==failed["fullTemporaryReceiptSHA256"],
                "The retained pre-failure raw is inspected without modification")
        pp["failedAttempt"]={"outerBytes":FAILED_BYTES,"outerSHA256":FAILED_SHA,
          "rawBytes":rawp.stat().st_size,"rawSHA256":sha_file(rawp),
          "recordedStatus":failed["result"]["status"]}
        log=Path(a.step_log)
        require(log.is_file(),"Actual session combined stdout/stderr file")
        with log.open("rb") as z:
            z.seek(max(0,log.stat().st_size-12000));tail=z.read().decode(errors="replace")
        pp["actualLog"]={"basename":log.name,"bytes":log.stat().st_size,
                        "sha256":sha_file(log),"tail":tail}
        require(sha_file(a.first_driver)==FIRST_SHA,"Unmodified frozen first-exit source")
        x=module_at("critical_readonly_replay_first",a.first_driver)
        for key,digest in x.PINS.items():
            require(sha_file(getattr(a,key))==digest,"All original frozen helpers")
        require(sha_file(a.weak_driver)==x.WEAK_SHA and
                sha_file(a.high_driver)==x.Q7_SHA and sha_file(a.cubic_helper)==x.CUBIC_SHA,
                "All original mathematical ancestor sources")
        root=Path(a.failed_out)/"checkpoints";mf=root/"manifest.json"
        before={"bytes":mf.stat().st_size,"sha256":sha_file(mf)}
        manifest=json.loads(mf.read_text())
        require(manifest["format"]==x.FORMAT and manifest["binding"]==OLD_BINDING,
                "Actual current original mathematical binding is unchanged")
        records=[]
        for name,r in sorted(manifest["stages"].items()):
            require(Path(r["file"]).name==r["file"],"Immutable local phase basename")
            path=root/r["file"]
            require(path.stat().st_size==r["bytes"] and sha_file(path)==r["sha256"],
                    "Every full actual phase byte identity")
            with gzip.open(path,"rb") as z:data=z.read()
            require(hashlib.sha256(data).hexdigest()==r["payloadSHA256"],
                    "Every full phase canonical payload")
            phase=json.loads(data)
            require(phase["format"]==x.FORMAT and phase["binding"]==OLD_BINDING
                    and phase["stage"]==name and phase["verified"]==r["verified"],
                    "Every original phase name, binding and verified status")
            records.append({"stage":name,"verified":r["verified"],"bytes":r["bytes"],
               "sha256":r["sha256"],"payloadSHA256":r["payloadSHA256"]})
        pp["currentOriginalManifest"]=before;pp["allFullPhasesVerified"]=True
        pp["phases"]=records
        final="complete-original-first-critical-exit"
        pp["verifiedCompleteCochainPresent"]=final in manifest["stages"] and manifest["stages"][final]["verified"]
        if not pp["verifiedCompleteCochainPresent"]:
            pp["mathematicalCompletionRecovered"]=False
            pp["reason"]="No verified complete original cochain is present; diagnosis only"
            result["status"]="completed";code=0
        else:
            oldcache=x.Cache(root,OLD_BINDING)
            packed=oldcache.get(final)
            require(packed["allOriginalProductsZero"] and packed["exactEarlierConnectionsZero"]
                    and packed["constantRank4352Verified"] and packed["wholeHighRank4259Verified"],
                    "Saved complete original cochain gates, to be revalidated")
            w=module_at("critical_readonly_replay_weak",a.weak_driver)
            q7=module_at("critical_readonly_replay_high",a.high_driver)
            cubic=module_at("critical_readonly_replay_cubic",a.cubic_helper)
            m=module_at("critical_readonly_replay_original",a.generator)
            actions=module_at("critical_readonly_replay_actions",a.jet_actions)
            h=module_at("critical_readonly_replay_field",a.field_helper)
            F=w.make_field(h,w.FIELDS["e8"]["polynomial"])
            parent=x.Parent(w,a.parent_out,a.parent_receipt,"e8")
            high,hi=x.read_high(a,q7)
            readonly=ReadOnlyReplay(oldcache)
            def forbidden(*args,**kwargs):
                raise AssertionError("A new RREF/profile was requested; stop instead of recomputing")
            h.bareiss_profile=forbidden
            replay={"field":"e8"}
            def report(phase,step):
                raise AssertionError("A new elimination step was requested")
            # This is the identical frozen compute function, with only a
            # read-only cache adapter and a no-new-elimination guard.
            x.compute(F,h,w,cubic,m,actions,parent,high,readonly,report,replay,w.FIELDS["e8"])
            require(replay["allOriginal6188ProductsZero"] and
                    replay["all1870OriginalExitSpanningCoordinatesVerified"]
                    and replay["completeLeadingHeads"]==packed["fullLeadingRank"]
                    and replay["completeConnectionRank"]==packed["connectionRank"],
                    "All original mathematical gates repeated successfully")
            require(mf.stat().st_size==before["bytes"] and sha_file(mf)==before["sha256"],
                    "No original manifest or phase was changed")
            for r in manifest["stages"].values():
                path=root/r["file"]
                require(path.stat().st_size==r["bytes"] and sha_file(path)==r["sha256"],
                        "Every original phase remains byte-identical after replay")
            square=replay.pop("targetSquareReadouts")
            replay["targetSquareReadouts"]=[{k:r[k] for k in
                ("order","shape","sha256","nonzeroEntries")} for r in square]
            replay["fullSquareValuesRemainInVerifiedOriginalCochain"]=True
            replay["allSquareReadoutRecordsLogicalSHA256"]=hashlib.sha256(canonical(square)).hexdigest()
            pp.update(replay)
            pp["mathematicalCompletionRecovered"]=True
            pp["replayedPhaseWriteRequestsVerifiedWithoutWriting"]=readonly.checkedWrites
            pp["originalFailureRetainedAsHistoricalEvidence"]=True
            pp["highParent"]=hi
            identity={"failedOuterSHA256":FAILED_SHA,"originalBinding":OLD_BINDING,
                      "manifest":before,"completePhase":manifest["stages"][final]}
            result["binding"]=hashlib.sha256(canonical({"format":FORMAT,
                "scriptSHA256":result["scriptSHA256"],"identity":identity})).hexdigest()
            result["status"]="completed";code=0
    except BudgetStop as exc:
        result["status"]="budget-checkpoint";code=75
        result["parameters"]["error"]={"type":type(exc).__name__,"message":str(exc)}
    except Exception as exc:
        result["status"]="failed";code=1
        result["parameters"]["error"]={"type":type(exc).__name__,"message":str(exc)}
    finally:
        signal.setitimer(signal.ITIMER_REAL,0);save()
        print(json.dumps({"status":result["status"],"receipt":str(receipt),
          "bytes":receipt.stat().st_size,"sha256":sha_file(receipt),
          "elapsedSeconds":result["elapsedSeconds"],
          "mathematicalCompletionRecovered":result["parameters"].get("mathematicalCompletionRecovered")},
          sort_keys=True),flush=True)
    return code
if __name__=="__main__":
    sys.exit(main())
