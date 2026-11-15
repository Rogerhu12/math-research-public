#!/usr/bin/env python3
"""Resume the verified R150 zero-sixth top by exact constant-unit Schur.

The old verified residual and 2779x10 top kernel are mandatory read-only
ancestors. They are never recomputed. New middle/low matrices have their own
source binding and checkpoint directory. Each fixed-coefficient block is
eliminated independently of the large new rational RHS. Only the complete
small Schur RHS is reduced, with all homogeneous columns retained.
The final original driver still verifies every one of the 6188 source rows.
No completed sixth leading dimension is assumed.
"""
import argparse
import copy
import hashlib
import importlib.util
import json
from pathlib import Path
import resource
import signal
import time

PARENT_SHA="a6c423b98d70e06fb5a28797f09a11300129ec59128921c1e2d5c0e54fa8b5f2"
UNIT_HELPER_SHA="2d678264333a1edf3ed599e22bbdfc53b9eb95d9001f71a33f526e65c012c964"
ANCESTOR_BINDING="c72a1f2f398b4a964066621e92426bba93b486e9c94e70d22cd2efee1d5b4ac3"
ANCESTOR_MANIFEST_SHA="253d3a21506c7161b8dd5135d4855b79be6de72f85f28a181466b0ae6e16551f"
ANCESTOR_PHASES={
    "sixth-residuals":{
        "file":"sixth-residuals.json.gz","bytes":211242,
        "sha256":"d4c8142e2d3d80cc73f21454aed839d945331bb2f0a4a75645d9a2da879e5472",
        "matrixSHA256":"1ce58e3ce18ed349b25b60101888e40176db70024c7f354005cac0a43362d0d8",
        "shape":[6188,7],"verified":True},
    "top-kernel":{
        "file":"top-kernel.json.gz","bytes":43242447,
        "sha256":"f36b8e5566aa7f6975eb65fed151b702d2e9c71abaf9919e880d2101dece59ad",
        "matrixSHA256":"2bc2abc3ce44e5ba407519e90b8ec472243ff5711cce7d90aac61edcc8c77b52",
        "shape":[2779,10],"verified":True},
}

def req(ok,msg):
    if not ok: raise AssertionError(msg)

def sha(path):
    h=hashlib.sha256()
    with Path(path).open("rb") as f:
        for b in iter(lambda:f.read(1024*1024),b""): h.update(b)
    return h.hexdigest()

def module_at(name,path):
    spec=importlib.util.spec_from_file_location(name,path)
    out=importlib.util.module_from_spec(spec);spec.loader.exec_module(out)
    return out

def joined_hash(blocks):
    """Identical to matrix_hash(join_columns), without the large joined copy."""
    nr=blocks[0].nrows()
    req(all(X.nrows()==nr for X in blocks),"Original full-row block dimensions")
    h=hashlib.sha256()
    h.update(("%d,%d\n"%(nr,sum(X.ncols() for X in blocks))).encode("ascii"))
    for i in range(nr):
        h.update(("\t".join(str(X[i,c]) for X in blocks
                           for c in range(X.ncols()))+"\n").encode("ascii"))
    return h.hexdigest()

def column_diagnostics(M):
    out=[]
    for c in range(M.ncols()):
        nz=0;nb=0;db=0
        for r in range(M.nrows()):
            v=M[r,c]
            if v:
                nz+=1
                nb=max(nb,abs(int(v.numer())).bit_length())
                db=max(db,int(v.denom()).bit_length())
        out.append({"column":c,"nonzeroCoordinates":nz,
                    "maxNumeratorBits":nb,"maxDenominatorBits":db})
    return out

