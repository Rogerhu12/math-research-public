#!/usr/bin/env python3
"""One deterministic three-coordinate LLL attempt on an actual R150 checkpoint.

Astra-ISP-789f; AI-assisted, GPT-6 Astra Pro; 2026-11-15.
No Dixon digits, new prime, coordinate scan, or selected-only certificate.
python-flint 0.9: fmpz_mat.lll(transform=True) returns (L,T), L=T*M.
https://python-flint.readthedocs.io/en/latest/fmpz_mat.html#flint.fmpz_mat.lll

Large source/certificate files below are temporary same-job working files.
Never archive/upload them; preserve this script, parameters, run ID and hashes.
Only the small receipt is suitable for the repository.
"""
import argparse
import gzip
import hashlib
import itertools
import json
import math
import os
import pathlib
import resource
import signal
import struct
import sys
import time
import traceback

sys.dont_write_bytecode = True
P, ROWS, COLS, OUTPUTS = 31, 6188, 36, 4367
POINT_SHA = "97d31570a0bd99d33066fc6ea47984203b2964521ceeb50920f0a49dd3bb8074"
NATIVE_SHA = "291062a79112191f52dccf8ac066c72b735c76936199c1366a30d3824a63cac6"
SOURCE_MAGIC = b"R150BK31"

class BudgetExpired(Exception):
    pass

def canonical_hash(parts):
    h = hashlib.sha256()
    for x in parts:
        h.update(str(x).encode("ascii"))
        h.update(b"\n")
    return h.hexdigest()

def file_hash(path, check=lambda: None):
    h, n = hashlib.sha256(), 0
    with path.open("rb") as f:
        while True:
            b = f.read(1 << 20)
            if not b:
                break
            h.update(b)
            n += len(b)
            check()
    return n, h.hexdigest()

