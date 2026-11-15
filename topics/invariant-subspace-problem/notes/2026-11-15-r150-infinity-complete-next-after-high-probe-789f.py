#!/usr/bin/env python3
"""Complete original infinity next low solve after exact high inspection.

Author: Astra-ISP-789f / normal_annihilator.
AI-assisted: GPT-6 Astra Pro.
This consumes a completed high-forcing probe.  It accepts either exact
zero high forcing, or a proved Q high nonmembership eliminating the sole
extra previous representative.  A merely field-compatible nonzero high RHS
is not accepted as a rational particular.
The complete prior incoming image is transported as whole original maps.  Save exact RREF, complete low
kernel and all full source cochains before original order verification.
"""
import argparse
import gzip
import hashlib
import importlib.util
import io
import json
import os
from pathlib import Path
import resource
import signal
import subprocess
import sys
import time

FORMAT="r150-infinity-complete-next-left-stage-v1"
TEMP="r150-infinity-complete-next-temporary-v1"
PINS={
"generator":"2757b900480fe3bf1450100188df1679801351f0330d609e1a39b9c7ca146186",
"jet_actions":"2ebf418575df39ca2ed0a2165a37e92071c415b4734969c5bedc64e0b9ef4332",
"projection_consumer":"dc17dc88a5f1415c648b6ba5bf3fab4f7fb810aef6cc1552a5b2ea4acacbdf79",
"sixth_consumer":"4d759c0efbc8a647bd5845b21da5e871de28f0d43ae6f2fc84c376afb472e328"}
PROBE_SHA="9438d69051a9bac1a0e0f0b0b2214dc4277b81214f778900adfd02fab6a4df18"
PROBE_FORMAT="r150-infinity-next-original-high-forcing-v1"
FIELD_SPECTRUM=[1,1,1,1,3,4,4,4,5,6,7,8,10,11]
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
    if STOP or time.monotonic()>=DEADLINE:raise TimeoutError("Complete next boundary: "+stage)
def stop(*_):
    global STOP
    STOP=True
def flush():
    if REC is not None:
        REC["elapsedSeconds"]=time.monotonic()-REC["_start"]
        o={k:v for k,v in REC.items() if not k.startswith("_")}
        require(len(canonical(o))<95000,"Small next receipt");atomic(OUT,o)
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
        self.binding=binding;self.q=q;self.path=self.root/"complete-next-checkpoints.json"
        if self.path.exists():
            self.man=json.loads(self.path.read_bytes())
            require(self.man["format"]==TEMP and self.man["binding"]==binding and
                    self.man["temporaryOnly"] is True,"Same original next checkpoint")
        else:self.man={"format":TEMP,"binding":binding,"temporaryOnly":True,"phases":{}}
    def save(self,name,data):
        o={"format":TEMP,"binding":self.binding,"phase":name,"complete":True,"data":self.q.enc(data)}
        t=self.root/(name+".tmp.json.gz")
        with t.open("wb") as raw:
            with gzip.GzipFile(filename="",mode="wb",fileobj=raw,compresslevel=1,mtime=0) as gz:
                with io.TextIOWrapper(gz,encoding="utf-8",newline="\n") as f:
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
    root=Path(a.probe_out);item=probe["parameters"]["temporaryPhases"]["complete-next-original-forcings"]
    path=checked(root,item)
    with gzip.open(path,"rt",encoding="utf-8") as f:o=json.load(f)
    require(o["format"]==PROBE_FORMAT and o["binding"]==probe["parameters"]["binding"] and
            o["phase"]=="complete-next-original-forcings" and o["complete"] is True,
            "Actual complete original next forcing payload")
    data=q.dec(o["data"],q.DQ);meta=probe["parameters"]["originalForcing"]
    require(q.mh(data["high"])==meta["originalNextHighSHA256"] and
            q.mh(data["low"])==meta["originalNextLowSHA256"] and
            q.mh(data["incoming"])==meta["priorIncomingSHA256"],
            "Complete actual forcing and incoming matrix identities")
    return data

