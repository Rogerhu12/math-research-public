#!/usr/bin/env python3
"""One fixed two-degree-block joint-source LLL trial on the paid p768 R150 infinity kernel.

Astra-ISP-789f / normal_annihilator; AI-assisted, GPT-6 Astra Pro.
2026-11-15. No new Dixon digit, normal form, prime, or source column.
The only published output is a small receipt. Full candidates remain temporary.
"""
import argparse
import hashlib
import importlib.util
import json
import math
import os
import pathlib
import resource
import signal
import sys
import time
import traceback
from fractions import Fraction

sys.dont_write_bytecode = True
P, ROWS, COLS, OUTPUTS = 31, 6188, 36, 4367
HELPER_SHA = "9332d9d394b1a17444c9ccc20b3971cf74b7e932cffc8d9189e4e2f64fe0c428"
SOURCE_BYTES = 36433748
SOURCE_SHA = "0ea5c472aa4013242357ae671b42226b217f61948ee741334eb8a1df0e5dbd07"
PAID_BYTES = 5978318
PAID_SHA = "fa3f1ae516dd7c8a4f366936b75d607010587b5a7b85b804e3d9002964b65b25"
EXPECTED_REMAINING = [17,18,19,26,27,28,29,30,31,32,33,34,35]

class BudgetExpired(Exception):
    pass

def require(ok, message):
    if not ok:
        raise ValueError(message)

def atomic_json(path, obj):
    tmp = path.with_name(path.name + ".tmp")
    with tmp.open("w", encoding="utf-8") as f:
        json.dump(obj, f, ensure_ascii=False, sort_keys=True, separators=(",", ":"))
        f.write("\n")
    os.replace(tmp, path)

def add_mod31(row, basis):
    v = [x % P for x in row]
    for pivot in sorted(basis):
        a = v[pivot]
        if a:
            b = basis[pivot]
            v = [(x-a*y) % P for x,y in zip(v,b)]
    pivot = next((i for i,x in enumerate(v) if x), None)
    if pivot is None:
        return False
    inv = pow(v[pivot], -1, P)
    basis[pivot] = [(x*inv) % P for x in v]
    return True

def add_rational_row(row, basis):
    """Exact Q row rank, never a modular substitute for the free-block rank."""
    v = [Fraction(x) for x in row]
    for pivot in sorted(basis):
        a = v[pivot]
        if a:
            b = basis[pivot]
            v = [x-a*y for x,y in zip(v,b)]
    pivot = next((i for i,x in enumerate(v) if x), None)
    if pivot is None:
        return False
    a = v[pivot]
    basis[pivot] = [x/a for x in v]
    return True

