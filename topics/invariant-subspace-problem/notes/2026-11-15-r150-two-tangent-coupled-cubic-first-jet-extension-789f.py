#!/usr/bin/env python3
"""Original s=2: one tangent-coupled cubic correction to the paid first jets.

Author: Astra-ISP-789f / literature_audit; AI-assisted GPT-6 Astra Pro.
No old constant RREF, unit selection, or any of the23 paid RHS is recomputed.
A child binding records the exact paid source, receipt and immutable cache.
Only the tangent-coupled cubic column is solved against the paid 583-row unit.
All 6188 original source products are checked for the resulting first jets.
This does not construct second jets or claim local target membership.
"""
import argparse
from copy import copy
import hashlib
import importlib.util
import json
from pathlib import Path
import resource
import signal
import sys
import time

BASE_SHA="8f55c5b5f0db2a7dd9b0b042e00cd506fd6e38698b9dc264a602e3dc8ccb510b"
PAID_CUBIC_SHA="b529d51efeb7195f3783576035f7c5e32e9a94a3bb1f8c44582177ba9dc51843"
PAID_SHA="2342b75a4c4c57015157e8df8c19d7ae617fe4a1863ffd7b24abad3211b113a6"
PAID_RAW_SHA="ec321dbfff578676c8ca8ecb7b83ce15cc5fbf10b2854fe9cd6fbea5aeb43de4"
PAID_BINDING="ef9b747b9ad8c6b0413fb61b23e402df4c3ca14b13ad2ab568f7f8d1f048a03b"
PAID_MANIFEST_SHA="74771ab772fe3ec392d2b5cbc237542480853a36b4274808530a107f5255283f"
PAID_MANIFEST_BYTES=16411
GEN_SHA="2757b900480fe3bf1450100188df1679801351f0330d609e1a39b9c7ca146186"
ACT_SHA="2ebf418575df39ca2ed0a2165a37e92071c415b4734969c5bedc64e0b9ef4332"
UNIT_SHA="36356983e71ee1e67677da1a7a5f7aebf2987db282a5447a741b6a6af93084d5"
CONST_SHA="5d83b8784ea4e1d2b99f9ccd8881dcf6f2abe4241586219a3b459541c10d6272"

def require(ok,message):
    if not ok: raise AssertionError(message)
def sha(path): return hashlib.sha256(Path(path).read_bytes()).hexdigest()
def module_at(name,path):
    spec=importlib.util.spec_from_file_location(name,path)
    mod=importlib.util.module_from_spec(spec);sys.modules[name]=mod
    spec.loader.exec_module(mod)
    return mod
def cols(m,d,X,indices):
    return d.sub(m,X,range(X.nrows()),indices)
def copy_phase(d,m,a,binding,name,M,meta,result):
    old=d.load_matrix(m,a,binding,name,result)
    if old is None:
        d.save_matrix(m,a,binding,name,M,meta,result,True)
        return
    X,xmeta,verified=old
    require(verified and X==M and xmeta==meta,"Exact inherited child phase "+name)
def paid_phase(d,m,old_a,name,paid_parameters):
    dummy={"parameters":{}}
    got=d.load_matrix(m,old_a,PAID_BINDING,name,dummy)
    require(got is not None and got[2],"Verified paid phase "+name)
    M,meta,verified=got
    declared=paid_parameters["checkpointPhases"].get(name)
    actual=d.manifest(old_a,PAID_BINDING)["phases"][name]
    require(declared is not None and declared["verified"],"Paid receipt phase "+name)
    for key in ("shape","matrixSHA256","fileSHA256","bytes","verified"):
        require(declared[key]==actual[key],"Receipt/cache phase identity "+name+" "+key)
    return M,meta

