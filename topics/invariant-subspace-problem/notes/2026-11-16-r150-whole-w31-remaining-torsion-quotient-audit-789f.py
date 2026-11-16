#!/usr/bin/env python3
"""Read-only original T/S quotient audit and comparison with two complete P31 spectra.

AI-assisted: ChatGPT / literature_audit, 2026-11-16.
Uses integer relation lattices in the paid complete coefficient-torsion basis.
Does not repeat a source solve or infer integral equality from a field zero.
"""
import argparse
import hashlib
import json
from pathlib import Path
import time
from flint import fmpz_mat

P = 31
FORMAT = "r150-whole-w31-remaining-torsion-quotient-audit-v1"
PINS = {
    "root1": (662, "2598ebf23851c2bd48e2c32049dc5adb9a660984c336698bccd36215ead5fc55"),
    "root2": (16797, "46cb736d61e85daf6af0a4476ffa857c98b06f84d8c6e149b6180ce054d14a5c"),
    "qualification": (20106, "9b8c104b8cbd9d7fbe17c7e6fbddd1067c66d6a6a17252ed9c8f854b7cd2a2a7"),
    "projection1": (6740, "4ca163bbc3084bc2c05dab47a60a96dcfe8c90d242d2bc68cb63d1c66521e4b9"),
    "projection2": (7828, "9acb3368250f9efeeed1b358036f3ee6620846ba48fb176f6b2011a94c00e2a4"),
}


def canonical(x):
    return (json.dumps(x, sort_keys=True, separators=(",", ":"), ensure_ascii=True)+"\n").encode("ascii")


def sha(b):
    return hashlib.sha256(b).hexdigest()


def require(ok, message):
    if not ok:
        raise AssertionError(message)


def checked(path, pin):
    b = path.read_bytes()
    require((len(b), sha(b)) == pin, "Full paid input identity: "+str(path))
    return json.loads(b)


def valuation(n):
    require(n > 0, "Nonzero full relation-lattice index")
    v = 0
    while n % P == 0:
        n //= P
        v += 1
    require(n == 1, "Relation-lattice index is a pure power of31")
    return v


def lattice_index(rows, dimension):
    H = fmpz_mat(rows).hnf()
    B = [[int(H[i, j]) for j in range(dimension)] for i in range(H.nrows())
         if any(H[i, j] for j in range(dimension))]
    require(len(B) == dimension, "Complete finite-index HNF basis")
    return valuation(abs(int(fmpz_mat(B).det())))


def quotient(E, A):
    n = len(E)
    require(len(A) == n and len({len(row) for row in A}) == 1, "Complete coordinate shape")
    relations = [[P**E[j] if i == j else 0 for i in range(n)] for j in range(n)]
    columns = [list(v) for v in zip(*A)]
    index = lattice_index(relations+columns, n)
    lengths = []
    for k in range(max(E)+1):
        pk = [[P**k if i == j else 0 for i in range(n)] for j in range(n)]
        lengths.append(index-lattice_index(relations+columns+pk, n))
    require(lengths[0] == index and lengths[-1] == 0, "Complete quotient p-image lengths")
    at_least = [lengths[k]-lengths[k+1] for k in range(len(lengths)-1)]
    require(all(a >= b >= 0 for a, b in zip(at_least, at_least[1:])), "Actual quotient invariant-factor monotonicity")
    exponents = [i+1 for i, a in enumerate(at_least)
                 for _ in range(a-(at_least[i+1] if i+1 < len(at_least) else 0))]
    require(sum(exponents) == index, "Actual quotient length and type agree")
    return {"exponents": exponents, "length": index,
            "successivePImageLengths": lengths,
            "pTimesQuotientExponents": [v-1 for v in exponents if v > 1],
            "method": "complete-integer-relation-lattice-HNF-index"}


