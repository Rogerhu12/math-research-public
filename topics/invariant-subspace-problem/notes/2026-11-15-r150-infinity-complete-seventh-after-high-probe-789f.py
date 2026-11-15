#!/usr/bin/env python3
"""Complete original infinity seventh low solve after exact high inspection.

Author: Astra-ISP-789f / normal_annihilator.
AI-assisted: GPT-6 Astra Pro.
This consumes a completed high-forcing probe.  It accepts either exact
zero high forcing, or a proved Q high nonmembership eliminating the sole
extra sixth representative.  A merely field-compatible nonzero high RHS
is not accepted as a rational particular.
The full incoming has ten original maps.  Save exact RREF, complete low
kernel and all full source cochains before original order verification.
"""
import argparse
import gzip
import hashlib
import importlib.util
import json
import os
from pathlib import Path
import resource
import signal
import subprocess
import sys
import time

FORMAT="r150-infinity-complete-seventh-after-high-probe-v1"
TEMP="r150-infinity-complete-seventh-temporary-v1"
PINS={
"generator":"2757b900480fe3bf1450100188df1679801351f0330d609e1a39b9c7ca146186",
"jet_actions":"2ebf418575df39ca2ed0a2165a37e92071c415b4734969c5bedc64e0b9ef4332",
"projection_consumer":"dc17dc88a5f1415c648b6ba5bf3fab4f7fb810aef6cc1552a5b2ea4acacbdf79",
"sixth_consumer":"4d759c0efbc8a647bd5845b21da5e871de28f0d43ae6f2fc84c376afb472e328",
"sixth_receipt":"9f126c0bd4d2cd15f44257d3a21e13d6987beb2061f7bbf6e9146e7a1c771ba4"}
PROBE_SHA="2f8f22933ed5dd8d87869d6db3db0e571385233df86972dca5ff4e5dbcebe3f5"
PROBE_FORMAT="r150-infinity-seventh-original-high-forcing-probe-v1"
SIX_BINDING="835fcb2ddcede187e1be808472d23a9e5a12472108b1320ac795e13be7f2e917"
P_SPECTRUM=[1,1,1,1,3,4,4,4,5,6,6,7,8,10]
STOP=False
DEADLINE=0.0
REC=None
OUT=None

def require(ok,msg):
    if not ok:raise AssertionError(msg)
def canonical(x):return json.dumps(x,sort_keys=True,separators=(",",":"),ensure_ascii=True).encode("ascii")
def hash_obj(x):return hashlib.sha256(canonical(x)).hexdigest()
def sha(path):
    h=hashlib.sha256()
    with Path(path).open("rb") as f:
        for b in iter(lambda:f.read(1048576),b""):h.update(b)
    return h.hexdigest()
def atomic(path,obj):
    p=Path(path);p.parent.mkdir(parents=True,exist_ok=True)
    t=p.with_name(p.name+".tmp");t.write_bytes(canonical(obj));os.replace(t,p)
def module(name,path):
    spec=importlib.util.spec_from_file_location(name,path);m=importlib.util.module_from_spec(spec)
    sys.modules[name]=m;spec.loader.exec_module(m);return m
def check(stage):
    if STOP or time.monotonic()>=DEADLINE:raise TimeoutError("Complete seventh boundary: "+stage)
def stop(*_):
    global STOP
    STOP=True
def flush():
    if REC is not None:
        REC["elapsedSeconds"]=time.monotonic()-REC["_start"]
        o={k:v for k,v in REC.items() if not k.startswith("_")}
        require(len(canonical(o))<95000,"Small seventh receipt");atomic(OUT,o)
def event(phase,**data):REC["events"].append({"phase":phase,**data});flush()
def result(path):
    x=json.loads(Path(path).read_bytes());return x.get("result",x)
def descriptor(path):
    p=Path(path);return {"file":p.name,"bytes":p.stat().st_size,"sha256":sha(p),"temporaryOnly":True}