def integer_keys(high):
    return {int(k):{int(r):M for r,M in sector.items()} for k,sector in high.items()}
def prepare(a,q,s,m,j,store,probe,previous):
    old=store.load("prepared-complete-low")
    if old is not None:return old
    data=probe_data(a,q,probe);meta0=data["metadata"];high=data["high"]
    n=a.order;c0=meta0["newQuotientRepresentatives"];np=meta0["projectedExitRepresentativeColumns"]
    need_extra=meta0["newExtraRepresentativeColumns"]
    require(data["order"]==n and high.nrows()==5100 and high.ncols()==c0,
            "Actual original next forcing shape and order")
    necessity=probe["parameters"]["highNecessity"]
    if q.zero(high):
        active=list(range(c0));excluded=0;reason="all original high forcing coordinates exactly zero"
    else:
        require(need_extra==1 and necessity.get("performed") is True and
                necessity.get("extraHeadHighQNonmembershipProved") is True and
                necessity.get("fieldResidualRank")==1,
                "A field-compatible nonzero high RHS needs a genuine rational particular")
        require(q.zero(q.DQ.sub(high,range(5100),range(np))),"Projected next high coordinates zero")
        active=list(range(np));excluded=1;reason="actual augmented high Q rank excludes extra head"
    C=data["constantLow"];W=data["incoming"];d=meta0["completePriorIncomingColumns"]
    require((C.nrows(),C.ncols())==(1088,587) and (W.nrows(),W.ncols())==(1088,d),
            "Complete constant and actual incoming dimensions")
    ranks=meta0["previousCompleteConnectionRanks"]
    require(len(ranks)==n-1 and d==sum(ranks),"Complete cumulative original incoming image")
    require(q.mh(C)==previous["parameters"]["preparation"]["constantSHA256"],
            "Same original constant correction basis")
    R=q.DQ.sub(data["low"],range(1088),active);M=q.DQ.cat([C,W,R])
    require(q.zero(q.DQ.sub(high,range(5100),active)),"All surviving original high forcings zero")
    RH=integer_keys(data["representativeHigh"]);IH=integer_keys(data["incomingHigh"])
    RH={t:{r:q.DQ.sub(X,range(X.nrows()),active) for r,X in sector.items()} for t,sector in RH.items()}
    out={"order":n,"M":M,"representativeMaps":[q.DQ.sub(x,range(155),active) for x in data["representativeMaps"]],
        "representativeHigh":RH,"incomingMaps":data["incomingMaps"],"incomingHigh":IH,
        "stableMaps":data["stableMaps"],"Z3":data["Z3"],
        "coefficientData":data["coefficientData"],"top":data["top"]}
    meta={"order":n,"shape":[1088,587+d+len(active)],"activeOriginalQuotientRepresentatives":active,
        "originalQuotientRepresentatives":c0,"highExcludedHeadDimension":excluded,"highReductionReason":reason,
        "newLowForcingColumns":len(active),"completePriorIncomingColumns":d,
        "completeConstantColumns":587,"projectedStableHeadCount":data["stableMaps"][0].ncols(),
        "previousCompleteHeadCount":meta0["previousCompleteHeadCount"],
        "previousCompleteConnectionRanks":ranks,"matrixSHA256":q.mh(M),
        "allSurvivingOriginalHighForcingsExactlyZero":True,"fullQHighKernelOnlyTwoAlreadyProved":True,
        "originalProbeBinding":probe["parameters"]["binding"],"originalLowForcingSHA256":q.mh(R),
        "constantSHA256":q.mh(C),"incomingSHA256":q.mh(W),"allHigherIncomingCochainCoordinatesRetained":True,
        "unscaledOriginalRationalColumns":True}
    out["metadata"]=meta;store.save("prepared-complete-low",out)
    event("complete original next low matrix saved",order=n,shape=meta["shape"]);return out