def tangent_cubic(d,m,j,a,old_a,binding,coeff,L,paid_parameters,result):
    """Polarize the paid second constant normal column with the paid weak line."""
    W0,wmeta=paid_phase(d,m,old_a,"actual-weak-cubic",paid_parameters)
    w=[m.fmpq(v) for v in wmeta["weakColumn"]]
    require(len(w)==9 and wmeta["linearRank"]==8 and any(w),
            "Paid original unique weak normal line")
    LL=m.fmpq_mat([[coeff["linear"][k][0][0][i] for k in range(2,11)]
                  for i in range(17)])
    require(m.matrix_hash(LL)==wmeta["originalLinearSHA256"]
            and m.matrix_zero(LL*m.column(w)),"Same original linear weak column")
    keys1=j.target_columns(1)
    index1={key:i for i,key in enumerate(keys1)}
    candidates=[]
    for col in (20,21):
        require(all(not L[20+i,col] for i,(cdegree,ddegree,normal) in enumerate(keys1)
                    if cdegree+ddegree>1),"Paid constant normal heads have tangent degree at most1")
        vv=[L[20+index1[(0,0,(k,))],col] for k in range(2,11)]
        cc=[L[20+index1[(1,0,(k,))],col] for k in range(2,11)]
        dd=[L[20+index1[(0,1,(k,))],col] for k in range(2,11)]
        if any(cc) or any(dd):candidates.append((col,vv,cc,dd))
    require(candidates,"A true second constant head has a nonzero tangent component")
    col,v,cc,dd=candidates[0]
    pivot=next(i for i,x in enumerate(w) if x)
    aa=cc[pivot]/w[pivot];bb=dd[pivot]/w[pivot]
    require((aa or bb) and all(cc[i]==aa*w[i] and dd[i]==bb*w[i] for i in range(9)),
            "Actual c/d coefficients are the same weak direction")
    for eq in range(17):
        value=sum((coeff["linear"][k][0][0][eq]*v[k-2]
                   +aa*coeff["linear"][k][1][0][eq]*w[k-2]
                   +bb*coeff["linear"][k][2][0][eq]*w[k-2]
                   for k in range(2,11)),m.fmpq(0))
        require(not value,"All17 original tangent-coupled weak-column identities")
    original_identity={"originalLinearSHA256":m.matrix_hash(LL),
        "paidWeakColumnSHA256":wmeta["weakColumnSHA256"],
        "paidConstantColumn":col,"v":[str(x) for x in v],
        "a":str(aa),"b":str(bb),"sameWeakDirectionForBothTangentCoefficients":True,
        "all17OriginalCoupledIdentitiesVerified":True}
    identitysha=d.small_hash(original_identity)
    done=d.load_matrix(m,a,binding,"actual-tangent-cubic",result)
    if done is not None:
        W1,meta,verified=done
        require(verified and meta["coupledIdentitySHA256"]==identitysha
                and [W1.nrows(),W1.ncols()]==[990,1],"True tangent-cubic cache")
        return W0,W1,meta
    d.guard(a,"actual tangent-coupled cubic normal column",1)
    keys3=j.target_columns(3);W1=m.fmpq_mat(990,1)
    for i,(cdegree,ddegree,normal) in enumerate(keys3):
        inds=[k-2 for k in normal]
        product=m.fmpq(1)
        for k in inds:product*=w[k]
        if (cdegree,ddegree)==(0,0):
            value=m.fmpq(0)
            for position in range(3):
                term=v[inds[position]]
                for other in range(3):
                    if other!=position:term*=w[inds[other]]
                value+=term
            W1[i,0]=value
        elif (cdegree,ddegree)==(1,0):W1[i,0]=aa*product
        elif (cdegree,ddegree)==(0,1):W1[i,0]=bb*product
    require(any(W1[i,0] for i,(cdegree,ddegree,_) in enumerate(keys3)
                if cdegree+ddegree==1),"New cubic has a genuine nonzero tangent part")
    require(all(not W0[i,0] for i,(cdegree,ddegree,_) in enumerate(keys3)
                if cdegree+ddegree>0),"Paid pure cubic has no tangent part")
    high=d.apply_rows(m,j,coeff,0,{3:W1},1,(2,3))
    require(m.matrix_zero(high),"All5100 original high rows of the new cubic")
    meta={**original_identity,"coupledIdentitySHA256":identitysha,
          "normalDegree":3,"totalDegreeBound":4,"tangentDegreeBound":1,
          "independentOfPaidPureCubic":True,"all5100OriginalHighRowsVerified":True,
          "highProductSHA256":m.matrix_hash(high),"noAssumedHighBlockRank":True}
    d.save_matrix(m,a,binding,"actual-tangent-cubic",W1,meta,result,True)
    return W0,W1,meta

def inherit_constant(d,m,a,old_a,binding,B,paid_parameters,result):
    expected=m.matrix_hash(B)
    for suffix in ("constant-kernel","unit","primitive-unit"):
        M,meta=paid_phase(d,m,old_a,"first-cubic-"+suffix,paid_parameters)
        if suffix=="constant-kernel":
            require(meta["constantSHA256"]==expected and meta["rank"]==583
                    and M.ncols()==2,"Same complete old constant block")
        if suffix=="unit":
            require(meta["constantSHA256"]==expected and meta["rank"]==583
                    and M.nrows()==583 and M.ncols()==583,
                    "Same genuine original unit")
        copy_phase(d,m,a,binding,"first-tangent-cubic-"+suffix,M,meta,result)

