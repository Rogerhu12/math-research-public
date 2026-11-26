#!/usr/bin/env sage-python
"""Small exact API fixtures for the whole weighted W recovery, no original Y."""
import os
if (os.environ.get("GITHUB_ACTIONS") != "true" or
        os.environ.get("GITHUB_REPOSITORY") != "Rogerhu12/math-research-public"):
    raise SystemExit("Run mathematical computations only in the public research Actions.")

import ast
import hashlib
import json
import time
from pathlib import Path
from sage.all import GF, PolynomialRing, diagonal_matrix, identity_matrix, matrix
from sage.env import SAGE_VERSION
from section_quotient_algebra import canonical, digest
import original_full_w_basis_transport as transport

HERE = Path(__file__).resolve().parent
ROOT, TOPIC = HERE.parents[2], HERE.parent
REQUEST = TOPIC/"ci/original-full-w-basis-api-request.json"
WORKFLOW = ROOT/".github/workflows/rank2-sha-full-w-basis-api.yml"
IMAGE = "sagemath/sagemath@sha256:19995db6194f4a4bab18ce9a88556fd15b9ed5e916b4504fefe618a7796ddbdb"
SOURCE_FILES = tuple(dict.fromkeys((
    "check-original-full-w-basis-api.py",
)+transport.SOURCE_DEPENDENCIES))
assert len(SOURCE_FILES) == len(set(SOURCE_FILES)) == 4
STARTED = time.monotonic()


def weight_five_case():
    fp = GF(41)
    R = PolynomialRing(fp, "constructed_weight_five_parameter")
    t, weights = R.gen(), (0, 5)
    U = identity_matrix(R, 2)
    U[1, 0] = t**5+1
    inverse_U = 2*identity_matrix(R, 2)-U
    assert U*inverse_U == inverse_U*U == identity_matrix(R, 2)
    P = diagonal_matrix(R, [(t+1)**(12-d) for d in weights])*inverse_U
    P_all = P.stack(matrix(R, [P.row(0)+P.row(1)]))
    C, receipt = transport._recover_complete_matrix(P_all, weights, fp)
    U_star = matrix(R, 2, 2, lambda i, j:transport._homogeneous_substitute(
        U[i, j], weights[i]-weights[j], t+3, t-1))
    expected = U_star*diagonal_matrix(R, [R(fp(2)**d) for d in weights])*inverse_U
    assert C == expected
    assert receipt["exact_taylor_coefficient_degrees"] == list(range(6))
    assert max(p.degree() for p in C.list() if p) == 5
    return dict(
        constructed_prime=41, constructed_weights=list(weights),
        six_coefficients_and_full_degree_five_matrix_returned=True,
        whole_source_and_inverse_returns=receipt,
        original_r41_apery_weights_or_geometry_claimed=False)


def exact_quadratic_embedding_case():
    fp = GF(29)
    base = PolynomialRing(fp, "constructed_constant_polynomial")
    z = base.gen()
    k = GF(29**2, name="constructed_omega", modulus=z*z+z+1)
    omega = k.gen()
    assert omega*omega+omega+1 == 0 and omega**29 != omega
    R = PolynomialRing(k, "constructed_original_presentation_parameter")
    t, weights = R.gen(), (0, 1)
    P = diagonal_matrix(R, [(t+1)**(12-d) for d in weights])
    C, receipt = transport._recover_complete_matrix(P, weights, fp)
    assert C.base_ring() is R
    assert C == diagonal_matrix(R, [R.one(), R(k(2))])
    corrupted = P.copy()
    corrupted[0, 0] += omega
    rejected = False
    try:
        transport._recover_complete_matrix(corrupted, weights, fp)
    except AssertionError:
        rejected = True
    assert rejected
    return dict(
        same_given_quadratic_presentation_returned=True,
        nonprime_input_coefficient_rejected=True,
        whole_source_and_inverse_returns=receipt,
        original_local_context_or_geometric_root_generated=False)


def degree_zero_case():
    fp = GF(29)
    R = PolynomialRing(fp, "constructed_weight_zero_parameter")
    t = R.gen()
    P = matrix(R, [[(t+1)**12], [2*(t+1)**12]])
    C, receipt = transport._recover_complete_matrix(P, (0,), fp)
    assert C == identity_matrix(R, 1)
    assert receipt["exact_taylor_coefficient_degrees"] == [0]
    return dict(weight_zero_one_coefficient_boundary_passed=True,
                whole_source_and_inverse_returns=receipt)


def main():
    raw = REQUEST.read_bytes()
    request = json.loads(raw)
    assert request == {
        "schema":"rank2-original-full-w-basis-api/v1",
        "checks":["complete-weighted-matrix", "full-extra-source-rejection",
                  "weight-five-r41", "exact-prime-field-embedding", "degree-zero"],
        "original_geometry":False,
    }
    assert len(raw) <= 4096 and SAGE_VERSION == "10.6"
    assert os.environ["RANK2_IMAGE"] == IMAGE
    source = os.environ["RANK2_SOURCE_SHA"]
    assert len(source) == 40 and all(c in "0123456789abcdef" for c in source)
    assert os.environ["RANK2_RUN_ID"].isdecimal()
    assert os.environ["RANK2_RUN_ATTEMPT"].isdecimal()
    for name in SOURCE_FILES:
        ast.parse((HERE/name).read_text(encoding="utf-8"), filename=name)
    files = [HERE/name for name in SOURCE_FILES]+[
        REQUEST, WORKFLOW, ROOT/"README.md", TOPIC/"README.md"]
    manifest = dict(
        source=source, run_id=os.environ["RANK2_RUN_ID"],
        run_attempt=os.environ["RANK2_RUN_ATTEMPT"], image=IMAGE,
        sage_version=SAGE_VERSION, request=request,
        request_sha256=hashlib.sha256(raw).hexdigest(),
        source_sha256={str(p.relative_to(ROOT)):hashlib.sha256(p.read_bytes()).hexdigest()
                       for p in files},
        readme_blobs={"root":os.environ["RANK2_ROOT_README_SHA"],
                      "topic":os.environ["RANK2_TOPIC_README_SHA"]},
        source_mount_read_only=True, Sage_network_mode="none",
        original_geometric_input_generated=False)
    print("RANK2_FULL_W_BASIS_API_MANIFEST "+canonical(manifest), flush=True)
    four = transport.complete_w_matrix_recovery_preflight()
    five = weight_five_case()
    quadratic = exact_quadratic_embedding_case()
    zero = degree_zero_case()
    result = dict(
        kind="rank2_original_full_weighted_W_basis_API",
        status="constructed_complete_source_and_inverse_returns_passed",
        source=source, run_id=os.environ["RANK2_RUN_ID"],
        run_attempt=os.environ["RANK2_RUN_ATTEMPT"], image=IMAGE,
        sage_version=SAGE_VERSION, manifest_sha256=digest(manifest),
        constructed_weight_four=four, constructed_weight_five=five,
        exact_given_quadratic_field=quadratic, constructed_weight_zero=zero,
        all_source_ASTs_checked=True, source_file_count=len(SOURCE_FILES),
        original_306_W_matrix_normalization_divisors_or_shadow_computed=False,
        coefficient_or_data_file_written=False,
        elapsed_seconds=time.monotonic()-STARTED)
    payload = canonical(result)
    print("RANK2_FULL_W_BASIS_API_RESULT "+payload, flush=True)
    print("RANK2_FULL_W_BASIS_API_SHA256 "+hashlib.sha256(payload.encode()).hexdigest(),
          flush=True)


if __name__ == "__main__":
    main()
