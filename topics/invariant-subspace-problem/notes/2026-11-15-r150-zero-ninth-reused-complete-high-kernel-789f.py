#!/usr/bin/env python3
"""R150 zero ninth left jets, reusing the paid complete high homogeneous space.

No top/middle RREF or full inverse is recomputed.  The paid middle lift has
9 columns and head rank7, so its complete zero-head fiber is2 dimensional.
After checking the actual eighth cochains entrywise, all5100 new high RHS
rows are verified zero.  The new full equation is the old582-rank low base
plus2 complete high homogeneous columns and the actual4 ninth RHS columns.
All6188 original rows, Q ambiguity and source multipliers are retained.
Temporary arrays stay in this job.  The permanent output is a small receipt.
"""
import argparse
import hashlib
import json
import os
from pathlib import Path
import resource
import signal
import time

FIRST_SHA="2757b900480fe3bf1450100188df1679801351f0330d609e1a39b9c7ca146186"
ACTIONS_SHA="4e63c72c550e8f90c022b086d3758f8e7b12edf4fb16a0ef387bc1a92f97366a"
PARENT_SHA="a6c423b98d70e06fb5a28797f09a11300129ec59128921c1e2d5c0e54fa8b5f2"
HELPER_SHA="36356983e71ee1e67677da1a7a5f7aebf2987db282a5447a741b6a6af93084d5"
PAID_RECEIPT_SHA="0f30617b728af521fe9d928e37a0ee04a2274abd9d148e033a23c29c20ff10f1"
PAID_BINDING="2ab96ac89edbf80802073e1278419af544682d9d7f6186ce27aa0fcc6559c7da"
PAID_MANIFEST_SHA="89fbd83c0d75ed64b6be2dfc77f2128cc903971585b16796ee3456613907da44"
PAID_PACK_SHA="b40ff9e7ea5d6897a10df27ecfb159521140fea786753e33d562796608ab9df5"
OLD_FORMAT="r150-zero-sixth-full-source-temporary-v1"
FORMAT="r150-zero-ninth-complete-high-homogeneous-temporary-v1"
EIGHTH_RECEIPT_SHA="05d534b390673fc26d1bccb1ef84ff04a9de1896970c9dc10d6e86fe0053fa4a"
EIGHTH_MANIFEST_SHA="dfbad6c66fb77779194907e975fbe93286da67220cc3c869b3ae2542b6f9e4b2"
EIGHTH_BINDING="534c92386282dde35d7745a9893d0415f5fadf11f12fc2a1ebd94babd9671734"
EIGHTH_SCRIPT_SHA="37417c1be7a2e3b6a97b5b467187725eb6acfcc528994eb66150a421717eefde"
EIGHTH_PACK_SHA="e3f77a4210b49683b80761c9d56a4c813726f4d905e2ce0380742ebd62f82076"

def req(ok,msg):
    if not ok: raise AssertionError(msg)

def sha(path):
    h=hashlib.sha256()
    with Path(path).open("rb") as f:
        for block in iter(lambda:f.read(1048576),b""): h.update(block)
    return h.hexdigest()

def small_hash(x):
    return hashlib.sha256(json.dumps(x,sort_keys=True,separators=(",",":")).encode()).hexdigest()

def mod_at(name,path):
    import importlib.util
    spec=importlib.util.spec_from_file_location(name,path)
    obj=importlib.util.module_from_spec(spec);spec.loader.exec_module(obj)
    return obj

def load_paid(d,m,a,manifest,paid,phase,result):
    entry=manifest["phases"][phase]
    expected=paid["checkpointPhases"][phase]
    req({k:v for k,v in entry.items() if k!="file"}==expected,
        "Paid actual phase receipt "+phase)
    path=Path(a.sixth_checkpoint_dir)/entry["file"]
    req(path.parent==Path(a.sixth_checkpoint_dir)
        and path.stat().st_size==entry["bytes"] and sha(path)==entry["sha256"],
        "Paid original phase bytes "+phase)
    obj=d.read_json(path)
    req(obj["format"]==OLD_FORMAT and obj["binding"]==PAID_BINDING
        and obj["phase"]==phase and obj["verified"] is True
        and entry["verified"] is True,"Paid original verified phase "+phase)
    nr,nc=obj["shape"]
    req(obj["shape"]==entry["shape"] and len(obj["matrix"])==nr
        and all(len(row)==nc for row in obj["matrix"]),"Paid original phase dimensions")
    M=m.fmpq_mat(nr,nc,[m.fmpq(x) for row in obj["matrix"] for x in row])
    req(m.matrix_hash(M)==obj["matrixSHA256"]==entry["matrixSHA256"],
        "Paid original full rational matrix "+phase)
    result["parameters"].setdefault("readOnlyPaidPhases",{})[phase]=expected
    return M,obj["metadata"]