def inherited_and_new_schur(d,m,j,u,a,old_a,binding,B,C,Ch,paid_parameters,result):
    """Preserve the old23 full Schur columns; compute only the added column."""
    prefix="first-tangent-cubic"
    Cnew=m.join_columns(C,Ch)
    require(C.ncols()==23 and Ch.ncols()==1,"Exactly23 paid and one new RHS")
    require(cols(m,d,Cnew,range(23))==C,"All25024 old RHS entries unchanged")
    inherit_constant(d,m,a,old_a,binding,B,paid_parameters,result)
    N,P,F,I,U,bsha=u.constant_unit(d,m,j,a,binding,prefix,B,583,result)
    csha=m.matrix_hash(Cnew);oldcsha=m.matrix_hash(C);usha=m.matrix_hash(U)
    Xold,xmeta=paid_phase(d,m,old_a,"first-cubic-unit-rhs-solution",paid_parameters)
    Sold,smeta=paid_phase(d,m,old_a,"first-cubic-full-schur",paid_parameters)
    xoldsha=m.matrix_hash(Xold)
    require(xmeta["constantSHA256"]==bsha and xmeta["rhsSHA256"]==oldcsha
            and xmeta["unitSHA256"]==usha and xmeta["unitRows"]==I
            and xmeta["pivotColumns"]==P and xmeta["allOriginalUnitRHSRowsVerified"],
            "All paid original RHS/constant/unit identities")
    require(smeta["constantSHA256"]==bsha and smeta["rhsSHA256"]==oldcsha
            and smeta["unitSolutionSHA256"]==xoldsha
            and smeta["unitRows"]==I and smeta["allOriginalRowsRetained"]
            and smeta["unitRowsActuallyZero"],"Paid full Schur retained all1088 rows")
    require([Xold.nrows(),Xold.ncols()]==[583,23]
            and [Sold.nrows(),Sold.ncols()]==[1088,23],"Paid actual matrix sizes")
    oldconstant=paid_parameters["first-cubicConstantUnit"]
    require(bsha==oldconstant["constantSHA256"] and usha==oldconstant["unitSHA256"],
            "Fresh original B and U match paid mathematical matrices")
    # Each original unit solution is copied with an explicit child input binding.
    # Its verified product is inherited only after all original C entries match.
    for c in range(23):
        name=prefix+"-rhs-column-%04d"%c
        col=cols(m,d,Xold,[c])
        meta={"column":c,"constantSHA256":bsha,"rhsSHA256":csha,"unitSHA256":usha,
              "allOriginalUnitRowsVerified":True,"originalUnitProductCoordinates":583,
              "nativeSolveUsed":False,"algorithm":"inherited-paid-original-column",
              "nativeSeconds":0.0,"paidBinding":PAID_BINDING,
              "paidReceiptSHA256":PAID_SHA,"paidActualRHSSHA256":oldcsha,
              "paidCombinedSolutionSHA256":xoldsha,
              "all25024OriginalRHSValuesMatchedBySHA256BeforeInheritance":True}
        copy_phase(d,m,a,binding,name,col,meta,result)
    solved=d.load_matrix(m,a,binding,prefix+"-unit-rhs-solution",result)
    if solved is None:
        X=u.solve_actual_rhs_columns(d,m,a,binding,prefix,U,Cnew,I,bsha,csha,usha,result)
        require(cols(m,d,X,range(23))==Xold,"All13409 paid solution entries preserved")
        meta={"constantSHA256":bsha,"rhsSHA256":csha,"unitSHA256":usha,
              "unitRows":I,"pivotColumns":P,"fullOriginalUnitProductCoordinates":583*24,
              "allOriginalUnitRHSRowsVerified":True,"onlyActualRHSColumnsSolved":True,
              "noCompleteInverseConstructed":True,"newNativeRHSCountAtMost":1,
              "paidOriginalRHSCountInherited":23,"paidBinding":PAID_BINDING}
        d.save_matrix(m,a,binding,prefix+"-unit-rhs-solution",X,meta,result,True)
    else:
        X,meta,verified=solved
        require(verified and meta["constantSHA256"]==bsha and meta["rhsSHA256"]==csha
                and meta["unitSHA256"]==usha and meta["unitRows"]==I
                and meta["pivotColumns"]==P and meta["allOriginalUnitRHSRowsVerified"],
                "Verified child actual RHS cache")
        require(cols(m,d,X,range(23))==Xold,"Cached old solution columns unchanged")
    current=d.load_matrix(m,a,binding,prefix+"-full-schur",result)
    if current is None:
        d.guard(a,"one new actual full-row Schur column",1)
        BP=d.sub(m,B,range(B.nrows()),P)
        Snew=Ch+BP*cols(m,d,X,[23])
        require(m.matrix_zero(d.sub(m,Snew,I)),"All583 original unit rows of new column")
        require(not m.matrix_zero(Snew),
                "A new high cubic cannot lie in the paid complete low constant kernel")
        S=m.join_columns(Sold,Snew)
        require(cols(m,d,S,range(23))==Sold,"All25024 paid full Schur entries preserved")
        meta={"constantSHA256":bsha,"rhsSHA256":csha,
              "unitSolutionSHA256":m.matrix_hash(X),"unitRows":I,
              "allOriginalRowsRetained":True,"unitRowsActuallyZero":True,
              "old23SchurColumnsInheritedWithoutRepeatedProduct":True,
              "newColumnOriginalRows":1088,
              "newColumnNotInOriginalBImage":True,
              "paidFullSchurSHA256":m.matrix_hash(Sold)}
        d.save_matrix(m,a,binding,prefix+"-full-schur",S,meta,result,True)
    else:
        S,meta,verified=current
        require(verified and meta["constantSHA256"]==bsha and meta["rhsSHA256"]==csha
                and meta["unitSolutionSHA256"]==m.matrix_hash(X)
                and meta["unitRows"]==I and meta["allOriginalRowsRetained"]
                and meta["unitRowsActuallyZero"],"Full child Schur identity")
        require(cols(m,d,S,range(23))==Sold,"Same old full Schur in resumed child")
    result["parameters"]["paidReuse"]={
        "paidBinding":PAID_BINDING,"paidReceiptSHA256":PAID_SHA,
        "originalBEqualsPaid":True,"oldRHSRows":1088,"oldRHSColumns":23,
        "all25024OldRHSValuesMatchedBySHA256":True,
        "all13409OldSolutionValuesCompared":True,
        "oldFullSchurColumns":23,"allOldFullSchurValuesCompared":True,
        "oldRREFRepeated":False,"oldUnitSelectionRepeated":False,
        "oldNativeRHSSolvesRepeated":False,"newNativeRHSCountAtMost":1}
    return u.complete_kernel(d,m,j,a,binding,prefix,B,Cnew,583,result)