def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--helper", required=True, type=pathlib.Path)
    ap.add_argument("--source", required=True, type=pathlib.Path)
    ap.add_argument("--source-bytes", required=True, type=int)
    ap.add_argument("--source-sha256", required=True)
    ap.add_argument("--source-receipt", required=True, type=pathlib.Path)
    ap.add_argument("--paid-certificates", required=True, type=pathlib.Path)
    ap.add_argument("--point-model", required=True, type=pathlib.Path)
    ap.add_argument("--native-model", required=True, type=pathlib.Path)
    ap.add_argument("--out", required=True, type=pathlib.Path)
    ap.add_argument("--seconds", type=float, default=180.0)
    ap.add_argument("--memory-mib", type=int, default=512)
    args = ap.parse_args()
    require(math.isfinite(args.seconds) and 0 < args.seconds <= 180, "shared budget <=180s; native LLL separately bounded by outer process")
    require(0 < args.memory_mib <= 512, "address space <=512 MiB")
    require(args.source_bytes == SOURCE_BYTES and args.source_sha256 == SOURCE_SHA,
            "this one trial is bound to the actual paid p768 source")
    resource.setrlimit(resource.RLIMIT_AS, (args.memory_mib * 1024**2,)*2)
    out = args.out.resolve()
    require(not out.exists() or not any(out.iterdir()), "fresh output directory required")
    out.mkdir(parents=True, exist_ok=True)
    receipt_path = out/"graded-joint-source-lll-receipt.json"
    start = time.monotonic()
    reserve = min(2.0, args.seconds/10)
    deadline = start + args.seconds - reserve
    receipt = {
        "format":"isp-selected-infinity-two-degree-block-lll-p768-v1",
        "status":"running", "secondsLimit":args.seconds, "memoryMiB":args.memory_mib,
        "newDixonDigitsComputed":0, "oldNormalFormsRecomputed":False,
        "sameSelected4354OriginalSources":True,
        "actualSourceExponent":768, "paidExactKernelCount":23,
        "maximumLatticeDimension":39, "maximumCandidateCount":39,
        "newExactKernelDimension":0, "totalFull4367ExactKernelDimension":23,
        "all36Full4367TrueRationalKernelsVerified":False,
        "characteristicZeroSelectedRankBounds":[4318,4331],
        "characteristicZeroSelectedColumnsFull4367RankBounds":[4318,4331],
        "negativeScope":"only the rows of this one deterministic two-degree-block joint-source LLL basis",
        "largeDataUploadedOrCommitted":False, "largeFilesTemporaryOnly":True,
        "parameters": {
            "observationRule":"separately in multiplier degrees <=2 and degree3: greedy original-source order outside all36 free rows, a complete mod31 row basis on the13 unpaid slots",
            "latticeRule":"rows [M*I_k,0] and [observedSourceColumns,I_d], M=31^768",
            "candidateRule":"every LLL basis row; complete 6188 centered source followed by complete 4367 exact integer product",
            "independenceRule":"exact rational rank of the complete 36 free coordinates together with all 23 paid kernels",
            "paidSlotsExcludedOnlyFromNewCombination":True,
            "noCoordinateScanOrSecondLattice":True, "exactlyTheseTwoPredeterminedDegreeBlocks":True,
        },
    }
    candidates, accepted, temporary_files = [], [], []
    completed_candidates = 0
    validated = False
    code = 1
    H = None
    def check():
        if time.monotonic() >= deadline:
            raise BudgetExpired("shared mathematical time budget")
    def alarm(signum, frame):
        raise BudgetExpired("shared mathematical time budget")
    def snapshot():
        receipt["parameters"]["candidates"] = candidates
        receipt["parameters"]["accepted"] = accepted
        receipt["parameters"]["temporaryFiles"] = temporary_files
        receipt["completedCandidateCount"] = completed_candidates
        receipt["mathematicalElapsedSeconds"] = time.monotonic()-start
        atomic_json(receipt_path, receipt)
    try:
        if hasattr(signal, "setitimer"):
            signal.signal(signal.SIGALRM, alarm)
            signal.setitimer(signal.ITIMER_REAL, max(0.001,deadline-time.monotonic()))
        hb = args.helper.read_bytes()
        require(hashlib.sha256(hb).hexdigest() == HELPER_SHA, "paid helper SHA")
        spec = importlib.util.spec_from_file_location("paid_three_coordinate_lll", args.helper)
        H = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(H)
        import flint
        from flint import fmpz_mat
        receipt["pythonFlintVersion"] = getattr(flint,"__version__","unavailable")
        pbytes = args.point_model.read_bytes()
        require(hashlib.sha256(pbytes).hexdigest() == H.POINT_SHA, "same original point model")
        point = json.loads(pbytes)
        selected = H.read_native_selected(args.native_model, point)
        rowterms = H.original_row_terms(point)
        native_receipt = H.read_json(args.source_receipt)
        exponent, binding, values = H.read_source(
            args.source, args.source_bytes, args.source_sha256, native_receipt, check)
        require(exponent == 768, "actual source exponent")
        size, digest = H.file_hash(args.paid_certificates, check)
        require((size,digest) == (PAID_BYTES,PAID_SHA), "same paid23 plain certificate")
        paid = H.read_json(args.paid_certificates)
        free = list(map(int, paid["normalizedFreeOriginalSourceRows"]))
        require(len(free) == len(set(free)) == COLS and set(free) <= selected, "same free sources")
        require(paid.get("allFreeSourceCoordinatesIdentity") is True, "paid free scope")
        certs = list(paid["certificates"])
        require(int(paid["kernelCount"]) == len(certs) == 23, "paid23 count")
        modulus, qbasis, known = P**exponent, {}, {}
        half = modulus//2
        def center(x):
            x %= modulus
            return x-modulus if x > half else x
        for cert in certs:
            slot = int(cert["slot"])
            require(0 <= slot < COLS and slot not in known, "paid slots")
            require(cert.get("all4367ExactIntegerProductsZero") is True and
                    cert.get("all4354SelectedExactIntegerProductsZero") is True,
                    "paid full original exact product")
            den = int(cert["commonDenominator"])
            nums = list(map(int, cert["originalIntegerSourceNumerators"]))
            require(den > 0 and math.gcd(den,P) == 1 and len(nums) == ROWS, "paid source")
            require(int(cert["freeOriginalSource"]) == free[slot], "paid free source")
            actual_free = [nums[r-1] for r in free]
            require(actual_free == [den if j == slot else 0 for j in range(COLS)],
                    "paid exact free normalization")
            for r,num in enumerate(nums):
                require(r+1 in selected or num == 0, "paid selected-source support")
                require((num-den*values[r*COLS+slot]) % modulus == 0, "paid source/p768 congruence")
                if r % 1024 == 0:
                    check()
            require(add_rational_row(actual_free,qbasis), "paid free Q independence")
            known[slot] = cert
        remaining = [j for j in range(COLS) if j not in known]
        require(remaining == EXPECTED_REMAINING, "actual remaining13 after paid23")
        for r in range(ROWS):
            if r+1 not in selected:
                require(all(values[r*COLS+j] == 0 for j in range(COLS)), "p768 selected support")
            if r % 512 == 0:
                check()
        for i,r in enumerate(free):
            require([values[(r-1)*COLS+j] for j in range(COLS)] ==
                    [int(i==j) for j in range(COLS)], "actual complete free I36")
        validated = True
        receipt["parameters"].update({
            "helperSHA256":HELPER_SHA,
            "scriptSHA256":H.file_hash(pathlib.Path(__file__),check)[1],
            "sourceRawBytes":SOURCE_BYTES, "sourceRawSHA256":SOURCE_SHA,
            "sourceBinding":binding, "paidBytes":PAID_BYTES, "paidSHA256":PAID_SHA,
            "pointModelSHA256":H.POINT_SHA, "nativeModelSHA256":H.NATIVE_SHA,
            "sourceReceipt":dict(zip(("bytes","sha256"),H.file_hash(args.source_receipt,check))),
            "normalizedFreeOriginalSourceRows":free, "remainingSlots":remaining,
            "paidFreeMatrixRankOverQ":len(qbasis),
        })
        free_set, observed_rows, observed = set(free), [], []
        d = len(remaining)
        block_receipts = []
        # Original ordering: 17 equations for each monomial of degrees0,1,2,3.
        # 17*(1+11+66)=1326 is the last original source of multiplier degree<=2.
        for block_name, first, last in [
            ("multiplier-degree-at-most-two",0,1326),
            ("multiplier-degree-three",1326,ROWS)]:
            mbasis, chosen_rows = {}, []
            for r in range(first,last):
                if r+1 not in free_set and r+1 in selected:
                    row = [center(values[r*COLS+j]) for j in remaining]
                    if add_mod31(row,mbasis):
                        chosen_rows.append(r+1)
                        observed_rows.append(r+1)
                        observed.append(row)
                        if len(mbasis) == d:
                            break
                if r % 256 == 0:
                    check()
            block_receipts.append({
                "block":block_name,"originalSourceInclusiveRange":[first+1,last],
                "rowRankModulo31":len(mbasis),
                "chosenOriginalSourceRows":chosen_rows,
                "completeBlockRowSpaceSpannedModulo31":True,
            })
        joint_basis = {}
        for row in observed:
            add_mod31(row,joint_basis)
        k = len(observed)
        dim = d+k
        require(k <= 2*d and dim <= 39,"fixed two-block lattice dimension")
        receipt["parameters"].update({
            "observationBlocks":block_receipts,
            "observationOriginalSourceRows":observed_rows,
            "observationRowCount":k,
            "observationMatrixRankModulo31":len(joint_basis),
            "observationMatrixSHA256":H.canonical_hash(x for row in observed for x in row),
            "actualLatticeDimension":dim, "actualCandidateCount":dim,
        })
        L = []
        for i in range(k):
            L.append([modulus if j==i else 0 for j in range(k)] + [0]*d)
        for j in range(d):
            L.append([observed[i][j] for i in range(k)] +
                     [int(j==a) for a in range(d)])
        lattice = fmpz_mat(L)
        check()
        # A prior 60s Python alarm was delivered only after native LLL returned
        # at 84.744s; no basis survived that attempt. Repeat the SAME lattice,
        # retain its full exact basis/transform before consulting the shared
        # deadline, and rely on the request's 225s hard outer process bound.
        snapshot()
        if hasattr(signal, "setitimer"):
            signal.setitimer(signal.ITIMER_REAL, 0)
        lll_start = time.monotonic()
        reduced, transform = lattice.lll(transform=True,delta=0.99,eta=0.51)
        require(transform*lattice == reduced and abs(int(transform.det())) == 1,
                "complete unimodular LLL row transformation")
        checkpoint_path = out/"temporary-exact-lll-basis-and-transform.json"
        atomic_json(checkpoint_path, {
            "format":"isp-temporary-exact-lll-basis-transform-v1",
            "sourceSHA256":SOURCE_SHA, "sourceExponent":exponent,
            "sourceBinding":binding, "remainingSlots":remaining,
            "observationOriginalSourceRows":observed_rows,
            "observationRowCount":k, "dimension":dim,
            "basis":[[str(reduced[i,j]) for j in range(dim)] for i in range(dim)],
            "transform":[[str(transform[i,j]) for j in range(dim)] for i in range(dim)],
            "unimodularTransformationVerified":True,
            "temporaryOnly":True, "doNotUpload":True,
        })
        checkpoint_bytes, checkpoint_sha = H.file_hash(checkpoint_path)
        receipt["parameters"]["temporaryLLLCheckpoint"] = {
            "file":checkpoint_path.name, "bytes":checkpoint_bytes,
            "sha256":checkpoint_sha, "temporaryOnly":True,
        }
        receipt["parameters"]["sameLatticeRepeatedAfterUnretainedNativeTimeout"] = True
        receipt["parameters"]["nativeLLLProtectedUntilCheckpoint"] = True
        receipt["parameters"]["hardOuterProcessSeconds"] = 225
        receipt["parameters"]["lllUnimodularTransformationVerified"] = True
        receipt["parameters"]["lllSeconds"] = time.monotonic()-lll_start
        snapshot()
        check()
        if hasattr(signal, "setitimer"):
            signal.setitimer(signal.ITIMER_REAL, max(0.001, deadline-time.monotonic()))
        receipt["parameters"].update({
            "lllSeconds":time.monotonic()-lll_start,
            "lllUnimodularTransformationVerified":True,
            "lllBasisSHA256":H.canonical_hash(int(reduced[i,j]) for i in range(dim) for j in range(dim)),
            "lllTransformSHA256":H.canonical_hash(int(transform[i,j]) for i in range(dim) for j in range(dim)),
        })
        snapshot()
        for i in range(dim):
            check()
            row = [int(reduced[i,j]) for j in range(dim)]
            c = row[k:]
            require(all((row[a]-sum(c[j]*observed[a][j] for j in range(d))) % modulus == 0
                        for a in range(k)), "LLL actual observed source congruence")
            candidate = {
                "basisRow":i, "freeCombinationSHA256":H.canonical_hash(c),
                "maximumCombinationCoefficientBits":max((abs(x).bit_length() for x in c),default=0),
                "rankBefore":len(qbasis),
            }
            candidates.append(candidate)
            # All 6188 original source coefficients are formed, including zeros.
            nums = []
            for r in range(ROWS):
                nums.append(center(sum(values[r*COLS+j]*a for j,a in zip(remaining,c))))
                if r % 128 == 0:
                    check()
            expected_free = [0]*COLS
            for j,a in zip(remaining,c):
                expected_free[j] = center(a)
            actual_free = [nums[r-1] for r in free]
            require(actual_free == expected_free, "all36 actual centered free coordinates")
            require(all(r+1 in selected or num == 0 for r,num in enumerate(nums)),
                    "all6188 actual selected-source support")
            product = H.exact_product(nums,rowterms,check)
            bad = [j for j,x in enumerate(product) if x]
            candidate.update({
                "all6188CenteredOriginalSourceCoordinatesFormed":True,
                "all4354SelectedOriginalSourcesRetained":True,
                "all4367ExactIntegerProductComputed":True,
                "maximumNumeratorBits":max((abs(x).bit_length() for x in nums),default=0),
                "full4367IntegerProductSHA256":H.canonical_hash(product),
                "nonzeroOriginalOutputCount":len(bad),
            })
            if bad:
                b = bad[0]
                candidate.update({
                    "status":"rejected-nonzero-full-original-integer-product",
                    "firstNonzeroOriginalOutputIndexZeroBased":b,
                    "firstNonzeroResidualBits":abs(product[b]).bit_length(),
                    "firstNonzeroResidualSHA256":H.canonical_hash([product[b]]),
                })
            elif not any(actual_free):
                require(not any(nums), "free-zero centered candidate must be zero")
                candidate["status"] = "verified-zero-candidate"
            else:
                common = 0
                for num in nums:
                    common = math.gcd(common,abs(num))
                require(common > 0, "nonzero source gcd")
                nums = [num//common for num in nums]
                actual_free = [nums[r-1] for r in free]
                first = next(x for x in actual_free if x)
                if first < 0:
                    nums = [-x for x in nums]
                    actual_free = [-x for x in actual_free]
                # Division/sign preserve an already exact zero original product.
                require(all(nums[r-1] == actual_free[j] for j,r in enumerate(free)),
                        "primitive actual free block")
                candidate["primitiveSourceSHA256"] = H.canonical_hash(nums)
                candidate["primitiveFreeBlockSHA256"] = H.canonical_hash(actual_free)
                independent = add_rational_row(actual_free,qbasis)
                candidate["independentOfAllPaidAndAcceptedOverQ"] = independent
                if independent:
                    accepted_index = len(accepted)
                    filename = "temporary-joint-exact-kernel-%02d.json" % accepted_index
                    certificate = {
                        "format":"isp-full-original-integer-kernel-with-general-free-block-v1",
                        "sourceExponent":exponent, "sourceSHA256":SOURCE_SHA,
                        "basisRow":i, "commonIntegerDivisorRemoved":str(common),
                        "originalIntegerSourceNumerators":list(map(str,nums)),
                        "normalizedFreeOriginalSourceRows":free,
                        "actual36FreeIntegerCoordinates":list(map(str,actual_free)),
                        "all4367ExactIntegerProductsZero":True,
                        "all4354SelectedOriginalSourcesRetained":True,
                        "all6188OriginalSourceCoordinatesRetained":True,
                        "sourceCanonicalSHA256":candidate["primitiveSourceSHA256"],
                        "temporaryOnly":True, "doNotUpload":True,
                    }
                    atomic_json(out/filename,certificate)
                    n,h = H.file_hash(out/filename,check)
                    temp = {"file":filename,"bytes":n,"sha256":h,"temporaryOnly":True}
                    temporary_files.append(temp)
                    accepted.append({
                        "basisRow":i, "temporaryCertificate":temp,
                        "sourceCanonicalSHA256":candidate["primitiveSourceSHA256"],
                        "freeBlockSHA256":candidate["primitiveFreeBlockSHA256"],
                        "complete36FreeRankOverQAfter":len(qbasis),
                    })
                    candidate["status"] = "accepted-new-full-original-kernel-direction"
                else:
                    candidate["status"] = "verified-exact-kernel-already-in-paid-free-span"
            completed_candidates += 1
            candidate["rankAfter"] = len(qbasis)
            receipt["newExactKernelDimension"] = len(qbasis)-23
            receipt["totalFull4367ExactKernelDimension"] = len(qbasis)
            receipt["all36Full4367TrueRationalKernelsVerified"] = len(qbasis)==36
            receipt["characteristicZeroSelectedRankBounds"] = [4318,4354-len(qbasis)]
            receipt["characteristicZeroSelectedColumnsFull4367RankBounds"] = [4318,4354-len(qbasis)]
            snapshot()
            print(json.dumps({
                "phase":"graded-joint-source-lll-original-product","basisRow":i,
                "status":candidate["status"],"exactKernelDimension":len(qbasis)}),flush=True)
        receipt["status"]="completed"
        receipt["allLatticeRowsCompletedFullOriginalCheck"]=completed_candidates==dim
        code=0
    except BudgetExpired as e:
        receipt["status"]="budget-exhausted"
        receipt["error"]=str(e)
        code=75
    except Exception as e:
        receipt["status"]="failed"
        receipt["error"]=str(e)
        receipt["exceptionType"]=type(e).__name__
        (out/"exception.log").write_text(traceback.format_exc(),encoding="utf-8")
        code=1
    finally:
        if hasattr(signal,"setitimer"):
            signal.setitimer(signal.ITIMER_REAL,0)
        receipt["paidInputsCompletelyValidated"]=validated
        receipt["parameters"]["largeDataPolicy"]="temporary same-job files only; no Git, Release, or large artifact"
        receipt["parameters"]["negativeScope"]=receipt["negativeScope"]
        snapshot()
        require(receipt_path.stat().st_size < 100000,"published receipt must remain below100KB")
    print(json.dumps({key:receipt.get(key) for key in [
        "status","actualSourceExponent","completedCandidateCount","newExactKernelDimension",
        "totalFull4367ExactKernelDimension","all36Full4367TrueRationalKernelsVerified",
        "characteristicZeroSelectedRankBounds","mathematicalElapsedSeconds"]}),flush=True)
    return code

if __name__=="__main__":
    sys.exit(main())