def checked(root,item):
    require(Path(item["file"]).name==item["file"],"Temporary basename")
    p=Path(root)/item["file"]
    require(p.stat().st_size==item["bytes"] and sha(p)==item["sha256"],"Full temporary bytes/SHA")
    return p

class Store:
    def __init__(self,root,binding,q):
        self.root=Path(root);self.root.mkdir(parents=True,exist_ok=True)
        self.binding=binding;self.q=q;self.path=self.root/"complete-seventh-checkpoints.json"
        if self.path.exists():
            self.man=json.loads(self.path.read_bytes())
            require(self.man["format"]==TEMP and self.man["binding"]==binding and
                    self.man["temporaryOnly"] is True,"Same original seventh checkpoint")
        else:self.man={"format":TEMP,"binding":binding,"temporaryOnly":True,"phases":{}}
    def save(self,name,data):
        o={"format":TEMP,"binding":self.binding,"phase":name,"complete":True,"data":self.q.enc(data)}
        t=self.root/(name+".tmp.json.gz")
        with gzip.open(t,"wt",encoding="utf-8",compresslevel=1) as f:
            json.dump(o,f,sort_keys=True,separators=(",",":"))
        h=sha(t);p=self.root/(name+"-"+h+".json.gz");os.replace(t,p)
        self.man["phases"][name]=descriptor(p);atomic(self.path,self.man)
        REC["parameters"]["temporaryPhases"]=self.man["phases"]
        REC["parameters"]["temporaryManifestSHA256"]=sha(self.path);flush()
    def load(self,name):
        item=self.man["phases"].get(name)
        if item is None:return None
        p=checked(self.root,item)
        with gzip.open(p,"rt",encoding="utf-8") as f:o=json.load(f)
        require(o["format"]==TEMP and o["binding"]==self.binding and
                o["phase"]==name and o["complete"] is True,"Complete same-bound phase")
        REC["parameters"]["temporaryPhases"]=self.man["phases"]
        REC["parameters"]["temporaryManifestSHA256"]=sha(self.path)
        return self.q.dec(o["data"],self.q.DQ)
    def admit_rref(self,path):
        with gzip.open(path,"rt",encoding="utf-8") as f:o=json.load(f)
        require(o["format"]==TEMP and o["binding"]==self.binding and
                o["phase"]=="complete-rref" and o["complete"] is True,"Completed exact worker RREF")
        h=sha(path);dest=self.root/("complete-rref-"+h+".json.gz");os.replace(path,dest)
        self.man["phases"]["complete-rref"]=descriptor(dest);atomic(self.path,self.man)
        return self.load("complete-rref")

def probe_data(a,q,probe):
    root=Path(a.probe_out);item=probe["parameters"]["temporaryPhases"]["complete-two-original-seventh-forcings"]
    path=checked(root,item)
    with gzip.open(path,"rt",encoding="utf-8") as f:o=json.load(f)
    require(o["format"]==PROBE_FORMAT and o["binding"]==probe["parameters"]["binding"] and
            o["phase"]=="complete-two-original-seventh-forcings" and o["complete"] is True,
            "Actual complete original seventh forcing payload")
    data=q.dec(o["data"],q.DQ);meta=probe["parameters"]["originalForcing"]
    require(q.mh(data["high"])==meta["originalSeventhHighSHA256"] and
            q.mh(data["low"])==meta["originalSeventhLowSHA256"] and
            q.mh(data["incoming"])==meta["priorIncomingSHA256"],
            "Complete actual forcing and incoming matrix identities")
    return data