def solve(d,m,j,u,a,old_a,binding,paid_parameters,result):
    coeff=d.original_at_two(m,j,2)
    require(coeff["physical"]==paid_parameters["physicalCoefficientSHA256"],
            "All original parameter2 physical coefficient matrices unchanged")
    result["parameters"]["physicalCoefficientSHA256"]=coeff["physical"]
    L,lmeta=paid_phase(d,m,old_a,"constant-heads",paid_parameters)
    require(L.nrows()==155 and L.ncols()==22
            and lmeta["completeOriginalConstantDimension"]==22,
            "Complete original constant head space")
    copy_phase(d,m,a,binding,"constant-heads",L,lmeta,result)
    B=d.vjoin(m,j,[d.hjoin(m,[j.block(m,coeff,0,r,t) for t in (1,2)])
                  for r in (0,1)])
    C22=d.apply_rows(m,j,coeff,1,d.sections(m,j,L,1),22,(0,1))
    W0,W1,wmeta=tangent_cubic(d,m,j,a,old_a,binding,coeff,L,paid_parameters,result)
    Ch0=d.apply_rows(m,j,coeff,0,{3:W0},1,(0,1))
    Ch1=d.apply_rows(m,j,coeff,0,{3:W1},1,(0,1))
    require(not m.matrix_zero(Ch1),"A genuine new low tangent-cubic correction column")
    Cold=m.join_columns(C22,Ch0)
    K,meta=inherited_and_new_schur(d,m,j,u,a,old_a,binding,B,Cold,Ch1,
                                   paid_parameters,result)
    chosen,H,h=d.leading_basis(m,j,K,585,22)
    require(h in (15,16),"One new correction can gain at most one paid head")
    require(K.ncols()-h==2,"Complete zero-leading fiber is the two low constant columns")
    oldH,oldhmeta=paid_phase(d,m,old_a,"first-leading-map",paid_parameters)
    rr,rank=m.join_columns(H,oldH).rref()
    require(rank==h,"The entire paid15-head space is retained")
    del rr
    L0=L*H
    L1low=d.append_zero_pure(m,d.sub(m,chosen,range(585)))
    coefficients=d.sub(m,chosen,[607,608])
    L1high=W0*d.sub(m,coefficients,[0])+W1*d.sub(m,coefficients,[1])
    L1=d.vjoin(m,j,[L1low,L1high])
    d.verify_jets(m,j,coeff,[L0,L1],[1,3],result,"tangentCubicExtendedFirstFamily")
    read=d.square_read(m,j,L1,3)
    require(m.matrix_zero(d.square_read(m,j,d.embed_01_to_012(m,L),2)),
            "All22 complete constant correction square readings vanish")
    for name,M in (("first-leading-map",H),("first-lambda0",L0),
                   ("first-lambda1",L1),("first-square-read",read),
                   ("first-cubic-coefficients",coefficients)):
        d.save_matrix(m,a,binding,name,M,{},result,True)
    result["parameters"]["tangentCubic"]={
        **wmeta,"paidPureCubicSHA256":m.matrix_hash(W0),
        "newTangentCubicSHA256":m.matrix_hash(W1),
        "paidLowCubicColumnSHA256":m.matrix_hash(Ch0),
        "newLowColumnSHA256":m.matrix_hash(Ch1)}
    result["parameters"]["firstTangentCubicExtendedFamily"]={
        "constantHeads":22,"paidFirstHeads":15,"leadingDimension":h,
        "newLeadingDirections":h-15,"completeZeroLeadingLowFiber":2,
        "normalDegreeBounds":[1,3],"lambda1CubicAllowedSpaceDimension":2,
        "lambda1CubicTangentDegreeBound":1,"allPaidHeadsRetained":True,
        "headMapSHA256":m.matrix_hash(H),"lambda0SHA256":m.matrix_hash(L0),
        "lambda1SHA256":m.matrix_hash(L1),"cubicCoefficientsSHA256":m.matrix_hash(coefficients),
        "nineLambda1SquareReadShape":[9,h],"nineLambda1SquareReadSHA256":m.matrix_hash(read),
        "nineLambda1SquareReadAllZero":m.matrix_zero(read),
        "firstNonzeroSquareRead":d.first_nonzero(read),
        "sameHeadReadInvariantUnderAnyCompleteConstantCorrection":True,
        "all6188OriginalSourceRowsVerified":True,
        "notClaimedCompleteFirstHeadSpace":True,
        "notClaimedCompleteNormalThreeHighKernel":True}
    result["parameters"]["directedConclusion"]={
        "scope":"actual first jets with low corrections and the two constructed high cubics",
        "secondJetsConstructed":False,
        "nonzeroFirstReadWouldRequireTrueSecondLiftBeforeObstruction":True,
        "noCandidateForSpecifiedSecondJetObstructionInThisFamily":m.matrix_zero(read),
        "localTargetMembershipNotProved":True,
        "noClaimOfFullFirstOrSecondConnectionRank":True,
        "noInvariantSubspaceProblemConclusion":True}