def install_ancestor_loader(d,a,result):
    original_load=d.load_matrix
    original_consume=d.consume_pack
    state={}
    manifest=Path(a.parent_checkpoint_dir)/"sixth-checkpoint.json"
    req(Path(a.checkpoint_dir).resolve()!=Path(a.parent_checkpoint_dir).resolve(),
        "New continuation must not write the original ancestor directory")
    req(manifest.is_file() and manifest.stat().st_size==861
        and sha(manifest)==ANCESTOR_MANIFEST_SHA,
        "Exact paid residual/top ancestor manifest is required")
    oldman=d.read_json(manifest)
    req(oldman.get("format")==d.FORMAT and oldman.get("temporaryOnly") is True
        and oldman.get("binding")==ANCESTOR_BINDING,
        "Actual paid ancestor provenance")
    for phase,expected in ANCESTOR_PHASES.items():
        req(oldman.get("phases",{}).get(phase)==expected,
            "Actual verified ancestor inventory changed: "+phase)
    parent_args=copy.copy(a);parent_args.checkpoint_dir=a.parent_checkpoint_dir

    def consume(m,args,res):
        blocks,md,oldbinding,names=original_consume(m,args,res)
        req(oldbinding==ANCESTOR_BINDING,
            "Actual pack and original driver no longer identify the paid top")
        semantic={"continuation":sha(__file__),"constantUnitHelper":UNIT_HELPER_SHA,
                  "parentDriver":PARENT_SHA,"ancestorBinding":oldbinding,
                  "ancestorManifest":ANCESTOR_MANIFEST_SHA,
                  "ancestorPhases":ANCESTOR_PHASES,"paidOriginalSemanticInputs":names}
        newbinding=d.small_hash(semantic)
        state["binding"]=newbinding
        res["parameters"].update({
            "ancestorBinding":oldbinding,"ancestorManifestSHA256":ANCESTOR_MANIFEST_SHA,
            "ancestorDirectoryReadOnly":True,"noTopRrefRecomputed":True,
            "newCheckpointBinding":newbinding,
            "constantUnitHelperSHA256":UNIT_HELPER_SHA,
            "parentDriverSHA256":PARENT_SHA,
        })
        # Explicit empty shapes are needed if the final leading image is zero.
        oldsub=m.submatrix
        def submatrix(M,rows,cols):
            rows=list(rows);cols=list(cols)
            if not rows or not cols: return m.fmpq_mat(len(rows),len(cols))
            return oldsub(M,rows,cols)
        m.submatrix=submatrix
        return blocks,md,newbinding,semantic

    def load(m,args,binding,phase,res):
        req(binding==state.get("binding"),"New continuation semantic binding")
        if phase not in ANCESTOR_PHASES:
            return original_load(m,args,binding,phase,res)
        # Whitelist only the two actually verified ancestor phases. Missing
        # files are an error, never a request to regenerate the old top.
        saved=original_load(m,parent_args,ANCESTOR_BINDING,phase,res)
        req(saved is not None and saved[2] is True,
            "Mandatory verified ancestor is unavailable: "+phase)
        M,meta,verified=saved
        expected=ANCESTOR_PHASES[phase]
        req([M.nrows(),M.ncols()]==expected["shape"]
            and m.matrix_hash(M)==expected["matrixSHA256"],
            "Exact verified ancestor matrix identity")
        if phase=="top-kernel":
            req(meta.get("all2805OriginalTopKernelRowsVerified") is True
                and meta.get("completeTopKernelSHA256")==expected["matrixSHA256"],
                "All original top rows must already be verified")
            res["parameters"]["actualTopColumnBitLengths"]=column_diagnostics(M)
            res["parameters"]["actualTopPayloadIsOnlyCompleteKernel"]=True
        else:
            req(meta.get("all6188NewResidualRowsConstructed") is True,
                "Complete original residual inventory")
        res["parameters"].setdefault("adoptedVerifiedAncestorPhases",{})[phase]=expected
        return saved

    d.consume_pack=consume
    d.load_matrix=load
    return state