def prepare(a,q,s,m,j,store,probe,six):
    old=store.load("prepared-complete-low")
    if old is not None:return old
    data=probe_data(a,q,probe);high=data["high"];necessity=probe["parameters"]["highNecessity"]
    if q.zero(high):
        active=[0,1];excluded=0;reason="all original high forcing coordinates exactly zero"
    else:
        require(necessity.get("performed") is True and
                necessity.get("extraHeadHighQNonmembershipProved") is True and
                necessity.get("fieldResidualRank")==1,
                "Nonzero high forcing needs a genuine Q particular or a proved Q nonmembership")
        require(q.zero(q.DQ.sub(high,range(5100),[0])),"Only the extra sixth representative can be excluded")
        active=[0];excluded=1;reason="actual full high Q rank increases on the extra representative"
    C=data["constantLow"];W=data["incoming"]
    require((C.nrows(),C.ncols())==(1088,587) and (W.nrows(),W.ncols())==(1088,10),
            "Complete original constant and incoming blocks")
    sp=six["parameters"]["preparation"]
    require(q.mh(q.DQ.sub(C,range(1088),range(585)))==sp["J0SHA256"] and
            q.mh(q.DQ.sub(C,range(1088),range(585,587)))==sp["highLowReturnSHA256"] and
            q.mh(q.DQ.sub(W,range(1088),range(9)))==sp["completeIncomingSHA256"] and
            q.mh(data["Z3"])==sp["paidHighMetadata"]["matrixSHA256"],
            "Exact original constant basis and old incoming sources unchanged")
    R=q.DQ.sub(data["low"],range(1088),active)
    M=q.DQ.cat([C,W,R]);c=len(active)
    require((M.nrows(),M.ncols())==(1088,597+c),"Complete seventh low dimensions")
    L=[q.DQ.sub(x,range(155),active) for x in data["twoMaps"]]
    X2=q.DQ.sub(data["sixthNormalTwo"],range(450),active)
    X3=q.DQ.sub(data["sixthNormalThree"],range(990),active)
    require(q.zero(q.DQ.sub(high,range(5100),active)),
            "All surviving original head combinations have zero high forcing")
    meta={"shape":[1088,597+c],"activeOriginalQuotientRepresentatives":active,
        "highExcludedHeadDimension":excluded,"highReductionReason":reason,
        "newLowForcingColumns":c,"completePriorIncomingColumns":10,
        "completeConstantColumns":587,"matrixSHA256":q.mh(M),
        "allSurvivingOriginalHighForcingsExactlyZero":True,
        "fullQHighKernelOnlyTwoAlreadyProved":True,
        "allOriginalLowerForcingProductsVerifiedByActualProbe":True,
        "originalProbeBinding":probe["parameters"]["binding"],
        "originalLowForcingSHA256":q.mh(R),"constantSHA256":q.mh(C),"incomingSHA256":q.mh(W),
        "unscaledOriginalRationalColumns":True}
    out={"M":M,"twoMaps":L,"sixthNormalTwo":X2,"sixthNormalThree":X3,
        "incomingMaps":data["incomingMaps"],"stableMaps":data["stableMaps"],"Z3":data["Z3"],
        "coefficientData":data["coefficientData"],"top":data["top"],"metadata":meta}
    store.save("prepared-complete-low",out);event("complete original seventh low matrix saved",shape=meta["shape"])
    return out

def worker(a):
    if hasattr(sys,"set_int_max_str_digits"):sys.set_int_max_str_digits(0)
    resource.setrlimit(resource.RLIMIT_AS,(a.memory_mib*1024**2,)*2)
    require(sha(a.projection_consumer)==PINS["projection_consumer"],"Worker pinned exact arithmetic")
    q=module("r150_seventh_worker_Q",a.projection_consumer)
    require(sha(a.worker_input)==a.worker_input_sha256,"Complete worker input hash")
    with gzip.open(a.worker_input,"rt",encoding="utf-8") as f:o=json.load(f)
    require(o["format"]==TEMP and o["binding"]==a.worker_binding and
            o["phase"]=="prepared-complete-low" and o["complete"] is True,"Exact worker input binding")
    M=q.dec(o["data"]["M"],q.DQ)
    require(M.nrows()==1088 and M.ncols() in (598,599),"Actual exact seventh matrix")
    t=time.monotonic();R,r=M.rref();piv=q.pivots(R,r)
    obj={"format":TEMP,"binding":a.worker_binding,"phase":"complete-rref","complete":True,
        "data":{"R":q.enc(R),"rank":r,"pivotColumns":piv,"sourceMatrixSHA256":q.mh(M),
                "elapsedSeconds":time.monotonic()-t}}
    path=Path(a.worker_out);tmp=path.with_name(path.name+".tmp")
    with gzip.open(tmp,"wt",encoding="utf-8",compresslevel=1) as f:
        json.dump(obj,f,sort_keys=True,separators=(",",":"))
    os.replace(tmp,path);print(json.dumps({"status":"complete-rref-saved","rank":r}),flush=True)