def worker(a):
    if hasattr(sys,"set_int_max_str_digits"):sys.set_int_max_str_digits(0)
    resource.setrlimit(resource.RLIMIT_AS,(a.memory_mib*1024**2,)*2)
    require(sha(a.projection_consumer)==PINS["projection_consumer"],"Worker pinned exact arithmetic")
    q=module("r150_next_worker_Q",a.projection_consumer)
    require(sha(a.worker_input)==a.worker_input_sha256,"Complete worker input hash")
    with gzip.open(a.worker_input,"rt",encoding="utf-8") as f:o=json.load(f)
    require(o["format"]==TEMP and o["binding"]==a.worker_binding and
            o["phase"]=="prepared-complete-low" and o["complete"] is True,"Exact worker input binding")
    M=q.dec(o["data"]["M"],q.DQ)
    require(M.nrows()==1088 and 587<=M.ncols()<=605 and
            list((M.nrows(),M.ncols()))==o["data"]["metadata"]["shape"],"Actual exact next matrix")
    t=time.monotonic();R,r=M.rref();actual_rref_seconds=time.monotonic()-t;piv=q.pivots(R,r)
    obj={"format":TEMP,"binding":a.worker_binding,"phase":"complete-rref","complete":True,
        "data":{"R":q.enc(R),"rank":r,"pivotColumns":piv,"sourceMatrixSHA256":q.mh(M)}}
    path=Path(a.worker_out);tmp=path.with_name(path.name+".tmp")
    with tmp.open("wb") as raw:
        with gzip.GzipFile(filename="",mode="wb",fileobj=raw,compresslevel=1,mtime=0) as gz:
            with io.TextIOWrapper(gz,encoding="utf-8",newline="\n") as f:
                json.dump(obj,f,sort_keys=True,separators=(",",":"))
    os.replace(tmp,path);print(json.dumps({"status":"complete-rref-saved","rank":r,"actualRrefSeconds":actual_rref_seconds}),flush=True)

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
    check("before exact next low RREF");log=store.root/"exact-low-rref-worker.log"
    with log.open("wb") as f:
        p=subprocess.run(cmd,stdout=f,stderr=subprocess.STDOUT,
                         timeout=max(.05,DEADLINE-time.monotonic()),check=False)
    require(p.returncode==0 and pending.exists(),"Exact next RREF: "+log.read_text(errors="replace")[-2500:])
    out=store.admit_rref(pending)
    timing=json.loads(log.read_text().splitlines()[-1])
    require(timing["status"]=="complete-rref-saved" and timing["rank"]==out["rank"],"Actual worker time record")
    event("complete exact next RREF saved",rank=out["rank"],seconds=timing["actualRrefSeconds"])
    return out

