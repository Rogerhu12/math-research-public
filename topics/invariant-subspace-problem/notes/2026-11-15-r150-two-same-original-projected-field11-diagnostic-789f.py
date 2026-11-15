#!/usr/bin/env python3
"""Diagnose the s=2 projected Smith pages in the SAME paid original field11 input.

Author: Astra-ISP-789f / literature_audit, AI-assisted GPT-6 Astra Pro.
Date: 2026-11-15.
This consumes the verified full coefficient0..3 input.  It does not repeat
the full4345 elimination, change prime, or compute a new rational normal form.
All6188 source rows are inspected; the5100 rows with at least two normal
multiplier variables are verified to have ZERO projected products at each
order before they are removed.  The1088 remaining rows retain all155 pure
and one-normal target coordinates.
"""
import argparse
import hashlib
import json
import os
import resource
import struct
import sys
import time
from itertools import combinations_with_replacement
from pathlib import Path
from flint import nmod_mat

PAID_SHA="0d721310db73560427a1c14a59c08853387c9761e117cb0dcaf24951b9aa2ac8"
PROJECTION_SHA="693da6446a6f04cba2c343ea49d9d3466caad1aebd056e91db338163b20d3332"
PAID_BINDING="56c8b50a909bf2bb163e80734890bef26d927b5a7b7491e1d7dbb1b74d0dbdb4"
INPUT_SHA="980a6008a41b904b3802cd71c56d49a65651422534d62ebdd265037e674dc0db"
INPUT_BYTES=3633604
PRIME=11
ORDER=3

def require(ok,message):
    if not ok:
        raise AssertionError(message)
def canonical(obj):
    return json.dumps(obj,sort_keys=True,separators=(",",":"),ensure_ascii=True).encode("ascii")
def digest(obj):
    return hashlib.sha256(canonical(obj)).hexdigest()
def file_sha(path):
    h=hashlib.sha256()
    with Path(path).open("rb") as f:
        while True:
            b=f.read(1024*1024)
            if not b:break
            h.update(b)
    return h.hexdigest()
def atomic_json(path,obj):
    path=Path(path);path.parent.mkdir(parents=True,exist_ok=True)
    tmp=path.with_name(path.name+".tmp")
    tmp.write_bytes(canonical(obj));os.replace(tmp,path)
def remaining(a):
    value=a._deadline-time.monotonic()
    if value<=0:raise TimeoutError("Shared budget exhausted")
    return value
def zero(n,m):
    return nmod_mat(n,m,[0]*(n*m),PRIME)
def identity(n):
    return nmod_mat(n,n,[int(i==j) for i in range(n) for j in range(n)],PRIME)
def block(M,rows,cols):
    return nmod_mat(len(rows),len(cols),[int(M[i,j]) for i in rows for j in cols],PRIME)
def is_zero(M):
    return all(not M[i,j] for i in range(M.nrows()) for j in range(M.ncols()))
def matrix_hash(M):
    h=hashlib.sha256(struct.pack("<3I",PRIME,M.nrows(),M.ncols()))
    h.update(bytes(int(M[i,j]) for i in range(M.nrows()) for j in range(M.ncols())))
    return h.hexdigest()
def pivots(R,r):
    p=[]
    for i in range(r):
        c=next((j for j in range(R.ncols()) if R[i,j]),None)
        require(c is not None and int(R[i,c])==1,"True field RREF pivot")
        p.append(c)
    require(p==sorted(set(p)),"Distinct ordered pivots")
    return p