def rref(a,q,store):
    old=store.load("complete-rref")
    if old is not None:return old
    pending=store.root/"complete-rref-worker.json.gz"
    if pending.exists():return store.admit_rref(pending)
    item=store.man["phases"]["prepared-complete-low"];ip=checked(store.root,item)
    cmd=[sys.executable,str(Path(__file__).resolve()),"--worker-input",str(ip.resolve()),
        "--worker-input-sha256",item["sha256"],"--worker-binding",store.binding,
        "--worker-out",str(pending.resolve()),"--projection-consumer",str(Path(a.projection_consumer).resolve()),
        "--memory-mib",str(a.memory_mib)]
    check("before exact seventh low RREF");log=store.root/"exact-low-rref-worker.log"
    with log.open("wb") as f:
        p=subprocess.run(cmd,stdout=f,stderr=subprocess.STDOUT,
                         timeout=max(.05,DEADLINE-time.monotonic()),check=False)
    require(p.returncode==0 and pending.exists(),"Exact seventh RREF: "+log.read_text(errors="replace")[-2500:])
    out=store.admit_rref(pending);event("complete exact seventh RREF saved",rank=out["rank"],seconds=out["elapsedSeconds"])
    return out

def kernel(q,m,j,store,data,rr):
    old=store.load("verified-low-kernel")
    if old is not None:return old
    M=data["M"];R=rr["R"];rank=rr["rank"];piv=rr["pivotColumns"];c=M.ncols()-597
    require(rr["sourceMatrixSHA256"]==q.mh(M) and q.pivots(R,rank)==piv,"Complete exact original RREF")
    pref=[sum(p<n for p in piv) for n in (585,587,597,M.ncols())]
    require(pref[:3]==[578,580,590],"Actual complete constant / prior-sixth incoming prefix")
    K,pp,free=j.canonical_kernel(m,R,rank)
    require(pp==piv and q.zero(M*K),"Complete original seventh low kernel")
    C=q.DQ.sub(K,range(597,597+c),range(K.ncols()))
    CR,h=C.rref();choice=q.pivots(CR,h)
    require(h==c-(rank-590) and h in (0,1),"Complete surviving seventh head count")
    G=q.DQ.sub(K,range(K.nrows()),choice)
    meta={"rank":rank,"prefixRanks":pref,"completeKernelDimension":K.ncols(),
        "headProjectionRank":h,"completeFullSeventhLeadingDimension":15+h,
        "fullSeventhConnectionRank":2-h,"allOriginalLowKernelProductsZero":True,
        "originalLowKernelProductCoordinates":1088*K.ncols(),"kernelSHA256":q.mh(K),
        "freeColumns":free,"chosenKernelColumns":choice}
    out={"K":K,"selected":G,"metadata":meta}
    store.save("verified-low-kernel",out);event("complete seventh low kernel verified",rank=rank,newHeads=h)
    return out