def kernel(a,q,m,j,store,data,rr):
    old=store.load("verified-low-kernel")
    if old is not None:return old
    M=data["M"];R=rr["R"];rank=rr["rank"];piv=rr["pivotColumns"];md=data["metadata"]
    d=md["completePriorIncomingColumns"];base=587+d;c=M.ncols()-base
    require(rr["sourceMatrixSHA256"]==q.mh(M) and q.pivots(R,rank)==piv,"Complete actual rational RREF")
    pref=[sum(p<n for p in piv) for n in (585,587,base,M.ncols())]
    require(pref[:3]==[578,580,580+d],"Complete original constant and incoming rank prefix")
    K,pp,free=j.canonical_kernel(m,R,rank)
    require(pp==piv and q.zero(M*K),"Every original next low kernel product")
    C=q.DQ.sub(K,range(base,base+c),range(K.ncols()))
    CR,h=C.rref();choice=q.pivots(CR,h)
    require(h==c-(rank-(580+d)) and 0<=h<=c,"Complete surviving next head count")
    stable=md["projectedStableHeadCount"];full=stable+h
    beta=md["previousCompleteHeadCount"]-full
    require(full>=13 and beta>=0 and beta==md["originalQuotientRepresentatives"]-h,
            "Complete next original leading space dimension")
    prior=md["previousCompleteConnectionRanks"]
    fp=[FIELD_SPECTRUM.count(i) for i in range(1,a.order+1)]
    if prior==fp[:-1]:require(beta>=fp[-1],"Legal next field lower after all prior ranks agree")
    G=q.DQ.sub(K,range(K.nrows()),choice)
    meta={"rank":rank,"prefixRanks":pref,"completeKernelDimension":K.ncols(),"headProjectionRank":h,
        "completeFullNextLeadingDimension":full,"fullNextConnectionRank":beta,
        "previousCompleteConnectionRanks":prior,"allOriginalLowKernelProductsZero":True,
        "originalLowKernelProductCoordinates":1088*K.ncols(),"kernelSHA256":q.mh(K),
        "freeColumns":free,"chosenKernelColumns":choice}
    out={"K":K,"selected":G,"metadata":meta};store.save("verified-low-kernel",out)
    event("complete next low kernel verified",order=a.order,rank=rank,newHeads=h);return out

def cochains(a,q,store,data,ker):
    old=store.load("complete-next-cochains-candidate")
    if old is not None:return old
    n=a.order;G=ker["selected"];h=G.ncols();d=data["metadata"]["completePriorIncomingColumns"]
    base=587+d;c=data["M"].ncols()-base;st=data["stableMaps"][0].ncols()
    X=q.DQ.sub(G,range(585),range(h));A=q.DQ.sub(G,range(585,587),range(h))
    Y=q.DQ.sub(G,range(587,base),range(h));C=q.DQ.sub(G,range(base,base+c),range(h))
    low=[]
    for k in range(n+1):
        new=data["representativeMaps"][k]*C+data["incomingMaps"][k]*Y
        if k==n:new+=q.DQ.vcat([q.DQ.mat(20,h),q.DQ.sub(X,range(135),range(h))])
        low.append(q.DQ.cat([data["stableMaps"][k],new]))
    RH=integer_keys(data["representativeHigh"]);IH=integer_keys(data["incomingHigh"]);high={}
    for k in range(6,n):
        high[k]={}
        for r,size in ((2,450),(3,990)):
            P=RH.get(k,{}).get(r,q.DQ.mat(size,c));U=IH.get(k,{}).get(r,q.DQ.mat(size,d))
            high[k][r]=q.DQ.cat([q.DQ.mat(size,st),P*C+U*Y])
    high[n]={2:q.DQ.cat([q.DQ.mat(450,st),q.DQ.sub(X,range(135,585),range(h))]),
             3:q.DQ.cat([q.DQ.mat(990,st),data["Z3"]*A])}
    nc=st+h;RT,r=low[0].transpose().rref();free=q.pivots(RT,r)
    require(r==nc,"All complete next heads independent")
    unit=q.DQ.sub(low[0],free,range(nc));N=unit.inv()
    require(unit*N==q.DQ.eye(nc),"Actual original leading normalization")
    low=[M*N for M in low];high={t:{r:M*N for r,M in sector.items()} for t,sector in high.items()}
    require(q.DQ.sub(low[0],free,range(nc))==q.DQ.eye(nc),"Original free head I")
    pack=q.DQ.vcat(low[:6]+[q.DQ.vcat([low[k],high[k][2],high[k][3]]) for k in range(6,n+1)])
    require((pack.nrows(),pack.ncols())==(930+1595*(n-5),nc),"Complete next original coefficient pack")
    ranges={}
    for k in range(6,n+1):
        z=930+1595*(k-6)
        ranges[str(k)]={"normal0":[z,z+20],"normal1":[z+20,z+155],
                        "normal2":[z+155,z+605],"normal3":[z+605,z+1595]}
    md={"cochainOrder":n,"shape":[pack.nrows(),nc],"headRank":nc,"newHeadCount":h,
        "packSHA256":q.mh(pack),"headSHA256":q.mh(low[0]),"normalizerSHA256":q.mh(N),
        "freeOriginalHeadCoordinates":free,"lambda0Through5Ranges":[[155*k,155*(k+1)] for k in range(6)],
        "higherCoefficientRanges":ranges,"allActualHigherCoefficientsRetained":True,
        "allWholeIncomingHighCoordinatesActuallyAdded":True,"noNextHighForcingZeroAssumption":True}
    out={"pack":pack,"normalizer":N,"selectedKernel":G,"metadata":md}
    store.save("complete-next-cochains-candidate",out);return out