def read_projection(a,paid,result):
    info=paid["originalSeriesInput"]
    require(info["bytes"]==INPUT_BYTES and info["sha256"]==INPUT_SHA,
            "Actual full original series input descriptor")
    path=Path(a.parent_checkpoint_dir)/info["file"]
    require(path.name==info["file"] and path.stat().st_size==INPUT_BYTES and
            file_sha(path)==INPUT_SHA,"Same immutable full original input")
    data=path.read_bytes();at=0
    def take(n):
        nonlocal at
        require(at+n<=len(data),"Truncated original series input")
        value=data[at:at+n];at+=n;return value
    require(take(8)==b"R15SJ311","Original input magic")
    require(struct.unpack("<5I",take(20))==(11,6188,4367,22,3),"Original dimensions")
    require(take(64).decode("ascii")==PAID_BINDING,"Original series binding")
    require(take(64).decode("ascii")==paid["parentBinding"],"Original first-stage binding")
    targets=[mon for d in range(5,0,-1)
             for mon in combinations_with_replacement(range(11),d)]
    sources=[(eq,mon) for d in range(4) for eq in range(17)
             for mon in combinations_with_replacement(range(11),d)]
    prep=paid["originalPreparation"]
    require(digest(targets)==prep["sameTargetOrderSHA256"] and
            digest(sources)==prep["sameSourceOrderSHA256"],
            "Same complete original dictionaries")
    source_ids=[i for i,(_,mon) in enumerate(sources) if sum(v>=2 for v in mon)<=1]
    target_ids=[i for i,mon in enumerate(targets) if sum(v>=2 for v in mon)<=1]
    require(len(source_ids)==1088 and len(target_ids)==155,"Complete projected dimensions")
    ri={r:i for i,r in enumerate(source_ids)}
    ci={c:i for i,c in enumerate(target_ids)}
    seq=[zero(1088,155) for _ in range(4)]
    inspected=0;zero_high=0;retained_nonzeros=[]
    for k in range(4):
        nnz=0
        for row in range(6188):
            if row%256==0:remaining(a)
            count=struct.unpack("<H",take(2))[0]
            require(count<=77,"Original quadratic support bound")
            last=-1;has_projected=False
            for _ in range(count):
                col,value=struct.unpack("<HB",take(3))
                require(last<col<4367 and 0<value<11,"Canonical original field support")
                last=col
                if col in ci:
                    has_projected=True
                    require(row in ri,"A higher-normal source must have zero projection")
                    seq[k][ri[row],ci[col]]=value;nnz+=1
            if row not in ri:
                require(not has_projected,"All original high-source projections vanish")
                zero_high+=1
            inspected+=1
        retained_nonzeros.append(nnz)
    require(at==len(data) and inspected==4*6188 and zero_high==4*5100,
            "Exact EOF and every original source checked")
    result["parameters"]["originalProjection"]={
        "sameOriginalSeriesInput":info,
        "allOriginalSourceRows":6188,"allProjectedSourceRows":1088,
        "allProjectedTargetCoordinates":155,
        "inspectedOriginalSourceCoefficientRows":inspected,
        "zeroHigherNormalSourceCoefficientRows":zero_high,
        "all5100HighSourceRowsVerifiedZeroAtEveryOrder":True,
        "all1088ProjectedSourceRowsRetained":True,
        "sameOriginalSourceIndicesSHA256":digest(source_ids),
        "sameOriginalTargetIndicesSHA256":digest(target_ids),
        "projectedCoefficientSHA256":[matrix_hash(M) for M in seq],
        "projectedNonzerosByOrder":retained_nonzeros,
        "projectionUsesActualOriginalEquationsNotBare54UnitRows":True}
    return seq,source_ids,target_ids