def adopt(d,m,a,binding,prefix,M,meta,result):
    old=d.load_matrix(m,a,binding,prefix,result)
    if old is None:
        d.save_matrix(m,a,binding,prefix,M,meta,result,True)
    else:
        X,xmeta,verified=old
        req(verified and m.matrix_hash(X)==m.matrix_hash(M)
            and xmeta==meta,"New checkpoint changed actual adopted constant")


def load_eighth(d,m,a,result):
    req(sha(a.eighth_receipt)==EIGHTH_RECEIPT_SHA,"Completed eighth outer bytes")
    outer=d.read_json(a.eighth_receipt);paid=outer["result"]["parameters"]
    req(outer["runId"]=="43702348535" and outer["exitCode"]==0
        and outer["result"]["status"]=="completed"
        and outer["scriptSHA256"]==EIGHTH_SCRIPT_SHA
        and paid["independentEighthLeadingCount"]==4
        and paid["all6188OriginalEighthRowsVerified"]
        and paid["completeZeroHeadFiberDimension"]==10,
        "Actual complete eighth provenance")
    path=Path(a.eighth_checkpoint_dir)/"sixth-checkpoint.json"
    req(sha(path)==EIGHTH_MANIFEST_SHA,"Completed eighth manifest bytes")
    manifest=d.read_json(path)
    req(manifest["format"]=="r150-zero-eighth-complete-high-homogeneous-temporary-v1"
        and manifest["binding"]==EIGHTH_BINDING,"Completed eighth checkpoint source")
    phase="complete-eighth-cochains";entry=manifest["phases"][phase]
    req({k:v for k,v in entry.items() if k!="file"}==paid["checkpointPhases"][phase],
        "Completed actual eighth cochain entry")
    file=Path(a.eighth_checkpoint_dir)/entry["file"]
    req(file.parent==Path(a.eighth_checkpoint_dir)
        and file.stat().st_size==entry["bytes"] and sha(file)==entry["sha256"],
        "All actual eighth cochain bytes")
    obj=d.read_json(file)
    req(obj["format"]==manifest["format"] and obj["binding"]==EIGHTH_BINDING
        and obj["phase"]==phase and obj["verified"] is True
        and obj["shape"]==[17651,4],"Completed eighth cochain header")
    nheads=paid["independentEighthLeadingCount"]
    req(len(obj["matrix"])==17651 and all(len(row)==nheads for row in obj["matrix"]),
        "All actual eighth cochain coordinates")
    M=m.fmpq_mat(17651,nheads,[m.fmpq(x) for row in obj["matrix"] for x in row])
    req(m.matrix_hash(M)==obj["matrixSHA256"]==entry["matrixSHA256"]==EIGHTH_PACK_SHA,
        "Complete actual eighth logical matrix")
    md=obj["metadata"]
    req(md["order"]==8 and md["chart"]=="zero" and md["leadingColumns"]==nheads
        and md["all6188OriginalEighthRowsVerified"]
        and md["allPaidLowerCochainsTransportedTogether"],
        "Actual original eighth cochain source")
    result["parameters"].update({
        "paidEighthReceiptSHA256":EIGHTH_RECEIPT_SHA,
        "paidEighthBinding":EIGHTH_BINDING,
        "paidEighthCompleteCochainSHA256":EIGHTH_PACK_SHA,
        "paidEighthCochainFileSHA256":entry["sha256"],
        "paidEighthDirectoryReadOnly":True,"actualPreviousLeadingCount":nheads})
    return M,md,paid