def main():
    ap = argparse.ArgumentParser()
    for k in PINS:
        ap.add_argument("--"+k, type=Path, required=True)
    ap.add_argument("--out", type=Path, required=True)
    a = ap.parse_args()
    started = time.monotonic()
    data = {k: checked(getattr(a, k), pin) for k, pin in PINS.items()}
    r1, r2 = data["root1"], data["root2"]
    require(r1["binding"] == "c7a18e56374d223e1653fd48561d5f5c7dd4d2548e77486bdb4cbd9cf5ffe3df",
            "Actual root-one complete two-digit binding")
    require(r2["binding"] == "4d3f5dbf2bd02328ba5e7cea47641cd2c21cdc6467950eaee97c2b22d4864222",
            "Actual root-two complete six-digit completion binding")
    E1, A1 = r1["ambientExponents"], r1["coordinateRows"]
    E2, A2 = r2["ambientExponents"], r2["coordinateRows"]
    require(E1 == [1, 2] and E2 == [1, 2, 2, 2, 2, 3, 3, 4, 4, 4, 4, 5, 5, 6],
            "Complete actual two-primary torsion bases")
    require(all(x == 0 for x in A1[0]) and all(x % P == 0 for x in A1[1])
            and any((x//P) % P for x in A1[1]), "Actual S1 is exactly pT1")
    H1, H2 = quotient(E1, A1), quotient(E2, A2)
    require(sum(E1)+sum(E2) == 50 and H1["length"]+H2["length"] == 15,
            "Full T length50 minus paid S length35")
    q = data["qualification"]
    require(q["status"] == "completed" and q["binding"] ==
            "f03f4892d70cdf39aceaebf8d8e9dc979196904e8ca75afbfc3d080230cb365f",
            "Same complete primitive-free qualification")
    final = q["parameters"]["final"]
    require(final["completePrimitiveFreeLatticeQualified"] and final["all225OriginalParameterProductsVerified"]
            and final["all315CoordinatesRetained"] and final["all505OriginalFreeChecksVerified"],
            "Whole original qualified target and carrier scope")
    require(final["paidRationalFreeDimension"] == 25 and final["originalTargetFieldDimension"] == 34,
            "Actual complete target/free dimensions")
    primary = {r["center"]: r for r in final["primary"] if r["center"] in (1, 2)}
    comparisons = []
    for center, H in ((1, H1), (2, H2)):
        r = data["projection"+str(center)]
        require(r["status"] == "completed" and r["exitCode"] == 0
                and sha(canonical(r["parameters"]["bindingInput"])) == r["binding"],
                "Complete actual projection binding")
        s = r["parameters"]["actualSmith"]
        require(s["prime"] == P and s["center"] == center and s["complete"]
                and s["cumulativeGenericRank"] == 142 and s["remainingConstantHeadCount"] == 13
                and s["allOriginal6188PositiveAndRemainingProductsVerified"],
                "Complete original projected Smith spectrum")
        z = primary[center]
        require(z["primitiveFreeLineQualified"] and z["all315OriginalPrimaryProductsVerified"],
                "Same original primary free line and target map")
        Wbar = z["wholePrimaryDimension"]-s["positiveLength"]
        Mbar = z["targetFieldDimension"]
        require(Wbar >= Mbar, "Original target submodule is contained in wholeW")
        deficit = Wbar-Mbar
        require(deficit <= len(H["exponents"]), "Actual image in complete H/pH")
        comparisons.append({"center": center,
                            "fullFieldTorsionLength": z["wholePrimaryDimension"],
                            "completeProjectedFieldTorsionLength": s["positiveLength"],
                            "wholeWFieldImageLength": Wbar,
                            "nineTargetFieldImageLength": Mbar,
                            "imageDimensionOfWholeWOverMInHmodP": deficit,
                            "completeHmodPDimension": len(H["exponents"]),
                            "fullCarrierQuotientDefectNotRemovedFromFieldLength": True})
    require(all(x["imageDimensionOfWholeWOverMInHmodP"] == 0 for x in comparisons),
            "This actual comparison only places the remaining gap inside pH")
    result = {"format": FORMAT, "status": "completed",
              "source": {"bytes": Path(__file__).stat().st_size, "sha256": sha(Path(__file__).read_bytes())},
              "inputPins": {k: {"bytes": v[0], "sha256": v[1]} for k, v in PINS.items()},
              "rootOneTOverS": H1, "rootTwoTOverS": H2,
              "totalTOverSLength": H1["length"]+H2["length"],
              "actualComparisons": comparisons,
              "actualRootOneSIsPtimesWholeT": True,
              "remainingWholeWOverMRootOneZeroByKilledByP": True,
              "remainingWholeWOverMEmbedsInPtimesRootTwoTOverS": True,
              "remainingGapLengthUpperBound": sum(H2["pTimesQuotientExponents"]),
              "remainingGapCoefficientExponentUpperBound": max(H2["pTimesQuotientExponents"], default=0),
              "remainingRootTwoGapNotDeclaredZero": True,
              "noOriginalSolveRepeated": True, "mathematicalArraysTemporaryOnly": True,
              "elapsedSeconds": time.monotonic()-started}
    a.out.write_bytes(canonical(result))
    print(json.dumps(result, sort_keys=True))


if __name__ == "__main__":
    main()
