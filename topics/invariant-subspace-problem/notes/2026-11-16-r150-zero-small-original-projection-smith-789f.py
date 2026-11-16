#!/usr/bin/env python3
"""Exact ORIGINAL zero-chart 224 by 155 projection, independently of infinity.

Use the already published Schur helper only as an imported arithmetic engine.
Rebuild the zero chart from ORIGINAL_K and the original physical seventeen
equations.  Keep all 170 pure source rows and 54 ACTUAL one-normal rows,
including their s^2 factor.  Eliminate the other 864 rows only by whole
polynomial ratios with a nonzero constant denominator.  All 5100 remaining
source rows are checked to project to zero.  Every new finite Smith chain
is checked on all 6188 original source rows after zero extension.

The paid generic rank142 and full zero spectrum66/max11 are mathematical
input theorems, pinned below; no infinity spectrum or fifth cochain value
is used.  Fourteen positive directions must actually exit.  No value of
the zero projection length, or of the relative length, is prefilled.
Only complete phases are reusable.  All arrays remain in the Actions tmp.
Author: Astra-ISP-789f / normal_annihilator.
AI-assisted: GPT-6 Astra Pro.
"""
import argparse
import hashlib
import importlib.util
import json
import os
from pathlib import Path
import resource
import signal
import time

from flint import fmpq

FORMAT = "r150-zero-small-original-projection-smith-v1"
CHECKPOINT_FORMAT = "r150-zero-small-original-projection-temporary-v1"
RECEIPT_NAME = "zero-small-original-projection-smith-receipt.json"
PINS = {
    "schur_helper": (37379, "dc17dc88a5f1415c648b6ba5bf3fab4f7fb810aef6cc1552a5b2ea4acacbdf79"),
    "generator": (15328, "2757b900480fe3bf1450100188df1679801351f0330d609e1a39b9c7ca146186"),
    "jet_actions": (10050, "2ebf418575df39ca2ed0a2165a37e92071c415b4734969c5bedc64e0b9ef4332"),
    "zero_full_proof": (11871, "3cad75a461aba1da02f41510d41f3d684a18ab64fd0d9deead0bab3ab3f39f80"),
    "generic_image_proof": (11857, "53fd48dbeb2dd2f16e8d0c3efee9c595fb9ae826528b86bea18de0048a8febbd"),
}
PAID_ZERO_POSITIVE = [1,1,1,1,3,4,4,4,5,6,7,8,10,11]
REC = None
OUT = None

def require(ok, message):
    if not ok:
        raise ValueError(message)

def sha(path):
    h = hashlib.sha256()
    with Path(path).open("rb") as f:
        for block in iter(lambda: f.read(1048576), b""):
            h.update(block)
    return h.hexdigest()

def canonical(x):
    return json.dumps(x, sort_keys=True, separators=(",",":"), ensure_ascii=True).encode("ascii")

def write_json(path, obj):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    tmp = path.with_name(path.name + ".tmp")
    tmp.write_text(json.dumps(obj, sort_keys=True, indent=2) + "\n", encoding="utf-8")
    os.replace(tmp, path)

def flush():
    if REC is None or OUT is None:
        return
    obj = {k:v for k,v in REC.items() if not k.startswith("_")}
    obj["elapsedSeconds"] = time.monotonic() - REC["_start"]
    write_json(OUT / RECEIPT_NAME, obj)

def pinned(path, pin, label):
    path = Path(path)
    require(path.is_file() and path.stat().st_size == pin[0], label + " byte count")
    digest = sha(path)
    require(digest == pin[1], label + " SHA256")
    return {"bytes":pin[0], "sha256":digest}