def projected_smith(a,seq,rows,cols,result):
    covered=0;power=0;positive=[];phases=[]
    while seq and covered<142:
        remaining(a);nr,nc=seq[0].nrows(),seq[0].ncols()
        R,r=seq[0].rref();pc=pivots(R,r)
        require(covered+r<=142,"Same original projected generic rank at most142")
        phase={"exponent":power,"shape":[nr,nc],"rank":r,
               "precisionCoefficients":len(seq),
               "coefficientSHA256":[matrix_hash(M) for M in seq]}
        if r==0:
            require(is_zero(seq[0]),"Rank zero is the entire constant block")
            phase.update({"allRemainingRowsRetained":True,"constantBlockZero":True,
                          "cumulativeRank":covered,"positiveLengthSoFar":sum(positive)})
            phases.append(phase);seq=seq[1:];power+=1;continue
        Rt,rr=block(seq[0],list(range(nr)),pc).transpose().rref()
        require(rr==r,"Independent actual original unit rows")
        pr=pivots(Rt,rr);rs=set(pr);cs=set(pc)
        fr=[i for i in range(nr) if i not in rs]
        fc=[j for j in range(nc) if j not in cs]
        U=[block(M,pr,pc) for M in seq];V=[block(M,pr,fc) for M in seq]
        W=[block(M,fr,pc) for M in seq];Z=[block(M,fr,fc) for M in seq]
        inv=U[0].inv()
        require(U[0]*inv==identity(r) and inv*U[0]==identity(r),"Both constant unit inverses")
        Yi=[inv]
        for k in range(1,len(seq)):
            t=zero(r,r)
            for i in range(1,k+1):t+=U[i]*Yi[k-i]
            Yi.append(-(inv*t))
        for k in range(len(seq)):
            left=zero(r,r);right=zero(r,r)
            for i in range(k+1):
                left+=U[i]*Yi[k-i];right+=Yi[i]*U[k-i]
            wanted=identity(r) if k==0 else zero(r,r)
            require(left==wanted and right==wanted,"Both full Taylor unit convolutions")
        corrections=[]
        for k in range(len(seq)):
            t=zero(r,len(fc))
            for i in range(k+1):t+=Yi[i]*V[k-i]
            corrections.append(-t)
        schur=[]
        for k in range(len(seq)):
            t=Z[k]
            for i in range(k+1):t+=W[i]*corrections[k-i]
            schur.append(t)
        lifts=[]
        for k in range(len(seq)):
            X=zero(nc,len(fc))
            if k==0:
                for j,c in enumerate(fc):X[c,j]=1
            for i,c in enumerate(pc):
                for j in range(len(fc)):X[c,j]=corrections[k][i,j]
            lifts.append(X)
        verified=0
        for k in range(len(seq)):
            t=zero(nr,len(fc))
            for i in range(k+1):t+=seq[i]*lifts[k-i]
            require(is_zero(block(t,pr,list(range(len(fc))))) and
                    block(t,fr,list(range(len(fc))))==schur[k],
                    "Every remaining original-row Schur product")
            verified+=nr*len(fc)
        require(is_zero(schur[0]),"Complete constant residual zero")
        covered+=r
        if power:positive.extend([power]*r)
        phase.update({"unitRows":pr,"unitColumns":pc,
                      "survivingOriginalSourceLabelsAtUnitRows":[rows[i] for i in pr],
                      "survivingOriginalTargetLabelsAtUnitColumns":[cols[i] for i in pc],
                      "unitDeterminantModulo11":int(U[0].det()),
                      "unitConstantSHA256":matrix_hash(U[0]),
                      "allUnitConvolutionsVerified":True,
                      "allRemainingRowSchurProductsVerified":True,
                      "originalRemainingProductCoordinates":verified,
                      "schurSHA256":[matrix_hash(M) for M in schur],
                      "cumulativeRank":covered,"positiveLengthSoFar":sum(positive)})
        phases.append(phase)
        rows=[rows[i] for i in fr];cols=[cols[i] for i in fc]
        seq=schur[1:];power+=1
    result["parameters"]["exactProjectedFieldPhases"]=phases
    result["parameters"]["confirmedProjectedPositiveExponents"]=positive
    result["parameters"]["projectedGenericRankReached"]=(covered==142)
    result["parameters"]["projectedFieldRankCovered"]=covered
    result["parameters"]["allProjectedOriginalSchurRowsVerified"]=True
    return phases,positive,covered

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--paid-receipt",required=True)
    ap.add_argument("--projection-receipt",required=True)
    ap.add_argument("--parent-checkpoint-dir",required=True)
    ap.add_argument("--out",required=True)
    ap.add_argument("--remaining-seconds",type=float,default=30)
    ap.add_argument("--memory-mib",type=int,default=512)
    a=ap.parse_args();start=time.monotonic();a._deadline=start+a.remaining_seconds
    require(a.remaining_seconds>0 and a.memory_mib>=256,"Finite resource budget")
    soft,hard=resource.getrlimit(resource.RLIMIT_AS)
    limit=a.memory_mib*1024*1024
    if hard!=resource.RLIM_INFINITY:limit=min(limit,hard)
    resource.setrlimit(resource.RLIMIT_AS,(limit,hard))
    out=Path(a.out);out.mkdir(parents=True,exist_ok=True)
    result={"format":"r150-two-same-original-projected-field11-diagnostic-v1",
            "status":"running","parameters":{},"events":[]};status=0
    try:
        require(file_sha(a.paid_receipt)==PAID_SHA,"Pinned actual full Schur receipt")
        require(file_sha(a.projection_receipt)==PROJECTION_SHA,"Pinned true Q projection receipt")
        parent=json.loads(Path(a.paid_receipt).read_bytes())
        require(parent["exitCode"]==0 and parent["result"]["status"]=="completed",
                "Actual completed original full series")
        paid=parent["result"]["parameters"]
        require(paid["binding"]==PAID_BINDING and paid["all22OriginalHeadsRetained"]
                and paid["nativeResult"]["allOriginalResidualIdentitiesVerified"]
                and paid["originalPreparation"]["allOriginalParameterDenominatorsUnitsAt11"],
                "Same actual original integral series with all22 heads")
        projected=json.loads(Path(a.projection_receipt).read_bytes())
        pp=projected["result"]["parameters"]
        require(projected["exitCode"]==0 and projected["result"]["status"]=="completed"
                and pp["projectedTorsionLengthExact"]==12
                and pp["projectionGenericRankReached"]
                and pp["all6188OriginalProjectedSourcesRetained"]
                and pp["localGenerationBothDirectionsVerified"],
                "Paid exact Q projection, with all original sources")
        selfsha=file_sha(__file__)
        binding=digest({"format":"r150-projected-field11-diagnostic-binding-v1",
                        "selfSHA256":selfsha,"paidReceiptSHA256":PAID_SHA,
                        "trueQProjectionReceiptSHA256":PROJECTION_SHA,
                        "originalInputSHA256":INPUT_SHA,"order":3,"prime":11})
        result["parameters"].update({
            "binding":binding,"selfSHA256":selfsha,"prime":11,"throughOrder":3,
            "paidReceiptSHA256":PAID_SHA,"trueQProjectionReceiptSHA256":PROJECTION_SHA,
            "parentBinding":PAID_BINDING,"sharedSeconds":a.remaining_seconds,
            "memoryMiB":a.memory_mib,"allMatricesTemporary":True,
            "noFullConstantEliminationRepeated":True,
            "noRationalNormalFormRepeated":True,
            "noHigherOrderOrNewPrimeComputed":True,
            "paidTrueQProjectedPositiveExponents":[1,1,1,1,1,1,1,2,3]})
        seq,rows,cols=read_projection(a,paid,result)
        phases,positive,covered=projected_smith(a,seq,rows,cols,result)
        ranks={v["exponent"]:v["rank"] for v in phases}
        stable_prefix=(ranks.get(0)==133 and ranks.get(1)==7)
        beta2=ranks.get(2)
        beta3=ranks.get(3)
        result["parameters"]["conclusion"]={
            "projectedFieldConstantRank":ranks.get(0),
            "projectedFieldFirstConnectionRank":ranks.get(1),
            "projectedFieldSecondConnectionRank":beta2,
            "projectedFieldThirdConnectionRank":beta3,
            "constantAndFirstPagesAgreeWithQ":stable_prefix,
            "projectionSecondConnectionDropsAt11":
                (beta2==0) if stable_prefix and beta2 is not None else None,
            "projectionSecondConnectionRetainsRankOneAt11":
                (beta2==1) if stable_prefix and beta2 is not None else None,
            "trueQProjectedSecondConnectionRank":1,
            "actualFullFieldSecondConnectionRank":0,
            "fullCharacteristicZeroSecondConnectionRankStillIn":[0,1],
            "projectedFieldLengthExact":sum(positive) if covered==142 else None,
            "projectedFieldPositiveExponentsExact":positive if covered==142 else None,
            "noFullCharacteristicZeroLengthUpperBoundInferred":True,
            "noOriginalTargetLocalMembershipConclusion":True}
        result["status"]="completed"
    except TimeoutError as exc:
        result["status"]="budget-paused";result["error"]=str(exc);status=124
    except Exception as exc:
        result["status"]="failed";result["error"]=type(exc).__name__+": "+str(exc);status=1
    finally:
        result["elapsedSeconds"]=time.monotonic()-start
        require(len(canonical(result))<65000,"Small reproducible receipt")
        atomic_json(out/"two-same-original-projected-field11-diagnostic-receipt.json",result)
        print(canonical(result).decode("ascii"),flush=True)
    return status

if __name__=="__main__":raise SystemExit(main())