def unpack(m,pack,ranges):
    nheads=pack.ncols()
    co=[{} for _ in range(9)]
    for name,item in ranges.items():
        left,right=name.split("Normal")
        k=int(left[len("lambda"):]);r=int(right)
        X=m.submatrix(pack,range(item["start"],item["stop"]),range(nheads))
        req(m.matrix_hash(X)==item["matrixSHA256"],"Paid eighth cochain block "+name)
        co[k][r]=X
    req(set(co[0])=={0,1},"Actual eighth constant support")
    for k in range(1,9):
        req(1 in co[k],"Each actual paid eighth cochain one-normal block")
        for r,X in co[k].items():
            if r>=2:
                req(m.matrix_zero(X),"Actual eighth high block not entrywise zero")
    return co

def build_high_homogeneous(d,m,j,a,coeff,mid,binding,result):
    key="complete-paid-high-homogeneous"
    cached=d.load_matrix(m,a,binding,key,result)
    if cached is None:
        Z=m.submatrix(mid,range(3762,3769),range(9))
        Qz,rank,piv,free=m.nullspace(Z)
        req(rank==7 and Qz.nrows()==9 and Qz.ncols()==2,
            "Complete paid middle head rank7 and kernel2")
        full=mid*Qz
        req(m.matrix_zero(m.submatrix(full,range(3762,3769),range(2))),
            "Actual complete high homogeneous columns have zero old head")
        N=m.submatrix(full,range(3762),range(2))
        nsect={3:m.submatrix(N,range(990),range(2)),
               4:m.submatrix(N,range(990,2475),range(2)),
               5:m.submatrix(N,range(2475,3762),range(2))}
        for r in (2,3):
            req(m.matrix_zero(j.apply(m,coeff,0,r,nsect,2)),
                "All original high rows of the complete homogeneous space")
        _,rn=N.rref();req(rn==2,"Independent complete high homogeneous columns")
        both=j.join_vertical(m,[N,Qz])
        meta={"paidMiddleSHA256":m.matrix_hash(mid),"oldHeadRank":7,
              "all5100OriginalHighRowsVerified":True,"dimension":2,
              "completeByPaidKernelZeroHeadFiber":True,
              "oldHeadKernelSHA256":m.matrix_hash(Qz),
              "completeHighHomogeneousSHA256":m.matrix_hash(N)}
        d.save_matrix(m,a,binding,key,both,meta,result,True)
    else:
        both,meta,verified=cached
        req(verified and meta["paidMiddleSHA256"]==m.matrix_hash(mid)
            and meta["all5100OriginalHighRowsVerified"]
            and meta["completeByPaidKernelZeroHeadFiber"]
            and [both.nrows(),both.ncols()]==[3771,2],
            "Complete paid high homogeneous source")
        N=m.submatrix(both,range(3762),range(2))
        Qz=m.submatrix(both,range(3762,3771),range(2))
    result["parameters"].update(meta)
    return N,Qz

def residual(d,m,j,a,coeff,co,binding,result):
    phase="ninth-residuals"
    nheads=co[0][1].ncols()
    old=d.load_matrix(m,a,binding,phase,result)
    if old is None:
        pieces=[]
        for r in range(4):
            d.guard(a,"new original ninth source sector "+str(r),1.0)
            R=m.fmpq_mat(len(j.source_rows(r)),nheads)
            for k in range(9):
                R+=j.apply_sparse(m,coeff,9-k,r,co[k],nheads)
            pieces.append(R)
        req(m.matrix_zero(pieces[2]) and m.matrix_zero(pieces[3]),
            "All5100 original high ninth residual rows")
        R=j.join_vertical(m,pieces)
        meta={"originalPhysicalSHA256":small_hash(coeff["physical"]),
              "all6188SourceRowsRetained":True,"all5100HighResidualRowsZero":True,
              "actualEighthHighBlocksEntrywiseZero":True}
        d.save_matrix(m,a,binding,phase,R,meta,result,True)
    else:
        R,meta,verified=old
        req(verified and meta["originalPhysicalSHA256"]==small_hash(coeff["physical"])
            and meta["all5100HighResidualRowsZero"]
            and [R.nrows(),R.ncols()]==[6188,nheads],"Actual ninth residual cache")
    result["parameters"].update(meta)
    result["parameters"]["ninthResidualSHA256"]=m.matrix_hash(R)
    return R