def cochains(q,store,data,ker):
    old=store.load("complete-seventh-cochains-candidate")
    if old is not None:return old
    G=ker["selected"];h=G.ncols();c=data["M"].ncols()-597
    X=q.DQ.sub(G,range(585),range(h));A=q.DQ.sub(G,range(585,587),range(h))
    Y=q.DQ.sub(G,range(587,597),range(h));C=q.DQ.sub(G,range(597,597+c),range(h))
    low=[]
    for k in range(8):
        new=data["twoMaps"][k]*C+data["incomingMaps"][k]*Y
        if k==7:new+=q.DQ.vcat([q.DQ.mat(20,h),q.DQ.sub(X,range(135),range(h))])
        low.append(q.DQ.cat([data["stableMaps"][k],new]))
    six2=q.DQ.cat([q.DQ.mat(450,15),data["sixthNormalTwo"]*C])
    six3=q.DQ.cat([q.DQ.mat(990,15),data["sixthNormalThree"]*C])
    seven2=q.DQ.cat([q.DQ.mat(450,15),q.DQ.sub(X,range(135,585),range(h))])
    seven3=q.DQ.cat([q.DQ.mat(990,15),data["Z3"]*A])
    n=15+h;RT,r=low[0].transpose().rref();free=q.pivots(RT,r)
    require(r==n,"All complete seventh original heads independent")
    unit=q.DQ.sub(low[0],free,range(n));N=unit.inv()
    require(unit*N==q.DQ.eye(n),"Actual head normalization")
    low=[x*N for x in low];six2=six2*N;six3=six3*N;seven2=seven2*N;seven3=seven3*N
    require(q.DQ.sub(low[0],free,range(n))==q.DQ.eye(n),"Original free head I")
    pack=q.DQ.vcat(low[:6]+[q.DQ.vcat([low[6],six2,six3]),q.DQ.vcat([low[7],seven2,seven3])])
    require((pack.nrows(),pack.ncols())==(4120,n),"Complete original eight-coefficient pack")
    meta={"shape":[4120,n],"headRank":n,"newHeadCount":h,"packSHA256":q.mh(pack),
        "headSHA256":q.mh(low[0]),"normalizerSHA256":q.mh(N),"freeOriginalHeadCoordinates":free,
        "lambda0Through5Ranges":[[155*k,155*(k+1)] for k in range(6)],
        "lambda6Ranges":{"normal0":[930,950],"normal1":[950,1085],
                         "normal2":[1085,1535],"normal3":[1535,2525]},
        "lambda7Ranges":{"normal0":[2525,2545],"normal1":[2545,2680],
                         "normal2":[2680,3130],"normal3":[3130,4120]},
        "allActualSixthAndSeventhHighCoefficientsRetained":True,
        "noHighForcingZeroAssumptionAtOrderEight":True}
    out={"pack":pack,"normalizer":N,"selectedKernel":G,"metadata":meta}
    store.save("complete-seventh-cochains-candidate",out);return out

def verify(q,s,m,j,store,data,cand):
    done=store.load("complete-seventh-cochains-verified")
    if done is not None:return done
    pack=cand["pack"];n=pack.ncols();coeff=q.coefficient_decode(data["coefficientData"])
    low=[q.DQ.sub(pack,range(155*k,155*(k+1)),range(n)) for k in range(6)]
    low+=[q.DQ.sub(pack,range(930,1085),range(n)),q.DQ.sub(pack,range(2525,2680),range(n))]
    high={6:{2:q.DQ.sub(pack,range(1085,1535),range(n)),3:q.DQ.sub(pack,range(1535,2525),range(n))},
          7:{2:q.DQ.sub(pack,range(2680,3130),range(n)),3:q.DQ.sub(pack,range(3130,4120),range(n))}}
    ledger=store.load("original-verification-ledger")
    if ledger is None:ledger={"packSHA256":q.mh(pack),"completedOrders":[],"originalCoordinates":0}
    require(ledger["packSHA256"]==q.mh(pack) and
            ledger["completedOrders"]==list(range(len(ledger["completedOrders"]))),"Whole-order verification ledger")
    for k in range(len(ledger["completedOrders"]),8):
        check("before original order"+str(k))
        lowprod=s.original_low(q,m,j,coeff,data["top"],low,k)
        for t in (6,7):
            if t<=k:lowprod+=q.DQ.vcat([j.apply(m,coeff,k-t,r,high[t],n) for r in (0,1)])
        require(q.zero(lowprod),"All original low products through order7")
        for r in (2,3):
            HH=q.DQ.mat(len(j.source_rows(r)),n)
            for t in (6,7):
                if t<=k:HH+=j.apply_sparse(m,coeff,k-t,r,high[t],n)
            require(q.zero(HH),"All original high products through order7")
        ledger["completedOrders"].append(k);ledger["originalCoordinates"]+=6188*n
        store.save("original-verification-ledger",ledger);event("complete original order verified",order=k,heads=n)
    require(ledger["originalCoordinates"]==8*6188*n,"All original eight-order coordinates")
    md=dict(cand["metadata"]);md.update({"allEightOrdersAll6188OriginalSourceRowsVerified":True,
        "fullOriginalVerificationComplete":True,"originalProductCoordinates":ledger["originalCoordinates"]})
    out={"pack":pack,"normalizer":cand["normalizer"],"selectedKernel":cand["selectedKernel"],"metadata":md}
    store.save("complete-seventh-cochains-verified",out);return out

