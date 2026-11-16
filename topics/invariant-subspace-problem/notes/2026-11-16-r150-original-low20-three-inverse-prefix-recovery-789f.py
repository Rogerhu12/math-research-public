#!/usr/bin/env python3
"""Re-execute and byte-recover the verified original low20 inverse prefix.

Author: Astra-ISP-789f / normal_annihilator, with /root.
AI-assisted: GPT-6 Astra Pro. Date: 2026-11-16.

This is a NEW execution of the same frozen original mathematics. Its separate
recovery receipt has its own source and binding. Six previously paid phase
files and the paid manifest are restored only if all exact stored and logical
SHA identities match. The original constants stage remains INCOMPLETE.
The frozen build_constants function is stopped at its existing completed-225
event, before C construction. No mathematical array is uploaded or committed.
"""
from __future__ import annotations
import argparse, gc, gzip, hashlib, importlib.util, json, os
import resource, signal, sys, time, zlib
from pathlib import Path

sys.set_int_max_str_digits(0)
FORMAT="r150-original-low20-three-inverse-prefix-recovery-v1"
PARENT_FORMAT="r150-original-low-commutator-twenty-exact-constants-v2"
PARENT_SOURCE={"bytes":33539,"sha256":"d9d98bc379e322e9c212b7ad7721399ec8b1bab9970a2755700338f7053d47da"}
PARENT_BINDING="672c57bb68079e9a49cff09e4a7fdadd7b89dc017927913ee0d35261a08d2522"
PARENT_MANIFEST={"bytes":3418,"sha256":"c7b010a2c16e2896782eaaad74f977d00e640af6c8142b623474a015b948bf9b"}
STOP_EVENT="original-all-fifteen-quadratic-source-identities"
EXPECTED_PHASES={
  "original-inverse-05-76593af361b4": {
    "bytes": 449054,
    "logicalBytes": 903340,
    "logicalSha256": "cd56ffd2b657f39b3a4d23fe87fd131c12c6a65dbca7f3534d20db6c3aeea619",
    "path": "original-inverse-05-76593af361b4.json.gz",
    "sha256": "e538b1965de75be034810e89f3beaba2e8ae22d96abf9c642a48ffcde70f1029"
  },
  "original-inverse-05-76593af361b4-candidate": {
    "bytes": 448917,
    "logicalBytes": 903163,
    "logicalSha256": "c8ab25e1b3e98c959d412f05ed57bc85f0da451256ad6d6006713689c2b965f1",
    "path": "original-inverse-05-76593af361b4-candidate.json.gz",
    "sha256": "1cd3730016e52468b15f21836f476ddfea37475dc4867b799d1703f97487ed07"
  },
  "original-inverse-06-75b6be84bce4": {
    "bytes": 81221,
    "logicalBytes": 186144,
    "logicalSha256": "e3ba7aa0ab6c8d3ad3c5e114839f6f266dfbb58effb6dd214d45e1aaa72d5cdc",
    "path": "original-inverse-06-75b6be84bce4.json.gz",
    "sha256": "8686bcc92319a8b1e0f0f4334062ef7692594cc696b0ef6fae674e4a76adb944"
  },
  "original-inverse-06-75b6be84bce4-candidate": {
    "bytes": 81082,
    "logicalBytes": 185967,
    "logicalSha256": "3909f378c9c6c12c5f89cd8e1e17412f23a71675bf42728eb40a7fb155c9be75",
    "path": "original-inverse-06-75b6be84bce4-candidate.json.gz",
    "sha256": "8b4c79e68f6c1691ac1f600e2ade9ad6d8149bfefb3d78ff0d6a76d98fe058fb"
  },
  "original-inverse-11-abb2c7a819cd": {
    "bytes": 1473718,
    "logicalBytes": 2975996,
    "logicalSha256": "31bf451e26193eed026feba6bf00a71a9394a78ecce0a7571aea661380b76c05",
    "path": "original-inverse-11-abb2c7a819cd.json.gz",
    "sha256": "ec9d6e2758ae835f027fd0c3d8da26945814cb3599949057f96ac542b78300e6"
  },
  "original-inverse-11-abb2c7a819cd-candidate": {
    "bytes": 1473579,
    "logicalBytes": 2975818,
    "logicalSha256": "4906c6aca9ddf8b6f5cf96e87fefabeae0c9cc027db477cea4cf060dc7d0dbaa",
    "path": "original-inverse-11-abb2c7a819cd-candidate.json.gz",
    "sha256": "e255565835b771d523afbb91421a3eebe6c9fc4fdde6268ca6aeff3093dbb7cc"
  }
}
COMPLETE_KEYS=("original-inverse-06-75b6be84bce4",
               "original-inverse-05-76593af361b4",
               "original-inverse-11-abb2c7a819cd")

