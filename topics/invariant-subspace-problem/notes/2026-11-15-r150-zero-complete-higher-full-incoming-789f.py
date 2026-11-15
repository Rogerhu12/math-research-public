#!/usr/bin/env python3
"""R150 full zero higher connection with ALL earlier cochain incoming images.

Concrete next use: order5, paid full third=1 and fourth=3.
All earlier R_j(K_(j-1)) are kept, not merely the last M1Q ambiguity.
A coefficient of R_j shifts its actual cochain by s^(order-j).
Every final coefficient is checked on all6188 original sources.

Only the verified homogeneous-high branch is solved here.  A new nonzero
high residual is saved and reported without any connection rank claim.
The paid582 unit and ALL old actual RHS solutions are reused; no full
inverse or old large RREF is reconstructed.  Large arrays are job-temporary.
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
ACTIONS_SHA="2ebf418575df39ca2ed0a2165a37e92071c415b4734969c5bedc64e0b9ef4332"
PARENT_SHA="a6c423b98d70e06fb5a28797f09a11300129ec59128921c1e2d5c0e54fa8b5f2"
HELPER_SHA="36356983e71ee1e67677da1a7a5f7aebf2987db282a5447a741b6a6af93084d5"
REUSE_SHA="b46ca6a4fc594b53687d692986229edc97ca770e21ac6332703eaf998c9e0b67"
THIRD_SOURCE_SHA="180b7f6c3a4d3c9ff560b9f9e4a590af04d00996abcba75cfeb35c1778272156"
FOURTH_SOURCE_SHA="18e21310a161b3fca3b61df8d263e549e1230a4c8ef90c971c8c4b00082c0642"
FORMAT="r150-zero-complete-higher-full-incoming-temporary-v1"
RESULT_FORMAT="r150-zero-complete-higher-full-incoming-v1"
KNOWN={
 3:{"receiptSHA256":"a9c26663f6761fd68f911f6fe506410dd13efcf5ce440191f1a03c4bdcf8d7b6",
    "sourceSHA256":THIRD_SOURCE_SHA,
    "manifestSHA256":"9a50e9509bfd33d4b9de7460ae929d9adbdef6abbb9b38f9ae89a2efe7ddd3f0",
    "binding":"3610d8e38d27934108c32a13e01b87c70c3e6e449c1a7d122abb442b6a60a97e",
    "checkpointFormat":"r150-zero-complete-third-full-high-temporary-v1",
    "resultFormat":"r150-zero-complete-third-reused-full-high-v1",
    "cochainPhase":"complete-full-third-cochains",
    "residualPhase":"all-thirteen-original-third-residuals",
    "unitPrefix":"complete-third-unit","rankKey":"fullZeroThirdConnectionRank",
    "headKey":"fullThirdLeadingDimension","physicalKey":"originalPhysicalHashesThroughOrder3"},
 4:{"receiptSHA256":"28cdc32d3c8deb1b67603b7641125ae59f22e20cdc5767238f42510479d25efa",
    "sourceSHA256":FOURTH_SOURCE_SHA,
    "manifestSHA256":"e7a78ace79b3a0d9c4a1fca9651ead13c72004d103b7bb4e021f14021734d652",
    "binding":"8aaae7863723dfe75a63d33ee545e8d4e07896e8e12632c542291c81eea2827d",
    "checkpointFormat":"r150-zero-complete-fourth-full-incoming-temporary-v1",
    "resultFormat":"r150-zero-complete-fourth-full-incoming-v1",
    "cochainPhase":"complete-full-fourth-cochains",
    "residualPhase":"all-complete-third-head-fourth-residuals",
    "unitPrefix":"complete-fourth-unit","rankKey":"fullZeroFourthConnectionRank",
    "headKey":"fullFourthLeadingDimension","physicalKey":"originalPhysicalHashesThroughOrder4"}
}
OLD_CUMULATIVE={1:4,2:4,3:5,4:8,5:10,6:12,7:12,8:13}

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

def append_zero(m,X,count):
    return m.fmpq_mat(X.nrows(),X.ncols()+count,
        [X[i,c] if c<X.ncols() else m.fmpq(0)
         for i in range(X.nrows()) for c in range(X.ncols()+count)])

def add_section(section,degree,X):
    if degree in section: section[degree]+=X
    else: section[degree]=X

def joined(m,matrices):
    req(bool(matrices),"Nonempty actual matrix list")
    X=matrices[0]
    for Y in matrices[1:]: X=m.join_columns(X,Y)
    return X

def describe_known(order,selfsha):
    if order in KNOWN: return dict(KNOWN[order])
    return {"sourceSHA256":selfsha,"checkpointFormat":FORMAT,"resultFormat":RESULT_FORMAT,
            "cochainPhase":"complete-order-"+str(order)+"-cochains",
            "residualPhase":"all-complete-order-"+str(order)+"-residuals",
            "unitPrefix":"complete-order-"+str(order)+"-unit",
            "rankKey":"fullConnectionRank","headKey":"fullLeadingDimension",
            "physicalKey":"originalPhysicalHashes"}

def records(d,a,result):
    req(len(a.paid_stage)==a.order-3,"Exactly all original paid stages")
    rows={}
    for order_text,path,want,directory in a.paid_stage:
        order=int(order_text)
        req(order not in rows and 3<=order<a.order,"Paid stage order and uniqueness")
        req(len(want)==64 and all(c in "0123456789abcdef" for c in want),"Actual receipt SHA")
        req(sha(path)==want,"Actual completed stage small receipt "+str(order))
        cfg=describe_known(order,sha(__file__))
        if "receiptSHA256" in cfg: req(want==cfg["receiptSHA256"],"Pinned original third/fourth outer")
        o=d.read_json(path)
        req(o["exitCode"]==0 and o["result"]["status"]=="completed","Actual completed full stage")
        actual=o["result"];p=actual["parameters"]
        req(actual["scriptSHA256"]==cfg["sourceSHA256"] and actual["format"]==cfg["resultFormat"],
            "Exact full-stage implementation")
        if order==3:
            req(p["fullThirdConnectionNotMerelyEnvelope"] and p["allFourOrdersAll6188RowsVerified"]
                and p["exactFirstConnectionRank"]==4 and p["exactSecondConnectionRank"]==0,
                "Actual complete third")
        elif order==4:
            req(p["fullFourthConnectionNotMerelyFixedRepresentativeEnvelope"]
                and p["allFiveOrdersAll6188RowsVerified"] and p["allEarlierCochainImagesRetained"],
                "Actual complete fourth")
        else:
            req(p["completeOrder"]==order and p["fullConnectionNotMerelyEnvelope"]
                and p["allOriginalOrdersAndSourcesVerified"] and p["allEarlierCochainImagesRetained"],
                "Actual complete previous higher order")
        mp=Path(directory)/"sixth-checkpoint.json"
        req(mp.stat().st_size==p["checkpointManifestBytes"]
            and sha(mp)==p["checkpointManifestSHA256"],"Actual stage manifest")
        man=d.read_json(mp)
        req(man["format"]==cfg["checkpointFormat"] and man["binding"]==p["checkpointBinding"],
            "Actual checkpoint format/binding")
        for key,actual_value in (("manifestSHA256",sha(mp)),("binding",man["binding"])):
            if key in cfg: req(cfg[key]==actual_value,"Pinned original checkpoint "+key)
        rows[order]={"order":order,"receiptSHA256":want,"directory":directory,"actual":actual,
            "parameters":p,"manifest":man,"manifestSHA256":sha(mp),"config":cfg,
            "rank":p[cfg["rankKey"]],"heads":p[cfg["headKey"]]}
    req(sorted(rows)==list(range(3,a.order)),"No missing complete incoming stage")
    ranks={1:4,2:0}
    identities=[]
    for order in sorted(rows):
        r=rows[order];ranks[order]=r["rank"]
        req(r["rank"]>=0 and r["heads"]==27-sum(ranks.values()) and r["heads"]>=13,
            "Complete head/rank count")
        if order>=5:
            paid={int(k):v for k,v in r["parameters"]["fullConnectionRanks"].items()}
            req(paid==ranks,"All exact previous connection ranks agree")
            prior=r["parameters"]["priorReceiptIdentities"]
            req(prior==identities,"All original prior cochains kept in the same ancestry")
        identities.append({"order":order,"receiptSHA256":r["receiptSHA256"],
            "manifestSHA256":r["manifestSHA256"],"sourceSHA256":r["config"]["sourceSHA256"],
            "binding":r["manifest"]["binding"]})
    result["parameters"]["priorReceiptIdentities"]=identities
    return rows,ranks

def load_paid(d,m,record,phase,result):
    p=record["parameters"];man=record["manifest"];cfg=record["config"]
    e=man["phases"][phase]
    req(e["verified"] and {k:v for k,v in e.items() if k!="file"}==p["checkpointPhases"][phase],
        "Actual completed phase "+str(record["order"])+":"+phase)
    directory=Path(record["directory"]);file=directory/e["file"]
    req(file.parent==directory and file.stat().st_size==e["bytes"] and sha(file)==e["sha256"],
        "Full temporary source bytes")
    q=d.read_json(file)
    req(q["format"]==cfg["checkpointFormat"] and q["binding"]==man["binding"]
        and q["phase"]==phase and q["shape"]==e["shape"] and q["verified"],
        "Exact full temporary source provenance")
    nr,nc=q["shape"]
    req(len(q["matrix"])==nr and all(len(r)==nc for r in q["matrix"]),"All source matrix entries")
    M=m.fmpq_mat(nr,nc,[m.fmpq(v) for row in q["matrix"] for v in row])
    req(m.matrix_hash(M)==q["matrixSHA256"]==e["matrixSHA256"],"Actual logical source matrix")
    result["parameters"].setdefault("actualPaidInputs",{})[str(record["order"])+":"+phase]={
        k:v for k,v in e.items() if k!="file"}
    return M,q["metadata"]

def compact_squares(m,j,co):
    index={v:i for i,v in enumerate(j.target_columns(2))}
    nc=next(iter(co[0].values())).ncols();out={}
    for k,section in enumerate(co):
        X=section.get(2)
        R=(m.fmpq_mat(9,nc) if X is None else
           m.fmpq_mat(9,nc,[X[index[(0,0,(i,i))],c]
                            for i in range(2,11) for c in range(nc)]))
        entry={"shape":[9,nc],"matrixSHA256":m.matrix_hash(R),"allEntriesZero":m.matrix_zero(R)}
        if not entry["allEntriesZero"]:
            for i in range(9):
                for c in range(nc):
                    if R[i,c]:
                        value=str(R[i,c]);hit={"target":i+2,"headColumn":c}
                        if len(value)<=1500: hit["value"]=value
                        else: hit["valueSHA256"]=hashlib.sha256(value.encode()).hexdigest()
                        entry["firstNonzero"]=hit;break
                if "firstNonzero" in entry: break
        out["lambda"+str(k)]=entry
    return out

def residual(d,m,j,c3,a,binding,coeff,co,n,result):
    phase="all-complete-order-"+str(a.order)+"-residuals"
    old=d.load_matrix(m,a,binding,phase,result)
    if old is None:
        R=m.fmpq_mat(6188,n)
        for k in range(a.order):
            d.guard(a,"New original residual term "+str(k),1.0)
            section={sr:m.submatrix(X,range(X.nrows()),range(n)) for sr,X in co[k].items()}
            R+=c3.all_rows(m,j,coeff,a.order-k,section,n)
        H=m.submatrix(R,range(1088,6188),range(n));highzero=m.matrix_zero(H)
        meta={"order":a.order,"fullPreviousHeadSpaceUsed":True,
            "all6188OriginalRowsRetained":True,"all5100HighRowsActuallyZero":highzero,
            "highResidualSHA256":m.matrix_hash(H),
            "originalPhysicalHashes":coeff["physical"],"nonexactLeadingColumns":n}
        if not highzero:
            hit=[]
            for i in range(5100):
                if any(H[i,c] for c in range(n)):
                    hit.append(1088+i)
                    if len(hit)==16: break
            meta["firstNonzeroHighRows"]=hit
        d.save_matrix(m,a,binding,phase,R,meta,result,True)
    else:
        R,meta,verified=old
        req(verified and [R.nrows(),R.ncols()]==[6188,n]
            and meta["order"]==a.order and meta["originalPhysicalHashes"]==coeff["physical"]
            and meta["all6188OriginalRowsRetained"],"Actual full original residual checkpoint")
    result["parameters"]["newOriginalResidualSHA256"]=m.matrix_hash(R)
    result["parameters"]["all5100NewHighRowsActuallyZero"]=meta["all5100HighRowsActuallyZero"]
    return R,meta

def seed_unit(d,m,w,a,binding,prefix,B,C,oldC,oldX,constants,result):
    for suffix,(X,meta) in constants.items():
        w.adopt(d,m,a,binding,prefix+"-"+suffix,X,meta,result)
    U,umeta=constants["unit"];I=umeta["rows"];nk=oldC.ncols()
    req(m.submatrix(C,range(1088),range(nk))==oldC,"All earlier actual RHS retained verbatim")
    bsha=m.matrix_hash(B);csha=m.matrix_hash(C);usha=m.matrix_hash(U)
    for c in range(nk):
        X=m.submatrix(oldX,range(582),[c])
        req(m.matrix_zero(U*X+m.submatrix(oldC,I,[c])),"Every original inherited unit product")
        phase=prefix+"-rhs-column-%04d"%c
        meta={"column":c,"constantSHA256":bsha,"rhsSHA256":csha,"unitSHA256":usha,
            "allOriginalUnitRowsVerified":True,"originalUnitProductCoordinates":582,
            "algorithm":"same-actual-paid-column","nativeSeconds":0.0,"nativeSolveUsed":False}
        old=d.load_matrix(m,a,binding,phase,result)
        if old is None: d.save_matrix(m,a,binding,phase,X,meta,result,True)
        else:
            Y,ymeta,verified=old
            req(verified and Y==X and ymeta==meta,"Same saved original inherited unit solution")

def scalar_bounds(ranks):
    last=max(max(ranks),8);cumulative={0:0};c=0
    for k in range(1,last+1):
        if k in ranks:
            c+=ranks[k];cumulative[k]=c
            if k in OLD_CUMULATIVE:
                req(c<=OLD_CUMULATIVE[k],"Previously proved actual head lower bound")
        else: cumulative[k]=OLD_CUMULATIVE[k]
    delta=sum(max(0,14-cumulative[k]) for k in range(last+1))
    subdelta=sum(max(0,13-cumulative[k]) for k in range(last+1))
    req(delta<=66 and subdelta<=55,"Existing mod31 affine divisor upper bounds")
    return delta,subdelta,cumulative

def run(d,m,j,u,w,c3,a,result):
    paid,ranks=records(d,a,result)
    inputs={"script":sha(__file__),"order":a.order,"paid":result["parameters"]["priorReceiptIdentities"],
        "first":FIRST_SHA,"actions":ACTIONS_SHA,"parent":PARENT_SHA,"helper":HELPER_SHA,
        "reuse":REUSE_SHA,"thirdSource":THIRD_SOURCE_SHA}
    binding=small_hash(inputs)
    result["parameters"].update({"checkpointBinding":binding,"checkpointSemanticInputs":inputs})
    coeff=j.original_coefficients(m,"zero",a.order)
    for order,record in paid.items():
        oldphys=record["parameters"][record["config"]["physicalKey"]]
        for key,value in oldphys.items():
            req(coeff["physical"].get(key)==value,"Same original coefficient "+str(order)+":"+key)
    result["parameters"]["originalPhysicalHashes"]=coeff["physical"]

    cochains={}
    P,meta=load_paid(d,m,paid[3],"complete-paid-second-cochains",result)
    req([P.nrows(),P.ncols()]==[875,23] and meta["allThreeOrdersAll6188RowsVerified"],
        "Complete actual second cochains")
    cochains[2]=c3.unpack_sections(m,P,meta["ranges"],2);del P
    heads={2:23}
    for order,record in paid.items():
        P,meta=load_paid(d,m,record,record["config"]["cochainPhase"],result)
        req(P.ncols()==record["heads"],"Every complete actual prior head retained")
        cochains[order]=c3.unpack_sections(m,P,meta["ranges"],order)
        heads[order]=record["heads"];del P
    current=cochains[a.order-1];oldheads=heads[a.order-1];n=oldheads-10
    for k in range(1,a.order):
        for X in current[k].values():
            req(m.matrix_zero(m.submatrix(X,range(X.nrows()),range(n,oldheads))),
                "Actual exact-pure tail has no higher coefficients")
    exact={sr:m.submatrix(X,range(X.nrows()),range(n,oldheads)) for sr,X in current[0].items()}
    req(m.matrix_zero(c3.all_rows(m,j,coeff,a.order,exact,10)),
        "New original coefficient on the ten exact pure heads")
    R,rm=residual(d,m,j,c3,a,binding,coeff,current,n,result)
    if not rm["all5100HighRowsActuallyZero"]:
        result["status"]="stage-completed"
        result["parameters"].update({"newHighForcingNeedsFullLift":True,
            "noNewConnectionRankClaimed":True})
        return
    if a.through=="residual":
        result["status"]="stage-completed";return

    H,hm=load_paid(d,m,paid[3],"complete-paid-high-homogeneous",result)
    req([H.nrows(),H.ncols()]==[3771,2] and hm["completeByPaidKernelZeroHeadFiber"]
        and hm["all5100OriginalHighRowsVerified"],"Complete actual high homogeneous source")
    Nh=m.submatrix(H,range(3762),range(2));del H
    high_sections={3:m.submatrix(Nh,range(990),range(2)),
                   4:m.submatrix(Nh,range(990,2475),range(2)),
                   5:m.submatrix(Nh,range(2475,3762),range(2))}
    Ch=c3.low(m,j,coeff,0,high_sections,2)
    incoming=[];blocks=[];cursor=594
    for order in range(3,a.order):
        rec=paid[order];Rold,oldmeta=load_paid(d,m,rec,rec["config"]["residualPhase"],result)
        count=heads[order-1]-10
        req([Rold.nrows(),Rold.ncols()]==[6188,count]
            and m.matrix_zero(m.submatrix(Rold,range(1088,6188),range(count))),
            "All original earlier incoming rows")
        incoming.append(m.submatrix(Rold,range(1088),range(count)))
        blocks.append({"connectionOrder":order,"start":cursor,"stop":cursor+count,
            "shift":a.order-order,"cochainOrder":order-1,
            "residualSHA256":m.matrix_hash(Rold)})
        cursor+=count;del Rold
    oldC=joined(m,[Ch]+incoming)
    C=m.join_columns(oldC,m.submatrix(R,range(1088),range(n)))
    req(cursor==592+oldC.ncols(),"Every actual incoming parameter retained")
    P0=j.block(m,coeff,0,0,1);Q,r0,_,_=m.nullspace(P0)
    req(r0==128 and Q.ncols()==7,"Original complete normal constant kernel")
    J0=j.join_vertical(m,[m.join_columns(j.block(m,coeff,0,sr,1),
                                         j.block(m,coeff,0,sr,2)) for sr in (0,1)])
    B=m.join_columns(J0,c3.low(m,j,coeff,1,{1:Q},7))
    previous=paid[a.order-1];prevprefix=previous["config"]["unitPrefix"]
    constants={}
    for suffix in ("constant-kernel","unit","primitive-unit"):
        X,xmeta=load_paid(d,m,previous,prevprefix+"-"+suffix,result)
        if suffix!="primitive-unit":
            req(xmeta["constantSHA256"]==m.matrix_hash(B),"Same full original constant low block")
        constants[suffix]=(X,xmeta)
    oldX,xmeta=load_paid(d,m,previous,prevprefix+"-unit-rhs-solution",result)
    req([oldX.nrows(),oldX.ncols()]==[582,oldC.ncols()]
        and xmeta["constantSHA256"]==m.matrix_hash(B)
        and xmeta["rhsSHA256"]==m.matrix_hash(oldC)
        and xmeta["allOriginalUnitRHSRowsVerified"],"All earlier actual unit solutions")
    prefix="complete-order-"+str(a.order)+"-unit"
    seed_unit(d,m,w,a,binding,prefix,B,C,oldC,oldX,constants,result)
    del oldX
    K,kmeta=u.complete_kernel(d,m,j,a,binding,prefix,B,C,582,result)
    req(K.nrows()==cursor+n,"All current complete low variables")
    S,sm,verified=d.load_matrix(m,a,binding,prefix+"-full-schur",result)
    req(verified and sm["allOriginalRowsRetained"],"Every actual full Schur source row")
    _,oldSchurRank=m.submatrix(S,range(1088),range(oldC.ncols())).rref()
    incomingRank=584+sum(ranks[k] for k in range(3,a.order))
    req(oldSchurRank==incomingRank-582,"Complete incoming image matches all paid exact ranks")
    chosen,Z,r=c3.head_basis(m,K,cursor,n)
    newrank=n-r;newheads=r+10;zerofiber=cursor-incomingRank
    req(newrank==kmeta["rank"]-incomingRank and newrank>=0
        and K.ncols()-r==zerofiber and newheads==oldheads-newrank and newheads>=13,
        "Full connection rank and complete normalized zero-head fiber")
    ranks[a.order]=newrank
    leading=m.fmpq_mat(oldheads,newheads)
    for i in range(n):
        for c in range(r): leading[i,c]=Z[i,c]
    for c in range(10): leading[n+c,r+c]=1
    co=[{sr:X*leading for sr,X in sec.items()} for sec in current]
    shiftmeta=[]
    for item in blocks:
        order=item["cochainOrder"];count=item["stop"]-item["start"]
        Y=m.submatrix(chosen,range(item["start"],item["stop"]),range(r))
        Yfull=append_zero(m,Y,10)
        for k in range(order+1):
            for sr,X in cochains[order][k].items():
                part=m.submatrix(X,range(X.nrows()),range(count))*Yfull
                add_section(co[item["shift"]+k],sr,part)
        shiftmeta.append(dict(item,coefficientSHA256=m.matrix_hash(Yfull),
            coefficientShape=[Yfull.nrows(),Yfull.ncols()]))
    b=m.submatrix(chosen,range(585,592),range(r))
    add_section(co[a.order-1],1,append_zero(m,Q*b,10))
    hi=Nh*m.submatrix(chosen,range(592,594),range(r))
    lo=m.submatrix(chosen,range(585),range(r))
    top={1:m.submatrix(lo,range(135),range(r)),
         2:m.submatrix(lo,range(135,585),range(r)),
         3:m.submatrix(hi,range(990),range(r)),
         4:m.submatrix(hi,range(990,2475),range(r)),
         5:m.submatrix(hi,range(2475,3762),range(r))}
    co.append({sr:append_zero(m,X,10) for sr,X in top.items()})
    c3.check_jets(m,j,coeff,co,a.order,newheads)
    _,rh=j.join_vertical(m,[co[0][0],co[0][1]]).rref()
    req(rh==newheads,"Actual independent complete higher heads")
    pack,ranges=c3.pack_sections(m,j,co);reads=compact_squares(m,j,co)
    delta,subdelta,cumulative=scalar_bounds(ranks)
    meta={"chart":"zero","parameter":"s","order":a.order,"leadingColumns":newheads,
        "ranges":ranges,"fullConnectionRanks":ranks,"allOriginalOrdersAndSourcesVerified":True,
        "allEarlierCochainImagesRetained":True,"completeIncomingBlocks":shiftmeta,
        "actualHeadInPreviousCompleteBasis":[[str(leading[i,c]) for c in range(newheads)] for i in range(oldheads)],
        "leadingMatrixSHA256":m.matrix_hash(leading),"targetSquareReadouts":reads,
        "nextPageRule":"Keep all prior Rj and add this actual Rorder; transport by s^(nextOrder-j) times the saved true (j-1) cochain",
        "temporaryOnly":True}
    d.save_matrix(m,a,binding,"complete-order-"+str(a.order)+"-cochains",pack,meta,result,True)
    result.update({"status":"completed","completeOrder":a.order,
        "fullConnectionRank":newrank,"fullLeadingDimension":newheads,
        "fullZeroMaximalMinorOrderLowerBound":delta,"fullZeroSubmaximalMinorOrderLowerBound":subdelta})
    result["parameters"].update({
        "completeOrder":a.order,"fullConnectionRank":newrank,"fullLeadingDimension":newheads,
        "fullConnectionRanks":ranks,"completeLowShape":[1088,cursor+n],
        "completeLowRank":kmeta["rank"],"completeLowKernelDimension":K.ncols(),
        "fullIncomingLowRank":incomingRank,"normalizedZeroHeadParameterFiberDimension":zerofiber,
        "fullConnectionNotMerelyEnvelope":True,"allEarlierCochainImagesRetained":True,
        "allOriginalOrdersAndSourcesVerified":True,"completeIncomingBlocks":shiftmeta,
        "all4347NonpureCorrectionsRetained":True,"all6188OriginalSourcesRetained":True,
        "newFinalOriginalProductCoordinates":(a.order+1)*6188*newheads,
        "wholeCochainShape":[pack.nrows(),pack.ncols()],"wholeCochainSHA256":m.matrix_hash(pack),
        "wholeCochainRanges":ranges,"leadingMatrixShape":[oldheads,newheads],
        "leadingMatrixSHA256":m.matrix_hash(leading),"targetSquareReadouts":reads,
        "fullZeroMaximalMinorOrderLowerBound":delta,"fullZeroSubmaximalMinorOrderLowerBound":subdelta,
        "cumulativeSmithCountsUsed":cumulative,"currentFactorDegreeLowerBound":delta+46,
        "largestPositiveSmithExponentUpperBound":66-subdelta,
        "largestPositiveSmithExponentLowerBound":max(9,a.order+1 if newheads>13 else 0),
        "unitPrefix":prefix,"onlyNewActualRHSColumnsSolved":n,"oldActualRHSColumnsReused":oldC.ncols(),
        "noFullInverseConstructed":True,"noOldLargeRrefRecomputed":True,
        "allIncomingShiftsAppliedToEveryCoefficient":True,"fullTargetMembershipNotClaimed":True})

def main():
    p=argparse.ArgumentParser()
    for name in ("parent-driver","unit-schur-helper","reused-driver","complete-third-driver",
                 "generator","jet-actions","checkpoint-dir","out"):
        p.add_argument("--"+name,required=True)
    p.add_argument("--paid-stage",action="append",nargs=4,required=True,
        metavar=("ORDER","RECEIPT","SHA256","CHECKPOINT"))
    p.add_argument("--order",type=int,required=True)
    p.add_argument("--through",choices=("residual","final"),default="final")
    p.add_argument("--remaining-seconds",type=float,default=180.0)
    p.add_argument("--memory-mib",type=int,default=2048)
    p.add_argument("--unit-algorithm",choices=("dixon","fflu"),default="dixon")
    p.add_argument("--unit-batch-columns",type=int,choices=(1,2),default=1)
    p.add_argument("--max-new-unit-groups",type=int,default=64)
    a=p.parse_args()
    req(5<=a.order<=17 and a.remaining_seconds>0 and 512<=a.memory_mib<=8192
        and a.max_new_unit_groups>0,"Explicit actual bounded next order")
    for path,want in ((a.parent_driver,PARENT_SHA),(a.unit_schur_helper,HELPER_SHA),
                      (a.reused_driver,REUSE_SHA),(a.complete_third_driver,THIRD_SOURCE_SHA),
                      (a.generator,FIRST_SHA),(a.jet_actions,ACTIONS_SHA)):
        req(sha(path)==want,"Pinned source dependency "+str(path))
    req(all(Path(a.checkpoint_dir).resolve()!=Path(row[3]).resolve() for row in a.paid_stage),
        "New checkpoint distinct from all actual paid stages")
    resource.setrlimit(resource.RLIMIT_AS,(a.memory_mib*1024**2,a.memory_mib*1024**2))
    d=module_at("r150_higher_storage",a.parent_driver)
    m=module_at("r150_higher_generator",a.generator)
    j=module_at("r150_higher_actions",a.jet_actions)
    u=module_at("r150_higher_unit",a.unit_schur_helper)
    w=module_at("r150_higher_paid",a.reused_driver)
    c3=module_at("r150_higher_complete3",a.complete_third_driver)
    d.FORMAT=FORMAT
    started=time.monotonic();a._deadline=started+a.remaining_seconds
    result={"format":RESULT_FORMAT,"status":"started","arithmetic":"exact rational python-flint",
        "scriptSHA256":sha(__file__),"parameters":{"completeOrder":a.order,"naturalParameter":"s",
        "sharedSeconds":a.remaining_seconds,"memoryMiB":a.memory_mib,"through":a.through,
        "checkpointDirectory":str(Path(a.checkpoint_dir)),"paidDirectoriesReadOnly":True,
        "sourceStrata":[170,918,2295,2805],"all6188OriginalSourcesRetained":True,
        "sourceMultiplierTransport":"all original degree<=3 multipliers under exact co-moving translation",
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
        mp=Path(a.checkpoint_dir)/"sixth-checkpoint.json"
        if mp.exists():
            result["parameters"]["checkpointManifestSHA256"]=sha(mp)
            result["parameters"]["checkpointManifestBytes"]=mp.stat().st_size
        raw=json.dumps(result,sort_keys=True,indent=2).encode()
        req(len(raw)<100000,"Only compact permanent receipt")
        out=Path(a.out);out.parent.mkdir(parents=True,exist_ok=True)
        tmp=out.with_name(out.name+".tmp");tmp.write_bytes(raw);os.replace(tmp,out)
        print(json.dumps({"status":result["status"],"receipt":str(out),"receiptBytes":len(raw),
            "receiptSHA256":hashlib.sha256(raw).hexdigest(),"elapsedSeconds":result["elapsedSeconds"],
            "completeOrder":a.order,"fullConnectionRank":result.get("fullConnectionRank"),
            "fullLeadingDimension":result.get("fullLeadingDimension")},sort_keys=True),flush=True)

if __name__=="__main__":
    main()