def report_middle(m,full,meta,result):
    result["parameters"].update({
        "middleMatrixShape":meta["shape"],"middleAugmentedRank":meta["rank"],
        "middleKernelDimension":full.ncols(),
        "middleAugmentedSHA256":meta["augmentedSHA256"],
        "middleKernelSHA256":meta["middleKernelSHA256"],
        "completeMiddleLiftSHA256":m.matrix_hash(full),
        "all2295OriginalMiddleKernelRowsVerified":True,
        "allTopAndMiddleHomogeneousKernelsRetained":True,
        "middleUsesCompleteConstantUnitSchur":True,
        "noLargeMiddleAugmentedRref":True,
    })

def middle_continuation(d,u,m,j,a,coeff,mid,topK,binding,result):
    tsha=m.matrix_hash(topK);rsha=m.matrix_hash(mid);nt=topK.ncols()
    done=d.load_matrix(m,a,binding,"middle-complete-lift",result)
    if done is None:
        H3=j.block(m,coeff,0,2,3);hsha=m.matrix_hash(H3)
        saved=d.load_matrix(m,a,binding,"middle-actual-rhs",result)
        if saved is None:
            d.guard(a,"complete new middle RHS",0.0)
            N4=m.submatrix(topK,range(1485),range(nt))
            Z=m.submatrix(topK,range(2772,2779),range(nt))
            C=j.apply(m,coeff,0,2,{4:N4},nt)+mid*Z
            cm={"topKernelSHA256":tsha,"middleResidualSHA256":rsha,
                "constantH3SHA256":hsha,"all2295OriginalRowsRetained":True,
                "expression":"A0[normal2,normal4]*top4+R6normal2*topHead"}
            d.save_matrix(m,a,binding,"middle-actual-rhs",C,cm,result,True)
            del N4,Z
        else:
            C,cm,verified=saved
            req(verified and cm["topKernelSHA256"]==tsha
                and cm["middleResidualSHA256"]==rsha
                and cm["constantH3SHA256"]==hsha
                and cm["all2295OriginalRowsRetained"],"Complete middle RHS cache")
        req(C.nrows()==2295 and C.ncols()==nt,"All middle RHS columns retained")
        augsha=joined_hash([H3,C])
        result["parameters"]["actualMiddleRHSColumnBitLengths"]=column_diagnostics(C)
        K,km=u.complete_kernel(d,m,j,a,binding,"middle-unit",H3,C,988,result)
        req(K.nrows()==990+nt and km["constantRank"]==988,
            "Complete H3 homogeneous plus transported top kernel")
        d.guard(a,"actual complete middle source transport",0.0)
        T=m.submatrix(K,range(990,990+nt),range(K.ncols()))
        X3=m.submatrix(K,range(990),range(K.ncols()))
        fullTop=topK*T
        full=j.join_vertical(m,[X3,fullTop])
        req(full.nrows()==3769,"Every original middle-lift coordinate")
        meta={"shape":[2295,990+nt],"rank":km["rank"],"constantRank":988,
              "schurRank":km["schurRank"],"topKernelSHA256":tsha,
              "middleResidualSHA256":rsha,"H3SHA256":hsha,
              "transportedMiddleSHA256":m.matrix_hash(C),
              "augmentedSHA256":augsha,"middleKernelSHA256":m.matrix_hash(K),
              "constantUnitKernelFreeIndices":km["freeIndices"],
              "allTopAndMiddleHomogeneousKernelsRetained":True,
              "completeOriginalMiddleCoordinates":3769}
        d.save_matrix(m,a,binding,"middle-complete-lift",full,meta,result,False)
        verified=False
        del H3,C,K,T,X3,fullTop
    else:
        full,meta,verified=done
        req(meta["topKernelSHA256"]==tsha and meta["middleResidualSHA256"]==rsha
            and full.nrows()==3769
            and full.ncols()==990+nt-meta["rank"]
            and meta["allTopAndMiddleHomogeneousKernelsRetained"],
            "Actual complete middle lift source")
    if not verified:
        d.guard(a,"all2295 composed original middle rows",0.0)
        nc=full.ncols()
        X3=m.submatrix(full,range(990),range(nc))
        X4=m.submatrix(full,range(990,2475),range(nc))
        head=m.submatrix(full,range(3762,3769),range(nc))
        V=j.apply(m,coeff,0,2,{3:X3,4:X4},nc)+mid*head
        req(m.matrix_zero(V),"All2295 composed original middle equations")
        meta["all2295OriginalMiddleKernelRowsVerified"]=True
        meta["completeMiddleLiftSHA256"]=m.matrix_hash(full)
        d.save_matrix(m,a,binding,"middle-complete-lift",full,meta,result,True)
        del X3,X4,head,V
    report_middle(m,full,meta,result)
    return full,meta