def import_at(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod

def build_zero_projection(e, m, j, store, degree):
    cached = store.load("original-zero-projection-coefficients", e.DQ)
    if cached is not None:
        c = e.coefficient_decode(cached["coefficients"])
        require(c["chart"] == "zero" and c["maxOrder"] == degree,
                "Stored ORIGINAL zero chart and degree")
        return c, cached["P"], cached["metadata"]
    e.check("original zero-chart coefficient generation")
    c = j.original_coefficients(m, "zero", degree)
    require(c["chart"] == "zero" and c["maxOrder"] == degree,
            "New ORIGINAL zero chart and degree")
    source = [j.source_rows(r) for r in range(4)]
    target = [j.target_columns(r) for r in range(6)]
    require([len(x) for x in source] == [170,918,2295,2805],
            "All6188 original source records")
    require([len(x) for x in target] == [20,135,450,990,1485,1287],
            "All4367 original target records")
    require(len(set(row for rows in source for row in rows)) == 6188,
            "Original source records have no repetition")
    require(len(set(col for cols in target for col in cols)) == 4367,
            "Original output records have no repetition")
    ix0 = {v:i for i,v in enumerate(target[0])}
    ix1 = {v:i for i,v in enumerate(target[1])}

    # Entire degree<=14 pure polynomials, using the ORIGINAL K, not R K R.
    K = [[fmpq(v) for v in row] for row in m.ORIGINAL_K]
    require(len(K) == 6 and all(len(row) == 6 for row in K),
            "Original physical six by six K")
    fullpure = [[fmpq(0)] * 17 for _ in range(15)]
    for power, value in {2:24, 3:-8, 4:-2}.items():
        for aa in range(6):
            for bb in range(6):
                for ii in range(6):
                    for jj in range(6):
                        fullpure[power+aa+bb][ii+jj] += 4*value*K[ii][aa]*K[jj][bb]
    require(all(c["pure"][k] == (fullpure[k] if k < 15 else [fmpq(0)]*17)
                for k in range(degree+1)),
            "All17 whole zero-chart pure geometric coefficients")
    require(all(not fullpure[k][eq] for k in (0,1) for eq in range(17)),
            "Original zero pure rows all retain s^2")
    retained_eq = next((eq for eq in range(17) if fullpure[2][eq]), None)
    require(retained_eq is not None, "Actual whole pure coefficient with valuation2")
    denominator = [fullpure[k][retained_eq] for k in range(2,15)]
    require(denominator[0] != 0, "Retained pure factor divided by s^2 is a Q[[s]] unit")
    # This value follows independently from the original K first column.
    require(retained_eq == 8 and denominator[0] == 2400,
            "Actual ORIGINAL zero eq8 denominator constant2400")
    numerators = [[fullpure[k][eq] for k in range(2,15)] for eq in range(17)]
    ratios = []
    for eq in range(17):
        e.check("whole regular zero-source ratio")
        rr = []
        for k in range(degree-1):
            rhs = numerators[eq][k] if k < len(numerators[eq]) else fmpq(0)
            for v in range(1, min(k, len(denominator)-1)+1):
                rhs -= denominator[v] * rr[k-v]
            rr.append(rhs / denominator[0])
        for k in range(degree+1):
            value = sum((fullpure[i][retained_eq] * rr[k-i]
                         for i in range(2, min(k,14)+1) if k-i < len(rr)),
                        fmpq(0))
            require(value == c["pure"][k][eq],
                    "Complete actual regular source-ratio prefix")
        left = e.poly_product(numerators[eq], [row[retained_eq] for row in fullpure])
        right = e.poly_product(denominator, [row[eq] for row in fullpure])
        require(left == right, "Whole polynomial source-ratio identity, no inversion of s")
        ratios.append(rr)

    chosen = [i for i,row in enumerate(source[1]) if row[0] == retained_eq]
    require(len(chosen) == 54, "All54 actual selected one-normal source rows")
    group = {(a,b,mon):i for i,(eq,a,b,mon) in enumerate(source[1])
             if eq == retained_eq}
    require(len(group) == 54, "One actual selected source for each multiplier")
    PM = []
    projected_checks = 0
    high_empty_checks = 0
    for k in range(degree+1):
        e.check("complete original zero projection coefficient " + str(k))
        top = e.DQ.cat([j.block(m,c,k,0,0), j.block(m,c,k,0,1)])
        require((top.nrows(), top.ncols()) == (170,155), "Actual pure-source projection")
        bottom = e.DQ.mat(54,155)
        for r, si in enumerate(chosen):
            eq,a,b,mon = source[1][si]
            terms0 = list(j.sparse_row_terms(c,k,source[1][si],0,ix0))
            terms1 = list(j.sparse_row_terms(c,k,source[1][si],1,ix1))
            require(not terms0, "Retained one-normal source has no pure output")
            for col,value in terms1:
                bottom[r,20+col] += value
            require(bottom[r,20+ix1[(a,b+2,mon)]] == c["pure"][k][retained_eq],
                    "Selected original source retains complete F8, including s^2")
        PM.append(e.DQ.vcat([top,bottom]))
        for row in source[1]:
            eq,a,b,mon = row
            terms0 = list(j.sparse_row_terms(c,k,row,0,ix0))
            terms1 = list(j.sparse_row_terms(c,k,row,1,ix1))
            expected = [] if not c["pure"][k][eq] else [
                (ix1[(a,b+2,mon)], c["pure"][k][eq])]
            require(not terms0 and terms1 == expected,
                    "Every one of918 actual projected source rows")
            require((a,b,mon) in group, "Eliminated row has its actual retained source row")
            projected_checks += 1
        for sd in (2,3):
            for row in source[sd]:
                require(not list(j.sparse_row_terms(c,k,row,0,ix0)) and
                        not list(j.sparse_row_terms(c,k,row,1,ix1)),
                        "Every high-normal original source projects exactly to zero")
                high_empty_checks += 1
    require(e.rank(PM[0]) == 128, "Actual zero projection constant rank128")
    meta = {
        "chart":"zero", "originalParameter":"s",
        "originalKReversed":False, "projectionShape":[224,155],
        "originalSourceCount":6188, "originalOutputCount":4367,
        "sourceNormalDegreeCounts":[170,918,2295,2805],
        "outputNormalDegreeCounts":[20,135,450,990,1485,1287],
        "pureSourceRowsRetained":170, "oneNormalSourceRows":918,
        "retainedActualOneNormalRows":54, "regularlyEliminatedActualRows":864,
        "identicallyZeroProjectedHighSourceRows":5100,
        "actualRetainedEquationZeroBased":retained_eq,
        "actualRetainedSourceIndicesWithinOneNormal":chosen,
        "actualPureCommonParameterOrder":2,
        "pureDenominatorUnitConstant":str(denominator[0]),
        "wholePureNumeratorCoefficients":[[str(x) for x in row] for row in numerators],
        "wholePureDenominatorCoefficients":[str(x) for x in denominator],
        "all17WholePurePolynomialsVerified":True,
        "all918ActualProjectedRowsVerified":True,
        "all5100HigherNormalOriginalSourceRowsExactlyZero":True,
        "regularOriginalSourceOperationsRetainS2Factor":True,
        "oneNormalCoefficientRowChecks":projected_checks,
        "highNormalCoefficientEmptyRowChecks":high_empty_checks,
        "actualConstantRank":128, "originalCoefficientOrder":degree,
        "originalProjectionCoefficientSHA256":[e.mh(X) for X in PM],
        "originalPhysicalCoefficientHashes":c["physical"],
        "all6188OriginalSourceDictionarySHA256":hashlib.sha256(
            canonical([row for rows in source for row in rows])).hexdigest(),
        "all4367OriginalOutputDictionarySHA256":hashlib.sha256(
            canonical([col for cols in target for col in cols])).hexdigest(),
    }
    store.save("original-zero-projection-coefficients",
               {"coefficients":e.coefficient_encode(c), "P":PM,
                "regularSourceRatioPrefixes":[[str(x) for x in row] for row in ratios],
                "metadata":meta}, e.DQ)
    e.small_event("original-zero-projection-complete",
                  degree=degree, constantRank=128, retainedEquation=retained_eq)
    return c,PM,meta

def verify_all_original(e,m,j,c,PM,state,meta,store,degree):
    e.check("complete original zero-source verification")
    Top = [e.DQ.sub(X,range(170),range(155)) for X in PM]
    oneindex = {v:i for i,v in enumerate(j.target_columns(1))}
    chosen = meta["actualRetainedSourceIndicesWithinOneNormal"]
    require(len(chosen) == 54, "Original verification retained row dictionary")
    actual = {
        "degree":degree,
        "projection":meta["originalProjectionCoefficientSHA256"],
        "positive":[{"exponent":g["exponent"], "map":[e.mh(X) for X in g["map"]]}
                    for g in state["positive"]],
        "remainingMap":[e.mh(X) for X in state["map"]],
        "complete":state["complete"],
    }
    logical = hashlib.sha256(canonical(actual)).hexdigest()
    progress = store.load("Q-original-zero-verification", e.DQ)
    if progress is None:
        progress = {
            "smithAndOriginalCoefficientBinding":logical,
            "positiveGroupsVerified":0, "freeOrdersVerified":0,
            "zeroProductCoordinates":0, "nonzeroLeadingProductCoordinates":0,
            "positiveOriginalLifts":[], "complete":False}
    require(progress["smithAndOriginalCoefficientBinding"] == logical,
            "Original verification bound to the actual whole Smith maps")
    for gi in range(progress["positiveGroupsVerified"],len(state["positive"])):
        g = state["positive"][gi]
        exponent = g["exponent"]
        L = g["map"]
        width = L[0].ncols()
        for k in range(exponent):
            e.check("complete original positive-chain coefficient")
            A,B = e.original_product(m,j,c,Top,oneindex,L,k)
            require(e.zero(A) and e.zero(B), "All6188 original positive-chain source products")
        A,B = e.original_product(m,j,c,Top,oneindex,L,exponent)
        leading = e.DQ.vcat([A,e.DQ.sub(B,chosen,range(width))])
        require(e.rank(leading) == width,
                "Actual original leading obstruction has full exit rank")
        progress["zeroProductCoordinates"] += 6188*width*exponent
        progress["nonzeroLeadingProductCoordinates"] += 6188*width
        progress["positiveOriginalLifts"].append({
            "exponent":exponent, "columns":width,
            "originalHeadSHA256":e.mh(L[0]),
            "all1088OriginalLeadingRowsSHA256":e.mh(e.DQ.vcat([A,B])),
            "retained224LeadingRowsSHA256":e.mh(leading),
            "allOriginalOrdersBelowExponentZero":True,
            "actualLeadingRank":width})
        progress["positiveGroupsVerified"] = gi+1
        store.save("Q-original-zero-verification",progress,e.DQ)
    L = state["map"]
    cutoff = degree+1 if state["complete"] else min(state["level"],degree+1)
    require(progress["freeOrdersVerified"] <= cutoff, "Stored original verification precision")
    for k in range(progress["freeOrdersVerified"],cutoff):
        e.check("complete original remaining-chain coefficient")
        A,B = e.original_product(m,j,c,Top,oneindex,L,k)
        require(e.zero(A) and e.zero(B), "All6188 original remaining finite-jet products")
        progress["zeroProductCoordinates"] += 6188*L[0].ncols()
        progress["freeOrdersVerified"] = k+1
        store.save("Q-original-zero-verification",progress,e.DQ)
    progress["complete"] = True
    progress["remainingJetColumns"] = L[0].ncols()
    progress["remainingJetVerifiedThroughOrder"] = cutoff-1
    store.save("Q-original-zero-verification",progress,e.DQ)
    REC["parameters"].update({
        "allOriginal6188PositiveAndRemainingJetProductsVerified":True,
        "originalZeroProductCoordinates":progress["zeroProductCoordinates"],
        "originalExitLeadingProductCoordinates":progress["nonzeroLeadingProductCoordinates"],
        "positiveOriginalLifts":progress["positiveOriginalLifts"],
        "remainingOriginalJetCount":L[0].ncols(),
        "remainingOriginalJetVerifiedThroughOrder":cutoff-1,
        "original155ProjectionCoordinatesRetained":True,
        "all6188OriginalSourceRowsRetainedOrExactlyZeroBySupport":True,
        "noFullHighImageSurjectivityAssumed":True,
        "finiteFreeJetsNotAssertedToBeSpecifiedInfiniteKernelBasis":True,
        "originalVerificationLogicalBinding":logical,
    })
    return progress

def main():
    global REC,OUT
    ap = argparse.ArgumentParser()
    ap.add_argument("--schur-helper",required=True)
    ap.add_argument("--generator",required=True)
    ap.add_argument("--jet-actions",required=True)
    ap.add_argument("--zero-full-proof",required=True)
    ap.add_argument("--generic-image-proof",required=True)
    ap.add_argument("--degree",type=int,default=11)
    ap.add_argument("--out",required=True)
    ap.add_argument("--remaining-seconds",type=float,default=180)
    ap.add_argument("--memory-mib",type=int,default=2048)
    a = ap.parse_args()
    require(11 <= a.degree <= 17 and 0 < a.remaining_seconds <= 600,
            "Degree11..17 and positive bounded budget")
    require(512 <= a.memory_mib <= 4096, "Memory bound")
    started = time.monotonic()
    reserve = min(8.0,a.remaining_seconds/10)
    OUT = Path(a.out)
    OUT.mkdir(parents=True,exist_ok=True)
    REC = {
        "format":FORMAT, "status":"running", "outcome":"pending-original-zero-inputs",
        "scriptSHA256":sha(__file__), "arithmetic":"exact characteristic zero Q[[s]] jets",
        "parameters":{
            "sharedMathematicalSeconds":a.remaining_seconds, "memoryMiB":a.memory_mib,
            "TaylorDegree":a.degree, "chart":"zero", "temporaryOnly":True,
            "largeDataUploadedOrCommitted":False, "largeRecomputableDataPersisted":False,
            "infinityProjectionValuesUsed":False, "zeroProjectionLengthNotPrefilled":True,
            "originalPrimitiveScalingTransportUsesPinnedOriginalZeroProof":True},
        "events":[], "_start":started}
    exitcode = 1
    try:
        soft,hard = resource.getrlimit(resource.RLIMIT_AS)
        cap = a.memory_mib*1024*1024
        if hard != resource.RLIM_INFINITY:
            cap = min(cap,hard)
        resource.setrlimit(resource.RLIMIT_AS,(cap,hard))
        inputs = {key:pinned(getattr(a,key),pin,key) for key,pin in PINS.items()}
        named = {
            "format":FORMAT, "sourceSHA256":sha(__file__), "inputs":inputs,
            "degree":a.degree, "chart":"ORIGINAL zero without K reversal",
            "mathematicalPremises":{
                "originalFullGenericRank":4354, "originalProjectionGenericRank":142,
                "originalFullGenericFreeRank":13,
                "completeOriginalZeroPositiveIndices":PAID_ZERO_POSITIVE,
                "completeOriginalZeroLength":66, "completeOriginalZeroMaxExponent":11}}
        binding = hashlib.sha256(canonical(named)).hexdigest()
        REC["parameters"].update({
            "semanticBinding":binding, "inputFiles":inputs,
            "paidMathematicalPremises":named["mathematicalPremises"],
            "originalSourceOutputTransport":"whole degree-preserving binomial units and nonzero constant17 row scales over Q"})
        e = import_at("r150_paid_projection_schur_engine",a.schur_helper)
        m = import_at("r150_zero_projection_original_generator",a.generator)
        j = import_at("r150_zero_projection_original_actions",a.jet_actions)
        # Only task-local metadata/IO globals are replaced.  Arithmetic
        # functions are the unchanged, byte-pinned published helper.
        e.FORMAT = FORMAT
        e.CHECKPOINT_FORMAT = CHECKPOINT_FORMAT
        e.OUT = OUT
        e.REC = REC
        e.DEADLINE = started+a.remaining_seconds-reserve
        e.STOP = False
        e.flush_receipt = flush
        signal.signal(signal.SIGTERM,e.stop_requested)
        signal.signal(signal.SIGINT,e.stop_requested)
        store = e.Store(OUT/"temporary",binding)
        c,PM,meta = build_zero_projection(e,m,j,store,a.degree)
        REC["parameters"]["originalProjection"] = meta
        state,info = e.smith(PM,e.DQ,store,a.degree)
        verify_all_original(e,m,j,c,PM,state,meta,store,a.degree)
        REC["parameters"]["projectionIsActualOriginalCokernelQuotient"] = True
        REC["parameters"]["fullAndProjectionGenericFreeRanksBoth13"] = True
        REC["parameters"]["fourteenPositiveExitsRequiredNotAssumed"] = True
        if info["complete"]:
            require(len(info["positiveIndices"]) == 14 and info["freeRank"] == 13,
                    "Complete actual zero projection rank142 and free13")
            require(info["positiveLength"] <= 66 and info["maxPositiveIndex"] <= 11,
                    "Actual projection quotient of the paid full zero torsion")
            require(all(x <= y for x,y in zip(info["positiveIndices"],PAID_ZERO_POSITIVE)),
                    "Actual ordered projection Smith exponents bounded by full exponents")
            relative_length = 66-info["positiveLength"]
            REC["status"] = "completed"
            REC["outcome"] = "complete-original-zero-characteristic-zero-projection-smith"
            REC["parameters"].update({
                "characteristicZeroProjectionPositiveIndices":info["positiveIndices"],
                "characteristicZeroProjectionTorsionLength":info["positiveLength"],
                "characteristicZeroProjectionMaximumPositiveExponent":info["maxPositiveIndex"],
                "characteristicZeroProjectionConstantRank":128,
                "characteristicZeroProjectionGenericRank":142,
                "characteristicZeroProjectionFreeRank":13,
                "paidFullZeroTorsionLength":66,
                "characteristicZeroRelativeZeroTorsionLength":relative_length,
                "relativeLengthUsesOriginalExactSequenceAndEqualGenericFreeRanks":True,
                "allFourteenOriginalPositiveDirectionsActuallyExited":True,
                "allThirteenRemainingOriginalFiniteJetsVerified":True,
                "zeroProjectionEqualsInfinityNotAssumed":True,
                "jointNineTargetEqualityNotClaimedByThisCalculation":True})
            store.save("Q-zero-projection-complete-summary",
                       {"smith":info,"relativeLength":relative_length,
                        "allOriginalProductsVerified":True},e.DQ)
            exitcode = 0
        else:
            REC["status"] = "completed-prefix"
            REC["outcome"] = "actual-zero-projection-prefix-not-complete"
            REC["parameters"]["noUnfinishedSmithDirectionsDropped"] = True
            exitcode = 75
    except TimeoutError as err:
        REC["status"] = "checkpointed-time-budget-or-signal"
        REC["outcome"] = "complete-original-zero-phases-retained"
        REC["parameters"]["error"] = {"type":type(err).__name__,"message":str(err)}
        exitcode = 75
    except BaseException as err:
        REC["status"] = "failed"
        REC["outcome"] = "original-zero-projection-check-failed"
        REC["parameters"]["error"] = {"type":type(err).__name__,"message":str(err)}
        exitcode = 1
    finally:
        flush()
        print(json.dumps({"status":REC["status"],"outcome":REC["outcome"],
                          "receipt":str(OUT/RECEIPT_NAME),
                          "elapsedSeconds":time.monotonic()-started},sort_keys=True))
    return exitcode

if __name__ == "__main__":
    raise SystemExit(main())
