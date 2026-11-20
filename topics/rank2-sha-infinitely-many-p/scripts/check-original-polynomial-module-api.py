#!/usr/bin/env sage-python
"""Check the exact polynomial-module APIs required by R925 in pinned Sage.

This checks installed algorithm semantics, not an original Y divisor or a
Frobenius shadow.  In particular a same-rank unsaturated kernel must fail.
"""
import os
if (os.environ.get("GITHUB_ACTIONS") != "true" or
        os.environ.get("GITHUB_REPOSITORY") != "Rogerhu12/math-research-public"):
    raise SystemExit("Run mathematical checks only in public research Actions.")

import hashlib
import time
from pathlib import Path
from sage.all import GF, PolynomialRing, matrix
from sage.env import SAGE_VERSION
from original_ys_divisor_ideal_tools import (
    canonical, polynomial_module_preflight, _hermite_remainder_rows,
    polynomial_matrix_digest)
import original_ys_divisor_ideal_tools


def main():
    started = time.monotonic()
    cases = []
    for prime in (29, 41):
        fp = GF(prime)
        P = PolynomialRing(fp, "X_api_constants")
        X = P.gen()
        modulus = X**2+X+1
        assert modulus.is_irreducible()
        for degree in (1, 2):
            k = fp if degree == 1 else GF(prime**2, "omega_api", modulus=modulus)
            R = PolynomialRing(k, "t_api")
            t = R.gen()
            preflight = polynomial_module_preflight(R)
            generators = matrix(R, [[t, 0], [0, 1], [t**2, 1]])
            H, U = generators.hermite_form(include_zero_rows=False, transformation=True)
            assert H.dimensions() == (2, 2) and U.dimensions() == (2, 3)
            assert U*generators == H
            assert H.is_hermite()
            assert _hermite_remainder_rows(generators, H).is_zero()
            assert H.det() == t
            record = {
                "prime":prime, "constant_degree":degree,
                "polynomial_kernel_preflight":preflight,
                "zero_row_removal_transformation_shape_verified":True,
                "complete_Hermite_return_and_reverse_inclusion_verified":True,
                "actual_Hermite_sha256":polynomial_matrix_digest(H),
            }
            cases.append(record)
            print("RANK2_POLYNOMIAL_API_STAGE "+canonical(record), flush=True)
    receipt = {
        "kind":"rank2_complete_polynomial_module_api_preflight",
        "status":"saturated_kernel_and_full_Hermite_semantics_verified",
        "cases":cases, "sage_version":SAGE_VERSION,
        "image":os.environ.get("RANK2_IMAGE"),
        "source":os.environ.get("RANK2_SOURCE_SHA"),
        "run_id":os.environ.get("RANK2_RUN_ID", os.environ.get("GITHUB_RUN_ID")),
        "run_attempt":os.environ.get("RANK2_RUN_ATTEMPT"),
        "script_sha256":hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "helper_sha256":hashlib.sha256(
            Path(original_ys_divisor_ideal_tools.__file__).read_bytes()).hexdigest(),
        "readme_blobs":{"root":os.environ.get("RANK2_ROOT_README_SHA"),
                        "topic":os.environ.get("RANK2_TOPIC_README_SHA")},
        "original_curve_or_divisors_claimed":False,
        "original_shadow_claimed":False,
        "elapsed_seconds":time.monotonic()-started,
    }
    payload = canonical(receipt)
    print("RANK2_POLYNOMIAL_API_RESULT "+payload, flush=True)
    print("RANK2_POLYNOMIAL_API_SHA256 "+hashlib.sha256(payload.encode()).hexdigest(), flush=True)


if __name__ == "__main__":
    main()