def report_low(m,K,meta,result):
    result["parameters"].update({
        "lowMatrixShape":meta["shape"],"lowAugmentedRank":meta["rank"],
        "lowAugmentedSHA256":meta["augmentedSHA256"],
        "lowKernelSHA256":m.matrix_hash(K),
        "all1088OriginalLowKernelRowsVerified":True,
        "originalLambda5QAmbiguityRetained":True,
        "lowUsesCompleteConstantUnitSchur":True,
        "noLargeLowAugmentedRref":True,
    })

def low_continuation(d,u,m,j,a,coeff,low,midLift,Q,binding,result):
    nm=midLift.ncols();msha=m.matrix_hash(midLift);rsha=m.matrix_hash(low)
    saved=d.load_matrix(m,a,binding,"low-kernel",result)
    if saved is None:
        A0=j.join_vertical(m,[
            m.join_columns(j.block(m,coeff,0,r,1),j.block(m,coeff,0,r,2))
            for r in (0,1)])
        B1=j.join_vertical(m,[j.apply(m,coeff,1,r,{1:Q},7) for r in (0,1)])
        base=m.join_columns(A0,B1)
        asha=m.matrix_hash(A0);bsha=m.matrix_hash(B1);base_sha=m.matrix_hash(base)
        done=d.load_matrix(m,a,binding,"low-actual-rhs",result)
        if done is None:
            d.guard(a,"complete new low RHS",0.0)
            X3=m.submatrix(midLift,range(990),range(nm))
            head=m.submatrix(midLift,range(3762,3769),range(nm))
            C=j.join_vertical(m,[j.apply(m,coeff,0,r,{3:X3},nm)
                                  for r in (0,1)])+low*head
            cm={"middleLiftSHA256":msha,"lowResidualSHA256":rsha,
                "constantBaseSHA256":base_sha,"all1088OriginalRowsRetained":True,
                "expression":"A0[normal0or1,normal3]*middle3+R6low*middleHead"}
            d.save_matrix(m,a,binding,"low-actual-rhs",C,cm,result,True)
            del X3,head
        else:
            C,cm,verified=done
            req(verified and cm["middleLiftSHA256"]==msha
                and cm["lowResidualSHA256"]==rsha
                and cm["constantBaseSHA256"]==base_sha
                and cm["all1088OriginalRowsRetained"],"Complete low RHS cache")
        req(C.nrows()==1088 and C.ncols()==nm,"All transported middle RHS columns")
        augsha=joined_hash([base,C])
        result["parameters"]["actualLowRHSColumnBitLengths"]=column_diagnostics(C)
        K,km=u.complete_kernel(d,m,j,a,binding,"low-unit",base,C,582,result)
        nk=d.load_matrix(m,a,binding,"low-unit-constant-kernel",result)
        req(nk is not None and nk[2] and nk[1]["rank"]==582,
            "Complete paid low constant rank")
        pp=nk[1]["pivotColumns"]
        req(sum(x<585 for x in pp)==578 and len(pp)==582,
            "Actual A0/A1Q prefixes578/582 retained")
        meta={"shape":[1088,592+nm],"rank":km["rank"],
              "constantRank":582,"schurRank":km["schurRank"],
              "middleLiftSHA256":msha,"lowResidualSHA256":rsha,
              "A0LowSHA256":asha,"A1QSHA256":bsha,
              "transportedLowSHA256":m.matrix_hash(C),
              "augmentedSHA256":augsha,"freeIndices":km["freeIndices"],
              "originalLambda5QAmbiguityRetained":True,
              "allHomogeneousLowAndMiddleColumnsRetained":True}
        d.save_matrix(m,a,binding,"low-kernel",K,meta,result,False)
        verified=False
        del A0,B1,base,C,nk
    else:
        K,meta,verified=saved
        req(meta["middleLiftSHA256"]==msha and meta["lowResidualSHA256"]==rsha
            and K.nrows()==592+nm and K.ncols()==592+nm-meta["rank"]
            and meta["allHomogeneousLowAndMiddleColumnsRetained"],
            "Actual complete low kernel source")
    d.verify_free_identity(m,K,meta["freeIndices"])
    if not verified:
        d.guard(a,"all1088 composed original low rows",0.0)
        nc=K.ncols()
        T=m.submatrix(K,range(592,K.nrows()),range(nc));lift=midLift*T
        lo=m.submatrix(K,range(585),range(nc))
        b=m.submatrix(K,range(585,592),range(nc))
        high=m.submatrix(lift,range(990),range(nc))
        head=m.submatrix(lift,range(3762,3769),range(nc))
        pieces=[]
        for r in (0,1):
            part=j.apply(m,coeff,0,r,{
                1:m.submatrix(lo,range(135),range(nc)),
                2:m.submatrix(lo,range(135,585),range(nc)),3:high},nc)
            part+=j.apply(m,coeff,1,r,{1:Q*b},nc)
            pieces.append(part)
        V=j.join_vertical(m,pieces)+low*head
        req(m.matrix_zero(V),"All1088 composed original low equations")
        meta["all1088OriginalLowKernelRowsVerified"]=True
        d.save_matrix(m,a,binding,"low-kernel",K,meta,result,True)
        del T,lift,lo,b,high,head,pieces,V
    report_low(m,K,meta,result)
    return K,meta