def main():
    global DEADLINE,REC,OUT
    p=argparse.ArgumentParser()
    for k in ("generator","jet-actions","projection-consumer","sixth-consumer","sixth-receipt",
              "probe-receipt","probe-receipt-sha256","probe-out","checkpoint-dir","out"):
        p.add_argument("--"+k)
    p.add_argument("--remaining-seconds",type=float,default=180)
    p.add_argument("--memory-mib",type=int,default=2048)
    for k in ("worker-input","worker-input-sha256","worker-binding","worker-out"):p.add_argument("--"+k)
    a=p.parse_args()
    if a.worker_input:worker(a);return
    for k in ("generator","jet_actions","projection_consumer","sixth_consumer","sixth_receipt",
              "probe_receipt","probe_receipt_sha256","probe_out","checkpoint_dir","out"):
        require(getattr(a,k) is not None,"Required argument "+k)
    require(0<a.remaining_seconds<=600 and 512<=a.memory_mib<=4096,"Finite seventh resources")
    if hasattr(sys,"set_int_max_str_digits"):sys.set_int_max_str_digits(0)
    resource.setrlimit(resource.RLIMIT_AS,(a.memory_mib*1024**2,)*2)
    start=time.monotonic();DEADLINE=start+a.remaining_seconds-min(8,a.remaining_seconds/10)
    signal.signal(signal.SIGTERM,stop);signal.signal(signal.SIGINT,stop);OUT=Path(a.out)
    REC={"format":FORMAT,"status":"running","outcome":"pending-original-high-scope","_start":start,
        "scriptSHA256":sha(__file__),"events":[],"parameters":{"author":"Astra-ISP-789f / normal_annihilator",
        "aiAssisted":"GPT-6 Astra Pro","sharedSeconds":a.remaining_seconds,"memoryMiB":a.memory_mib,
        "temporaryOnly":True,"allAncestorFilesReadOnly":True,"largeDataUploadedOrCommitted":False,
        "eighthRankNotClaimed":True,"selectedMinorLeading31UnitNotClaimed":True,
        "fullCharacteristicZeroSpectrumNotClaimed":True}}
    code=1
    try:
        pins=dict(PINS);pins["probe_receipt"]=a.probe_receipt_sha256
        for k,d in pins.items():require(sha(getattr(a,k))==d,"Pinned actual source/input "+k)
        sixth=result(a.sixth_receipt);probe=result(a.probe_receipt)
        require(sixth["status"]=="completed" and sixth["parameters"]["binding"]==SIX_BINDING and
                sixth["parameters"]["fullFirstSixRanks"]==[4,0,1,3,1,1] and
                sixth["parameters"]["allSevenOrdersAll6188OriginalSourceRowsVerified"] is True,
                "Complete original preceding six stages")
        require(probe["status"]=="completed" and probe["format"]==PROBE_FORMAT and
                probe["parameters"]["selfSHA256"]==PROBE_SHA and
                probe["parameters"]["originalForcing"]["allOriginalRepresentativeLowerProductsZero"] is True and
                probe["parameters"]["originalForcing"]["allTenPriorIncomingDirectionsTransported"] is True,
                "Actual full original seventh high probe")
        necessity=probe["parameters"]["highNecessity"]
        require(probe["parameters"]["originalForcing"]["extraSixthHeadHighForcingZero"] is True or
                necessity.get("extraHeadHighQNonmembershipProved") is True,
                "A nonzero field-compatible high RHS still requires an actual Q lift")
        binding=hash_obj({"format":FORMAT,"sourceSHA256":sha(__file__),"inputSHA256":pins,
            "probeBinding":probe["parameters"]["binding"],"sixthBinding":SIX_BINDING,"order":7})
        REC["parameters"]["binding"]=binding;REC["parameters"]["inputSHA256"]=pins
        require(Path(a.checkpoint_dir).resolve()!=Path(a.probe_out).resolve(),"Do not overwrite the probe")
        q=module("r150_full_seventh_Q",a.projection_consumer)
        s=module("r150_full_seventh_sixth",a.sixth_consumer)
        m=module("r150_full_seventh_first",a.generator);j=module("r150_full_seventh_actions",a.jet_actions)
        store=Store(a.checkpoint_dir,binding,q)
        data=prepare(a,q,s,m,j,store,probe,sixth);REC["parameters"]["preparation"]=data["metadata"]
        rr=rref(a,q,store);ker=kernel(q,m,j,store,data,rr)
        REC["parameters"]["completeLowKernel"]=ker["metadata"]
        cand=cochains(q,store,data,ker);done=verify(q,s,m,j,store,data,cand)
        n=done["metadata"]["headRank"];beta=17-n
        require(beta in (1,2) and beta==ker["metadata"]["fullSeventhConnectionRank"],
                "Complete original seventh dimension formula")
        base=[1,1,1,1,3,4,4,4,5,6]+[7]*beta+[8]*(4-beta)
        lower=[max(x,y) for x,y in zip(P_SPECTRUM,base)]
        REC["parameters"].update({"completeFullSeventhConnectionRank":beta,
            "fullFirstSevenRanks":[4,0,1,3,1,1,beta],
            "completeFullSeventhLeadingDimension":n,"allFullSeventhHeadsCovered":True,
            "allEightOrdersAll6188OriginalSourceRowsVerified":True,
            "fullOriginalVerificationComplete":True,"actualCanonicalCochain":done["metadata"],
            "originalProductCoordinates":done["metadata"]["originalProductCoordinates"],
            "fullCharacteristicZeroPositiveIndicesLowerBounds":lower,
            "fullCharacteristicZeroLengthLowerBound":sum(lower),"fullCharacteristicZeroLengthUpperBound":66,
            "fullCharacteristicZeroNextMinorLowerBound":sum(lower[:-1]),
            "fullCharacteristicZeroMaximumPositiveIndexUpperBound":66-sum(lower[:-1]),
            "eighthOriginalHighForcingMustBeComputedFromAllSavedCoefficients":True})
        REC["status"]="completed";REC["outcome"]="complete-original-seventh-connection-exact";code=0
    except (TimeoutError,subprocess.TimeoutExpired) as e:
        REC["status"]="prefix-completed";REC["outcome"]="complete-stages-saved-time-budget";REC["error"]=str(e);code=75
    except BaseException as e:
        REC["status"]="failed";REC["error"]=type(e).__name__+": "+str(e);raise
    finally:
        flush();print(json.dumps({"status":REC["status"],"outcome":REC["outcome"],"receipt":str(OUT),
            "bytes":OUT.stat().st_size if OUT.exists() else 0,
            "sha256":sha(OUT) if OUT.exists() else None,"elapsedSeconds":time.monotonic()-start}),flush=True)
    if code:raise SystemExit(code)
if __name__=="__main__":main()
