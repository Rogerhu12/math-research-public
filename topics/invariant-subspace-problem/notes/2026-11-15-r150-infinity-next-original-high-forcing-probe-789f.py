#!/usr/bin/env python3
"""Next original infinity high forcing, orders nine through eleven.

Author: Astra-ISP-789f / normal_annihilator.
AI-assisted: GPT-6 Astra Pro.
Read one complete prior rational stage and the paid original projection.
Transport whole source maps, including every higher-normal coefficient and
all lower incoming directions. No old low RREF or high Gaussian is repeated.
A nonzero high forcing is only tested by the paid original constant-H DAG;
a zero field residual is not a rational particular.
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
import sys
import time

FORMAT="r150-infinity-next-original-high-forcing-v1"
PINS={
"generator":"2757b900480fe3bf1450100188df1679801351f0330d609e1a39b9c7ca146186",
"jet_actions":"2ebf418575df39ca2ed0a2165a37e92071c415b4734969c5bedc64e0b9ef4332",
"projection_consumer":"dc17dc88a5f1415c648b6ba5bf3fab4f7fb810aef6cc1552a5b2ea4acacbdf79",
"sixth_consumer":"4d759c0efbc8a647bd5845b21da5e871de28f0d43ae6f2fc84c376afb472e328",
"high_probe_helper":"cb246cfd93d03e3a842f47c6084f4bc3a4c3889f8fdbd740d2b68b22d27b123e",
"projection_receipt":"ea44027e462054b9fdb9c9101065faaba0b14dc5ab9b1a5602c06fecbb765207",
"high_receipt":"0f6cbe9bb23601be632d0045f35839b922e16e4d893aca6b9d4e2f849cbd9141"}
def need(ok,msg):
    if not ok:raise AssertionError(msg)
def canonical(x):return json.dumps(x,sort_keys=True,separators=(",",":"),ensure_ascii=True).encode("ascii")
def sha(path):
    h=hashlib.sha256()
    with Path(path).open("rb") as f:
        for b in iter(lambda:f.read(1048576),b""):h.update(b)
    return h.hexdigest()
def objhash(x):return hashlib.sha256(canonical(x)).hexdigest()
def atomic(path,obj):
    p=Path(path);p.parent.mkdir(parents=True,exist_ok=True)
    t=p.with_name(p.name+".tmp");t.write_bytes(canonical(obj));os.replace(t,p)
def module(name,path):
    spec=importlib.util.spec_from_file_location(name,path);m=importlib.util.module_from_spec(spec)
    sys.modules[name]=m;spec.loader.exec_module(m);return m
def result(path):
    x=json.loads(Path(path).read_bytes());return x.get("result",x)
def check(a):
    if time.monotonic()>=a._deadline:raise TimeoutError("Whole next-forcing boundary")
def checked(root,item):
    need(Path(item["file"]).name==item["file"],"Temporary basename")
    p=Path(root)/item["file"]
    need(p.stat().st_size==item["bytes"] and sha(p)==item["sha256"],"Exact complete temporary bytes")
    return p
def desc(path):
    p=Path(path);return {"file":p.name,"bytes":p.stat().st_size,"sha256":sha(p),"temporaryOnly":True}
def save(a,q,binding,phase,data,rec):
    root=Path(a.checkpoint_dir);root.mkdir(parents=True,exist_ok=True)
    payload={"format":FORMAT,"binding":binding,"phase":phase,"complete":True,
             "temporaryOnly":True,"data":q.enc(data)}
    temp=root/(phase+".tmp.json.gz")
    with temp.open("wb") as raw:
        with gzip.GzipFile(filename="",mode="wb",fileobj=raw,compresslevel=1,mtime=0) as gz:
            with io.TextIOWrapper(gz,encoding="utf-8",newline="\n") as f:
                json.dump(payload,f,sort_keys=True,separators=(",",":"))
    dg=sha(temp);dest=root/(phase+"-"+dg+".json.gz");os.replace(temp,dest)
    rec["parameters"].setdefault("temporaryPhases",{})[phase]=desc(dest)
    atomic(root/"next-forcing-checkpoints.json",{"format":FORMAT,"binding":binding,
        "temporaryOnly":True,"phases":rec["parameters"]["temporaryPhases"]})
    atomic(a.out,rec)
def previous_phase(a,q,previous,phase):
    n=a.order-1;root=Path(a.previous_out)
    if n==8:
        manifest="complete-eighth-checkpoints.json"
        fmt="r150-infinity-complete-eighth-temporary-v1"
    else:
        manifest="complete-next-checkpoints.json"
        fmt="r150-infinity-complete-next-temporary-v1"
    mp=root/manifest;par=previous["parameters"]
    need(sha(mp)==par["temporaryManifestSHA256"],"Actual previous complete manifest")
    man=json.loads(mp.read_bytes())
    need(man["format"]==fmt and man["binding"]==par["binding"] and man["temporaryOnly"] is True,
         "Original previous checkpoint identity")
    item=man["phases"][phase];need(item==par["temporaryPhases"][phase],"Actual previous phase descriptor")
    p=checked(root,item)
    with gzip.open(p,"rt",encoding="utf-8") as f:x=json.load(f)
    need(x["format"]==fmt and x["binding"]==par["binding"] and x["complete"] is True and x["phase"]==phase,
         "Previous complete mathematical payload")
    return q.dec(x["data"],q.DQ)
def integer_keys(high):
    return {int(k):{int(r):M for r,M in sector.items()} for k,sector in high.items()}
def unpack(q,pack,order,columns=None):
    cols=list(range(pack.ncols())) if columns is None else list(columns)
    need(pack.nrows()==930+1595*(order-5),"Complete original packed source shape")
    low=[q.DQ.sub(pack,range(155*k,155*(k+1)),cols) for k in range(6)]
    high={}
    for k in range(6,order+1):
        p=930+1595*(k-6)
        low.append(q.DQ.sub(pack,range(p,p+155),cols))
        high[k]={2:q.DQ.sub(pack,range(p+155,p+605),cols),
                 3:q.DQ.sub(pack,range(p+605,p+1595),cols)}
    return low,high
def source_product(a,q,s,m,j,coeff,Top,low,high,k):
    n=low[0].ncols();V=s.original_low(q,m,j,coeff,Top,low,k)
    for t,X in high.items():
        if t<=k:V+=q.DQ.vcat([j.apply(m,coeff,k-t,r,X,n) for r in (0,1)])
    H=[]
    for r in (2,3):
        X=q.DQ.mat(len(j.source_rows(r)),n)
        for t,sector in high.items():
            if t<=k:X+=j.apply_sparse(m,coeff,k-t,r,sector,n)
        H.append(X)
    return V,q.DQ.vcat(H)
def adapt_prepared(a,p):
    if a.order==9:
        high={6:{2:p["sixthNormalTwo"],3:p["sixthNormalThree"]},
              7:{2:p["seventhNormalTwo"],3:p["seventhNormalThree"]}}
        inc={7:{2:p["incomingSeventhNormalTwo"],3:p["incomingSeventhNormalThree"]}}
        return p["twoMaps"],high,p["incomingMaps"],inc
    return p["representativeMaps"],integer_keys(p["representativeHigh"]),p["incomingMaps"],integer_keys(p["incomingHigh"])

def forcing(a,q,s,m,j,projection,previous,rec):
    n=a.order;pr=previous["parameters"]
    prepared=previous_phase(a,q,previous,"prepared-complete-low")
    phase="complete-eighth-cochains-verified" if n==9 else "complete-next-cochains-verified"
    verified=previous_phase(a,q,previous,phase)
    pack=verified["pack"];N=verified["normalizer"];md=verified["metadata"]
    need(md["fullOriginalVerificationComplete"] is True and
         md["originalProductCoordinates"]==n*6188*pack.ncols() and
         q.mh(pack)==pr["actualCanonicalCochain"]["packSHA256"],
         "All original previous products and source pack")
    need(N.nrows()==N.ncols()==pack.ncols() and q.mh(N)==md["normalizerSHA256"],
         "Actual old source normalizer")
    Ni=N.inv();need(N*Ni==q.DQ.eye(N.nrows()) and Ni*N==q.DQ.eye(N.nrows()),"Actual old inverse")
    pre=pack*Ni;need(pre*N==pack,"Every coefficient transported by the true inverse")
    prevlow,prevhigh=unpack(q,pre,n-1)
    oldstable=prepared["stableMaps"][0].ncols();extra=md["newHeadCount"]
    need(extra in (0,1) and oldstable+extra==pack.ncols(),"Actual projected-plus-new head decomposition")
    for k in range(n):
        need(q.DQ.sub(prevlow[k],range(155),range(oldstable))==prepared["stableMaps"][k],
             "Every old projected coefficient matches")
    for X in prevhigh.values():
        for M in X.values():need(q.zero(q.DQ.sub(M,range(M.nrows()),range(oldstable))),
                                "Old projected chains have no hidden high coefficient")
    need(pr["preparation"]["highExcludedHeadDimension"]==0 and
         pr["preparation"]["allSurvivingOriginalHighForcingsExactlyZero"] is True,
         "This continuation needs the previous full zero-high reduction")
    origin=s.read_q_phase(a,q,projection,"original-projection-coefficients",s.COEFF)
    coeff=q.coefficient_decode(origin["coefficients"]);P=q.dec(origin["P"][:n+1],q.DQ)
    need(coeff["chart"]=="infinity" and coeff["maxOrder"]==11 and len(P)==n+1,
         "Paid full original coefficient precision")
    need([q.mh(x) for x in P]==projection["parameters"]["originalProjection"]["originalProjectionCoefficientSHA256"][:n+1],
         "Same natural original projection coefficient arrays")
    Top=[q.DQ.sub(x,range(170),range(155)) for x in P]
    state=q.dec(s.read_q_phase(a,q,projection,"Q-smith-state",s.Q_STATE),q.DQ)
    group=next((g for g in state["positive"] if g["exponent"]==n),None)
    np=0 if group is None else group["map"][0].ncols()
    need(np in (0,1),"Actual projected next exponent multiplicity")
    c=np+extra;L=[]
    for k in range(n+1):
        p=q.DQ.mat(155,0) if group is None else group["map"][k]
        x=q.DQ.sub(prevlow[k],range(155),range(oldstable,pack.ncols())) if k<n else q.DQ.mat(155,extra)
        L.append(q.DQ.cat([p,x]))
    LH={}
    for t,X in prevhigh.items():
        LH[t]={r:q.DQ.cat([q.DQ.mat(M.nrows(),np),q.DQ.sub(M,range(M.nrows()),range(oldstable,pack.ncols()))])
               for r,M in X.items()}
    later=[g for g in state["positive"] if g["exponent"]>n]
    stable=[q.DQ.cat([g["map"][k] for g in later]+[state["map"][k]]) for k in range(n+1)]
    stable_count=stable[0].ncols()
    need(stable_count+c==pack.ncols() and q.DQ.cat([stable[0],L[0]]).rref()[1]==pack.ncols(),
         "All full previous heads split into true projected and quotient heads")
    oldL,oldH,oldU,oldUH=adapt_prepared(a,prepared)
    dold=pr["preparation"]["completePriorIncomingColumns"];base=587+dold
    free=pr["completeLowKernel"]["freeColumns"]
    fail=[i for i in range(oldL[0].ncols()) if base+i not in free]
    ranks=pr["fullFirstEightRanks"] if n==9 else pr["fullConnectionRanks"]
    need(len(ranks)==n-1 and len(fail)==ranks[-1] and dold==sum(ranks[:-1]),
         "Actual complete prior failure basis and image dimensions")
    d=dold+len(fail);U=[]
    for k in range(n+1):
        U.append(q.DQ.mat(155,d) if k==0 else q.DQ.cat(
            [oldU[k-1],q.DQ.sub(oldL[k-1],range(155),fail)]))
    UH={}
    for t in sorted(set(oldH)|set(oldUH)):
        UH[t+1]={}
        for r,size in ((2,450),(3,990)):
            x=oldUH.get(t,{}).get(r,q.DQ.mat(size,dold))
            y=oldH.get(t,{}).get(r,q.DQ.mat(size,oldL[0].ncols()))
            UH[t+1][r]=q.DQ.cat([x,q.DQ.sub(y,range(size),fail)])
    count=0
    for k in range(n):
        check(a);V,H=source_product(a,q,s,m,j,coeff,Top,L,LH,k)
        need(q.zero(V) and q.zero(H),"Every original lower product of the next quotient representatives")
        count+=6188*c
    W,WH=source_product(a,q,s,m,j,coeff,Top,U,UH,n)
    expected=q.DQ.cat([q.DQ.sub(prepared["M"],range(1088),range(587,base)),
                      q.DQ.sub(prepared["M"],range(1088),[base+i for i in fail])])
    need(W==expected and q.zero(WH),"All whole incoming maps give the exact previous image")
    low,H=source_product(a,q,s,m,j,coeff,Top,L,LH,n)
    need(H.nrows()==5100 and H.ncols()==c and
         q.zero(q.DQ.sub(H,range(5100),range(np))),"Projected representatives have no high forcing")
    nonzero_extra=extra==1 and not q.zero(q.DQ.sub(H,range(5100),[np]))
    counts=lambda HH:{str(t):[sum(bool(X[r][i,k]) for i in range(X[r].nrows()) for k in range(X[r].ncols()))
                             for r in (2,3)] for t,X in HH.items()}
    meta={"order":n,"previousCompleteHeadCount":pack.ncols(),"projectedNextHeadCount":stable_count,
        "projectedExitRepresentativeColumns":np,"newExtraRepresentativeColumns":extra,
        "newQuotientRepresentatives":c,"completePriorIncomingColumns":d,
        "actualPreviousFailureColumnIndices":fail,"allOriginalRepresentativeLowerProductsZero":True,
        "originalLowerProductCoordinates":count,"allOriginalSourceRows":6188,
        "allWholeIncomingDirectionsTransported":True,"allIncomingHighCoefficientsRetained":True,
        "incomingHighForcingExactlyZero":True,"priorIncomingSHA256":q.mh(W),
        "originalNextLowSHA256":q.mh(low),"originalNextHighSHA256":q.mh(H),
        "highShape":[5100,c],"highQRank":int(nonzero_extra),
        "extraHeadHighForcingZero":not nonzero_extra,
        "representativeHighCoefficientNonzeroCounts":counts(LH),
        "incomingHighCoefficientNonzeroCounts":counts(UH),
        "previousCompleteConnectionRanks":ranks,"noNextConnectionRankClaimed":True,
        "noOldSmithOrLowRrefOrHighGaussianRepeated":True}
    rec["parameters"]["originalForcing"]=meta
    data={"order":n,"representativeMaps":L,"representativeHigh":LH,
        "incomingMaps":U,"incomingHigh":UH,"stableMaps":stable,"incoming":W,
        "low":low,"high":H,"constantLow":q.DQ.sub(prepared["M"],range(1088),range(587)),
        "Z3":prepared["Z3"],"coefficientData":q.coefficient_encode(coeff),"top":Top,"metadata":meta}
    return data,coeff,np,extra

def main():
    p=argparse.ArgumentParser()
    for k in ("generator","jet-actions","projection-consumer","sixth-consumer","high-probe-helper",
              "projection-receipt","high-receipt","previous-receipt","previous-receipt-sha256",
              "previous-source-sha256","projection-out","high-out","previous-out","checkpoint-dir","out"):
        p.add_argument("--"+k,required=True)
    p.add_argument("--order",type=int,required=True);p.add_argument("--remaining-seconds",type=float,default=90)
    p.add_argument("--memory-mib",type=int,default=2048);a=p.parse_args()
    need(9<=a.order<=11 and 0<a.remaining_seconds<=180 and 512<=a.memory_mib<=4096,"Bounded exact next stage")
    if hasattr(sys,"set_int_max_str_digits"):sys.set_int_max_str_digits(0)
    resource.setrlimit(resource.RLIMIT_AS,(a.memory_mib*1024**2,)*2)
    start=time.monotonic();a._deadline=start+a.remaining_seconds-min(5,a.remaining_seconds/10)
    rec={"format":FORMAT,"status":"running","events":[],"parameters":{"author":"Astra-ISP-789f / normal_annihilator",
        "aiAssisted":"GPT-6 Astra Pro","selfSHA256":sha(__file__),"order":a.order,"sharedSeconds":a.remaining_seconds,
        "memoryMiB":a.memory_mib,"temporaryOnly":True,"largeDataUploadedOrCommitted":False,
        "allAncestorFilesReadOnly":True,"newPhaseGzipMtime":0,"nextConnectionRankNotClaimed":True}}
    try:
        pins=dict(PINS);pins["previous_receipt"]=a.previous_receipt_sha256
        for k,d in pins.items():need(sha(getattr(a,k))==d,"Pinned actual input "+k)
        previous=result(a.previous_receipt);projection=result(a.projection_receipt);high=result(a.high_receipt)
        need(previous["status"]=="completed" and previous["scriptSHA256"]==a.previous_source_sha256 and
             previous["parameters"]["fullOriginalVerificationComplete"] is True,"Actual complete original prior stage")
        need(high["status"]=="completed" and high["parameters"]["conclusion"]["completeHighQRankExact"]==3760,
             "Complete original Q high constant rank")
        binding=objhash({"format":FORMAT,"sourceSHA256":sha(__file__),"inputSHA256":pins,
            "previousSourceSHA256":a.previous_source_sha256,"previousBinding":previous["parameters"]["binding"],
            "order":a.order,"highBinding":high["parameters"]["binding"]})
        rec["parameters"]["binding"]=binding;rec["parameters"]["inputSHA256"]=pins
        need(Path(a.checkpoint_dir).resolve() not in
             [Path(x).resolve() for x in (a.previous_out,a.projection_out,a.high_out)],"Separate new checkpoint")
        q=module("r150_next_projection",a.projection_consumer);s=module("r150_next_sixth",a.sixth_consumer)
        m=module("r150_next_original",a.generator);j=module("r150_next_actions",a.jet_actions)
        h=module("r150_next_high_dag",a.high_probe_helper)
        data,coeff,np,extra=forcing(a,q,s,m,j,projection,previous,rec)
        save(a,q,binding,"complete-next-original-forcings",data,rec)
        if q.zero(data["high"]):
            info={"performed":False,"allHighForcingsZeroOverQ":True,"QHighCorrectionCanBeHomogeneous":True}
        else:
            need(extra==1,"Only one genuinely new nonprojected high forcing")
            padded=q.DQ.cat([q.DQ.mat(5100,1),q.DQ.sub(data["high"],range(5100),[np])])
            info,arrays=h.field_necessary(a,q,m,j,high,coeff,padded,rec)
            info["actualOriginalRepresentativeColumn"]=np
            save(a,q,binding,"complete-paid-high-DAG-new-RHS",arrays,rec)
        rec["parameters"]["highNecessity"]=info
        rec["status"]="completed";rec["outcome"]="actual-original-next-high-forcing-inspected"
    except TimeoutError as e:
        rec["status"]="prefix-completed";rec["error"]=str(e)
    except BaseException as e:
        rec["status"]="failed";rec["error"]=type(e).__name__+": "+str(e);raise
    finally:
        rec["elapsedSeconds"]=time.monotonic()-start
        need(len(canonical(rec))<95000,"Small original next forcing receipt");atomic(a.out,rec)
        print(json.dumps({"status":rec["status"],"order":a.order,"receipt":a.out,
              "elapsedSeconds":rec["elapsedSeconds"]}),flush=True)
    if rec["status"]=="prefix-completed":raise SystemExit(75)
if __name__=="__main__":main()
