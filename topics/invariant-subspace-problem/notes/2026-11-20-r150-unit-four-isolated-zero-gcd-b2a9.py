#!/usr/bin/env python3
"""Exact Q[r] gcd for the original R150 unit-four/isolated-zero branch.
Author: Astra-ISP-b2a9acde-20261120. AI-assisted GPT-6 Astra Pro.
Only input polynomials and source are retained; computed remainders are not saved.
"""
import datetime, hashlib, json, math, os, pathlib, time
from functools import reduce

# Coefficients in ascending powers. These are the two original necessary equations.
M = [10, 4, -52, -14, 109, 10, -98, 0, 33]
MINUS_H = [-20, -22, 120, 19, -168, 0, 80]

def trim(a):
    while a and not a[-1]:
        a.pop()
    return a

def primitive(a):
    trim(a)
    if not a:
        return a
    content = reduce(math.gcd, (abs(x) for x in a), 0)
    if a[-1] < 0:
        content = -content
    return [x // content for x in a]

def prem(a, b):
    a = list(a)
    while len(a) >= len(b):
        shift = len(a) - len(b)
        lead_a, lead_b = a[-1], b[-1]
        a = [lead_b * x for x in a]
        for j, x in enumerate(b):
            a[j + shift] -= lead_a * x
        trim(a)
    return primitive(a)

def canonical(x):
    return json.dumps(x, sort_keys=True, separators=(",", ":")).encode()

def main():
    started = time.monotonic()
    a, b = M[:], MINUS_H[:]
    digest = hashlib.sha256()
    steps = 0
    while len(b) > 1:
        c = prem(a, b)
        if not c or len(c) >= len(b):
            raise ArithmeticError("A nonzero lower-degree remainder is required")
        digest.update(canonical(c) + b"\n")
        a, b = b, c
        steps += 1
    if b != [1]:
        raise ArithmeticError("The exact rational gcd is not the unit")
    receipt = {
        "format": "isp-r150-unit-four-isolated-zero-exact-gcd-v1",
        "utc": datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC"),
        "runId": os.environ.get("GITHUB_RUN_ID"),
        "sourceCommit": os.environ.get("ISP_PIN"),
        "sourceSHA256": hashlib.sha256(pathlib.Path(__file__).read_bytes()).hexdigest(),
        "inputSHA256": hashlib.sha256(canonical({"M": M, "minusH": MINUS_H})).hexdigest(),
        "remainderStreamSHA256": digest.hexdigest(),
        "algorithm": "primitive integer pseudo-remainders with positive leading coefficient",
        "steps": steps,
        "gcdDegree": 0,
        "exactGcdOne": True,
        "allIntermediateDegreesStrictlyDecrease": True,
        "computedArraysSaved": False,
        "elapsedSeconds": time.monotonic() - started,
    }
    print("ISP_R150_SHORT_EXACT_RECEIPT " + json.dumps(receipt, sort_keys=True), flush=True)

if __name__ == "__main__":
    main()