def write_family(d,m,j,a,coeff,co,Q,N,R,K,binding,result):
    nheads=co[0][1].ncols()
    req(K.nrows()==594+nheads,"All actual head columns retained")
    headall=m.submatrix(K,range(594,594+nheads),range(K.ncols()))
    rr,r=headall.rref();choice=m.pivot_columns(rr,r)
    chosen=m.submatrix(K,range(K.nrows()),choice)
    head=m.submatrix(headall,range(nheads),choice)
    req(K.ncols()-r==10,"Complete zero-head fiber agrees with exact paid first rank4")
    lo=m.submatrix(chosen,range(585),range(r))
    b=m.submatrix(chosen,range(585,592),range(r))
    high=N*m.submatrix(chosen,range(592,594),range(r))
    extra=Q*b
    lam9={1:m.submatrix(lo,range(135),range(r)),
          2:m.submatrix(lo,range(135,585),range(r)),
          3:m.submatrix(high,range(990),range(r)),
          4:m.submatrix(high,range(990,2475),range(r)),
          5:m.submatrix(high,range(2475,3762),range(r))}
    start=0
    for sr in range(4):
        count=len(j.source_rows(sr))
        V=j.apply(m,coeff,0,sr,lam9,r)
        V+=j.apply(m,coeff,1,sr,{1:extra},r)
        V+=m.submatrix(R,range(start,start+count),range(nheads))*head
        req(m.matrix_zero(V),"All original ninth rows in sector "+str(sr))
        start+=count
    req(start==6188,"All original ninth source coordinates")
    actual=[{sr:X*head for sr,X in section.items()} for section in co]
    actual[8][1]+=extra;actual.append(lam9)
    ranges={};blocks=[];offset=0;readout={}
    square={v:i for i,v in enumerate(j.target_columns(2))}
    for k,section in enumerate(actual):
        for sr,X in sorted(section.items()):
            name="lambda"+str(k)+"Normal"+str(sr)
            ranges[name]={"start":offset,"stop":offset+X.nrows(),
                          "matrixSHA256":m.matrix_hash(X)}
            blocks.append(X);offset+=X.nrows()
        X=section.get(2)
        sq=(m.fmpq_mat(9,r) if X is None else
            m.fmpq_mat(9,r,[X[square[(0,0,(i,i))],c]
                             for i in range(2,11) for c in range(r)]))
        if k<=8: req(m.matrix_zero(sq),"Paid complete target pairing changed")
        values=[[str(sq[i,c]) for c in range(r)] for i in range(9)]
        entry={"matrixSHA256":m.matrix_hash(sq),"allEntriesZero":m.matrix_zero(sq)}
        if len(json.dumps(values))<=6000: entry["nineByLeading"]=values
        else: entry["valuesOnlyInVerifiedTemporaryCochain"]=True
        readout["lambda"+str(k)]=entry
    pack=j.join_vertical(m,blocks)
    meta={"chart":"zero","parameter":"s","order":9,"leadingColumns":r,
          "ranges":ranges,"all6188OriginalNinthRowsVerified":True,
          "allPaidLowerCochainsTransportedTogether":True,
          "leadingInPaidHeads":[[str(head[i,c]) for c in range(r)] for i in range(nheads)],
          "targetSquareReadouts":readout,"temporaryOnly":True,
          "originalPhysicalHashesThroughOrder9":coeff["physical"]}
    d.save_matrix(m,a,binding,"complete-ninth-cochains",pack,meta,result,True)
    c9=min(14,17-r);dm=58+max(r-3,0);ds=49+max(r-4,0)
    result.update({"status":"completed","independentNinthLeadingCount":r,
                   "sumFirstNineConnectionRanksUpperBound":c9,
                   "fullZeroMaximalMinorOrderLowerBound":dm,
                   "fullZeroSubmaximalMinorOrderLowerBound":ds})
    result["parameters"].update({
        "independentNinthLeadingCount":r,"fullLowKernelDimension":K.ncols(),
        "completeZeroHeadFiberDimension":K.ncols()-r,
        "paidExactFirstConnectionRank":4,"paidExactSecondConnectionRank":0,
        "actualNinthLeadingSHA256":m.matrix_hash(head),
        "actualNinthCompleteCochainShape":[pack.nrows(),pack.ncols()],
        "actualNinthCompleteCochainSHA256":m.matrix_hash(pack),
        "actualNinthCochainRanges":ranges,
        "all6188OriginalNinthRowsVerified":True,
        "allHomogeneousHighAndLowKernelsRetained":True,
        "firstEightCumulativeRankUpperBounds":[4,4,5,8,10,12,12,13],
        "sumFirstNineConnectionRanksUpperBound":c9,
        "fullZeroMaximalMinorOrderLowerBound":dm,
        "fullZeroSubmaximalMinorOrderLowerBound":ds,
        "targetSquareReadoutsAfterActualNinthLift":readout,
        "notAFullNinthConnectionLowerBound":True,
        "fullTargetMembershipNotClaimed":True})
    if len(json.dumps(meta["leadingInPaidHeads"]))<=6000:
        result["parameters"]["actualNinthLeadingInPaidHeads"]=meta["leadingInPaidHeads"]

