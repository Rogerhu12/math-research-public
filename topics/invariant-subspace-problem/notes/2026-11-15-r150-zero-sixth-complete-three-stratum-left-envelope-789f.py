#!/usr/bin/env python3
"""R150 zero sixth left jets: all6188 sources, three exact source strata.

Consumer of the ACTUAL seven paid fifth cochains. No old page is recomputed.
New sixth residuals retain source normal degrees0,1,2,3 of sizes
170,918,2295,2805. Corrections retain ALL normal target degrees1..5.
Solve top [H4,H5,Rtop], then middle [H3,K4*top4+Rmid*topHead],
then low [J0,A1Q,K3*middle3+Rlow*middleHead].
Every homogeneous kernel and the actual Q ambiguity at lambda5 are retained.
An actual leading dimension gives only a positive lower bound on left6 jets;
it is NOT a lower bound on the full sixth connecting rank.

Native RREF is in-place. A complete candidate kernel is saved immediately
after each native call, before the independent original-row verification.
No candidate is counted until its full original identity is verified.
Temporary checkpoints are portable, bound to source and semantic input bytes.
The caller may stop after residual/top/middle/final and resume the same phase.
No normal form or large original Macaulay matrix is recomputed.
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
import time

FIRST_SHA="2757b900480fe3bf1450100188df1679801351f0330d609e1a39b9c7ca146186"
ACTIONS_SHA="4e63c72c550e8f90c022b086d3758f8e7b12edf4fb16a0ef387bc1a92f97366a"
EXPORT_SHA="f2e03d6c07e301c85f8c48358d4eefa2cdc201124b0cf32ca469c25005839fae"
FIFTH_SHA="94151693c2a0a9b8fc0eb84d442d6742818503b3cd069bffd82f95f1b0bc1f1b"
FIFTH_RECEIPT_SHA="5ba37fa2e82f4169375c2d3e869a3bb065238c3e4d7c2b60bd021f70266ccc41"
PAID_PACK_LOGICAL_SHA="cf952faf51a2e17fe9b5d668ac8d9c171ce299d0d3a413e5808053640ce94640"
PAID_PACK_BINDING="7291adb44a00beeda81ca10eafb4a7431dd40341907a399833dc0778b00b4e11"
ZERO97_SHA="50781d98bb92faafbe14ada9db16b30b1c1142776f5cbfb941b73489f02829a6"
FORMAT="r150-zero-sixth-full-source-temporary-v1"
STOP=False

class SafeStop(Exception):
    pass

def require(ok,msg):
    if not ok:
        raise AssertionError(msg)

def sha(path):
    h=hashlib.sha256()
    with Path(path).open("rb") as f:
        for b in iter(lambda:f.read(1024*1024),b""):
            h.update(b)
    return h.hexdigest()

def small_hash(obj):
    return hashlib.sha256(json.dumps(obj,sort_keys=True,separators=(",",":"))
                          .encode("ascii")).hexdigest()

def module_at(name,path):
    spec=importlib.util.spec_from_file_location(name,path)
    mod=importlib.util.module_from_spec(spec);spec.loader.exec_module(mod)
    return mod

def read_json(path):
    path=Path(path)
    with (gzip.open(path,"rt",encoding="utf-8") if path.suffix==".gz" else
          path.open("r",encoding="utf-8")) as f:
        return json.load(f)

def result_at(path):
    obj=read_json(path);obj=obj.get("result",obj)
    require(obj.get("status")=="completed","Required paid/prepare receipt incomplete")
    return obj

def atomic_json(path,obj,compressed=False):
    path=Path(path);path.parent.mkdir(parents=True,exist_ok=True)
    tmp=path.with_name(path.name+".tmp")
    if compressed:
        with tmp.open("wb") as raw:
            with gzip.GzipFile(fileobj=raw,mode="wb",compresslevel=1,mtime=0) as gz:
                with io.TextIOWrapper(gz,encoding="utf-8",newline="\n") as f:
                    json.dump(obj,f,sort_keys=True,separators=(",",":"))
    else:
        tmp.write_text(json.dumps(obj,sort_keys=True,indent=2),encoding="utf-8")
    os.replace(tmp,path)

def request_stop(signum,frame):
    global STOP
    STOP=True

def guard(a,label,reserve=2.0):
    if STOP or a._deadline-time.monotonic()<=reserve:
        raise SafeStop("Verified/candidate temporary state retained before "+label)

def read_manifest(a,binding):
    path=Path(a.checkpoint_dir)/"sixth-checkpoint.json"
    if not path.exists():
        return {"format":FORMAT,"binding":binding,"temporaryOnly":True,"phases":{}}
    obj=read_json(path)
    require(obj.get("format")==FORMAT and obj.get("binding")==binding
            and obj.get("temporaryOnly") is True,"Sixth checkpoint source/input mismatch")
    return obj

def save_matrix(m,a,binding,phase,M,meta,result,verified):
    directory=Path(a.checkpoint_dir);directory.mkdir(parents=True,exist_ok=True)
    man=read_manifest(a,binding)
    mh=m.matrix_hash(M)
    payload={"format":FORMAT,"binding":binding,"phase":phase,
             "shape":[M.nrows(),M.ncols()],"matrixSHA256":mh,
             "verified":bool(verified),"metadata":meta,
             "matrix":[[str(M[i,j]) for j in range(M.ncols())]
                       for i in range(M.nrows())]}
    file=directory/(phase+".json.gz")
    atomic_json(file,payload,True)
    man["phases"][phase]={"file":file.name,"bytes":file.stat().st_size,
                          "sha256":sha(file),"matrixSHA256":mh,
                          "shape":payload["shape"],"verified":bool(verified)}
    atomic_json(directory/"sixth-checkpoint.json",man)
    result["parameters"]["checkpointPhases"]={
        key:{k:v for k,v in value.items() if k!="file"}
        for key,value in man["phases"].items()}
    result["parameters"]["checkpointManifestSHA256"]=sha(
        directory/"sixth-checkpoint.json")
    result["parameters"]["lastSavedPhase"]=phase

def load_matrix(m,a,binding,phase,result):
    man=read_manifest(a,binding);e=man["phases"].get(phase)
    if e is None:
        return None
    file=Path(a.checkpoint_dir)/e["file"]
    require(file.parent==Path(a.checkpoint_dir) and file.stat().st_size==e["bytes"]
            and sha(file)==e["sha256"],"Actual temporary matrix bytes changed")
    obj=read_json(file)
    require(obj.get("format")==FORMAT and obj.get("binding")==binding
            and obj.get("phase")==phase,"Temporary phase/binding changed")
    nr,nc=obj["shape"]
    require(len(obj["matrix"])==nr and all(len(r)==nc for r in obj["matrix"]),
            "Complete temporary matrix dimensions")
    M=m.fmpq_mat(nr,nc,[m.fmpq(x) for row in obj["matrix"] for x in row])
    require(m.matrix_hash(M)==obj["matrixSHA256"]==e["matrixSHA256"],
            "Actual temporary rational matrix hash")
    require(obj["verified"]==e["verified"],"Temporary verification status mismatch")
    result["parameters"].setdefault("resumedPhases",[]).append(phase)
    return M,obj["metadata"],obj["verified"]

def verify_free_identity(m,K,free):
    require(K.ncols()==len(free),"Full candidate free-coordinate count")
    for j,f in enumerate(free):
        for k,g in enumerate(free):
            require(K[g,j]==(1 if j==k else 0),"Complete kernel free I changed")

def consume_pack(m,a,result):
    require(sha(a.generator)==FIRST_SHA,"Paid original generator source")
    require(sha(a.jet_actions)==ACTIONS_SHA,"Original jet-action helper source")
    require(sha(a.cochain_exporter)==EXPORT_SHA,"Paid cochain exporter source")
    require(sha(a.fifth_receipt)==FIFTH_RECEIPT_SHA,"Paid fifth outer receipt bytes")
    paid=result_at(a.fifth_receipt)
    require(paid["scriptSHA256"]==FIFTH_SHA
            and paid["parameters"]["all6188OriginalSourcesRetainedInFifthProof"]
            and paid["parameters"]["independentFifthLeadingCount"]==7,
            "Actual paid complete fifth family")
    er=result_at(a.cochain_receipt);ep=er["parameters"]
    require(er["format"]=="r150-paid-zero-fifth-cochains-export-v1"
            and er["scriptSHA256"]==EXPORT_SHA
            and ep["allPaidFifthCanonicalHashesVerified"]
            and ep["packProducerSourceSHA256"]==EXPORT_SHA
            and ep["paidFifthReceiptSHA256"]==FIFTH_RECEIPT_SHA,
            "Complete actual paid cochain export")
    manifest=read_json(a.cochain_manifest)
    require(manifest.get("format")=="r150-fifth-joint-high-low-temporary-v1"
            and manifest.get("temporaryOnly") is True
            and manifest["binding"]==ep["packBinding"]==PAID_PACK_BINDING,
            "Paid cochain pack producer binding")
    entry=manifest["phases"]["paid-fifth-full-cochains"]
    require(entry==ep["completePaidCochainPack"],"Prepared actual pack entry")
    folder=Path(a.cochain_manifest).parent;file=folder/entry["file"]
    require(file.parent==folder and file.stat().st_size==entry["bytes"]
            and sha(file)==entry["sha256"],"Prepared actual pack bytes/hash")
    p=read_json(file)
    require(p["format"]==manifest["format"] and p["binding"]==manifest["binding"]
            and p["phase"]=="paid-fifth-full-cochains" and p["complete"] is True
            and p["shape"]==[4738,7],"Complete paid cochain pack header")
    require(len(p["matrix"])==4738 and all(len(r)==7 for r in p["matrix"]),
            "All4738x7 paid cochain coordinates")
    M=m.fmpq_mat([[m.fmpq(x) for x in row] for row in p["matrix"]])
    require(m.matrix_hash(M)==p["matrixSHA256"]==entry["matrixSHA256"]==PAID_PACK_LOGICAL_SHA,
            "Full paid cochain pack logical SHA")
    md=p["metadata"]
    require(md["format"]=="r150-paid-zero-fifth-cochains-for-sixth-v1"
            and md["chart"]=="zero" and md["paidFifthProducerSHA256"]==FIFTH_SHA
            and md["paidFifthReceiptSHA256"]==FIFTH_RECEIPT_SHA
            and md["allPaidFifthCanonicalHashesVerified"]
            and md["all6188SourceFifthIdentityAlreadyPaidAndReconstructed"],
            "Original source provenance of all paid cochains")
    blocks={}
    for name,item in md["ranges"].items():
        X=m.submatrix(M,range(item["start"],item["stop"]),range(7))
        require(m.matrix_hash(X)==item["matrixSHA256"],"Paid block "+name)
        blocks[name]=X
    result["parameters"].update({
        "paidFifthCochainsSHA256":p["matrixSHA256"],
        "paidFifthCochainFileSHA256":entry["sha256"],
        "paidFifthProducerBinding":manifest["binding"],
        "paidFifthReceiptSHA256":FIFTH_RECEIPT_SHA,
        "paidCochainExporterSHA256":EXPORT_SHA,
        "allPaidFifthCanonicalHashesVerified":True,
        "noEarlierLeftJetEliminationRecomputed":True,
    })
    for k in (2,3,4,5):
        result["parameters"]["lambda"+str(k)+"NineSquares"]=md[
            "lambda"+str(k)+"NineSquares"]
        result["parameters"]["lambda"+str(k)+"NineSquareSHA256"]=md[
            "lambda"+str(k)+"NineSquareSHA256"]
    names={"script":sha(__file__),"first":FIRST_SHA,"actions":ACTIONS_SHA,
           "exporter":EXPORT_SHA,"paidFifth":FIFTH_RECEIPT_SHA,
           "packLogical":p["matrixSHA256"],"packFile":entry["sha256"],
           "packProducerBinding":manifest["binding"]}
    return blocks,md,small_hash(names),names

def physical_cochains(m,j,blocks):
    H0=blocks["lambda0ThirteenCoordinates"]
    q0=m.submatrix(blocks["firstSurvivingQ0Padded"],range(135),range(3))
    pure=m.fmpq_mat(20,7);ix={v:i for i,v in enumerate(j.target_columns(0))}
    k=0
    for degree in range(4):
        for aa in range(degree+1):
            row=ix[(aa,degree-aa+2,())]
            for c in range(7): pure[row,c]=H0[k,c]
            k+=1
    one=q0*m.submatrix(H0,range(10,13),range(7))
    co=[{0:pure,1:one},{1:blocks["lambda1OneNormal"]}]
    for k in (2,3,4,5):
        X=blocks["lambda"+str(k)+"Low"]
        section={1:m.submatrix(X,range(135),range(7)),
                 2:m.submatrix(X,range(135,585),range(7))}
        high=blocks.get("lambda"+str(k)+"ThreeNormal")
        if high is not None:
            section[3]=high
        co.append(section)
    Q=blocks["constantOneNormalQ"]
    require(Q.nrows()==135 and Q.ncols()==7,"All7 actual constant one-normal columns")
    square_ix={v:i for i,v in enumerate(j.target_columns(2))}
    for k in (2,3):
        sq=m.fmpq_mat([[co[k][2][square_ix[(0,0,(i,i))],c] for c in range(7)]
                       for i in range(2,11)])
        require(m.matrix_zero(sq) and m.matrix_hash(sq)==ZERO97_SHA,
                "Paid target square zero changed")
    return co,Q

def new_residuals(m,j,a,coeff,co,binding,result):
    old=load_matrix(m,a,binding,"sixth-residuals",result)
    if old is not None:
        R,meta,verified=old
        require(verified and R.nrows()==6188 and R.ncols()==7
                and meta["originalPhysicalSHA256"]==small_hash(coeff["physical"]),
                "Verified original sixth residual cache")
        counts=(1088,2295,2805);pos=0;parts=[]
        for n in counts:
            parts.append(m.submatrix(R,range(pos,pos+n),range(7)));pos+=n
        return parts,meta
    parts=[]
    for r in range(4):
        guard(a,"new original residual source sector"+str(r))
        R=m.fmpq_mat(len(j.source_rows(r)),7)
        for k in range(6):
            R+=j.apply_sparse(m,coeff,6-k,r,co[k],7)
        parts.append(R)
    # Independent explicit top source formula; the new2805 rows are NOT dropped.
    top=m.fmpq_mat(2805,7);ix={v:i for i,v in enumerate(j.target_columns(3))}
    for row,(i,aa,bb,mon) in enumerate(j.source_rows(3)):
        require(aa==bb==0,"Original source degree3 top is pure normal")
        target=ix[(0,2,mon)]
        for c in range(7): top[row,c]=coeff["pure"][2][i]*co[4][3][target,c]
    require(top==parts[3],"Original seed2 times lambda4-three top term omitted")
    low=j.join_vertical(m,parts[:2]);mid=parts[2]
    allR=j.join_vertical(m,[low,mid,top])
    meta={
        "originalPhysicalSHA256":small_hash(coeff["physical"]),
        "originalPhysicalHashesThroughOrder6":coeff["physical"],
        "sourceRowCounts":[170,918,2295,2805],
        "lowResidualSHA256":m.matrix_hash(low),
        "middleResidualSHA256":m.matrix_hash(mid),
        "topResidualSHA256":m.matrix_hash(top),
        "all6188NewResidualRowsConstructed":True,
        "topSeed2Lambda4ThreeIdentityVerified":True,
        "topSixthResidualIsExactlyZero":m.matrix_zero(top),
        "noThreeNormalSourceRowsDiscarded":True,
    }
    save_matrix(m,a,binding,"sixth-residuals",allR,meta,result,True)
    return [low,mid,top],meta

def original_block_sum(m,j,coeff,source_degree,sections,ncols):
    return j.apply(m,coeff,0,source_degree,sections,ncols)

def top_kernel(m,j,a,coeff,top,binding,result):
    saved=load_matrix(m,a,binding,"top-kernel",result)
    if saved is None:
        guard(a,"top2805x2779 exact RREF",4.0)
        H4=j.block(m,coeff,0,3,4);H5=j.block(m,coeff,0,3,5)
        top_is_zero=m.matrix_zero(top)
        H=m.join_columns(H4,H5)
        A=H if top_is_zero else m.join_columns(H,top)
        meta={"shape":[2805,A.ncols()],"logicalAugmentedShape":[2805,2779],
              "H4SHA256":m.matrix_hash(H4),"H5SHA256":m.matrix_hash(H5),
              "topResidualSHA256":m.matrix_hash(top),
              "actualRrefMatrixSHA256":m.matrix_hash(A),
              "topResidualIsExactlyZero":top_is_zero,
              "allQuarticAndQuinticCorrectionsRetained":True}
        del H4,H5,H
        rr,rank=A.rref(inplace=True)
        rawK,piv,rawfree=j.canonical_kernel(m,rr,rank)
        if top_is_zero:
            # Exact direct sum, after all19635 top residual entries were checked.
            K=m.fmpq_mat(2779,rawK.ncols()+7)
            for i in range(2772):
                for c in range(rawK.ncols()): K[i,c]=rawK[i,c]
            for c in range(7): K[2772+c,rawK.ncols()+c]=1
            free=rawfree+list(range(2772,2779))
        else:
            K=rawK;free=rawfree
        del rawK
        meta.update({"rank":rank,"pivotIndices":piv,"freeIndices":free,
                     "variableRanges":{"four":[0,1485],"five":[1485,2772],
                                       "paidFifthHead":[2772,2779]}})
        verify_free_identity(m,K,free)
        del A,rr
        # Complete candidate survives any later verification/time interruption.
        save_matrix(m,a,binding,"top-kernel",K,meta,result,False)
        verified=False
    else:
        K,meta,verified=saved
        require(K.nrows()==2779 and K.ncols()==2779-meta["rank"]
                and meta["topResidualSHA256"]==m.matrix_hash(top),
                "Original top kernel source mismatch")
        verify_free_identity(m,K,meta["freeIndices"])
    if not verified:
        guard(a,"original2805 top-kernel product",0.0)
        X4=m.submatrix(K,range(1485),range(K.ncols()))
        X5=m.submatrix(K,range(1485,2772),range(K.ncols()))
        Z=m.submatrix(K,range(2772,2779),range(K.ncols()))
        V=original_block_sum(m,j,coeff,3,{4:X4,5:X5},K.ncols())+top*Z
        require(m.matrix_zero(V),"All2805 original top-kernel rows failed")
        meta["all2805OriginalTopKernelRowsVerified"]=True
        meta["completeTopKernelSHA256"]=m.matrix_hash(K)
        save_matrix(m,a,binding,"top-kernel",K,meta,result,True)
    result["parameters"].update({
        "topMatrixShape":meta["shape"],"topLogicalAugmentedShape":[2805,2779],
        "topAugmentedRank":meta["rank"],
        "topKernelDimension":K.ncols(),"topActualRrefMatrixSHA256":meta["actualRrefMatrixSHA256"],
        "topResidualIsExactlyZero":meta["topResidualIsExactlyZero"],
        "topKernelSHA256":m.matrix_hash(K),
        "all2805OriginalTopKernelRowsVerified":True,
        "allTopHomogeneousKernelColumnsRetained":True,
    })
    return K,meta

def middle_kernel(m,j,a,coeff,mid,topK,binding,result):
    nt=topK.ncols()
    N4=m.submatrix(topK,range(1485),range(nt))
    Z=m.submatrix(topK,range(2772,2779),range(nt))
    saved=load_matrix(m,a,binding,"middle-kernel",result)
    if saved is None:
        guard(a,"actual middle2295 correction",3.0)
        C=j.apply(m,coeff,0,2,{4:N4},nt)+mid*Z
        H3=j.block(m,coeff,0,2,3)
        A=m.join_columns(H3,C)
        meta={"shape":[2295,990+nt],"topKernelSHA256":m.matrix_hash(topK),
              "middleResidualSHA256":m.matrix_hash(mid),
              "H3SHA256":m.matrix_hash(H3),"transportedMiddleSHA256":m.matrix_hash(C),
              "augmentedSHA256":m.matrix_hash(A)}
        del H3,C
        rr,rank=A.rref(inplace=True)
        K,piv,free=j.canonical_kernel(m,rr,rank)
        meta.update({"rank":rank,"pivotIndices":piv,"freeIndices":free})
        verify_free_identity(m,K,free);del A,rr
        save_matrix(m,a,binding,"middle-kernel",K,meta,result,False)
        verified=False
    else:
        K,meta,verified=saved
        require(K.nrows()==990+nt and K.ncols()==990+nt-meta["rank"]
                and meta["topKernelSHA256"]==m.matrix_hash(topK)
                and meta["middleResidualSHA256"]==m.matrix_hash(mid),
                "Middle kernel complete top transport mismatch")
        verify_free_identity(m,K,meta["freeIndices"])
    T=m.submatrix(K,range(990,990+nt),range(K.ncols()))
    fullTop=topK*T
    X3=m.submatrix(K,range(990),range(K.ncols()))
    if not verified:
        guard(a,"all2295 actual middle-kernel rows",0.0)
        X4=m.submatrix(fullTop,range(1485),range(K.ncols()))
        head=m.submatrix(fullTop,range(2772,2779),range(K.ncols()))
        V=original_block_sum(m,j,coeff,2,{3:X3,4:X4},K.ncols())+mid*head
        require(m.matrix_zero(V),"All2295 original middle rows failed")
        meta["all2295OriginalMiddleKernelRowsVerified"]=True
        save_matrix(m,a,binding,"middle-kernel",K,meta,result,True)
    full=j.join_vertical(m,[X3,fullTop])
    require(full.nrows()==3769,"Actual middle full-lift coordinate count")
    result["parameters"].update({
        "middleMatrixShape":meta["shape"],"middleAugmentedRank":meta["rank"],
        "middleKernelDimension":K.ncols(),"middleAugmentedSHA256":meta["augmentedSHA256"],
        "middleKernelSHA256":m.matrix_hash(K),"completeMiddleLiftSHA256":m.matrix_hash(full),
        "all2295OriginalMiddleKernelRowsVerified":True,
        "allTopAndMiddleHomogeneousKernelsRetained":True,
    })
    return full,meta

def low_kernel(m,j,a,coeff,low,midLift,Q,binding,result):
    nm=midLift.ncols()
    X3=m.submatrix(midLift,range(990),range(nm))
    head=m.submatrix(midLift,range(3762,3769),range(nm))
    old=load_matrix(m,a,binding,"low-kernel",result)
    if old is None:
        guard(a,"actual low1088 correction",3.0)
        A0=j.join_vertical(m,[
            m.join_columns(j.block(m,coeff,0,r,1),j.block(m,coeff,0,r,2))
            for r in (0,1)])
        B=j.join_vertical(m,[j.apply(m,coeff,1,r,{1:Q},7) for r in (0,1)])
        C=j.join_vertical(m,[j.apply(m,coeff,0,r,{3:X3},nm) for r in (0,1)])+low*head
        base=m.join_columns(A0,B)
        A=m.join_columns(base,C)
        meta={"shape":[1088,592+nm],"middleLiftSHA256":m.matrix_hash(midLift),
              "lowResidualSHA256":m.matrix_hash(low),"A0LowSHA256":m.matrix_hash(A0),
              "A1QSHA256":m.matrix_hash(B),"transportedLowSHA256":m.matrix_hash(C),
              "augmentedSHA256":m.matrix_hash(A)}
        del A0,B,C,base
        rr,rank=A.rref(inplace=True)
        K,piv,free=j.canonical_kernel(m,rr,rank)
        require(sum(c<585 for c in piv)==578 and sum(c<592 for c in piv)==582,
                "Paid complete A0/A1Q low prefix changed")
        meta.update({"rank":rank,"pivotIndices":piv,"freeIndices":free})
        verify_free_identity(m,K,free);del A,rr
        save_matrix(m,a,binding,"low-kernel",K,meta,result,False)
        verified=False
    else:
        K,meta,verified=old
        require(K.nrows()==592+nm and K.ncols()==592+nm-meta["rank"]
                and meta["middleLiftSHA256"]==m.matrix_hash(midLift)
                and meta["lowResidualSHA256"]==m.matrix_hash(low),
                "Low kernel complete middle transport mismatch")
        verify_free_identity(m,K,meta["freeIndices"])
    if not verified:
        guard(a,"all1088 original low-kernel rows",0.0)
        T=m.submatrix(K,range(592,K.nrows()),range(K.ncols()))
        lift=midLift*T
        lo=m.submatrix(K,range(585),range(K.ncols()))
        b=m.submatrix(K,range(585,592),range(K.ncols()))
        high=m.submatrix(lift,range(990),range(K.ncols()))
        h=m.submatrix(lift,range(3762,3769),range(K.ncols()))
        pieces=[]
        for r in (0,1):
            part=original_block_sum(m,j,coeff,r,{
                1:m.submatrix(lo,range(135),range(K.ncols())),
                2:m.submatrix(lo,range(135,585),range(K.ncols())),
                3:high},K.ncols())
            part+=j.apply(m,coeff,1,r,{1:Q*b},K.ncols())
            pieces.append(part)
        V=j.join_vertical(m,pieces)+low*h
        require(m.matrix_zero(V),"All1088 original low correction rows failed")
        meta["all1088OriginalLowKernelRowsVerified"]=True
        save_matrix(m,a,binding,"low-kernel",K,meta,result,True)
    result["parameters"].update({
        "lowMatrixShape":meta["shape"],"lowAugmentedRank":meta["rank"],
        "lowAugmentedSHA256":meta["augmentedSHA256"],"lowKernelSHA256":m.matrix_hash(K),
        "all1088OriginalLowKernelRowsVerified":True,
        "originalLambda5QAmbiguityRetained":True,
    })
    return K,meta

def final_family(m,j,a,coeff,co,Q,parts,midLift,lowK,binding,result):
    guard(a,"actual sixth leading image and all6188 products",0.0)
    tail=m.submatrix(lowK,range(592,lowK.nrows()),range(lowK.ncols()))
    allLift=midLift*tail
    allHead=m.submatrix(allLift,range(3762,3769),range(allLift.ncols()))
    rr,rank=allHead.rref();choice=m.pivot_columns(rr,rank)
    chosen=m.submatrix(lowK,range(lowK.nrows()),choice)
    lift=m.submatrix(allLift,range(allLift.nrows()),choice)
    head=m.submatrix(allHead,range(7),choice)
    require(0<=rank<=7,"Actual sixth independent leading dimension")
    lo=m.submatrix(chosen,range(585),range(rank))
    b=m.submatrix(chosen,range(585,592),range(rank))
    extra=Q*b
    lam6={1:m.submatrix(lo,range(135),range(rank)),
          2:m.submatrix(lo,range(135,585),range(rank)),
          3:m.submatrix(lift,range(990),range(rank)),
          4:m.submatrix(lift,range(990,2475),range(rank)),
          5:m.submatrix(lift,range(2475,3762),range(rank))}
    # Independently multiply the selected new row on every original source.
    for r in range(4):
        V=original_block_sum(m,j,coeff,r,lam6,rank)
        V+=j.apply(m,coeff,1,r,{1:extra},rank)
        R=parts[0] if r<2 else parts[r-1]
        if r==0: R=m.submatrix(R,range(170),range(7))
        if r==1: R=m.submatrix(R,range(170,1088),range(7))
        V+=R*head
        require(m.matrix_zero(V),"Actual sixth original source sector failed: "+str(r))
    actual=[{r:X*head for r,X in section.items()} for section in co]
    actual[5][1]+=extra
    actual.append(lam6)
    ranges={};blocklist=[];offset=0
    for k,section in enumerate(actual):
        for r in sorted(section):
            X=section[r];name="lambda"+str(k)+"Normal"+str(r)
            ranges[name]={"start":offset,"stop":offset+X.nrows(),
                          "matrixSHA256":m.matrix_hash(X)}
            blocklist.append(X);offset+=X.nrows()
    pack=j.join_vertical(m,blocklist)
    c6=min(14,17-rank)
    dmax=53+max(rank-3,0)
    dsub=47+max(rank-4,0)
    square_index={v:i for i,v in enumerate(j.target_columns(2))}
    targetRead={}
    for k in range(7):
        X=actual[k].get(2)
        sq=(m.fmpq_mat(9,rank) if X is None else
            m.fmpq_mat([[X[square_index[(0,0,(i,i))],c] for c in range(rank)]
                        for i in range(2,11)]))
        targetRead["lambda"+str(k)]={"matrixSHA256":m.matrix_hash(sq),
            "nineByLeading":[[str(sq[i,c]) for c in range(rank)] for i in range(9)]}
        if k<=3:
            require(m.matrix_zero(sq),"Paid low target readout changed after actual lift")
    meta={"chart":"zero","parameter":"s","order":6,"leadingColumns":rank,
          "ranges":ranges,"all6188OriginalSixthRowsVerified":True,
          "allPaidLowerCochainsTransportedTogether":True,
          "leadingInPaidSeven":[[str(head[i,c]) for i in range(7)] for c in range(rank)],
          "leadingSHA256":m.matrix_hash(head),
          "chosenLowCorrectionSHA256":m.matrix_hash(chosen),
          "allHighCorrectionsSHA256":m.matrix_hash(lift),
          "originalPhysicalHashesThroughOrder6":coeff["physical"],
          "targetSquareReadouts":targetRead,"temporaryOnly":True}
    save_matrix(m,a,binding,"complete-sixth-cochains",pack,meta,result,True)
    result.update({
        "status":"completed","independentSixthLeadingCount":rank,
        "sumFirstSixConnectionRanksUpperBound":c6,
        "fullZeroMaximalMinorOrderLowerBound":dmax,
        "fullZeroSubmaximalMinorOrderLowerBound":dsub,
    })
    result["parameters"].update({
        "independentSixthLeadingCount":rank,
        "actualSixthLeadingInPaidSeven":meta["leadingInPaidSeven"],
        "actualSixthLeadingSHA256":meta["leadingSHA256"],
        "actualSixthCompleteCochainSHA256":m.matrix_hash(pack),
        "actualSixthCompleteCochainShape":[pack.nrows(),pack.ncols()],
        "actualSixthCochainRanges":ranges,
        "sumFirstSixConnectionRanksUpperBound":c6,
        "firstFiveCumulativeRankUpperBounds":[4,4,5,8,10],
        "fullZeroMaximalMinorOrderLowerBound":dmax,
        "fullZeroSubmaximalMinorOrderLowerBound":dsub,
        "all6188OriginalSixthRowsVerified":True,
        "all4347NonpureOutputCoordinatesAvailableForSixthCorrection":True,
        "remaining20PureConstantKernelCoordinatesHaveZeroA0Action":True,
        "tenOtherPureLeftFunctionalsExactForAllParameters":True,
        "noQuarticQuinticNormalCorrectionDiscarded":True,
        "notAFullSixthConnectionLowerBound":True,
        "targetSquareReadoutsAfterActualSixthLift":targetRead,
        "h0TimesTargetThroughDegree6PairingZeroForThisActualFamily":True,
        "fullTargetMembershipNotClaimed":True,
    })

def run(a,result):
    require(sha(a.generator)==FIRST_SHA,"First generator SHA")
    require(sha(a.jet_actions)==ACTIONS_SHA,"Jet-action module SHA")
    m=module_at("r150_sixth_paid_first",a.generator)
    j=module_at("r150_sixth_original_actions",a.jet_actions)
    blocks,md,binding,named=consume_pack(m,a,result)
    result["parameters"]["checkpointBinding"]=binding
    result["parameters"]["checkpointSemanticInputs"]=named
    require(j.dimensions()=={"sourceSectors":[170,918,2295,2805],
                             "targetSectors":[20,135,450,990,1485,1287]},
            "All original source/target strata sizes")
    co,Q=physical_cochains(m,j,blocks)
    result["parameters"]["all990x7PaidLambda4ThreeEntriesZero"]=m.matrix_zero(co[4][3])
    result["parameters"]["all990x7PaidLambda5ThreeEntriesZero"]=m.matrix_zero(co[5][3])
    guard(a,"original coefficients through sixth order")
    coeff=j.original_coefficients(m,"zero",6)
    for key,value in md["originalPhysicalHashesThroughOrder5"].items():
        require(coeff["physical"].get(key)==value,
                "All paid physical coefficients through order5: "+key)
    result["parameters"].update({
        "allPaidPhysicalHashesThroughOrder5Verified":True,
        "originalPhysicalHashesThroughOrder6":coeff["physical"],
        "all17PureOriginalCoefficientsThroughOrder6Verified":True,
        "all6188OriginalSourcesRetained":True,
        "all4367TargetCoordinatesRetainedModuloExact20PureKernel":True,
        "newOriginalCoefficientOrder":6,
    })
    parts,meta=new_residuals(m,j,a,coeff,co,binding,result)
    for key in ("lowResidualSHA256","middleResidualSHA256","topResidualSHA256",
                "topSeed2Lambda4ThreeIdentityVerified","topSixthResidualIsExactlyZero"):
        result["parameters"][key]=meta[key]
    if a.through=="residual":
        result["status"]="stage-completed";return
    top,topmeta=top_kernel(m,j,a,coeff,parts[2],binding,result)
    if a.through=="top":
        result["status"]="stage-completed";return
    middle,midmeta=middle_kernel(m,j,a,coeff,parts[1],top,binding,result)
    if a.through=="middle":
        result["status"]="stage-completed";return
    low,lowmeta=low_kernel(m,j,a,coeff,parts[0],middle,Q,binding,result)
    final_family(m,j,a,coeff,co,Q,parts,middle,low,binding,result)

def main():
    p=argparse.ArgumentParser()
    for name in ("generator","jet-actions","cochain-exporter","cochain-manifest",
                 "cochain-receipt","fifth-receipt","checkpoint-dir","out"):
        p.add_argument("--"+name,required=True)
    p.add_argument("--through",choices=("residual","top","middle","final"),default="final")
    p.add_argument("--remaining-seconds",type=float,default=30.0)
    p.add_argument("--memory-mib",type=int,default=2048)
    a=p.parse_args()
    require(a.remaining_seconds>0,"Positive actual shared time")
    require(512<=a.memory_mib<=2048,"Explicit512..2048MiB caller limit")
    resource.setrlimit(resource.RLIMIT_AS,(a.memory_mib*1024**2,a.memory_mib*1024**2))
    started=time.monotonic();a._deadline=started+a.remaining_seconds
    result={"format":"r150-zero-sixth-full-source-left-envelope-v1",
            "status":"started","arithmetic":"exact rational python-flint",
            "scriptSHA256":sha(__file__),"parameters":{
                "sharedSeconds":a.remaining_seconds,"memoryMiB":a.memory_mib,
                "through":a.through,"naturalParameter":"s",
                "sourceStrata":[170,918,2295,2805],
                "newTopMatrixShape":[2805,2779],
                "checkpointDirectory":str(Path(a.checkpoint_dir)),
                "temporaryOnly":True,"largeDataUploadedOrCommitted":False,
                "firstConnectionExactRankNotAssumed":True,
                "sourceMultiplierTransport":
                    "m_j=sum_(k<=j)binom(j,k)s^(j-k)n_k on ALL degree<=3 multipliers",
                "targetLeftTransport":"A_new=T A_old V; lambda_old=T^T lambda_new",
                "nativeRrefInplace":True,"noUnverifiedCandidateCounted":True,
            }}
    signal.signal(signal.SIGALRM,request_stop)
    signal.signal(signal.SIGTERM,request_stop)
    signal.setitimer(signal.ITIMER_REAL,a.remaining_seconds)
    try:
        run(a,result)
    except SafeStop as exc:
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
        raw=json.dumps(result,sort_keys=True,indent=2).encode("utf-8")
        require(len(raw)<100000,"Small sixth receipt limit")
        path=Path(a.out);path.parent.mkdir(parents=True,exist_ok=True)
        tmp=path.with_name(path.name+".tmp");tmp.write_bytes(raw);os.replace(tmp,path)
        print(json.dumps({"status":result["status"],"receipt":str(path),
                          "receiptBytes":len(raw),"receiptSHA256":hashlib.sha256(raw).hexdigest(),
                          "elapsedSeconds":result["elapsedSeconds"],
                          "independentSixthLeadingCount":result.get("independentSixthLeadingCount"),
                          "fullZeroMaximalMinorOrderLowerBound":result.get("fullZeroMaximalMinorOrderLowerBound"),
                          "fullZeroSubmaximalMinorOrderLowerBound":result.get("fullZeroSubmaximalMinorOrderLowerBound")},
                         sort_keys=True),flush=True)

if __name__=="__main__":
    main()