def save_json(path, data):
    tmp = path.with_name(path.name + ".tmp")
    with tmp.open("w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, sort_keys=True, separators=(",", ":"))
        f.write("\n")
    os.replace(tmp, path)

def read_json(path):
    with path.open("rb") as f:
        magic = f.read(2)
    opener = gzip.open if magic == b"\x1f\x8b" else open
    with opener(path, "rt", encoding="utf-8") as f:
        return json.load(f)

def save_temporary_certificates(path, data):
    tmp = path.with_name(path.name + ".tmp")
    # Deterministic gzip header; this remains an ephemeral same-job file.
    import io
    with tmp.open("wb") as raw:
        with gzip.GzipFile(filename="", mode="wb", fileobj=raw,
                           compresslevel=1, mtime=0) as compressed:
            with io.TextIOWrapper(compressed, encoding="utf-8",
                                  newline="\n") as text:
                json.dump(data, text, ensure_ascii=False, sort_keys=True,
                          separators=(",", ":"))
                text.write("\n")
    os.replace(tmp, path)

def require(condition, message):
    if not condition:
        raise ValueError(message)

def read_native_selected(native, model):
    raw = native.read_bytes()
    require(hashlib.sha256(raw).hexdigest() == NATIVE_SHA, "native model SHA")
    tokens = raw.decode("ascii").split()
    require(tokens and tokens[0] == "R150_NATIVE_NF_V1", "native magic")
    pos = 1 + 11 * (66 + 11 * 11)
    npre = int(tokens[pos])
    pos += 1
    require(npre == 3333 and len(tokens) >= pos + 4*npre, "native prebasis")
    pre = []
    for j in range(npre):
        e, multkey, pivotkey, original = map(int, tokens[pos+4*j:pos+4*j+4])
        require(0 <= e < 17 and 1 <= original <= ROWS, "native source dictionary")
        require((original-1) % 17 == e, "native equation/source identity")
        pre.append(original)
    extra = list(map(int, model["selectedSourceRows"]))
    require(len(pre) == len(set(pre)) == 3333, "prebasis source uniqueness")
    require(len(extra) == len(set(extra)) == 1021, "selected extra sources")
    selected = set(pre) | set(extra)
    require(len(selected) == 4354, "selected 4354 ORIGINAL SOURCES")
    require(all(1 <= r <= ROWS for r in selected), "selected source range")
    return selected

def read_source(path, expected_size, expected_hash, native_receipt, check):
    size, digest = file_hash(path, check)
    require(size == expected_size and digest == expected_hash,
            "actual raw checkpoint bytes/SHA mismatch")
    with path.open("rb") as f:
        header = f.read(88)
        require(len(header) == 88 and header[:8] == SOURCE_MAGIC, "source header")
        prime, exponent, rows, columns = struct.unpack_from("<IIII", header, 8)
        require((prime, rows, columns) == (P, ROWS, COLS) and exponent > 0,
                "source prime/dimensions/exponent")
        binding = header[24:88].decode("ascii")
        require(len(binding) == 64 and all(c in "0123456789abcdef" for c in binding),
                "source binding format")
        require(native_receipt.get("status") == "completed" and
                int(native_receipt.get("exponent", -1)) == exponent and
                native_receipt.get("inputBinding") == binding,
                "native receipt/exponent/binding")
        flags = [
            "same36FreeOriginalCoordinatesIdentity",
            "all4367FreshExactOriginalProductsVerified",
            "all4367OriginalCoordinatesDivisibleByFullModulus",
            "exactResidualRecurrenceVerified",
            "allActualOriginalSourcesRetained",
        ]
        require(all(native_receipt.get(k) is True for k in flags),
                "native source receipt lacks paid full-original checks")
        values = []
        for j in range(ROWS * COLS):
            small = f.read(3)
            require(len(small) == 3, "truncated source integer header")
            sign, length = small[0], int.from_bytes(small[1:], "little")
            require(sign <= 1 and not (length == 0 and sign), "integer sign/zero")
            b = f.read(length)
            require(len(b) == length and (length == 0 or b[-1] != 0),
                    "noncanonical or truncated integer magnitude")
            x = int.from_bytes(b, "little")
            values.append(-x if sign else x)
            if j % 4096 == 0:
                check()
        require(f.read(1) == b"", "source has trailing bytes")
    return exponent, binding, values

def original_row_terms(model):
    equations = [list(map(int, row)) for row in model["primitivePointCoefficients"]]
    require(len(equations) == 17 and all(len(row) == 77 for row in equations),
            "original 17 x 77 integer polynomial model")
    require(model.get("characteristicZeroSameOriginal17Verified") is True,
            "original characteristic-zero model assertion")
    variables = [8**i for i in range(11)]
    outkeys = [sum(variables[i] for i in indexes)
               for degree in range(5, 0, -1)
               for indexes in itertools.combinations_with_replacement(range(11), degree)]
    require(len(outkeys) == OUTPUTS and len(set(outkeys)) == OUTPUTS,
            "full original 4367 output dictionary")
    index = {k:i for i,k in enumerate(outkeys)}
    multipliers = [sum(variables[i] for i in indexes)
                   for degree in range(4)
                   for indexes in itertools.combinations_with_replacement(range(11), degree)]
    terms = variables + [variables[i]+variables[j]
                         for i in range(11) for j in range(i,11)]
    result = [[(index[mul+terms[j]], c) for j,c in enumerate(equations[e]) if c]
              for mul in multipliers for e in range(17)]
    require(len(result) == ROWS, "original 6188 source dictionary")
    return result

def exact_product(nums, rowterms, check):
    product = [0] * OUTPUTS
    for r, a in enumerate(nums):
        if a:
            for target, c in rowterms[r]:
                product[target] += a*c
        if r % 256 == 0:
            check()
    return product

def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--source", required=True, type=pathlib.Path)
    ap.add_argument("--source-bytes", required=True, type=int)
    ap.add_argument("--source-sha256", required=True)
    ap.add_argument("--source-receipt", required=True, type=pathlib.Path)
    ap.add_argument("--paid-certificates", required=True, type=pathlib.Path)
    ap.add_argument("--point-model", required=True, type=pathlib.Path)
    ap.add_argument("--native-model", required=True, type=pathlib.Path)
    ap.add_argument("--out", required=True, type=pathlib.Path)
    ap.add_argument("--remaining-seconds", "--seconds", dest="seconds",
                    type=float, default=60.0)
    ap.add_argument("--memory-mib", type=int, default=512)
    args = ap.parse_args()
    require(math.isfinite(args.seconds) and 0 < args.seconds <= 60,
            "one actual shared budget, 0 < seconds <= 60")
    require(0 < args.memory_mib <= 512, "memory <= 512 MiB")
    require(args.source_bytes > 0 and len(args.source_sha256) == 64,
            "actual checkpoint size/hash required")
    resource.setrlimit(resource.RLIMIT_AS, (args.memory_mib * 1024**2,)*2)
    start = time.monotonic()
    reserve = min(2.0, args.seconds/10)
    deadline = start + args.seconds - reserve
    out = args.out.resolve()
    require(not out.exists() or not any(out.iterdir()), "new output directory required")
    out.mkdir(parents=True, exist_ok=True)
    receipt_path = out/"three-coordinate-lll-receipt.json"
    temporary_path = out/"exact-rational-kernel-certificates.json.gz"
    receipt = {
        "format":"isp-selected-infinity-fixed-three-coordinate-lll-v1",
        "status":"running", "newDixonDigitsComputed":0,
        "secondsLimit":args.seconds, "memoryMiB":args.memory_mib,
        "coordinateRule":"first three nonzero original source rows outside the 36 free rows",
        "maximumLLLRowsPerSlot":4, "newExactKernelCount":0,
        "attemptedSlots":[], "accepted":[],
        "negativeScope":"only this fixed triple and at most four LLL basis-row denominators",
        "largeFilesTemporaryOnly":True,
        "pythonFlintOfficialAPI":"https://python-flint.readthedocs.io/en/latest/fmpz_mat.html#flint.fmpz_mat.lll",
    }
    paid, certs, known = None, [], {}
    paid_validated = False
    code = 1
    def check():
        if time.monotonic() >= deadline:
            raise BudgetExpired("actual shared time budget")
    def alarm(signum, frame):
        raise BudgetExpired("actual shared time budget")
    try:
        if hasattr(signal, "setitimer"):
            signal.signal(signal.SIGALRM, alarm)
            signal.setitimer(signal.ITIMER_REAL, max(0.001, deadline-time.monotonic()))
        import flint
        from flint import fmpz_mat
        receipt["pythonFlintVersion"] = getattr(flint, "__version__", "unavailable")
        pbytes = args.point_model.read_bytes()
        require(hashlib.sha256(pbytes).hexdigest() == POINT_SHA, "point model SHA")
        point = json.loads(pbytes)
        selected = read_native_selected(args.native_model, point)
        rowterms = original_row_terms(point)
        native_receipt = read_json(args.source_receipt)
        exponent, binding, values = read_source(
            args.source, args.source_bytes, args.source_sha256, native_receipt, check)
        modulus = P**exponent
        half = modulus//2
        def center(x):
            x %= modulus
            return x-modulus if x > half else x
        paid = read_json(args.paid_certificates)
        free = list(map(int, paid["normalizedFreeOriginalSourceRows"]))
        require(len(free) == len(set(free)) == COLS and set(free) <= selected,
                "same 36 normalized original free sources")
        require(paid.get("allFreeSourceCoordinatesIdentity") is True,
                "paid free-coordinate scope")
        certs = list(paid["certificates"])
        require(int(paid["kernelCount"]) == len(certs), "paid kernel count")
        for cert in certs:
            slot = int(cert["slot"])
            require(0 <= slot < COLS and slot not in known, "paid slot uniqueness")
            require(cert.get("all4367ExactIntegerProductsZero") is True and
                    cert.get("all4354SelectedExactIntegerProductsZero") is True,
                    "only paid FULL-original rational kernels may be skipped")
            denominator = int(cert["commonDenominator"])
            nums = list(map(int, cert["originalIntegerSourceNumerators"]))
            require(denominator > 0 and math.gcd(denominator, P) == 1 and len(nums) == ROWS,
                    "paid exact source denominator")
            require(int(cert["freeOriginalSource"]) == free[slot], "paid free source")
            require(all(nums[r-1] == (denominator if j==slot else 0)
                        for j,r in enumerate(free)), "paid exact 36-free normalization")
            for r,num in enumerate(nums):
                require(r+1 in selected or num == 0, "paid selected SOURCE support")
                require((num-denominator*values[r*COLS+slot]) % modulus == 0,
                        "paid exact source does not match this actual checkpoint")
                if r % 1024 == 0:
                    check()
            known[slot] = cert
        for r in range(ROWS):
            if r+1 not in selected:
                require(all(values[r*COLS+j] == 0 for j in range(COLS)),
                        "checkpoint outside selected ORIGINAL SOURCE support")
            if r % 512 == 0:
                check()
        for j,r in enumerate(free):
            require(all(values[(r-1)*COLS+k] == (1 if j==k else 0)
                        for k in range(COLS)), "checkpoint exact free-coordinate I")
        initial_count = len(known)
        paid_validated = True
        input_files = {}
        for name, path in [("sourceReceipt",args.source_receipt),
                           ("paidCertificates",args.paid_certificates)]:
            count, digest = file_hash(path,check)
            input_files[name] = {"bytes":count,"sha256":digest}
        receipt.update({
            "actualSourceExponent":exponent, "sourceBinding":binding,
            "sourceRawBytes":args.source_bytes, "sourceRawSHA256":args.source_sha256,
            "paidKernelCount":initial_count, "samePaidSourceResiduesVerified":True,
            "all4354SelectedOriginalSourcesRetained":True,
            "same36FreeOriginalCoordinatesIdentity":True,
            "pointModelSHA256":POINT_SHA, "nativeModelSHA256":NATIVE_SHA,
            "scriptSHA256":file_hash(pathlib.Path(__file__), check)[1],
            "inputFiles":input_files,
        })
        free_set = set(free)
        for slot in range(COLS):
            if slot in known:
                continue
            check()
            chosen = []
            for r in range(ROWS):
                if r+1 not in free_set:
                    a = center(values[r*COLS+slot])
                    if a:
                        chosen.append((r+1,a))
                        if len(chosen) == 3:
                            break
            slot_receipt = {
                "slot":slot, "freeOriginalSource":free[slot],
                "selectedCoordinateRows":[r for r,a in chosen], "candidates":[],
            }
            receipt["attemptedSlots"].append(slot_receipt)
            if len(chosen) < 3:
                slot_receipt["status"]="skipped-fewer-than-three-nonzero-nonfree-coordinates"
                continue
            aa = [a for r,a in chosen]
            basis = fmpz_mat([
                [modulus,0,0,0],[0,modulus,0,0],[0,0,modulus,0],
                [aa[0],aa[1],aa[2],1]])
            reduced, transform = basis.lll(transform=True, delta=0.99, eta=0.51)
            require(transform*basis == reduced and abs(int(transform.det())) == 1,
                    "LLL row-lattice transformation identity")
            slot_receipt["lllUnimodularTransformationVerified"] = True
            slot_receipt["lllBasisSHA256"] = canonical_hash(
                int(reduced[i,j]) for i in range(4) for j in range(4))
            denominators = set()
            for row in range(4):
                check()
                v = [int(reduced[row,j]) for j in range(4)]
                require(all((v[i]-v[3]*aa[i]) % modulus == 0 for i in range(3)),
                        "original LLL row congruence")
                gcdrow = math.gcd(*map(abs,v))
                require(gcdrow > 0, "LLL nonzero row")
                v = [x//gcdrow for x in v]
                if v[3] < 0:
                    v = [-x for x in v]
                q = v[3]
                item = {
                    "basisRow":row, "denominatorBits":abs(q).bit_length(),
                    "denominatorSHA256":canonical_hash([q]),
                    "rowPrimitiveCongruencePreserved":
                        all((v[i]-q*aa[i]) % modulus == 0 for i in range(3)),
                }
                slot_receipt["candidates"].append(item)
                # Dividing a row gcd need not preserve lattice membership if it
                # contains 31.  q is only a heuristic candidate; all 6188
                # numerators are recomputed below, and exact products decide.
                if q <= 0 or math.gcd(q,P) != 1:
                    item["status"]="rejected-nonpositive-or-nonunit-denominator"
                    continue
                if q in denominators:
                    item["status"]="duplicate-denominator"
                    continue
                denominators.add(q)
                nums = [center(q*values[r*COLS+slot]) for r in range(ROWS)]
                if not all(nums[r-1] == (q if j==slot else 0)
                           for j,r in enumerate(free)):
                    item["status"]="rejected-exact-free-normalization"
                    continue
                require(all(r+1 in selected or n == 0 for r,n in enumerate(nums)),
                        "candidate original selected-source support")
                product = exact_product(nums,rowterms,check)
                bad = [i for i,x in enumerate(product) if x]
                item["nonzeroOriginalOutputCount"]=len(bad)
                item["maximumNumeratorBits"]=max(abs(x).bit_length() for x in nums)
                item["full4367IntegerProductSHA256"]=canonical_hash(product)
                if bad:
                    i = bad[0]
                    item.update({
                        "status":"rejected-nonzero-original-integer-product",
                        "firstNonzeroOriginalOutputIndexZeroBased":i,
                        "firstNonzeroResidualBits":abs(product[i]).bit_length(),
                        "firstNonzeroResidualSHA256":canonical_hash([product[i]]),
                    })
                    continue
                numerator_hash = canonical_hash([q]+nums)
                cert = {
                    "slot":slot, "firstSuccessfulExponent":exponent,
                    "method":"one-fixed-three-coordinate-lll-basis-row",
                    "freeOriginalSource":free[slot], "commonDenominator":str(q),
                    "originalIntegerSourceNumerators":list(map(str,nums)),
                    "all4354SelectedExactIntegerProductsZero":True,
                    "all4367ExactIntegerProductsZero":True,
                    "all36FreeSourceCoordinatesIdentity":True,
                    "all4354SelectedOriginalSourcesRetained":True,
                    "sourceRawSHA256":args.source_sha256,
                    "sourceBinding":binding, "LLLCoordinateRows":[r for r,a in chosen],
                    "LLLBasisRow":row, "originalSourceCanonicalSHA256":numerator_hash,
                }
                certs.append(cert)
                known[slot]=cert
                item["status"]="accepted-full-original-exact-kernel"
                receipt["accepted"].append({
                    "slot":slot, "commonDenominator":str(q),
                    "denominatorBits":q.bit_length(),
                    "originalSourceCanonicalSHA256":numerator_hash,
                    "all4367ExactIntegerProductsZero":True,
                    "all36FreeSourceCoordinatesIdentity":True,
                    "all4354SelectedOriginalSourcesRetained":True,
                })
                receipt["newExactKernelCount"]=len(receipt["accepted"])
                break
            slot_receipt["status"]=(
                "accepted" if slot in known else "fixed-triple-candidates-exhausted")
            print(json.dumps({
                "phase":"fixed-three-coordinate-lll-slot",
                "slot":slot, "status":slot_receipt["status"],
                "newExactKernelCount":len(receipt["accepted"])}),flush=True)
        receipt["status"]="completed"
        receipt["all36AlreadyPaidSkipped"]=initial_count==COLS
        code=0
    except BudgetExpired as e:
        receipt["status"]="budget-exhausted"
        receipt["error"]=str(e)
        code=75
    except Exception as e:
        receipt["status"]="failed"
        receipt["error"]=str(e)
        receipt["exceptionType"]=type(e).__name__
        # The small trace is diagnostic text, not a new mathematical result.
        (out/"exception.log").write_text(traceback.format_exc(),encoding="utf-8")
        code=1
    finally:
        if hasattr(signal,"setitimer"):
            signal.setitimer(signal.ITIMER_REAL,0)
        # Preserve accepted true sources for this job's next exact operation.
        # No binary/archive upload or persistent-storage action is performed.
        if paid_validated and certs:
            combined=dict(paid)
            combined["certificates"]=sorted(certs,key=lambda c:int(c["slot"]))
            combined["kernelCount"]=len(certs)
            combined["allFreeSourceCoordinatesIdentity"]=True
            combined["largeFileTemporaryOnly"]=True
            save_temporary_certificates(temporary_path,combined)
            size,digest=file_hash(temporary_path)
            receipt["temporaryCertificates"]={
                "file":temporary_path.name,"bytes":size,"sha256":digest,
                "temporaryOnly":True,"doNotUpload":True,
            }
        receipt["paidInputCompletelyValidated"]=paid_validated
        receipt["totalFull4367ExactKernelCount"]=len(known)
        receipt["all36Full4367TrueRationalKernelsVerified"]=len(known)==COLS
        if "paidKernelCount" in receipt:
            receipt["characteristicZeroSelectedRankBounds"]=[
                4318,min(4340,4354-len(known))]
        receipt["mathematicalElapsedSeconds"]=time.monotonic()-start
        receipt["parameters"] = {k: receipt[k] for k in (
            "inputFiles", "attemptedSlots", "accepted", "temporaryCertificates"
        ) if k in receipt}
        save_json(receipt_path,receipt)
    print(json.dumps({k:receipt.get(k) for k in [
        "status","actualSourceExponent","newExactKernelCount",
        "totalFull4367ExactKernelCount","all36Full4367TrueRationalKernelsVerified",
        "characteristicZeroSelectedRankBounds","mathematicalElapsedSeconds"]}),
        flush=True)
    return code

if __name__=="__main__":
    sys.exit(main())