def run(d,m,j,u,a,result):
    req(sha(a.sixth_receipt)==PAID_RECEIPT_SHA,"Paid completed sixth outer bytes")
    outer=d.read_json(a.sixth_receipt);paid=outer["result"]["parameters"]
    req(outer["runId"]=="43702348535" and outer["exitCode"]==0
        and outer["result"]["status"]=="completed"
        and paid["independentSixthLeadingCount"]==5
        and paid["all6188OriginalSixthRowsVerified"]
        and paid["middleKernelDimension"]==9
        and paid["allTopAndMiddleHomogeneousKernelsRetained"],
        "Actual complete sixth provenance")
    manifest_path=Path(a.sixth_checkpoint_dir)/"sixth-checkpoint.json"
    req(sha(manifest_path)==PAID_MANIFEST_SHA,"Paid completed manifest bytes")
    manifest=d.read_json(manifest_path)
    req(manifest["format"]==OLD_FORMAT and manifest["binding"]==PAID_BINDING,
        "Paid complete sixth manifest binding")
    inputs={"script":sha(__file__),"first":FIRST_SHA,"actions":ACTIONS_SHA,
            "parent":PARENT_SHA,"helper":HELPER_SHA,
            "sixthReceipt":PAID_RECEIPT_SHA,"sixthManifest":PAID_MANIFEST_SHA,
            "sixthBinding":PAID_BINDING,"eighthReceipt":EIGHTH_RECEIPT_SHA,
            "eighthManifest":EIGHTH_MANIFEST_SHA,"eighthBinding":EIGHTH_BINDING}
    binding=small_hash(inputs)
    result["parameters"]["checkpointBinding"]=binding
    result["parameters"]["checkpointSemanticInputs"]=inputs
    pack,packmeta,eighth=load_eighth(d,m,a,result)
    co=unpack(m,pack,packmeta["ranges"]);nheads=pack.ncols();del pack
    result["parameters"]["allPaidEighthNormalTwoThroughFiveEntriesZero"]=True
    d.guard(a,"original coefficients through ninth order",2.0)
    coeff=j.original_coefficients(m,"zero",9)
    for key,val in eighth["originalPhysicalHashesThroughOrder8"].items():
        req(coeff["physical"].get(key)==val,"Original physical coefficients through8 "+key)
    result["parameters"]["originalPhysicalHashesThroughOrder9"]=coeff["physical"]
    R=residual(d,m,j,a,coeff,co,binding,result)
    if a.through=="residual":
        result["status"]="stage-completed";return
    mid,midmeta=load_paid(d,m,a,manifest,paid,"middle-complete-lift",result)
    req([mid.nrows(),mid.ncols()]==[3769,9]
        and midmeta["all2295OriginalMiddleKernelRowsVerified"]
        and midmeta["allTopAndMiddleHomogeneousKernelsRetained"],
        "Complete paid composed middle family")
    N,Qz=build_high_homogeneous(d,m,j,a,coeff,mid,binding,result);del mid
    oldC,oldCmeta=load_paid(d,m,a,manifest,paid,"low-actual-rhs",result)
    oldX,oldXmeta=load_paid(d,m,a,manifest,paid,"low-unit-unit-rhs-solution",result)
    req([oldC.nrows(),oldC.ncols()]==[1088,9]
        and [oldX.nrows(),oldX.ncols()]==[582,9]
        and oldXmeta["rhsSHA256"]==m.matrix_hash(oldC)
        and oldXmeta["allOriginalUnitRHSRowsVerified"],"Paid actual low RHS/X pair")
    Ch=oldC*Qz;Xh=oldX*Qz;del oldC,oldX
    ns={3:m.submatrix(N,range(990),range(2)),
        4:m.submatrix(N,range(990,2475),range(2)),
        5:m.submatrix(N,range(2475,3762),range(2))}
    trueCh=j.join_vertical(m,[j.apply(m,coeff,0,sr,ns,2) for sr in (0,1)])
    req(Ch==trueCh,"Actual whole-source transport of all high homogeneous columns")
    P0=j.block(m,coeff,0,0,1)
    Q,rq,_,_=m.nullspace(P0)
    req(rq==128 and [Q.nrows(),Q.ncols()]==[135,7],"Complete constant one-normal Q")
    for sr in range(4):
        req(m.matrix_zero(j.apply(m,coeff,0,sr,{1:Q},7)),
            "All original constant Q rows")
    A0=j.join_vertical(m,[
        m.join_columns(j.block(m,coeff,0,sr,1),j.block(m,coeff,0,sr,2))
        for sr in (0,1)])
    B1=j.join_vertical(m,[j.apply(m,coeff,1,sr,{1:Q},7) for sr in (0,1)])
    B=m.join_columns(A0,B1)
    C=m.join_columns(Ch,m.submatrix(R,range(1088),range(nheads)))
    req([B.nrows(),B.ncols()]==[1088,592] and [C.nrows(),C.ncols()]==[1088,2+nheads],
        "Exact complete ninth reduced dimensions")
    prefix="ninth-unit";bsha=m.matrix_hash(B);csha=m.matrix_hash(C)
    for suffix in ("constant-kernel","unit","primitive-unit"):
        M,meta=load_paid(d,m,a,manifest,paid,"low-unit-"+suffix,result)
        if suffix!="primitive-unit":
            req(meta["constantSHA256"]==bsha,"Same actual low constant matrix")
        adopt(d,m,a,binding,prefix+"-"+suffix,M,meta,result)
        if suffix=="unit":
            I=meta["rows"];U=M;usha=m.matrix_hash(U)
    req(Xh.nrows()==582 and Xh.ncols()==2,"Actual inherited two RHS solutions")
    for c in range(2):
        phase=prefix+"-rhs-column-%04d"%c
        old=d.load_matrix(m,a,binding,phase,result)
        col=m.submatrix(Xh,range(582),[c])
        req(m.matrix_zero(U*col+m.submatrix(Ch,I,[c])),
            "Inherited RHS solution on all582 original unit rows")
        meta={"column":c,"constantSHA256":bsha,"rhsSHA256":csha,
              "unitSHA256":usha,"allOriginalUnitRowsVerified":True,
              "originalUnitProductCoordinates":582,
              "algorithm":"paid-source-linear-combination","nativeSeconds":0.0,
              "nativeSolveUsed":False,"oldHeadKernelSHA256":m.matrix_hash(Qz)}
        if old is None: d.save_matrix(m,a,binding,phase,col,meta,result,True)
        else:
            Y,ymeta,verified=old
            req(verified and Y==col and ymeta==meta,"Verified inherited RHS cache")
    del U,Xh
    result["parameters"].update({
        "completeHighHomogeneousDimension":2,
        "allThreeOriginalTopHomogeneousDirectionsRetainedThroughPaidMiddle":True,
        "all5100OriginalHighRowsRetained":True,
        "noTopOrMiddleRrefRecomputed":True,
        "noOldActualRHSSolveRepeated":True,"maximumNewUnitRHSColumns":nheads,
        "constantLowSHA256":bsha,"allReducedRHSColumnsSHA256":csha})
    K,km=u.complete_kernel(d,m,j,a,binding,prefix,B,C,582,result)
    result["parameters"].update({"lowMatrixShape":km["shape"],"lowAugmentedRank":km["rank"],
        "lowKernelSHA256":m.matrix_hash(K),"lowSchurRank":km["schurRank"]})
    write_family(d,m,j,a,coeff,co,Q,N,R,K,binding,result)