class Budget(Exception): pass
class StopBeforeCubic(Exception): pass

def need(ok,message):
    if not ok:raise ValueError(message)

def canon(x):
    return json.dumps(x,sort_keys=True,separators=(",",":"),ensure_ascii=True).encode("ascii")

def sha(b):return hashlib.sha256(b).hexdigest()

def identity(p):
    p=Path(p);h=hashlib.sha256()
    with p.open("rb") as f:
        for b in iter(lambda:f.read(1048576),b""):h.update(b)
    return {"path":p.name,"bytes":p.stat().st_size,"sha256":h.hexdigest()}

def exact(p,d):
    a=identity(p)
    need(all(a[k]==d[k] for k in ("bytes","sha256")),"complete exact file "+Path(p).name)
    return a

def atomic(p,raw):
    p=Path(p);p.parent.mkdir(parents=True,exist_ok=True);tmp=p.with_name(p.name+".tmp")
    with tmp.open("wb") as f:f.write(raw);f.flush();os.fsync(f.fileno())
    os.replace(tmp,p)

def load_source(p,d,name):
    exact(p,d);sp=importlib.util.spec_from_file_location(name,p)
    m=importlib.util.module_from_spec(sp);sp.loader.exec_module(m);return m

def parent_semantic(h,source):
    # This is exactly the frozen parent's semantic dictionary, not a new
    # mathematical provenance assigned to changed arrays.
    return {"format":h.FORMAT,"source":source,"matchedCubic":h.MATCHED,"prime":h.PRIME,"coefficientRoot":h.ROOT,
      "modelSourceSHA256":h.MODEL_SHA,"helperSHA256":h.HELPER_SHA,"paidModelSourceSHA256":h.PAID_MODEL_SHA,
      "paidModelBinding":h.PAID_MODEL_BINDING,"paidModelManifest":h.PAID_MANIFEST,"paidModelBase":h.PAID_BASE,
      "hankelPivots":h.HP,"hankelFree":h.HU,"keptQuadraticPaths":[list(x) for x in h.KEEP],
      "cubicUnitColumns":list(range(35)),"kernelProjectionColumns":list(range(35,55)),
      "twentyOriginalLowSeedIndices":h.LOW_IDS,"newArithmetic":"exact E projected20x50 system; no field coefficient lift"}

def verified_phase(p,d,key):
    exact(p,d);raw=gzip.decompress(Path(p).read_bytes())
    need(len(raw)==d["logicalBytes"] and sha(raw)==d["logicalSha256"],"full old logical phase "+key)
    o=json.loads(raw)
    need(o["format"]==PARENT_FORMAT+"-phase" and o["binding"]==PARENT_BINDING,"same restored original phase envelope")
    x=o["data"]
    if key in COMPLETE_KEYS:
        n=x["dimension"]
        need(x["bothOriginalEInverseProductsVerified"] and x["bothLocalPlaceInverseProductsVerified"] and
             x["originalEProductCount"]==2*n*n and x["faithfulRationalCoordinateCount"]==6*n*n and
             not x.get("candidateOnly",False),"genuine complete two-sided original inverse")
    else:
        need(key.endswith("-candidate") and x["candidateOnly"] and not x["bothOriginalEInverseProductsVerified"],
             "honest unverified historical candidate identity")
    return x

