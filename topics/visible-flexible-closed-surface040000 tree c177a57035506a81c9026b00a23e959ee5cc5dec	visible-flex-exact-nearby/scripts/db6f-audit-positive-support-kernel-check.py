#!/usr/bin/env python3
"""Independent Fraction reconstruction of the fixed positive-support obstruction.

Starts from R27 intervals and obtains square-root endpoints by rational bisection.
Does not import or call the author program.
"""
import argparse
from fractions import Fraction as Q
from hashlib import sha256
import json
from pathlib import Path


def dec(v):
    assert set(v) == {"numerator", "denominator"}
    return Q(int(v["numerator"]), int(v["denominator"]))


def enc(v):
    if isinstance(v, Q):
        return {"numerator": str(v.numerator), "denominator": str(v.denominator)}
    if isinstance(v, dict):
        return {k: enc(w) for k, w in v.items()}
    if isinstance(v, list):
        return [enc(w) for w in v]
    return v


def bisect_root(value):
    lo, hi = Q(0), Q(4)
    assert lo*lo <= value < hi*hi
    for _ in range(122):
        mid = (lo+hi)/2
        if mid*mid <= value:
            lo = mid
        else:
            hi = mid
    if lo*lo == value:
        hi = lo
    assert lo*lo <= value <= hi*hi
    assert hi-lo <= Q(1, 2**120)
    return lo, hi


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--out", required=True)
    args = ap.parse_args()
    base = Path(__file__).resolve().parents[1]
    pins = {
        "notes/2026-11-09-db6f-root-positive-support-kernel-obstruction.md":
            "0b3ad1fcdf31af4653547ae5d9d2bba520096210887f5ff24adf4f1ed7a2531f",
        "scripts/db6f-root-positive-support-kernel-obstruction.py":
            "56ae6c786589dfdbf9ed0acb4dcf7e1d0a9a17ee444f309e0c761e17623582cc",
        "notes/2026-11-09-db6f-root-positive-support-kernel-obstruction.json":
            "eb163aacdf57abb4511838753a3effec7b582ddc8ee27f9f3120d65483bc38c4",
        "notes/2026-11-09-db6f-audit-positive-support-kernel-replay.json":
            "eb163aacdf57abb4511838753a3effec7b582ddc8ee27f9f3120d65483bc38c4",
        "notes/2026-11-09-db6f-prefix-c3-poisson-bounds.json":
            "4d84a5f3533f367fc8acfb2501c20e16c157e0a41d02f5207e0ea05c3fc0908e",
        "notes/2026-11-09-db6f-audit-poisson-twin-marker-bounds.json":
            "9da6b3d013524995a831e5b55fe9d06b017957bbb87fd9b38fe093c7da8207ef",
        "notes/2026-11-09-db6f-audit-positive-collar-radial-interface.md":
            "a2b7586db4c7317d74c6a5a0d1fae655b1311d3b4ef917da30628e6afd2dc507",
    }
    inputs = []
    for rel, expected in pins.items():
        b = (base/rel).read_bytes()
        assert sha256(b).hexdigest() == expected, rel
        inputs.append({"path": rel, "bytes": len(b), "sha256": expected})
    original = json.loads((base/"notes/2026-11-09-db6f-prefix-c3-poisson-bounds.json").read_text())
    cases = [r for r in original["cases"] if dec(r["q"]) == Q(99,100) and dec(r["r"]) == Q(1,10)]
    assert len(cases) == 1
    row = cases[0]
    Hlo = dec(row["inradius"]["lower"])+dec(row["delta"]["lower"])
    Hhi = dec(row["inradius"]["upper"])+dec(row["delta"]["upper"])
    Llo = bisect_root(4*Hlo*Hlo+Q(31,100)**2)[0]
    Lhi = bisect_root(4*Hhi*Hhi+Q(31,100)**2)[1]
    old = json.loads((base/"notes/2026-11-09-db6f-audit-poisson-twin-marker-bounds.json").read_text())
    assert Hlo == dec(old["source_bounds"]["H_lower"])
    assert Hhi == dec(old["source_bounds"]["H_upper"])
    assert Llo == dec(old["witness_and_enclosures"]["L0_lower"])
    assert Lhi == dec(old["witness_and_enclosures"]["L0_upper"])

    # Interval vector q = (-H,0,3/10)+(1/10)*(-2H,0,31/100)/L.
    qxlo = -Hhi-Q(1,10)*(2*Hhi/Llo)
    qxhi = -Hlo-Q(1,10)*(2*Hlo/Lhi)
    qzlo = Q(3,10)+Q(1,10)*(Q(31,100)/Lhi)
    qzhi = Q(3,10)+Q(1,10)*(Q(31,100)/Llo)
    lam = Q(1,4)
    px, pz = -Q(7,20), Q(1,10)
    bxlo, bxhi = (px-lam*qxhi)/(1-lam), (px-lam*qxlo)/(1-lam)
    bzlo, bzhi = (pz-lam*qzhi)/(1-lam), (pz-lam*qzlo)/(1-lam)
    assert -Q(39,1000) < bxlo <= bxhi < -Q(38,1000)
    assert Q(29,1000) < bzlo <= bzhi < Q(30,1000)
    exact_upper = bxlo*bxlo+bzhi*bzhi
    coarse_upper = Q(39,1000)**2+Q(30,1000)**2
    assert exact_upper < coarse_upper == Q(2421,1_000_000) < Q(1,400)
    assert Q(1,400)-coarse_upper == Q(79,1_000_000)
    assert Q(1,20) < Q(189,2500)
    assert Q(34,100) < -px < Q(36,100)
    report = json.loads((base/"notes/2026-11-09-db6f-root-positive-support-kernel-obstruction.json").read_text())
    expected_centers = {"x_lower": bxlo, "x_upper": bxhi, "y": Q(0), "z_lower": bzlo, "z_upper": bzhi}
    assert all(dec(report["center_bounds"][k]) == v for k,v in expected_centers.items())
    assert dec(report["center_squared_norm_upper"]) == exact_upper
    assert dec(report["convex_weight"]) == lam
    result = {
        "status": "INDEPENDENT_EXACT_RECONSTRUCTION_PASS",
        "checker_sha256": sha256(Path(__file__).read_bytes()).hexdigest(),
        "inputs": inputs,
        "independent_method": "Rebuild H from R27; obtain both L endpoints by 122 rational bisections; interval-evaluate vector q and affine center; no author functions imported.",
        "H_interval": [Hlo,Hhi],
        "L_interval": [Llo,Lhi],
        "reconstructed_center": expected_centers,
        "center_squared_norm_upper_matches_author": exact_upper,
        "independent_coarse_bound": coarse_upper,
        "coarse_gap_to_one_over_400": Q(79,1_000_000),
        "source_endpoints_reconstructed": 4,
        "center_fields_reconstructed": 5,
        "author_and_replay_report_byte_hashes_equal": True,
        "scope": "Excludes the stated global radial support threshold only; does not exclude reach by another argument.",
        "candidate_or_solver_calls": 0,
    }
    out = Path(args.out).resolve()
    with out.open("x") as f:
        json.dump(enc(result),f,ensure_ascii=False,indent=2);f.write("\n")
    print(json.dumps({"status":result["status"],"inputs":len(inputs),
                      "coarse_bound":str(coarse_upper),"strict_gap":str(Q(79,1_000_000)),
                      "bytes":out.stat().st_size,"sha256":sha256(out.read_bytes()).hexdigest()}))


if __name__ == "__main__":
    main()