def main():
    p=argparse.ArgumentParser()
    for name in ("parent-driver","unit-schur-helper","generator","jet-actions",
                 "sixth-receipt","sixth-checkpoint-dir","eighth-receipt","eighth-checkpoint-dir",
                 "checkpoint-dir","out"):
        p.add_argument("--"+name,required=True)
    p.add_argument("--through",choices=("residual","final"),default="final")
    p.add_argument("--remaining-seconds",type=float,default=180.0)
    p.add_argument("--memory-mib",type=int,default=2048)
    p.add_argument("--unit-algorithm",choices=("dixon","fflu"),default="dixon")
    p.add_argument("--unit-batch-columns",type=int,choices=(1,2),default=1)
    p.add_argument("--max-new-unit-groups",type=int,default=32)
    a=p.parse_args()
    req(a.remaining_seconds>0 and 512<=a.memory_mib<=8192
        and a.max_new_unit_groups>0,"Positive actual shared bounded resources")
    for path,want in ((a.parent_driver,PARENT_SHA),(a.unit_schur_helper,HELPER_SHA),
                      (a.generator,FIRST_SHA),(a.jet_actions,ACTIONS_SHA)):
        req(sha(path)==want,"Exact paid source dependency "+str(path))
    req(Path(a.checkpoint_dir).resolve()!=Path(a.sixth_checkpoint_dir).resolve(),
        "New checkpoint distinct from read-only paid sixth")
    req(Path(a.checkpoint_dir).resolve()!=Path(a.eighth_checkpoint_dir).resolve(),
        "New ninth checkpoint distinct from read-only paid eighth")
    resource.setrlimit(resource.RLIMIT_AS,(a.memory_mib*1024**2,a.memory_mib*1024**2))
    d=mod_at("r150_ninth_parent_storage",a.parent_driver)
    m=mod_at("r150_ninth_original_generator",a.generator)
    j=mod_at("r150_ninth_original_actions",a.jet_actions)
    u=mod_at("r150_ninth_unit_schur",a.unit_schur_helper)
    d.FORMAT=FORMAT
    started=time.monotonic();a._deadline=started+a.remaining_seconds
    result={"format":"r150-zero-ninth-reused-complete-high-kernel-v1",
            "status":"started","arithmetic":"exact rational python-flint",
            "scriptSHA256":sha(__file__),"parameters":{
                "naturalParameter":"s","sharedSeconds":a.remaining_seconds,
                "memoryMiB":a.memory_mib,"through":a.through,
                "checkpointDirectory":str(Path(a.checkpoint_dir)),
                "paidDirectoryReadOnly":True,"temporaryOnly":True,
                "sourceStrata":[170,918,2295,2805],
                "all6188OriginalSourcesRetained":True,
                "sourceMultiplierTransport":"m_j=sum_(k<=j)binom(j,k)s^(j-k)n_k on ALL degree<=3 multipliers",
                "targetLeftTransport":"A_new=T A_old V; lambda_old=T^T lambda_new",
                "largeDataUploadedOrCommitted":False}}
    signal.signal(signal.SIGALRM,d.request_stop);signal.signal(signal.SIGTERM,d.request_stop)
    signal.setitimer(signal.ITIMER_REAL,a.remaining_seconds)
    try:
        run(d,m,j,u,a,result)
    except d.SafeStop as exc:
        result["status"]="incomplete";result["error"]=str(exc)
    except BaseException as exc:
        result["status"]="failed";result["error"]=type(exc).__name__+": "+str(exc)
        raise
    finally:
        signal.setitimer(signal.ITIMER_REAL,0)
        result["elapsedSeconds"]=time.monotonic()-started
        manifest=Path(a.checkpoint_dir)/"sixth-checkpoint.json"
        if manifest.exists():
            result["parameters"]["checkpointManifestSHA256"]=sha(manifest)
            result["parameters"]["checkpointManifestBytes"]=manifest.stat().st_size
        raw=json.dumps(result,sort_keys=True,indent=2).encode()
        req(len(raw)<100000,"Small permanent receipt only")
        out=Path(a.out);out.parent.mkdir(parents=True,exist_ok=True)
        temp=out.with_name(out.name+".tmp");temp.write_bytes(raw);os.replace(temp,out)
        print(json.dumps({"status":result["status"],"receipt":str(out),
            "receiptBytes":len(raw),"receiptSHA256":hashlib.sha256(raw).hexdigest(),
            "elapsedSeconds":result["elapsedSeconds"],
            "independentNinthLeadingCount":result.get("independentNinthLeadingCount"),
            "fullZeroMaximalMinorOrderLowerBound":result.get("fullZeroMaximalMinorOrderLowerBound"),
            "fullZeroSubmaximalMinorOrderLowerBound":result.get("fullZeroSubmaximalMinorOrderLowerBound")},
            sort_keys=True),flush=True)

if __name__=="__main__":
    main()