def keep_receipt_small(d,result):
    """Full exact values stay in the verified temporary cochain, not main."""
    p=result["parameters"]
    if result.get("status")!="completed": return
    removed=[]
    lead=p.get("actualSixthLeadingInPaidSeven")
    if lead is not None and len(json.dumps(lead,separators=(",",":")))>6000:
        p["actualSixthLeadingExactJSONSHA256"]=d.small_hash(lead)
        del p["actualSixthLeadingInPaidSeven"]
        removed.append("actualSixthLeadingInPaidSeven")
    for name,item in p.get("targetSquareReadoutsAfterActualSixthLift",{}).items():
        values=item.get("nineByLeading")
        if values is not None and len(json.dumps(values,separators=(",",":")))>6000:
            item["exactValuesJSONSHA256"]=d.small_hash(values)
            del item["nineByLeading"]
            item["exactValuesInVerifiedTemporaryCochainMetadata"]=True
            removed.append(name+".nineByLeading")
    if removed:
        p["temporaryCompleteCochainContainsAllOmittedExactValues"]=True
        p["exactValueFieldsOmittedOnlyFromSmallReceipt"]=removed


def main():
    p=argparse.ArgumentParser()
    for name in ("parent-driver","unit-schur-helper","parent-checkpoint-dir",
                 "generator","jet-actions","cochain-exporter","cochain-manifest",
                 "cochain-receipt","fifth-receipt","checkpoint-dir","out"):
        p.add_argument("--"+name,required=True)
    p.add_argument("--through",choices=("middle","final"),default="final")
    p.add_argument("--remaining-seconds",type=float,default=600.0)
    p.add_argument("--memory-mib",type=int,default=8192)
    a=p.parse_args()
    req(a.remaining_seconds>0,"Positive actual shared time")
    req(2048<=a.memory_mib<=8192,"Explicit2048..8192MiB actual caller limit")
    resource.setrlimit(resource.RLIMIT_AS,(a.memory_mib*1024**2,a.memory_mib*1024**2))
    req(sha(a.parent_driver)==PARENT_SHA,"Pinned original sixth driver")
    req(sha(a.unit_schur_helper)==UNIT_HELPER_SHA,"Pinned constant-unit Schur helper")
    d=module_at("r150_zero_sixth_paid_parent",a.parent_driver)
    u=module_at("r150_exact_constant_unit_schur",a.unit_schur_helper)
    started=time.monotonic();a._deadline=started+a.remaining_seconds
    result={"format":"r150-zero-sixth-verified-top-constant-unit-continuation-v1",
            "status":"started","arithmetic":"exact rational python-flint",
            "scriptSHA256":sha(__file__),"parameters":{
                "sharedSeconds":a.remaining_seconds,"memoryMiB":a.memory_mib,
                "through":a.through,"naturalParameter":"s",
                "sourceStrata":[170,918,2295,2805],
                "ancestorCheckpointDirectory":str(Path(a.parent_checkpoint_dir)),
                "checkpointDirectory":str(Path(a.checkpoint_dir)),
                "temporaryOnly":True,"largeDataUploadedOrCommitted":False,
                "sourceMultiplierTransport":
                    "m_j=sum_(k<=j)binom(j,k)s^(j-k)n_k on ALL degree<=3 multipliers",
                "targetLeftTransport":"A_new=T A_old V; lambda_old=T^T lambda_new",
                "noTopRrefRecomputed":True,"noLargeAugmentedRationalRref":True,
                "noUnverifiedCandidateCounted":True,
            }}
    signal.signal(signal.SIGALRM,d.request_stop)
    signal.signal(signal.SIGTERM,d.request_stop)
    signal.setitimer(signal.ITIMER_REAL,a.remaining_seconds)
    try:
        install_ancestor_loader(d,a,result)
        d.middle_kernel=lambda m,j,args,coeff,mid,top,binding,res: middle_continuation(
            d,u,m,j,args,coeff,mid,top,binding,res)
        d.low_kernel=lambda m,j,args,coeff,low,mid,Q,binding,res: low_continuation(
            d,u,m,j,args,coeff,low,mid,Q,binding,res)
        d.run(a,result)
    except d.SafeStop as exc:
        result["status"]="incomplete";result["error"]=str(exc)
    except BaseException as exc:
        result["status"]="failed";result["error"]=type(exc).__name__+": "+str(exc)
        raise
    finally:
        signal.setitimer(signal.ITIMER_REAL,0)
        result["elapsedSeconds"]=time.monotonic()-started
        man=Path(a.checkpoint_dir)/"sixth-checkpoint.json"
        if man.exists():
            result["parameters"]["checkpointManifestSHA256"]=sha(man)
            result["parameters"]["checkpointManifestBytes"]=man.stat().st_size
        keep_receipt_small(d,result)
        raw=json.dumps(result,sort_keys=True,indent=2).encode("utf-8")
        req(len(raw)<100000,"Small continuation receipt limit")
        path=Path(a.out);path.parent.mkdir(parents=True,exist_ok=True)
        tmp=path.with_name(path.name+".tmp");tmp.write_bytes(raw);tmp.replace(path)
        print(json.dumps({"status":result["status"],"receipt":str(path),
            "receiptBytes":len(raw),"receiptSHA256":hashlib.sha256(raw).hexdigest(),
            "elapsedSeconds":result["elapsedSeconds"],
            "independentSixthLeadingCount":result.get("independentSixthLeadingCount"),
            "fullZeroMaximalMinorOrderLowerBound":result.get("fullZeroMaximalMinorOrderLowerBound"),
            "fullZeroSubmaximalMinorOrderLowerBound":result.get("fullZeroSubmaximalMinorOrderLowerBound")},
            sort_keys=True),flush=True)

if __name__=="__main__":
    main()