def verify(a,q,s,m,j,store,data,cand):
    old=store.load("complete-next-cochains-verified")
    if old is not None:return old
    n=a.order;pack=cand["pack"];nc=pack.ncols();coeff=q.coefficient_decode(data["coefficientData"])
    low=[q.DQ.sub(pack,range(155*k,155*(k+1)),range(nc)) for k in range(6)];high={}
    for k in range(6,n+1):
        p=930+1595*(k-6);low.append(q.DQ.sub(pack,range(p,p+155),range(nc)))
        high[k]={2:q.DQ.sub(pack,range(p+155,p+605),range(nc)),
                 3:q.DQ.sub(pack,range(p+605,p+1595),range(nc))}
    ledger=store.load("original-verification-ledger")
    if ledger is None:ledger={"packSHA256":q.mh(pack),"completedOrders":[],"originalCoordinates":0}
    require(ledger["packSHA256"]==q.mh(pack) and
            ledger["completedOrders"]==list(range(len(ledger["completedOrders"]))),"Whole-order verification ledger")
    for k in range(len(ledger["completedOrders"]),n+1):
        check("before complete original order"+str(k));V=s.original_low(q,m,j,coeff,data["top"],low,k)
        for t,H in high.items():
            if t<=k:V+=q.DQ.vcat([j.apply(m,coeff,k-t,r,H,nc) for r in (0,1)])
        require(q.zero(V),"Every original low product")
        for r in (2,3):
            H=q.DQ.mat(len(j.source_rows(r)),nc)
            for t,X in high.items():
                if t<=k:H+=j.apply_sparse(m,coeff,k-t,r,X,nc)
            require(q.zero(H),"Every original high product")
        ledger["completedOrders"].append(k);ledger["originalCoordinates"]+=6188*nc
        store.save("original-verification-ledger",ledger);event("complete original order verified",order=k,heads=nc)
    require(ledger["originalCoordinates"]==(n+1)*6188*nc,"All original full products at every order")
    md=dict(cand["metadata"]);md.update({"allOrdersAll6188OriginalSourceRowsVerified":True,
        "fullOriginalVerificationComplete":True,"originalProductCoordinates":ledger["originalCoordinates"]})
    out={"pack":pack,"normalizer":cand["normalizer"],"selectedKernel":cand["selectedKernel"],"metadata":md}
    store.save("complete-next-cochains-verified",out);return out

