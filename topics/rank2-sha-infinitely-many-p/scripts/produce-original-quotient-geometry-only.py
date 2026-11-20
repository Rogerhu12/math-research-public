#!/usr/bin/env sage-python
"""Normalize the actual genus19 quotient before constructing the eta48 field.

This executes exactly the original quotient-divisor routine.  It does not
construct U, invert a degree48 derivative, return a shadow context, or claim
that the downstream maps and RR bases have been certified.
"""
import os
if (os.environ.get("GITHUB_ACTIONS") != "true" or
        os.environ.get("GITHUB_REPOSITORY") != "Rogerhu12/math-research-public"):
    raise SystemExit("Run only in the public research repository Actions.")

import argparse
import hashlib
import importlib.util
import time
from pathlib import Path
from sage.all import set_random_seed

HERE = Path(__file__).resolve().parent
SOURCE = HERE / "produce-r919-original-shadow-rr-tate19-geometry-first.py"
spec = importlib.util.spec_from_file_location("original_quotient_geometry", SOURCE)
geometry = importlib.util.module_from_spec(spec)
spec.loader.exec_module(geometry)
started = time.monotonic()


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--prime", type=int, choices=(29, 41), default=29)
    args = parser.parse_args()
    set_random_seed(20261116)
    k, Ks, poly, tate_certificate = geometry.direct_tate_atkin_polynomial(args.prime)
    assert poly.base_ring() is Ks
    D = Ks.extension(poly, "L_atkin")
    fields = {
        "constants": k,
        "quotient": D, "quotient_base": Ks,
        "quotient_polynomial": poly,
        "L_atkin": D.gen(), "s_atkin": D(Ks.gen()),
    }
    geometry.progress("quotient-only: original D ready, no eta48 inversion attempted")
    divs = geometry.quotient_divisors(fields)
    record = {
        "kind": "rank2_original_genus19_quotient_geometry",
        "prime": args.prime,
        "quotient_degree": 24,
        "genus_from_original_canonical_divisor": 19,
        "all_nine_geometric_cusps_checked": True,
        "all_original_Au_Av_branch_D0_checked": True,
        "quotient_divisor_hashes": {name: geometry.digest(
            geometry.divisor_record(divs[name])) for name in
            ("cusp_divisor", "Au", "Av", "branch", "D0", "s_poles", "L_poles")},
        "original_tate_certificate": tate_certificate,
        "full_eta48_RR_or_shadow_claimed": False,
        "source": os.environ.get("RANK2_SOURCE_SHA"),
        "run_id": os.environ.get("RANK2_RUN_ID"),
        "script_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "original_geometry_dependency_sha256": hashlib.sha256(SOURCE.read_bytes()).hexdigest(),
        "elapsed_seconds": time.monotonic() - started,
    }
    payload = geometry.canonical(record)
    print("RANK2_QUOTIENT_GEOMETRY_RESULT " + payload, flush=True)
    print("RANK2_QUOTIENT_GEOMETRY_SHA256 " + hashlib.sha256(payload.encode()).hexdigest(), flush=True)


if __name__ == "__main__":
    try:
        main()
    except Exception as exc:
        geometry.progress("quotient-only: failed", exception_type=type(exc).__name__, message=str(exc))
        raise
