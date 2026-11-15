#!/usr/bin/env python3
"""Full zero fourth connection after the actual complete-third reconnection.

Every complete third head is retained.  The incoming image is exactly
im(M0)+M1 K0+R3(K2), because the full second connection is zero.
A coefficient of R3 is transported by s times its ACTUAL second cochain,
not by changing only the last correction.  Pure exact heads are retained.
No full inverse, old RREF, top/middle solve, or original normal form is repeated.

This entry handles the verified homogeneous-high branch.  If the NEW R4
has a nonzero high row, it saves all6188 rows and stops with no rank claim.
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
REUSE_SHA="b46ca6a4fc594b53687d692986229edc97ca770e21ac6332703eaf998c9e0b67"
THIRD_SOURCE_SHA="180b7f6c3a4d3c9ff560b9f9e4a590af04d00996abcba75cfeb35c1778272156"
THIRD_RECEIPT_SHA="a9c26663f6761fd68f911f6fe506410dd13efcf5ce440191f1a03c4bdcf8d7b6"
THIRD_MANIFEST_SHA="9a50e9509bfd33d4b9de7460ae929d9adbdef6abbb9b38f9ae89a2efe7ddd3f0"
THIRD_BINDING="3610d8e38d27934108c32a13e01b87c70c3e6e449c1a7d122abb442b6a60a97e"
PAID_FORMAT="r150-zero-complete-third-full-high-temporary-v1"
FORMAT="r150-zero-complete-fourth-full-incoming-temporary-v1"

def req(ok,msg):
    if not ok: raise AssertionError(msg)

def sha(path):
    h=hashlib.sha256()
    with Path(path).open("rb") as f:
        for block in iter(lambda:f.read(1048576),b""): h.update(block)
    return h.hexdigest()

def small_hash(x):
    return hashlib.sha256(json.dumps(x,sort_keys=True,separators=(",",":")).encode()).hexdigest()

def module_at(name,path):
    import importlib.util
    s=importlib.util.spec_from_file_location(name,path)
    m=importlib.util.module_from_spec(s);s.loader.exec_module(m)
    return m

def load_paid(d,m,a,manifest,paid,phase,result):
    e=manifest["phases"][phase]
    req(e["verified"] and {k:v for k,v in e.items() if k!="file"}==
        paid["checkpointPhases"][phase],"Actual completed third phase "+phase)
    directory=Path(a.third_checkpoint_dir)
    file=directory/e["file"]
    req(file.parent==directory and file.stat().st_size==e["bytes"]
        and sha(file)==e["sha256"],"Actual temporary source bytes "+phase)
    q=d.read_json(file)
    req(q["format"]==PAID_FORMAT and q["binding"]==manifest["binding"]
        and q["phase"]==phase and q["shape"]==e["shape"] and q["verified"],
        "Actual temporary third phase provenance "+phase)
    nr,nc=q["shape"]
    req(len(q["matrix"])==nr and all(len(r)==nc for r in q["matrix"]),
        "All temporary matrix entries "+phase)
    M=m.fmpq_mat(nr,nc,[m.fmpq(v) for row in q["matrix"] for v in row])
    req(m.matrix_hash(M)==q["matrixSHA256"]==e["matrixSHA256"],
        "Actual temporary third logical matrix "+phase)
    result["parameters"].setdefault("actualThirdInputs",{})[phase]={
        k:v for k,v in e.items() if k!="file"}
    return M,q["metadata"]

def append_zero(m,X,count):
    return m.fmpq_mat(X.nrows(),X.ncols()+count,
        [X[i,c] if c<X.ncols() else m.fmpq(0)
         for i in range(X.nrows()) for c in range(X.ncols()+count)])

def add_section(m,section,degree,X):
    if degree in section: section[degree]+=X
    else: section[degree]=X

def original_residual(d,m,j,c3,a,binding,coeff,co,r,result):
    phase="all-complete-third-head-fourth-residuals"
    old=d.load_matrix(m,a,binding,phase,result)
    if old is None:
        R=m.fmpq_mat(6188,r)
        for k in range(4):
            d.guard(a,"Original fourth coefficient term "+str(k),1.0)
            sections={sr:m.submatrix(X,range(X.nrows()),range(r))
                      for sr,X in co[k].items()}
            R+=c3.all_rows(m,j,coeff,4-k,sections,r)
        high=m.submatrix(R,range(1088,6188),range(r))
        zero=m.matrix_zero(high)
        meta={"all6188OriginalSourceRowsRetained":True,
              "fullThirdHeadsNotFixedOldRepresentativeSubset":True,
              "originalPhysicalHashes":coeff["physical"],
              "all5100HighRowsActuallyZero":zero,
              "highResidualSHA256":m.matrix_hash(high),
              "leadingColumns":r}
        if not zero:
            meta["firstNonzeroHighRows"]=[]
            for i in range(5100):
                if any(high[i,c] for c in range(r)):
                    meta["firstNonzeroHighRows"].append(1088+i)
                    if len(meta["firstNonzeroHighRows"])==16: break
        d.save_matrix(m,a,binding,phase,R,meta,result,True)
    else:
        R,meta,verified=old
        req(verified and [R.nrows(),R.ncols()]==[6188,r]
            and meta["originalPhysicalHashes"]==coeff["physical"]
            and meta["all6188OriginalSourceRowsRetained"],
            "Actual complete original fourth residual checkpoint")
    result["parameters"]["fourthOriginalResidualSHA256"]=m.matrix_hash(R)
    result["parameters"]["all5100NewHighRowsActuallyZero"]=meta["all5100HighRowsActuallyZero"]
    return R,meta

def seed_old_unit_columns(d,m,w,a,binding,prefix,B,C,oldC,oldX,constants,result):
    for suffix,(X,meta) in constants.items():
        w.adopt(d,m,a,binding,prefix+"-"+suffix,X,meta,result)
    U,umeta=constants["unit"];I=umeta["rows"]
    req(m.submatrix(C,range(1088),range(15))==oldC,
        "All15 previous complete incoming columns retained verbatim")
    bsha=m.matrix_hash(B);csha=m.matrix_hash(C);usha=m.matrix_hash(U)
    for c in range(15):
        X=m.submatrix(oldX,range(582),[c])
        req(m.matrix_zero(U*X+m.submatrix(oldC,I,[c])),
            "All582 original inherited unit rows "+str(c))
        phase=prefix+"-rhs-column-%04d"%c
        meta={"column":c,"constantSHA256":bsha,"rhsSHA256":csha,"unitSHA256":usha,
              "allOriginalUnitRowsVerified":True,"originalUnitProductCoordinates":582,
              "algorithm":"same-actual-paid-column","nativeSeconds":0.0,"nativeSolveUsed":False}
        old=d.load_matrix(m,a,binding,phase,result)
        if old is None: d.save_matrix(m,a,binding,phase,X,meta,result,True)
        else:
            Y,ymeta,verified=old
            req(verified and Y==X and ymeta==meta,"Same saved actual unit column "+str(c))

def run(d,m,j,u,w,c3,a,result):
    req(sha(a.third_receipt)==a.third_receipt_sha256==THIRD_RECEIPT_SHA,
        "Actual third small receipt bytes")
    outer=d.read_json(a.third_receipt)
    req(outer["exitCode"]==0 and outer["result"]["status"]=="completed",
        "Actual complete third result")
    actual=outer["result"];paid=actual["parameters"]
    req(actual["scriptSHA256"]==THIRD_SOURCE_SHA
        and actual["format"]=="r150-zero-complete-third-reused-full-high-v1"
        and paid["fullThirdConnectionNotMerelyEnvelope"]
        and paid["allFourOrdersAll6188RowsVerified"]
        and paid["all23PaidSecondHeadsRestored"]
        and paid["exactFirstConnectionRank"]==4 and paid["exactSecondConnectionRank"]==0,
        "Actual full third provenance")
    b3=paid["fullZeroThirdConnectionRank"];heads=paid["fullThirdLeadingDimension"]
    req(b3 in (0,1) and heads==23-b3,"Actual full third dimensions")
    r=heads-10
    mp=Path(a.third_checkpoint_dir)/"sixth-checkpoint.json"
    req(mp.stat().st_size==paid["checkpointManifestBytes"]
        and sha(mp)==paid["checkpointManifestSHA256"]==THIRD_MANIFEST_SHA,
        "Actual third manifest bytes")
    man=d.read_json(mp)
    req(man["format"]==PAID_FORMAT and man["binding"]==paid["checkpointBinding"]==THIRD_BINDING,
        "Actual third manifest binding")
    inputs={"script":sha(__file__),"thirdReceipt":a.third_receipt_sha256,
            "thirdManifest":sha(mp),"thirdSource":THIRD_SOURCE_SHA,"parent":PARENT_SHA,
            "first":FIRST_SHA,"actions":ACTIONS_SHA,"unitHelper":HELPER_SHA,"reuse":REUSE_SHA}
    binding=small_hash(inputs)
    result["parameters"].update({"checkpointBinding":binding,"checkpointSemanticInputs":inputs,
        "actualFullThirdRank":b3,"actualFullThirdHeads":heads,
        "actualNonexactThirdHeads":r,"completeFourthIncoming":"im(M0)+M1K0+R3(K2)",
        "earlierZeroHeadImagesPaidByCompleteBeta2Zero":True})
    coeff=j.original_coefficients(m,"zero",4)
    for key,val in paid["originalPhysicalHashesThroughOrder3"].items():
        req(coeff["physical"].get(key)==val,"Same actual original coefficient "+key)
    result["parameters"]["originalPhysicalHashesThroughOrder4"]=coeff["physical"]

    P2,p2meta=load_paid(d,m,a,man,paid,"complete-paid-second-cochains",result)
    req([P2.nrows(),P2.ncols()]==[875,23] and p2meta["allThreeOrdersAll6188RowsVerified"],
        "All actual23 second cochains")
    co2=c3.unpack_sections(m,P2,p2meta["ranges"],2);del P2
    P3,p3meta=load_paid(d,m,a,man,paid,"complete-full-third-cochains",result)
    req([P3.nrows(),P3.ncols()]==[5222,heads]
        and p3meta["allFourOrdersAll6188RowsVerified"]
        and p3meta["exactThirdConnectionRank"]==b3,
        "All actual full third cochains")
    co3=c3.unpack_sections(m,P3,p3meta["ranges"],3);del P3
    for k in range(1,4):
        for X in co3[k].values():
            req(m.matrix_zero(m.submatrix(X,range(X.nrows()),range(r,heads))),
                "Last10 are actual exact-pure columns")
    exact={sr:m.submatrix(X,range(X.nrows()),range(r,heads)) for sr,X in co3[0].items()}
    req(m.matrix_zero(c3.all_rows(m,j,coeff,4,exact,10)),
        "New original fourth coefficient on exact-pure heads")
    R4,rmeta=original_residual(d,m,j,c3,a,binding,coeff,co3,r,result)
    if not rmeta["all5100HighRowsActuallyZero"]:
        result["status"]="stage-completed"
        result["parameters"]["newNonzeroHighForcingNeedsCompleteLift"]=True
        result["parameters"]["noFourthConnectionRankClaimed"]=True
        return
    if a.through=="residual":
        result["status"]="stage-completed";return

    H,hmeta=load_paid(d,m,a,man,paid,"complete-paid-high-homogeneous",result)
    req([H.nrows(),H.ncols()]==[3771,2] and hmeta["all5100OriginalHighRowsVerified"]
        and hmeta["completeByPaidKernelZeroHeadFiber"],"Complete original high kernel")
    Nh=m.submatrix(H,range(3762),range(2));del H
    high_section={3:m.submatrix(Nh,range(990),range(2)),
                  4:m.submatrix(Nh,range(990,2475),range(2)),
                  5:m.submatrix(Nh,range(2475,3762),range(2))}
    Ch=c3.low(m,j,coeff,0,high_section,2)
    R3,r3meta=load_paid(d,m,a,man,paid,"all-thirteen-original-third-residuals",result)
    req([R3.nrows(),R3.ncols()]==[6188,13] and r3meta["all5100HighRowsActuallyZero"]
        and m.matrix_zero(m.submatrix(R3,range(1088,6188),range(13))),
        "All13 actual complete lower-page incoming residuals")
    oldC=m.join_columns(Ch,m.submatrix(R3,range(1088),range(13)))
    C=m.join_columns(oldC,m.submatrix(R4,range(1088),range(r)))
    P0=j.block(m,coeff,0,0,1);Q,rank,_,_=m.nullspace(P0)
    req(rank==128 and Q.ncols()==7,"Same actual constant Q7")
    J0=j.join_vertical(m,[m.join_columns(j.block(m,coeff,0,sr,1),
                                         j.block(m,coeff,0,sr,2)) for sr in (0,1)])
    B=m.join_columns(J0,c3.low(m,j,coeff,1,{1:Q},7))
    constants={}
    for suffix in ("constant-kernel","unit","primitive-unit"):
        M,meta=load_paid(d,m,a,man,paid,"complete-third-unit-"+suffix,result)
        if suffix!="primitive-unit":
            req(meta["constantSHA256"]==m.matrix_hash(B),"Same original B592")
        constants[suffix]=(M,meta)
    oldX,xmeta=load_paid(d,m,a,man,paid,"complete-third-unit-unit-rhs-solution",result)
    req([oldX.nrows(),oldX.ncols()]==[582,15]
        and xmeta["constantSHA256"]==m.matrix_hash(B)
        and xmeta["rhsSHA256"]==m.matrix_hash(oldC)
        and xmeta["allOriginalUnitRHSRowsVerified"],
        "Actual all15 old incoming unit solutions")
    prefix="complete-fourth-unit"
    seed_old_unit_columns(d,m,w,a,binding,prefix,B,C,oldC,oldX,constants,result)
    del oldX
    K,kmeta=u.complete_kernel(d,m,j,a,binding,prefix,B,C,582,result)
    req(K.nrows()==607+r,"Every original correction/incoming/new head retained")
    Sch,sm,sv=d.load_matrix(m,a,binding,prefix+"-full-schur",result)
    req(sv and sm["allOriginalRowsRetained"],"All1088 full original fourth Schur rows")
    _,incoming_rank=m.submatrix(Sch,range(1088),range(15)).rref()
    req(incoming_rank==2+b3,"Full incoming rank agrees with actual complete third")
    chosen,Z,r4heads=c3.head_basis(m,K,607,r)
    b4=r-r4heads
    req(K.ncols()-r4heads==heads
        and b4==kmeta["rank"]-(584+b3) and 0<=b4<=4-b3,
        "Complete fourth rank, normalized zero-head fiber, paid older bound")
    Hprev=m.fmpq_mat(heads,r4heads+10)
    for i in range(r):
        for c in range(r4heads): Hprev[i,c]=Z[i,c]
    for c in range(10): Hprev[r+c,r4heads+c]=1
    co=[{sr:X*Hprev for sr,X in sec.items()} for sec in co3]
    Y=m.submatrix(chosen,range(594,607),range(r4heads))
    Yfull=append_zero(m,Y,10)
    for k in range(3):
        for sr,X in co2[k].items():
            part=m.submatrix(X,range(X.nrows()),range(13))*Yfull
            add_section(m,co[k+1],sr,part)
    b=m.submatrix(chosen,range(585,592),range(r4heads))
    add_section(m,co[3],1,append_zero(m,Q*b,10))
    high=Nh*m.submatrix(chosen,range(592,594),range(r4heads))
    lo=m.submatrix(chosen,range(585),range(r4heads))
    fourth={1:m.submatrix(lo,range(135),range(r4heads)),
            2:m.submatrix(lo,range(135,585),range(r4heads)),
            3:m.submatrix(high,range(990),range(r4heads)),
            4:m.submatrix(high,range(990,2475),range(r4heads)),
            5:m.submatrix(high,range(2475,3762),range(r4heads))}
    co.append({sr:append_zero(m,X,10) for sr,X in fourth.items()})
    c3.check_jets(m,j,coeff,co,4,r4heads+10)
    _,headrank=j.join_vertical(m,[co[0][0],co[0][1]]).rref()
    req(headrank==heads-b4==r4heads+10,"Independent FULL fourth head space")
    pack,ranges=c3.pack_sections(m,j,co)
    target=c3.square_readouts(m,j,co)
    meta={"chart":"zero","parameter":"s","order":4,"leadingColumns":headrank,
          "ranges":ranges,"completeSecondHeads":23,"completeThirdHeads":heads,
          "completeFourthHeads":headrank,"fullThirdConnectionRank":b3,
          "fullFourthConnectionRank":b4,"allFiveOrdersAll6188RowsVerified":True,
          "allEarlierCochainImagesRetained":True,
          "exactIncomingImage":"im(M0)+M1K0+R3(K2)",
          "actualSecondCochainShiftAppliedToLambda1Lambda2Lambda3":True,
          "nextPageIncoming":"im(M0)+M1K0+all13 R3+all current R4; shifts of saved actual second and third cochains",
          "actualFourthHeadInFullThirdBasis":[[str(Hprev[i,c]) for c in range(headrank)] for i in range(heads)],
          "actualThirdIncomingCoefficients":[[str(Yfull[i,c]) for c in range(headrank)] for i in range(13)],
          "targetSquareReadouts":target,"temporaryOnly":True}
    d.save_matrix(m,a,binding,"complete-full-fourth-cochains",pack,meta,result,True)
    delta=63-2*b3-b4;subdelta=54-2*b3-b4
    result.update({"status":"completed","fullZeroThirdConnectionRank":b3,
                   "fullZeroFourthConnectionRank":b4,"fullFourthLeadingDimension":headrank,
                   "fullZeroMaximalMinorOrderLowerBound":delta,
                   "fullZeroSubmaximalMinorOrderLowerBound":subdelta})
    result["parameters"].update({
        "completeLowShape":[1088,607+r],"completeLowRank":kmeta["rank"],
        "completeLowKernelDimension":K.ncols(),"normalizedCompleteZeroHeadFiberDimension":heads,
        "fullIncomingRankAfterConstantHighElimination":584+b3,
        "fullZeroFirstConnectionRank":4,"fullZeroSecondConnectionRank":0,
        "fullZeroThirdConnectionRank":b3,"fullZeroFourthConnectionRank":b4,
        "all6188OriginalSourcesRetained":True,"allFiveOrdersAll6188RowsVerified":True,
        "fullFourthConnectionNotMerelyFixedRepresentativeEnvelope":True,
        "allEarlierCochainImagesRetained":True,"actualSecondShiftAppliedToAllThreeCoefficients":True,
        "fullFourthLeadingDimension":headrank,"wholeCochainShape":[pack.nrows(),pack.ncols()],
        "wholeCochainSHA256":m.matrix_hash(pack),"wholeCochainRanges":ranges,
        "actualFourthHeadInFullThirdBasis":meta["actualFourthHeadInFullThirdBasis"],
        "actualThirdIncomingCoefficients":meta["actualThirdIncomingCoefficients"],
        "targetSquareReadouts":target,"fullZeroMaximalMinorOrderLowerBound":delta,
        "fullZeroSubmaximalMinorOrderLowerBound":subdelta,
        "currentFactorDegreeLowerBound":delta+46,
        "nextPageNeedsCompleteThirdAndFourthIncoming":True,
        "noOldRrefOrHighSolveRepeated":True,"noCompleteInverseConstructed":True,
        "newFinalOriginalProductCoordinates":5*6188*headrank,"fullTargetMembershipNotClaimed":True})

def main():
    p=argparse.ArgumentParser()
    for name in ("parent-driver","unit-schur-helper","reused-driver","complete-third-driver",
                 "generator","jet-actions","third-receipt","third-receipt-sha256",
                 "third-checkpoint-dir","checkpoint-dir","out"):
        p.add_argument("--"+name,required=True)
    p.add_argument("--through",choices=("residual","final"),default="final")
    p.add_argument("--remaining-seconds",type=float,default=180.0)
    p.add_argument("--memory-mib",type=int,default=2048)
    p.add_argument("--unit-algorithm",choices=("dixon","fflu"),default="dixon")
    p.add_argument("--unit-batch-columns",type=int,choices=(1,2),default=1)
    p.add_argument("--max-new-unit-groups",type=int,default=64)
    a=p.parse_args()
    req(a.remaining_seconds>0 and 512<=a.memory_mib<=8192 and a.max_new_unit_groups>0,
        "Explicit shared bounded resources")
    req(len(a.third_receipt_sha256)==64 and all(c in "0123456789abcdef" for c in a.third_receipt_sha256),
        "Actual immutable third outer receipt SHA")
    for path,want in ((a.parent_driver,PARENT_SHA),(a.unit_schur_helper,HELPER_SHA),
                      (a.reused_driver,REUSE_SHA),(a.complete_third_driver,THIRD_SOURCE_SHA),
                      (a.generator,FIRST_SHA),(a.jet_actions,ACTIONS_SHA)):
        req(sha(path)==want,"Pinned source dependency "+str(path))
    req(Path(a.checkpoint_dir).resolve()!=Path(a.third_checkpoint_dir).resolve(),
        "New checkpoint distinct from actual third")
    resource.setrlimit(resource.RLIMIT_AS,(a.memory_mib*1024**2,a.memory_mib*1024**2))
    d=module_at("r150_complete4_storage",a.parent_driver)
    m=module_at("r150_complete4_generator",a.generator)
    j=module_at("r150_complete4_actions",a.jet_actions)
    u=module_at("r150_complete4_rhs_unit",a.unit_schur_helper)
    w=module_at("r150_complete4_paid_reuse",a.reused_driver)
    c3=module_at("r150_complete4_previous",a.complete_third_driver)
    d.FORMAT=FORMAT
    started=time.monotonic();a._deadline=started+a.remaining_seconds
    result={"format":"r150-zero-complete-fourth-full-incoming-v1","status":"started",
        "arithmetic":"exact rational python-flint","scriptSHA256":sha(__file__),
        "parameters":{"naturalParameter":"s","sharedSeconds":a.remaining_seconds,
          "memoryMiB":a.memory_mib,"through":a.through,
          "checkpointDirectory":str(Path(a.checkpoint_dir)),"paidDirectoryReadOnly":True,
          "sourceStrata":[170,918,2295,2805],"all6188OriginalSourcesRetained":True,
          "sourceMultiplierTransport":"all degree<=3 original multipliers under exact co-moving moment translation",
          "targetLeftTransport":"A_new=T A_old V; lambda_old=T^T lambda_new",
          "temporaryOnly":True,"largeDataUploadedOrCommitted":False}}
    signal.signal(signal.SIGALRM,d.request_stop);signal.signal(signal.SIGTERM,d.request_stop)
    signal.setitimer(signal.ITIMER_REAL,a.remaining_seconds)
    try:
        run(d,m,j,u,w,c3,a,result)
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
        raw=json.dumps(result,sort_keys=True,indent=2).encode()
        req(len(raw)<100000,"Small permanent receipt only")
        out=Path(a.out);out.parent.mkdir(parents=True,exist_ok=True)
        tmp=out.with_name(out.name+".tmp");tmp.write_bytes(raw);os.replace(tmp,out)
        print(json.dumps({"status":result["status"],"receipt":str(out),
            "receiptBytes":len(raw),"receiptSHA256":hashlib.sha256(raw).hexdigest(),
            "elapsedSeconds":result["elapsedSeconds"],
            "fullZeroFourthConnectionRank":result.get("fullZeroFourthConnectionRank"),
            "fullFourthLeadingDimension":result.get("fullFourthLeadingDimension")},sort_keys=True),flush=True)

if __name__=="__main__":
    main()