def main():
    p=argparse.ArgumentParser()
    for name in ("paid-probe","paid-cubic-source","paid-receipt","paid-checkpoint-dir","generator",
                 "jet-actions","unit-schur-helper","constant-receipt",
                 "checkpoint-dir","out"):
        p.add_argument("--"+name,required=True)
    p.add_argument("--remaining-seconds",type=float,default=180)
    p.add_argument("--memory-mib",type=int,default=2048)
    a=p.parse_args()
    require(0<a.remaining_seconds<=600 and 512<=a.memory_mib<=8192,
            "Actual shared resource bounds")
    resource.setrlimit(resource.RLIMIT_AS,(a.memory_mib*1024**2,)*2)
    if hasattr(sys,"set_int_max_str_digits"):sys.set_int_max_str_digits(0)
    for path,digest in ((a.paid_probe,BASE_SHA),(a.paid_cubic_source,PAID_CUBIC_SHA),
                        (a.paid_receipt,PAID_SHA),
                        (a.generator,GEN_SHA),(a.jet_actions,ACT_SHA),
                        (a.unit_schur_helper,UNIT_SHA),(a.constant_receipt,CONST_SHA)):
        require(sha(path)==digest,"Pinned original source or receipt "+path)
    require(Path(a.checkpoint_dir).resolve()!=Path(a.paid_checkpoint_dir).resolve(),
            "Paid ancestor cache is read-only; child must have a distinct path")
    outer=json.loads(Path(a.paid_receipt).read_bytes())
    paid=outer["result"];pp=paid["parameters"]
    require(paid["status"]=="completed" and pp["binding"]==PAID_BINDING
            and outer["fullTemporaryReceiptSHA256"]==PAID_RAW_SHA
            and outer["scriptSHA256"]==PAID_CUBIC_SHA,
            "Actual completed original ancestor")
    require(pp["firstCubicExtendedFamily"]["leadingDimension"]==15
            and pp["firstCubicExtendedFamily"]["nineLambda1SquareReadAllZero"]
            and pp["cubicExtendedFirstFamilyVerification"]["all6188OriginalRowsVerified"],
            "Paid original15-head scope")
    man=Path(a.paid_checkpoint_dir)/"manifest.json"
    require(man.stat().st_size==PAID_MANIFEST_BYTES and sha(man)==PAID_MANIFEST_SHA,
            "Exact completed immutable ancestor manifest")
    d=module_at("r150_two_paid_base_for_tangent_cubic",a.paid_probe)
    m=module_at("r150_two_cubic_original_generator",a.generator)
    j=module_at("r150_two_cubic_original_actions",a.jet_actions)
    u=module_at("r150_two_cubic_actual_rhs_unit",a.unit_schur_helper)
    d.ARGS=a
    a.unit_algorithm="dixon";a.unit_batch_columns=1;a.max_new_unit_groups=128
    a._new_unit_groups=0
    old_a=copy(a);old_a.checkpoint_dir=a.paid_checkpoint_dir
    started=time.monotonic();a._deadline=started+a.remaining_seconds
    binding=d.small_hash({"format":"r150-two-tangent-cubic-child-input-v1",
        "selfSHA256":sha(__file__),"base":BASE_SHA,"paidCubicSource":PAID_CUBIC_SHA,
        "paidReceipt":PAID_SHA,
        "paidManifest":PAID_MANIFEST_SHA,"paidBinding":PAID_BINDING,
        "generator":GEN_SHA,"actions":ACT_SHA,"helper":UNIT_SHA,"constant":CONST_SHA,
        "mean":2,"newCorrection":"actual-second-constant-head-tangent-coupled-cubic",
        "all6188OriginalSources":True})
    result={"format":"r150-two-tangent-coupled-cubic-first-jet-extension-v1",
            "status":"started","parameters":{"binding":binding,
            "selfSHA256":sha(__file__),"parentBinding":PAID_BINDING,
            "inputSHA256":{"paidProbe":BASE_SHA,"paidCubicSource":PAID_CUBIC_SHA,
                          "paidReceipt":PAID_SHA,
                          "paidManifest":PAID_MANIFEST_SHA,"generator":GEN_SHA,
                          "jetActions":ACT_SHA,"unitHelper":UNIT_SHA,
                          "constantReceipt":CONST_SHA},
            "sharedSeconds":a.remaining_seconds,"memoryMiB":a.memory_mib,
            "noLargeRecomputableDataUploaded":True,"allMatricesTemporary":True,
            "ancestorCacheReadOnly":True}}
    def alarm(_s,_f):raise d.SafeStop("Actual shared tangent-cubic extension budget exhausted")
    signal.signal(signal.SIGALRM,alarm);signal.setitimer(signal.ITIMER_REAL,a.remaining_seconds)
    try:
        solve(d,m,j,u,a,old_a,binding,pp,result)
        result["status"]="completed"
    except d.SafeStop as exc:
        result["status"]="prefix-completed";result["error"]=str(exc)
    except BaseException as exc:
        result["status"]="failed";result["error"]=type(exc).__name__+": "+str(exc)
        raise
    finally:
        signal.setitimer(signal.ITIMER_REAL,0)
        result["elapsedSeconds"]=time.monotonic()-started
        mp=Path(a.checkpoint_dir)/"manifest.json"
        if mp.exists():result["parameters"]["temporaryManifest"]={
            "binding":binding,"bytes":mp.stat().st_size,"sha256":sha(mp)}
        d.compact_metadata(result)
        raw=d.canonical_bytes(result)
        require(len(raw)<90000,"Compact mathematical receipt below90KB")
        d.atomic_json(a.out,result)
        print(json.dumps({"status":result["status"],"receipt":a.out,
            "bytes":len(raw),"sha256":hashlib.sha256(raw).hexdigest(),
            "elapsedSeconds":result["elapsedSeconds"]}),flush=True)

if __name__=="__main__":main()
