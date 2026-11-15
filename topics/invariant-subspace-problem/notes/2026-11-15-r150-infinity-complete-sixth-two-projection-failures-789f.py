#!/usr/bin/env python3
"""Complete original infinity sixth connection from two projection failures.

Author: Astra-ISP-789f / normal_annihilator.
AI-assisted: GPT-6 Astra Pro.
Read the completed original Q projection and the independently verified
complete constant high kernel.  Reuse the actual two exponent-six maps.
The nine earlier positive maps supply every lower incoming class, since
the complete full and projected first five leading spaces agree.
The only new exact system is 1088 by598.  Its full RREF is saved before
kernel extraction or source verification.  No field kernel is lifted.
All cochains are transported to the original 6188 source rows at all
seven orders.  Large reproducible files are temporary job checkpoints.
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

FORMAT="r150-infinity-complete-sixth-two-projection-failures-v1"
TEMP_FORMAT="r150-infinity-complete-sixth-temporary-v1"
GEN_SHA="2757b900480fe3bf1450100188df1679801351f0330d609e1a39b9c7ca146186"
ACT_SHA="2ebf418575df39ca2ed0a2165a37e92071c415b4734969c5bedc64e0b9ef4332"
Q_SOURCE_SHA="dc17dc88a5f1415c648b6ba5bf3fab4f7fb810aef6cc1552a5b2ea4acacbdf79"
HIGH_SOURCE_SHA="1a578441929247d114b7f39e9824b243dbc0433de781dd2ffce4d4e11dea4122"
Q_RECEIPT_SHA="ea44027e462054b9fdb9c9101065faaba0b14dc5ab9b1a5602c06fecbb765207"
FIFTH_RECEIPT_SHA="17361fc2f385bbc1ffe8b843d185d0c3acd2998276579d08e5d76e8233eaf036"
Q_BINDING="01ba6e6d1f1d0c0ae9ae22a319615887dce4c313d29c9ce1bde346445ae10766"
Q_STATE=(12208895,"839af8f6f6ae87d75c2cfcd206323a0ceb6193dd49a398134fdb8448e693b5ae")
COEFF=(267400,"94cffcf53fe22e7693e4c22bd67b237fe9d65933a50571891647c378a4b98034")
P_SPECTRUM=[1,1,1,1,3,4,4,4,5,6,6,7,8,10]
F_SPECTRUM=[1,1,1,1,3,4,4,4,5,6,7,8,10,11]
STOP=False
DEADLINE=0.0
REC=None
OUT=None

def require(ok,message):
    if not ok:raise AssertionError(message)
def canonical(x):
    return json.dumps(x,sort_keys=True,separators=(",",":"),ensure_ascii=True).encode("ascii")
def sha(path):
    h=hashlib.sha256()
    with Path(path).open("rb") as f:
        for b in iter(lambda:f.read(1048576),b""):h.update(b)
    return h.hexdigest()
def hsmall(x):return hashlib.sha256(canonical(x)).hexdigest()
def atomic(path,obj):
    path=Path(path);path.parent.mkdir(parents=True,exist_ok=True)
    t=path.with_name(path.name+".tmp");t.write_bytes(canonical(obj));os.replace(t,path)
def module(name,path):
    spec=importlib.util.spec_from_file_location(name,path)
    obj=importlib.util.module_from_spec(spec);sys.modules[name]=obj
    spec.loader.exec_module(obj);return obj
def stop_requested(*_):
    global STOP
    STOP=True
def check(stage):
    if STOP or time.monotonic()>=DEADLINE:
        raise TimeoutError("Stopped at complete boundary: "+stage)
def flush():
    if REC is not None:
        REC["elapsedSeconds"]=time.monotonic()-REC["_start"]
        obj={k:v for k,v in REC.items() if not k.startswith("_")}
        require(len(canonical(obj))<95000,"Small sixth receipt")
        atomic(OUT,obj)
def event(name,**values):
    REC["events"].append({"phase":name,**values});flush()
def descriptor(path):
    path=Path(path)
    return {"file":path.name,"bytes":path.stat().st_size,"sha256":sha(path),"temporaryOnly":True}
def checked(root,item):
    require(Path(item["file"]).name==item["file"],"Temporary basename")
    path=Path(root)/item["file"]
    require(path.stat().st_size==item["bytes"] and sha(path)==item["sha256"],
            "Complete temporary bytes/SHA")
    return path
def result(path):
    x=json.loads(Path(path).read_bytes());return x.get("result",x)
def fpin(path,digest):
    require(sha(path)==digest,"Actual input SHA: "+str(Path(path).name))

class Store:
    def __init__(self,root,binding,q):
        self.root=Path(root);self.root.mkdir(parents=True,exist_ok=True)
        self.binding=binding;self.q=q
        self.path=self.root/"complete-sixth-checkpoints.json"
        if self.path.exists():
            self.man=json.loads(self.path.read_bytes())
            require(self.man["format"]==TEMP_FORMAT and self.man["binding"]==binding
                    and self.man["temporaryOnly"] is True,"Same sixth checkpoint binding")
        else:
            self.man={"format":TEMP_FORMAT,"binding":binding,"temporaryOnly":True,"phases":{}}
    def save(self,name,data):
        obj={"format":TEMP_FORMAT,"binding":self.binding,"phase":name,"complete":True,
             "data":self.q.enc(data)}
        tmp=self.root/(name+".tmp.json.gz")
        with gzip.open(tmp,"wt",encoding="utf-8",compresslevel=1) as f:
            json.dump(obj,f,sort_keys=True,separators=(",",":"))
        digest=sha(tmp);dest=self.root/(name+"-"+digest+".json.gz")
        os.replace(tmp,dest)
        item=descriptor(dest);self.man["phases"][name]=item;atomic(self.path,self.man)
        REC["parameters"]["temporaryPhases"]=self.man["phases"]
        REC["parameters"]["temporaryManifestSHA256"]=sha(self.path);flush()
        return item
    def load(self,name):
        item=self.man["phases"].get(name)
        if item is None:return None
        path=checked(self.root,item)
        with gzip.open(path,"rt",encoding="utf-8") as f:obj=json.load(f)
        require(obj["format"]==TEMP_FORMAT and obj["binding"]==self.binding and
                obj["phase"]==name and obj["complete"] is True,"Complete same-bound phase")
        REC["parameters"]["temporaryPhases"]=self.man["phases"]
        REC["parameters"]["temporaryManifestSHA256"]=sha(self.path)
        return self.q.dec(obj["data"],self.q.DQ)
    def admit_worker_rref(self,path):
        with gzip.open(path,"rt",encoding="utf-8") as f:obj=json.load(f)
        require(obj["format"]==TEMP_FORMAT and obj["binding"]==self.binding and
                obj["phase"]=="complete-rref" and obj["complete"] is True,
                "Complete worker RREF identity")
        digest=sha(path);dest=self.root/("complete-rref-"+digest+".json.gz")
        os.replace(path,dest)
        self.man["phases"]["complete-rref"]=descriptor(dest);atomic(self.path,self.man)
        return self.load("complete-rref")

def read_q_phase(a,q,projection,phase,pin):
    root=Path(a.projection_out)/"temporary"
    mp=root/"small-projection-checkpoints.json"
    fpin(mp,projection["parameters"]["temporaryManifestSHA256"])
    man=json.loads(mp.read_bytes())
    require(man["binding"]==Q_BINDING and man["temporaryOnly"] is True,"Actual Q manifest")
    item=man["phases"][phase]
    require((item["bytes"],item["sha256"])==pin and
            item==projection["parameters"]["temporaryPhaseFiles"][phase],"Paid Q phase pin")
    path=checked(root,item)
    with gzip.open(path,"rt",encoding="utf-8") as f:obj=json.load(f)
    require(obj["format"]=="r150-infinity-small-projection-temporary-v1" and
            obj["binding"]==Q_BINDING and obj["domain"]=="Q" and
            obj["phase"]==phase and obj["complete"] is True,"Paid complete original Q phase")
    return obj["data"]

def coefficient_and_maps(a,q,m,j,h,projection,fifth):
    coeff,Z3,highmeta=h.paid_inputs(a,q,m,projection,fifth)
    original=read_q_phase(a,q,projection,"original-projection-coefficients",COEFF)
    PM=q.dec(original["P"][:7],q.DQ)
    require(len(PM)==7 and all((x.nrows(),x.ncols())==(224,155) for x in PM),
            "Actual original projected coefficient prefix")
    hashes=projection["parameters"]["originalProjection"]["originalProjectionCoefficientSHA256"]
    require([q.mh(x) for x in PM]==hashes[:7],"Same actual seven original projection matrices")
    Top=[q.DQ.sub(x,range(170),range(155)) for x in PM]
    data=read_q_phase(a,q,projection,"Q-smith-state",Q_STATE)
    state=q.dec(data,q.DQ)
    require(state["complete"] is True and state["level"]==10,"Actual complete Q positive directions")
    positive=state["positive"]
    require([g["exponent"] for g in positive]==[1,3,4,5,6,7,8,10],
            "Actual ordered complete positive groups")
    require([g["map"][0].ncols() for g in positive]==[4,1,3,1,2,1,1,1],
            "Actual ordered original map widths")
    require(all(len(g["map"])==12 and all(x.nrows()==155 for x in g["map"])
                for g in positive),"Complete original155 map coefficients")
    require(len(state["map"])==12 and state["map"][0].ncols()==13,"Actual13 free jets")
    for g,p in zip(positive,projection["parameters"]["positiveOriginalLifts"]):
        require(g["exponent"]==p["exponent"] and q.mh(g["map"][0])==p["originalHeadSHA256"],
                "Actual unchanged original Smith source heads")
    old=[g for g in positive if g["exponent"]<=5]
    new=next(g for g in positive if g["exponent"]==6)
    later=[g for g in positive if g["exponent"]>6]
    U=[]
    for k in range(7):
        blocks=[]
        for g in old:
            t=k-(6-g["exponent"])
            blocks.append(g["map"][t] if t>=0 else q.DQ.mat(155,g["map"][0].ncols()))
        U.append(q.DQ.cat(blocks))
    T=new["map"][:7]
    stable=[q.DQ.cat([g["map"][k] for g in later]+[state["map"][k]]) for k in range(7)]
    require(all(x.ncols()==9 for x in U) and all(x.ncols()==2 for x in T)
            and all(x.ncols()==16 for x in stable),"Nine incoming / two failures / sixteen paid heads")
    require(q.zero(U[0]),"All prior incoming shifts have zero leading head")
    head=q.DQ.cat([stable[0],T[0]])
    require(head.rref()[1]==18,"Actual full18 fifth leading heads before testing sixth")
    return coeff,Top,Z3,U,T,stable,highmeta

def original_low(q,m,j,coeff,Top,L,k):
    oneindex={v:i for i,v in enumerate(j.target_columns(1))}
    A,B=q.original_product(m,j,coeff,Top,oneindex,L,k)
    return q.DQ.vcat([A,B])

def prepare(a,q,m,j,h,store,projection,fifth):
    old=store.load("prepared-complete-low")
    if old is not None:return old
    check("read actual original Q maps")
    coeff,Top,Z3,U,T,stable,highmeta=coefficient_and_maps(a,q,m,j,h,projection,fifth)
    require(all(not x for x in coeff["pure"][0]),"Actual original F0 pure part zero")
    require(j.dimensions()=={"sourceSectors":[170,918,2295,2805],
                             "targetSectors":[20,135,450,990,1485,1287]},
            "Complete original coordinate dictionaries")
    require(all(x.nrows()==155 for x in U+T+stable),"Original pure/one support")
    # Targets of normal degree0/1 cannot occur in any source row of normal degree2/3.
    high_structural_rows=0
    indices={r:{v:i for i,v in enumerate(j.target_columns(r))} for r in (0,1)}
    for r in (2,3):
        for row in j.source_rows(r):
            require(all(not list(j.sparse_row_terms(coeff,k,row,t,indices[t]))
                        for k in range(7) for t in (0,1)),"All original high rows vanish on pure/one maps")
            high_structural_rows+=1
    require(high_structural_rows==5100,"All original high source rows accounted for")
    verified=0
    for k in range(6):
        check("actual incoming and failure low identities")
        require(q.zero(original_low(q,m,j,coeff,Top,U,k)) and
                q.zero(original_low(q,m,j,coeff,Top,T,k)),
                "All lower original source products of shifted incoming/failure maps")
        verified+=6188*11
    W=original_low(q,m,j,coeff,Top,U,6)
    R=original_low(q,m,j,coeff,Top,T,6)
    check("complete original constant correction block")
    J=q.DQ.vcat([q.DQ.cat([j.block(m,coeff,0,r,t) for t in (1,2)]) for r in (0,1)])
    L3=q.DQ.vcat([j.apply(m,coeff,0,r,{3:Z3},2) for r in (0,1)])
    require((J.nrows(),J.ncols())==(1088,585) and
            (L3.nrows(),L3.ncols())==(1088,2) and
            (W.nrows(),W.ncols())==(1088,9) and
            (R.nrows(),R.ncols())==(1088,2),"Complete low matrix dimensions")
    for r in (2,3):
        require(q.zero(j.apply_sparse(m,coeff,0,r,{3:Z3},2)),
                "Actual complete homogeneous high columns rechecked")
    M=q.DQ.cat([J,L3,W,R])
    require((M.nrows(),M.ncols())==(1088,598),"Complete original1088 by598 low system")
    metadata={"shape":[1088,598],"constantColumns":587,"pureConstantColumnsOmittedAsExactZero":20,
        "normalOneTwoColumns":585,"completeHighKernelColumns":2,"allPriorIncomingColumns":9,
        "newExponentSixForcingColumns":2,"fullSixthPaidProjectionHeads":16,
        "matrixSHA256":q.mh(M),"J0SHA256":q.mh(J),"highLowReturnSHA256":q.mh(L3),
        "completeIncomingSHA256":q.mh(W),"twoOriginalForcingSHA256":q.mh(R),
        "twoHeadSHA256":q.mh(T[0]),"sixteenPaidHeadSHA256":q.mh(stable[0]),
        "verifiedOriginalPrecedingProductCoordinates":verified,
        "all5100OriginalHighForcingRowsExactlyZero":True,
        "highRowsProvedZeroByActualCoordinateSupport":True,
        "all10200HomogeneousHighProductsRechecked":True,
        "allOriginalLowRowsRetained":1088,"incomingShifts":[5,5,5,5,3,2,2,2,1],
        "allIncomingSignsPositive":True,"unscaledOriginalRationalColumns":True,
        "paidHighMetadata":highmeta}
    data={"M":M,"Z3":Z3,"incomingMaps":U,"twoMaps":T,"stableMaps":stable,
          "coefficientData":q.coefficient_encode(coeff),"top":Top,"metadata":metadata}
    store.save("prepared-complete-low",data)
    REC["parameters"]["preparation"]=metadata
    event("complete original low preparation saved",shape=[1088,598])
    return data

def rref_worker(a):
    # Only an exact RREF is performed here.  The parent verifies the original
    # nullspace identity and source equations after this complete result is saved.
    if hasattr(sys,"set_int_max_str_digits"):sys.set_int_max_str_digits(0)
    resource.setrlimit(resource.RLIMIT_AS,(a.memory_mib*1024**2,)*2)
    fpin(a.projection_consumer,Q_SOURCE_SHA)
    q=module("r150_infinity_sixth_worker_projection",a.projection_consumer)
    require(sha(a.worker_input)==a.worker_input_sha256,"Worker complete input bytes")
    with gzip.open(a.worker_input,"rt",encoding="utf-8") as f:obj=json.load(f)
    require(obj["format"]==TEMP_FORMAT and obj["binding"]==a.worker_binding and
            obj["phase"]=="prepared-complete-low" and obj["complete"] is True,
            "Worker exact prepared matrix binding")
    M=q.dec(obj["data"]["M"],q.DQ)
    require((M.nrows(),M.ncols())==(1088,598),"Worker exact matrix shape")
    t=time.monotonic();R,r=M.rref()
    require((R.nrows(),R.ncols())==(1088,598),"Full actual RREF shape")
    piv=q.pivots(R,r)
    out={"format":TEMP_FORMAT,"binding":a.worker_binding,"phase":"complete-rref","complete":True,
         "data":{"R":q.enc(R),"rank":r,"pivotColumns":piv,
                 "sourceMatrixSHA256":q.mh(M),"elapsedSeconds":time.monotonic()-t}}
    temp=Path(a.worker_out).with_name(Path(a.worker_out).name+".tmp")
    with gzip.open(temp,"wt",encoding="utf-8",compresslevel=1) as f:
        json.dump(out,f,sort_keys=True,separators=(",",":"))
    os.replace(temp,a.worker_out)
    print(json.dumps({"status":"complete-rref-saved","rank":r,"sha256":sha(a.worker_out),
                      "bytes":Path(a.worker_out).stat().st_size}),flush=True)

def obtain_rref(a,q,store,prepared):
    old=store.load("complete-rref")
    if old is not None:return old
    pending=store.root/"complete-rref-worker.json.gz"
    if pending.exists():return store.admit_worker_rref(pending)
    check("before original exact small RREF")
    item=store.man["phases"]["prepared-complete-low"]
    source=checked(store.root,item)
    cmd=[sys.executable,str(Path(__file__).resolve()),"--worker-input",str(source.resolve()),
         "--worker-input-sha256",item["sha256"],"--worker-binding",store.binding,
         "--worker-out",str(pending.resolve()),"--projection-consumer",str(Path(a.projection_consumer).resolve()),
         "--memory-mib",str(a.memory_mib)]
    log=store.root/"exact-rref-worker.log"
    event("exact1088 by598 RREF worker started")
    with log.open("wb") as f:
        p=subprocess.run(cmd,stdout=f,stderr=subprocess.STDOUT,
                         timeout=max(.05,DEADLINE-time.monotonic()),check=False)
    require(p.returncode==0 and pending.exists(),"Exact RREF worker: "+log.read_text(errors="replace")[-2500:])
    old=store.admit_worker_rref(pending)
    event("complete exact RREF saved",rank=old["rank"],seconds=old["elapsedSeconds"])
    return old

def complete_kernel(a,q,m,j,store,prepared,rr):
    old=store.load("verified-low-kernel")
    if old is not None:return old
    M=prepared["M"];R=rr["R"];rank=rr["rank"];piv=rr["pivotColumns"]
    require(rr["sourceMatrixSHA256"]==q.mh(M) and q.pivots(R,rank)==piv,"RREF full original matrix identity")
    ranks=[sum(p<n for p in piv) for n in (585,587,596,598)]
    require(ranks[:3]==[578,580,589],"Actual J0 / complete constant image / complete incoming ranks")
    require(ranks[3] in (590,591),"Full sixth rank against paid field lower and two projection exits")
    K,piv2,free=j.canonical_kernel(m,R,rank)
    require(piv2==piv and K.nrows()==598 and K.ncols()==598-rank,"Complete exact low kernel")
    check("complete low kernel full multiplication")
    require(q.zero(M*K),"Complete original1088 by598 kernel multiplication")
    C=q.DQ.sub(K,range(596,598),range(K.ncols()))
    CR,head=C.rref();choice=q.pivots(CR,head)
    require(head==591-rank and head in (0,1),"Actual new leading projection dimension")
    selected=q.DQ.sub(K,range(598),choice)
    leading=q.DQ.sub(C,range(2),choice)
    require(head==0 or leading.rref()[1]==head,"Actual independent new two-dimensional quotient heads")
    meta={"rank":rank,"prefixRanks":{"normalOneTwo":ranks[0],"completeConstant":ranks[1],
        "completeConstantAndIncoming":ranks[2],"withTwoSixthForcings":ranks[3]},
        "completeKernelDimension":K.ncols(),"newLeadingDimension":head,
        "kernelSHA256":q.mh(K),"allOriginalLowKernelProductsZero":True,
        "originalLowKernelProductCoordinates":1088*K.ncols(),
        "fullSixthRank":2-head,"completeFullSixthLeadingDimension":16+head,
        "freeColumns":free,"selectedKernelColumns":choice,
        "leadingOnActualTwoFailuresSHA256":q.mh(leading)}
    data={"K":K,"selected":selected,"leading":leading,"metadata":meta}
    store.save("verified-low-kernel",data)
    REC["parameters"]["completeLowKernel"]=meta
    event("complete low kernel and head projection verified",rank=rank,newHeads=head)
    return data

def construct_cochains(q,m,j,store,prepared,kernel):
    old=store.load("complete-sixth-cochains-candidate")
    if old is not None:return old
    G=kernel["selected"];h=G.ncols()
    C=q.DQ.sub(G,range(596,598),range(h))
    Y=q.DQ.sub(G,range(587,596),range(h))
    X=q.DQ.sub(G,range(585),range(h))
    A=q.DQ.sub(G,range(585,587),range(h))
    U=prepared["incomingMaps"];T=prepared["twoMaps"];stable=prepared["stableMaps"];Z3=prepared["Z3"]
    low=[]
    for k in range(7):
        new=T[k]*C+U[k]*Y
        if k==6:
            new+=q.DQ.vcat([q.DQ.mat(20,h),q.DQ.sub(X,range(135),range(h))])
        low.append(q.DQ.cat([stable[k],new]))
    two=q.DQ.cat([q.DQ.mat(450,16),q.DQ.sub(X,range(135,585),range(h))])
    three=q.DQ.cat([q.DQ.mat(990,16),Z3*A])
    heads=low[0];n=16+h
    require(heads.rref()[1]==n,"Original pure/one leading heads independent")
    RT,r=heads.transpose().rref();free=q.pivots(RT,r)
    unit=q.DQ.sub(heads,free,range(n))
    normalizer=unit.inv()
    require(unit*normalizer==q.DQ.eye(n),"Actual leading normalizer")
    low=[x*normalizer for x in low];two=two*normalizer;three=three*normalizer
    require(q.DQ.sub(low[0],free,range(n))==q.DQ.eye(n),"Canonical full leading free I")
    pack=q.DQ.vcat(low[:6]+[q.DQ.vcat([low[6],two,three])])
    require((pack.nrows(),pack.ncols())==(2525,n),"Complete seven-order canonical source pack")
    metadata={"shape":[2525,n],"heads":n,"newHeadCount":h,
        "normalizerSHA256":q.mh(normalizer),"fullHeadSHA256":q.mh(low[0]),
        "packSHA256":q.mh(pack),"freeOriginalPureOneCoordinates":free,
        "sevenOrdersRetained":True,"sourceCoordinateSectorsAtOrdersZeroThroughFive":[0,1],
        "sourceCoordinateSectorsAtOrderSix":[0,1,2,3],
        "normalFourFiveAtOrderSixZeroByCompleteHighKernel":True,
        "allTwoEmbeddingsAndIncomingShiftsRetained":True,
        "lambda0Through5Ranges":[[155*k,155*(k+1)] for k in range(6)],
        "lambda6Ranges":{"normal0":[930,950],"normal1":[950,1085],
                         "normal2":[1085,1535],"normal3":[1535,2525]}}
    data={"pack":pack,"normalizer":normalizer,"selectedKernel":G,"metadata":metadata}
    store.save("complete-sixth-cochains-candidate",data)
    event("all actual sixth cochains saved before original verification",heads=n)
    return data

def verify_cochains(a,q,m,j,store,prepared,candidate):
    done=store.load("complete-sixth-cochains-verified")
    if done is not None:return done
    pack=candidate["pack"];n=pack.ncols();coeff=q.coefficient_decode(prepared["coefficientData"])
    low=[q.DQ.sub(pack,range(155*k,155*(k+1)),range(n)) for k in range(6)]
    low.append(q.DQ.sub(pack,range(930,1085),range(n)))
    X2=q.DQ.sub(pack,range(1085,1535),range(n))
    X3=q.DQ.sub(pack,range(1535,2525),range(n))
    Top=prepared["top"]
    ledger=store.load("original-verification-ledger")
    if ledger is None:ledger={"packSHA256":q.mh(pack),"completedOrders":[],"originalCoordinates":0}
    require(ledger["packSHA256"]==q.mh(pack),"Verification ledger exact same complete cochains")
    require(ledger["completedOrders"]==list(range(len(ledger["completedOrders"]))),
            "Only complete ascending original verification orders")
    for k in range(len(ledger["completedOrders"]),7):
        check("before complete original order"+str(k))
        low_product=original_low(q,m,j,coeff,Top,low,k)
        if k==6:
            extra=q.DQ.vcat([j.apply(m,coeff,0,r,{2:X2,3:X3},n) for r in (0,1)])
            low_product+=extra
        require(q.zero(low_product),"All1088 original low source products at order"+str(k))
        for r in (2,3):
            if k==6:
                H=j.apply_sparse(m,coeff,0,r,{2:X2,3:X3},n)
                require(q.zero(H),"All original high source products at order6")
            else:
                # The actual complete support test was performed during preparation.
                require(prepared["metadata"]["all5100OriginalHighForcingRowsExactlyZero"] is True,
                        "Paid all original high rows are structurally zero")
        ledger["completedOrders"].append(k);ledger["originalCoordinates"]+=6188*n
        ledger["lastCompleteOrder"]=k
        store.save("original-verification-ledger",ledger)
        event("complete original order verified",order=k,allSourceRows=6188,heads=n)
    require(ledger["originalCoordinates"]==7*6188*n,"Every original seven-order product counted")
    md=dict(candidate["metadata"])
    md.update({"allSevenOrdersAll6188OriginalSourceRowsVerified":True,
        "originalProductCoordinates":ledger["originalCoordinates"],
        "fullOriginalVerificationComplete":True,
        "headRank":n,"allOriginalHighCrossTermsRetained":True,
        "allOriginalNormalFourFiveEquationsIncludedViaCompleteKernel":True})
    data={"pack":pack,"normalizer":candidate["normalizer"],
          "selectedKernel":candidate["selectedKernel"],"metadata":md}
    store.save("complete-sixth-cochains-verified",data)
    return data

def main():
    global DEADLINE,REC,OUT
    p=argparse.ArgumentParser()
    for key in ("projection-consumer","generator","jet-actions","high-consumer","projection-receipt",
                "projection-out","fifth-receipt","fifth-checkpoint-dir","high-receipt",
                "high-receipt-sha256","checkpoint-dir","out"):
        p.add_argument("--"+key)
    p.add_argument("--remaining-seconds",type=float,default=180)
    p.add_argument("--memory-mib",type=int,default=2048)
    p.add_argument("--worker-input")
    p.add_argument("--worker-input-sha256")
    p.add_argument("--worker-binding")
    p.add_argument("--worker-out")
    a=p.parse_args()
    if a.worker_input:
        rref_worker(a);return
    for key in ("projection_consumer","generator","jet_actions","high_consumer","projection_receipt",
                "projection_out","fifth_receipt","fifth_checkpoint_dir","high_receipt",
                "high_receipt_sha256","checkpoint_dir","out"):
        require(getattr(a,key) is not None,"Required --"+key.replace("_","-"))
    require(0<a.remaining_seconds<=600 and 512<=a.memory_mib<=4096,"Finite sixth resources")
    if hasattr(sys,"set_int_max_str_digits"):sys.set_int_max_str_digits(0)
    resource.setrlimit(resource.RLIMIT_AS,(a.memory_mib*1024**2,)*2)
    start=time.monotonic();DEADLINE=start+a.remaining_seconds-min(8.0,a.remaining_seconds/10)
    OUT=Path(a.out)
    signal.signal(signal.SIGTERM,stop_requested);signal.signal(signal.SIGINT,stop_requested)
    REC={"format":FORMAT,"status":"running","outcome":"pending-complete-original-inputs",
         "scriptSHA256":sha(__file__),"_start":start,"events":[],
         "parameters":{"author":"Astra-ISP-789f / normal_annihilator","aiAssisted":"GPT-6 Astra Pro",
             "sharedMathematicalSeconds":a.remaining_seconds,"memoryMiB":a.memory_mib,
             "chart":"original natural infinity u=1/s","onlyTwoNewForcingColumns":True,
             "noFieldKernelLiftedToQ":True,"allAncestorCachesReadOnly":True,
             "temporaryOnly":True,"largeDataUploadedOrCommitted":False,
             "fullHigherQuotientCharacteristicZeroNotClaimed":True,
             "selectedMinorLeading31UnitNotClaimed":True}}
    rc=1
    try:
        pins={"projection_consumer":Q_SOURCE_SHA,"generator":GEN_SHA,"jet_actions":ACT_SHA,
              "high_consumer":HIGH_SOURCE_SHA,"projection_receipt":Q_RECEIPT_SHA,
              "fifth_receipt":FIFTH_RECEIPT_SHA,"high_receipt":a.high_receipt_sha256}
        require(len(a.high_receipt_sha256)==64 and all(x in "0123456789abcdef" for x in a.high_receipt_sha256),
                "Actual new high receipt SHA pin")
        for key,digest in pins.items():fpin(getattr(a,key),digest)
        require(Path(a.checkpoint_dir).resolve() not in
                (Path(a.projection_out).resolve(),Path(a.fifth_checkpoint_dir).resolve()),
                "New sixth checkpoints cannot overwrite an ancestor")
        projection=result(a.projection_receipt);fifth=result(a.fifth_receipt);high=result(a.high_receipt)
        require(projection["status"]=="completed" and
                projection["parameters"]["semanticBinding"]==Q_BINDING and
                projection["parameters"]["QProjectionSmith"]["positiveIndices"]==P_SPECTRUM and
                projection["parameters"]["QProjectionSmith"]["complete"] is True and
                projection["parameters"]["allOriginal6188PositiveAndRemainingJetProductsZero"] is True,
                "Actual complete original P spectrum61 and original maps")
        require(fifth["status"]=="completed" and fifth["parameters"]["fullFirstFiveRanks"]==[4,0,1,3,1]
                and fifth["parameters"]["allSixOrdersAll6188OriginalSourceRowsVerified"] is True,
                "Complete full first five actual leading spaces")
        require(high["status"]=="completed" and high["parameters"]["selfSHA256"]==HIGH_SOURCE_SHA,
                "Actual complete pinned high driver")
        hc=high["parameters"]["conclusion"];hp=high["parameters"]["originalPreparation"]
        require(hc["completeHighQRankExact"]==3760 and
                hc["completeHighQKernelEqualsPaidTwoCubicColumns"] is True and
                hc["allNormalFourFiveCoordinatesOfAnyHighKernelAreZero"] is True and
                hp["all5100OriginalSourceRowsRetained"] is True and
                hp["all3762OriginalColumnsRetained"] is True and
                hp["allCrossSectorTermsRetained"] is True and
                hp["rationalUpperCertificate"]["all10200OriginalHighProductsVerified"] is True,
                "Complete Q high kernel two with all cross sectors")
        require(high["parameters"]["actualNativeRank"]["rank"]==3760,
                "Actual fixed-field lower agrees with true rational upper")
        binding=hsmall({"format":FORMAT,"sourceSHA256":sha(__file__),"inputSHA256":pins,
            "QStateSHA256":Q_STATE[1],"coefficientSHA256":COEFF[1],
            "originalQBinding":Q_BINDING,"completeHighBinding":high["parameters"]["binding"],
            "shape":[1088,598],"cochainOrder":6,"incomingExponentShifts":[5,5,5,5,3,2,2,2,1]})
        REC["parameters"]["binding"]=binding
        REC["parameters"]["inputSHA256"]=pins
        REC["parameters"]["completeHighQRank"]=3760
        REC["parameters"]["priorFullConnectionRanks"]=[4,0,1,3,1]
        q=module("r150_infinity_sixth_projection",a.projection_consumer)
        require(q.FULL_FIELD_SPECTRUM==F_SPECTRUM and
                projection["parameters"]["inputFiles"]["field_full_receipt"]["sha256"]==
                "14f396c3969ea90694d06e6f26fe75299bf2e678381b491ddb6cb78b93826815",
                "Paid original full-field spectrum bound by the completed projection receipt")
        REC["parameters"]["paidFullFieldSpectrum"]=F_SPECTRUM
        REC["parameters"]["paidFullFieldReceiptSHA256"]=projection["parameters"]["inputFiles"]["field_full_receipt"]["sha256"]
        m=module("r150_infinity_sixth_first",a.generator)
        j=module("r150_infinity_sixth_actions",a.jet_actions)
        h=module("r150_infinity_sixth_high",a.high_consumer)
        store=Store(a.checkpoint_dir,binding,q)
        prepared=prepare(a,q,m,j,h,store,projection,fifth)
        REC["parameters"]["preparation"]=prepared["metadata"];flush()
        rr=obtain_rref(a,q,store,prepared)
        kernel=complete_kernel(a,q,m,j,store,prepared,rr)
        REC["parameters"]["completeLowKernel"]=kernel["metadata"]
        candidate=construct_cochains(q,m,j,store,prepared,kernel)
        verified=verify_cochains(a,q,m,j,store,prepared,candidate)
        n=verified["metadata"]["headRank"];beta=18-n
        require(beta in (1,2) and beta==kernel["metadata"]["fullSixthRank"],"Complete sixth dimension formula")
        prefix=[1,1,1,1,3,4,4,4,5]+[6]*beta+[7]*(5-beta)
        lower=[max(x,y) for x,y in zip(P_SPECTRUM,prefix)]
        REC["parameters"].update({
            "completeFullSixthConnectionRank":beta,"fullFirstSixRanks":[4,0,1,3,1,beta],
            "completeFullSixthLeadingDimension":n,
            "newHeadsBeyondActualProjection":n-16,"allSevenOrdersAll6188OriginalSourceRowsVerified":True,
            "fullOriginalVerificationComplete":True,"originalProductCoordinates":verified["metadata"]["originalProductCoordinates"],
            "actualCanonicalCochain":verified["metadata"],
            "completeIncomingNineBeforeSixthRetained":True,
            "completeHighKernelOnlyTwoProvedIndependently":True,
            "allFullSixthHeadDirectionsCovered":True,
            "headRankActualOriginalCoordinates":n,
            "fullCharacteristicZeroPositiveIndicesLowerBounds":lower,
            "fullCharacteristicZeroLengthLowerBound":sum(lower),
            "fullCharacteristicZeroLengthUpperBound":66,
            "fullCharacteristicZeroNextMinorLowerBound":sum(lower[:-1]),
            "fullCharacteristicZeroMaximumPositiveIndexUpperBound":66-sum(lower[:-1]),
            "noHigherConnectionRankClaimed":True,
            "sixthNormalTwoAndThreeCoefficientsRetainedForSeventh":True,
            "seventhHighForcingAutomaticallyZeroByHeadEquality":beta==2,
            "seventhActualHighForcingRequiredIfRankOne":beta==1})
        REC["status"]="completed";REC["outcome"]="complete-original-sixth-connection-exact";rc=0
    except (TimeoutError,subprocess.TimeoutExpired) as exc:
        REC["status"]="prefix-completed";REC["outcome"]="complete-stages-saved-time-budget"
        REC["error"]=str(exc);rc=75
    except BaseException as exc:
        REC["status"]="failed";REC["error"]=type(exc).__name__+": "+str(exc);rc=1
        raise
    finally:
        flush()
        print(json.dumps({"status":REC["status"],"outcome":REC["outcome"],"receipt":str(OUT),
            "bytes":OUT.stat().st_size if OUT.exists() else 0,
            "sha256":sha(OUT) if OUT.exists() else None,
            "elapsedSeconds":time.monotonic()-start}),flush=True)
    if rc:raise SystemExit(rc)
if __name__=="__main__":main()