def main():
    global DEADLINE,REC,OUT
    p=argparse.ArgumentParser()
    for k in ("generator","jet-actions","projection-consumer","sixth-consumer",
              "previous-receipt","previous-receipt-sha256","previous-source-sha256",
              "probe-receipt","probe-receipt-sha256","probe-out","checkpoint-dir","out"):
        p.add_argument("--"+k)
    p.add_argument("--order",type=int)
    p.add_argument("--remaining-seconds",type=float,default=180);p.add_argument("--memory-mib",type=int,default=2048)
    for k in ("worker-input","worker-input-sha256","worker-binding","worker-out"):p.add_argument("--"+k)
    a=p.parse_args()
    if a.worker_input:worker(a);return
    for k in ("generator","jet_actions","projection_consumer","sixth_consumer","previous_receipt",
              "previous_receipt_sha256","previous_source_sha256","probe_receipt","probe_receipt_sha256",
              "probe_out","checkpoint_dir","out"):require(getattr(a,k) is not None,"Required "+k)
    require(a.order is not None and 9<=a.order<=11 and 0<a.remaining_seconds<=600 and
            512<=a.memory_mib<=4096,"Bounded complete next stage")
    if hasattr(sys,"set_int_max_str_digits"):sys.set_int_max_str_digits(0)
    resource.setrlimit(resource.RLIMIT_AS,(a.memory_mib*1024**2,)*2)
    start=time.monotonic();DEADLINE=start+a.remaining_seconds-min(8,a.remaining_seconds/10)
    signal.signal(signal.SIGTERM,stop);signal.signal(signal.SIGINT,stop);OUT=Path(a.out)
    REC={"format":FORMAT,"status":"running","outcome":"pending-original-next-inputs","_start":start,
        "scriptSHA256":sha(__file__),"events":[],"parameters":{"author":"Astra-ISP-789f / normal_annihilator",
        "aiAssisted":"GPT-6 Astra Pro","order":a.order,"sharedSeconds":a.remaining_seconds,"memoryMiB":a.memory_mib,
        "temporaryOnly":True,"allAncestorFilesReadOnly":True,"largeDataUploadedOrCommitted":False,
        "selectedMinorLeading31UnitNotClaimed":True,"higherSourceQuotientQ26NotClaimed":True,
        "newPhaseGzipMtime":0,"newPhaseGzipFilename":"","runtimeExcludedFromMathematicalPhasePayload":True}}
    code=1
    try:
        pins=dict(PINS);pins["probe_receipt"]=a.probe_receipt_sha256;pins["previous_receipt"]=a.previous_receipt_sha256
        for k,d in pins.items():require(sha(getattr(a,k))==d,"Actual input pin "+k)
        previous=result(a.previous_receipt);probe=result(a.probe_receipt)
        require(previous["status"]=="completed" and previous["scriptSHA256"]==a.previous_source_sha256 and
                previous["parameters"]["fullOriginalVerificationComplete"] is True,"Actual complete preceding stage")
        require(probe["status"]=="completed" and probe["format"]==PROBE_FORMAT and
                probe["parameters"]["selfSHA256"]==PROBE_SHA and probe["parameters"]["order"]==a.order,
                "Actual original next forcing probe")
        pm=probe["parameters"]["originalForcing"]
        prior_ranks=previous["parameters"]["fullFirstEightRanks"] if a.order==9 else previous["parameters"]["fullConnectionRanks"]
        require(probe["parameters"]["inputSHA256"]["previous_receipt"]==a.previous_receipt_sha256 and
                pm["previousCompleteConnectionRanks"]==prior_ranks and
                pm["previousCompleteHeadCount"]==previous["parameters"]["actualCanonicalCochain"]["headRank"],
                "The high probe and low solve share the exact complete preceding source")
        require(pm["allOriginalRepresentativeLowerProductsZero"] is True and
                pm["allWholeIncomingDirectionsTransported"] is True and pm["allIncomingHighCoefficientsRetained"] is True and
                pm["incomingHighForcingExactlyZero"] is True,"Complete original incoming source identities")
        necessity=probe["parameters"]["highNecessity"]
        require(pm["extraHeadHighForcingZero"] is True or necessity.get("extraHeadHighQNonmembershipProved") is True,
                "Nonzero compatible high forcing still requires a rational lift")
        binding=hash_obj({"format":FORMAT,"sourceSHA256":sha(__file__),"inputSHA256":pins,
            "previousSourceSHA256":a.previous_source_sha256,"previousBinding":previous["parameters"]["binding"],
            "probeBinding":probe["parameters"]["binding"],"order":a.order})
        REC["parameters"]["binding"]=binding;REC["parameters"]["inputSHA256"]=pins
        require(Path(a.checkpoint_dir).resolve()!=Path(a.probe_out).resolve(),"Separate new low checkpoint")
        q=module("r150_next_low_Q",a.projection_consumer);s=module("r150_next_low_sixth",a.sixth_consumer)
        m=module("r150_next_low_first",a.generator);j=module("r150_next_low_actions",a.jet_actions)
        store=Store(a.checkpoint_dir,binding,q);data=prepare(a,q,s,m,j,store,probe,previous)
        REC["parameters"]["preparation"]=data["metadata"]
        rr=rref(a,q,store);ker=kernel(a,q,m,j,store,data,rr)
        REC["parameters"]["completeLowKernel"]=ker["metadata"]
        cand=cochains(a,q,store,data,ker);done=verify(a,q,s,m,j,store,data,cand)
        beta=ker["metadata"]["fullNextConnectionRank"];ranks=ker["metadata"]["previousCompleteConnectionRanks"]+[beta]
        require(len(ranks)==a.order and sum(ranks)<=14,"Complete original connection counts")
        known=[e for e,b in enumerate(ranks,1) for _ in range(b)]
        require(all(x>=P_SPECTRUM[i] for i,x in enumerate(known)),"Actual known exponents dominate true projection")
        lower=known+[max(a.order+1,P_SPECTRUM[i]) for i in range(len(known),14)]
        require(len(lower)==14 and lower==sorted(lower) and sum(lower)<=66 and sum(lower[:-1])<=55,
                "Actual rational lower spectrum within paid original field minor upper bounds")
        complete=len(known)==14 or sum(lower)==66
        REC["parameters"].update({"completeFullConnectionRank":beta,"fullConnectionRanks":ranks,
            "completeFullLeadingDimension":done["metadata"]["headRank"],"allFullNextHeadsCovered":True,
            "allOrdersAll6188OriginalSourceRowsVerified":True,"fullOriginalVerificationComplete":True,
            "actualCanonicalCochain":done["metadata"],"originalProductCoordinates":done["metadata"]["originalProductCoordinates"],
            "fullCharacteristicZeroPositiveIndicesLowerBounds":lower,
            "fullCharacteristicZeroLengthLowerBound":sum(lower),"fullCharacteristicZeroLengthUpperBound":66,
            "fullCharacteristicZeroNextMinorLowerBound":sum(lower[:-1]),
            "fullCharacteristicZeroNextMinorUpperBound":55,
            "fullCharacteristicZeroMaximumPositiveIndexUpperBound":66-sum(lower[:-1]),
            "completeFullCharacteristicZeroSpectrumProved":complete,
            "completeFullCharacteristicZeroPositiveSpectrum":lower if complete else None,
            "completeFullCharacteristicZeroSpectrumEqualsPaidField":complete and lower==FIELD_SPECTRUM,
            "explicitInfiniteFreeSourceBasisNotConstructedByThisStage":True,
            "nextOriginalHighForcingRequiresAllSavedCoefficients":True,
            "firstAllComputedRanksAgreeWithPaidField":ranks==[FIELD_SPECTRUM.count(i) for i in range(1,a.order+1)]})
        REC["status"]="completed";REC["outcome"]="complete-original-next-connection-exact";code=0
    except (TimeoutError,subprocess.TimeoutExpired) as e:
        REC["status"]="prefix-completed";REC["outcome"]="complete-stages-saved-time-budget";REC["error"]=str(e);code=75
    except BaseException as e:
        REC["status"]="failed";REC["error"]=type(e).__name__+": "+str(e);raise
    finally:
        flush();print(json.dumps({"status":REC["status"],"outcome":REC["outcome"],"order":a.order,
            "receipt":str(OUT),"elapsedSeconds":time.monotonic()-start}),flush=True)
    if code:raise SystemExit(code)
if __name__=="__main__":main()