def main():
    ap=argparse.ArgumentParser()
    for key in ("exact-source","model-source","helper","paid-model-source","paid-model-out","restored-out","out"):
        ap.add_argument("--"+key,type=Path,required=True)
    ap.add_argument("--seconds",type=float,default=120)
    ap.add_argument("--memory-mib",type=int,default=768)
    a=ap.parse_args()
    need(0<a.seconds<=600 and 512<=a.memory_mib<=2048,"bounded original-prefix recovery")
    need(a.restored_out.resolve()!=a.out.resolve(),"old recovered bytes and new recovery receipt have distinct directories")
    resource.setrlimit(resource.RLIMIT_AS,(a.memory_mib*1048576,)*2)
    a.restored_out.mkdir(parents=True,exist_ok=True);a.out.mkdir(parents=True,exist_ok=True)
    own=identity(Path(__file__));start=time.monotonic();deadline=start+a.seconds
    code=1;state=None;binding=None;h=None;written=[];reused=[];stopped=False
    oldmp=a.restored_out/"exact-low20-manifest.json"
    newmp=a.out/"prefix-recovery-manifest.json"
    rec={"format":FORMAT,"source":own,"status":"running","parameters":{
        "seconds":a.seconds,"memoryMiB":a.memory_mib,"newExecution":True,
        "originalConstantsStageComplete":False,"stopBeforeCubicConstruction":True,
        "oldRawOrElapsedRewritten":False,"newE20SolveClaimed":False,"unitIdealClaimed":False}}
    def tick():
        if time.monotonic()+8>=deadline:raise Budget("whole original inverse-prefix recovery budget")
    def alarm(sig=None,frame=None):raise Budget("actual original inverse-prefix recovery wall budget")
    def flush():
        atomic(oldmp,canon(state))
        cp={"format":FORMAT+"-manifest","binding":binding,"source":own,
            "restoredParentBinding":PARENT_BINDING,"expectedParentManifest":PARENT_MANIFEST,
            "completeRestoredPhases":state["phases"],"writtenThisExecution":written,
            "originalConstantsStageComplete":False}
        atomic(newmp,canon(cp))
    def read(key):
        if key not in state["phases"]:return None
        need(key in EXPECTED_PHASES and state["phases"][key]==EXPECTED_PHASES[key],"same paid original phase descriptor")
        return verified_phase(a.restored_out/EXPECTED_PHASES[key]["path"],EXPECTED_PHASES[key],key)
    def write(key,data):
        need(key in EXPECTED_PHASES,"only the six paid original inverse prefix phases may be restored")
        raw=h.canon({"format":h.FORMAT+"-phase","binding":PARENT_BINDING,"data":data})
        target=EXPECTED_PHASES[key]
        need(len(raw)==target["logicalBytes"] and sha(raw)==target["logicalSha256"],
             "new original arithmetic must exactly recover old logical bytes "+key)
        packed=gzip.compress(raw,compresslevel=1,mtime=0)
        need(len(packed)==target["bytes"] and sha(packed)==target["sha256"],
             "fixed-runtime new compression must exactly recover old whole bytes "+key)
        p=a.restored_out/target["path"]
        if p.exists():exact(p,target)
        else:atomic(p,packed)
        state["phases"][key]=dict(target);written.append(key);flush()
        return dict(target)
    def event(name,**kw):
        nonlocal stopped
        rec["parameters"]["lastEvent"]=name
        if state is not None and name in state["phases"]:rec["parameters"]["lastWholePhase"]=name
        if name.endswith("-reused"):reused.append(name[:-7])
        print(json.dumps({"phase":name,"elapsedSeconds":time.monotonic()-start,
            "peakRssKiB":resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,**kw},separators=(",",":")),flush=True)
        if name==STOP_EVENT:
            need(kw.get("exactECoefficients")==225,"stop only after the exact original all225 products event")
            stopped=True
            raise StopBeforeCubic("all225 original products complete; do not enter C construction")
    signal.signal(signal.SIGALRM,alarm);signal.setitimer(signal.ITIMER_REAL,a.seconds)
    try:
        import flint
        need(tuple(sys.version_info[:3])==(3,12,14) and flint.__version__=="0.9.0","same exact Python3.12.14 and flint0.9.0")
        rec["parameters"]["runtime"]={"python":sys.version.split()[0],"pythonFlint":flint.__version__,"zlib":zlib.ZLIB_VERSION}
        h=load_source(a.exact_source,PARENT_SOURCE,"original_low20_prefix_frozen_v2")
        need(h.FORMAT==PARENT_FORMAT and h.PRIME==127 and h.ROOT==100 and
             h.MATCHED==[52565262336,6080833024,-43931504,3725],"same original E and legal place")
        original_source=identity(a.exact_source)
        oldsem=parent_semantic(h,original_source)
        need(sha(canon(oldsem))==PARENT_BINDING,"exact original source semantic binding, including source basename")
        semantic={"format":FORMAT,"source":own,"exactOriginalSource":original_source,
            "originalParentBinding":PARENT_BINDING,"originalParentManifest":PARENT_MANIFEST,
            "expectedOriginalSixPhases":EXPECTED_PHASES,"stopEvent":STOP_EVENT,"completedOriginalQuadraticCoefficients":225,
            "modelSourceSHA256":h.MODEL_SHA,"helperSHA256":h.HELPER_SHA,"paidModelSourceSHA256":h.PAID_MODEL_SHA,
            "paidModelBinding":h.PAID_MODEL_BINDING,"paidModelManifest":h.PAID_MANIFEST,"paidModelBase":h.PAID_BASE}
        binding=sha(canon(semantic));rec["binding"]=binding;rec["parameters"]["semantic"]=semantic
        state={"format":PARENT_FORMAT+"-manifest","binding":PARENT_BINDING,"semantic":oldsem,"phases":{}}
        if oldmp.exists():
            state=json.loads(oldmp.read_bytes())
            need(state["format"]==PARENT_FORMAT+"-manifest" and state["binding"]==PARENT_BINDING and
                 state["semantic"]==oldsem and set(state["phases"])<=set(EXPECTED_PHASES),
                 "same honest partial original six-phase recovery")
            for key in state["phases"]:read(key)
        if newmp.exists():
            prior=json.loads(newmp.read_bytes())
            need(prior["format"]==FORMAT+"-manifest" and prior["binding"]==binding and prior["source"]==own and
                 prior["restoredParentBinding"]==PARENT_BINDING,"same independent new recovery execution binding")
        fd=h.import_source(a.model_source,h.MODEL_SHA,"exact_low20_recovery_original_physical")
        helper=h.import_source(a.helper,h.HELPER_SHA,"exact_low20_recovery_original_field")
        need(identity(a.paid_model_source)["sha256"]==h.PAID_MODEL_SHA,"same original field model producer source")
        paid,parent=h.read_paid_base(a.paid_model_out);rec["parameters"]["actualPaidParent"]=parent
        F=h.EField(inverse_reader=read,inverse_writer=write,progress=event,tick=tick)
        tick();original=fd.prepare(helper);event("original-physical-model-rebuilt-for-new-prefix")
        try:
            h.build_constants(F,original,paid,tick)
        except StopBeforeCubic:
            pass
        need(stopped,"frozen original mathematics reached exactly the all225 stop, not an arbitrary early return")
        del original,paid,F;gc.collect()
        need(set(state["phases"])==set(EXPECTED_PHASES),"all six original files fully recovered")
        checks=[]
        for key in sorted(EXPECTED_PHASES):
            x=read(key)
            checks.append({"phase":key,"descriptor":EXPECTED_PHASES[key],"label":x["label"],
                "dimension":x["dimension"],"inputSha256":x["inputSha256"],"determinant127":x["determinant127"],
                "bothOriginalEInverseProductsVerified":x["bothOriginalEInverseProductsVerified"],
                "originalEProductCount":x.get("originalEProductCount",0),
                "faithfulRationalCoordinateCount":x.get("faithfulRationalCoordinateCount",0)})
            del x;gc.collect()
        flush();exact(oldmp,PARENT_MANIFEST)
        need("original-exact-constants" not in state["phases"],"old constants stage remains incomplete after byte recovery")
        rec["parameters"].update({"allSixOriginalStoredAndLogicalBytesRecovered":True,
            "all3418OriginalManifestBytesRecovered":True,"restoredManifest":identity(oldmp),
            "completeOriginalInverseCount":3,"verifiedOriginalInverseEProducts":364,
            "verifiedOriginalInverseRationalCoordinates":1092,"all225OriginalQuadraticSourceCoefficientsReverified":True,
            "cubicConstructionEntered":False,"actualCompleteOriginalPhaseChecks":checks,
            "writtenWholePhasesThisExecution":written,"reusedWholePhasesThisExecution":reused})
        rec["status"]="completed-prefix-byte-recovery";code=0;return code
    except Budget as e:
        rec["status"]="budget-checkpoint";rec["parameters"]["error"]={"type":type(e).__name__,"message":str(e)};code=75;return code
    except BaseException as e:
        rec["status"]="failed";rec["parameters"]["error"]={"type":type(e).__name__,"message":str(e)};code=1;return code
    finally:
        signal.setitimer(signal.ITIMER_REAL,0)
        rec["parameters"]["elapsedSeconds"]=time.monotonic()-start
        rec["parameters"]["peakRssKiB"]=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
        rec["parameters"]["exitCode"]=code;rec["parameters"]["reachedAll225StopEvent"]=stopped
        rec["parameters"]["wholeRestoredPhaseCount"]=len(state["phases"]) if state is not None else 0
        if newmp.exists():rec["parameters"]["recoveryManifest"]=identity(newmp)
        if oldmp.exists():rec["parameters"]["actualRestoredPrefixManifest"]=identity(oldmp)
        atomic(a.out/"original-low20-prefix-recovery-receipt.json",canon(rec))
        print(json.dumps(rec,separators=(",",":")),flush=True)

if __name__=="__main__":raise SystemExit(main())
