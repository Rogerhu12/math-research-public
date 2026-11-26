#!/usr/bin/env sage-python
"""Exercise the exact nonprime-base residue-field failure from Artinian v7."""
import os
if (os.environ.get("GITHUB_ACTIONS") != "true" or
        os.environ.get("GITHUB_REPOSITORY") != "Rogerhu12/math-research-public"):
    raise SystemExit("Run mathematical computations only in the public research Actions.")

import ast
import hashlib
import json
import time
from pathlib import Path
from sage.all import GF, PolynomialRing, matrix
from sage.env import SAGE_VERSION
from original_ys_closed_point_tools import (
    ActualFiniteFieldQuotient, native_absolute_degree, native_matrix_digest)
from original_ys_divisor_ideal_tools import (
    canonical, digest, field_description, finite_field_coordinates, polynomial_digest)

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
TOPIC = HERE.parent
REQUEST = TOPIC/"ci/original-finite-field-quotient-api-request.json"
WORKFLOW = ROOT/".github/workflows/rank2-sha-finite-field-quotient-api.yml"
IMAGE = "sagemath/sagemath@sha256:19995db6194f4a4bab18ce9a88556fd15b9ed5e916b4504fefe618a7796ddbdb"
SOURCE_FILES = (
    "check-original-finite-field-quotient-api.py",
    "original_ys_closed_point_tools.py", "original_ys_divisor_ideal_tools.py")
STARTED = time.monotonic()


def check_case(polynomial, tag):
    P, k = polynomial.parent(), polynomial.parent().base_ring()
    d = int(polynomial.degree())
    extension = ActualFiniteFieldQuotient(polynomial, tag)
    K, root = extension.field, extension.root
    assert extension.base is k and extension.P is P
    assert native_absolute_degree(K) == native_absolute_degree(k)*d
    assert K.cardinality() == k.cardinality()**d
    x, a = P.gen(), k.gen()
    basis = [x**i for i in range(d)]
    for f in basis:
        assert extension.lift(extension.reduce(f)) == f % polynomial
        for g in basis:
            assert extension.reduce(f*g) == extension.reduce(f)*extension.reduce(g)
            assert extension.reduce(f+a*g) == (
                extension.reduce(f)+extension.embed_base(a)*extension.reduce(g))
    for j in range(native_absolute_degree(K)):
        b = K.gen()**j
        assert extension.reduce(extension.lift(b)) == b
    # A complete operator, determinant and original relative norm all return.
    M = matrix(k, [[a+1, a], [a*a, a+2]])
    MK = matrix(K, [[extension.embed_base(c) for c in row] for row in M.rows()])
    assert MK.det() == extension.embed_base(M.det())
    native_matrix_digest(MK)
    f = x+a if d > 1 else P(a+1)
    if not f % polynomial:
        f += 1
    h = extension.reduce(f)
    assert h
    expected = k(polynomial.resultant(f))
    actual = h**((int(K.cardinality())-1)//(int(k.cardinality())-1))
    assert actual == extension.embed_base(expected)
    assert extension.lift(actual) == P(expected)
    assert extension.lift(extension.embed_base(a)) == P(a)
    return extension, {
        "tag":tag, "original_polynomial_sha256":polynomial_digest(polynomial),
        "extension":extension.receipt(),
        "all_power_basis_products_and_original_scalars_returned":True,
        "full_absolute_native_coordinate_basis_returned":True,
        "actual_full_operator_determinant_returned":True,
        "native_matrix_hash":native_matrix_digest(MK),
        "relative_resultant_norm_in_original_base":finite_field_coordinates(expected,k),
        "relative_norm_target_and_entire_embedding_preserved":True,
    }


def main():
    raw = REQUEST.read_bytes()
    assert len(raw) <= 4096
    request = json.loads(raw)
    assert request == {
        "schema":"rank2-original-finite-field-quotient-api/v1",
        "prime":29, "original_modulus_ascending":[1,1,1],
        "checks":["actual-v7-nonprime-polynomial-extension-failure",
                  "linear-prime-quadratic-cubic-and-native-tower-returns",
                  "full-coordinate-and-original-base-operator-returns",
                  "original-thick-preflight-scalar-norm"],
        "original_geometry":False,
    }
    assert SAGE_VERSION == "10.6" and os.environ["RANK2_IMAGE"] == IMAGE
    source = os.environ["RANK2_SOURCE_SHA"]
    assert len(source) == 40 and all(c in "0123456789abcdef" for c in source)
    for key in ("RANK2_RUN_ID", "RANK2_RUN_ATTEMPT"):
        assert os.environ[key].isdecimal()
    for key in ("RANK2_ROOT_README_SHA", "RANK2_TOPIC_README_SHA"):
        assert len(os.environ[key]) == 40
    for name in SOURCE_FILES:
        ast.parse((HERE/name).read_text(encoding="utf-8"), filename=name)
    files = [HERE/name for name in SOURCE_FILES]+[
        REQUEST, WORKFLOW, ROOT/"README.md", TOPIC/"README.md"]
    manifest = {
        "source":source, "run_id":os.environ["RANK2_RUN_ID"],
        "run_attempt":os.environ["RANK2_RUN_ATTEMPT"],
        "image":IMAGE, "sage_version":SAGE_VERSION,
        "request":request, "request_sha256":hashlib.sha256(raw).hexdigest(),
        "source_sha256":{str(p.relative_to(ROOT)):hashlib.sha256(p.read_bytes()).hexdigest()
                         for p in files},
        "readme_blobs":{"root":os.environ["RANK2_ROOT_README_SHA"],
                        "topic":os.environ["RANK2_TOPIC_README_SHA"]},
        "source_mount_read_only":True, "Sage_network_mode":"none",
        "algorithm_fixtures_only":True, "production_files_modified":False,
    }
    print("RANK2_FINITE_FIELD_QUOTIENT_API_MANIFEST "+canonical(manifest),flush=True)
    fp = GF(request["prime"])
    M = PolynomialRing(fp,"original_omega_modulus")
    k = GF(29**2,name="original_omega",modulus=M(request["original_modulus_ascending"]))
    assert k.gen()**2+k.gen()+1 == 0
    P = PolynomialRing(k,"xi")
    x, c = P.gen(), k.multiplicative_generator()
    pi = x*x-c
    assert pi.is_irreducible()
    old_quotient = P.quotient(pi,names="old_v7_quotient")
    old_field, old_forward, old_backward = old_quotient.field_extension("old_v7_field")
    assert old_field.cardinality() == 29**4
    assert old_field.cardinality() != 29**int(old_field.degree())
    assert old_backward(old_forward(old_quotient.gen())) == old_quotient.gen()
    cases = []
    linear, record = check_case(x-(2+k.gen()),"original_linear")
    assert linear.field is k
    cases.append(record)
    quadratic, record = check_case(pi,"original_v7_quadratic")
    cases.append(record)
    cubic, record = check_case(x**3-c,"original_cubic")
    cases.append(record)
    F = PolynomialRing(fp,"prime_x")
    prime_case, record = check_case(F.gen()**2-fp.multiplicative_generator(),"prime_base")
    cases.append(record)
    T = PolynomialRing(quadratic.field,"tower_x")
    tower, record = check_case(T.gen()**2-quadratic.field.multiplicative_generator(),"native_tower")
    omega_image = tower.embed_base(quadratic.embed_base(k.gen()))
    first_return = tower.lift(omega_image)
    assert first_return.degree() == 0
    assert quadratic.lift(first_return[0]) == P(k.gen())
    record["entire_original_omega_returned_through_two_levels"] = True
    cases.append(record)
    # The exact scalar part of v7's 1530-length norm preflight, including
    # BOTH repetitions of its quadratic factor and all 306 module copies.
    norm_root = quadratic.root**((29**4-1)//(29**2-1))
    assert norm_root == quadratic.embed_base(-c)
    full_norm = norm_root**(2*306)
    expected = k((-c)**612)
    assert full_norm == quadratic.embed_base(expected)
    assert quadratic.lift(full_norm) == P(expected)
    assert expected**29 != expected
    result = {
        "kind":"rank2_R974_exact_original_finite_field_quotient_API",
        "status":"native_absolute_models_and_complete_original_returns_passed",
        "source":source,"run_id":os.environ["RANK2_RUN_ID"],
        "run_attempt":os.environ["RANK2_RUN_ATTEMPT"],
        "manifest_sha256":digest(manifest),"image":IMAGE,"sage_version":SAGE_VERSION,
        "original_constants":field_description(k),"cases":cases,
        "actual_v7_relative_degree_failure_reproduced":True,
        "original_thick_preflight_norm":finite_field_coordinates(expected,k),
        "original_thick_preflight_norm_not_in_prime_field":True,
        "all_source_ASTs_checked":True,"source_file_count":len(SOURCE_FILES),
        "original_maps_recomputed":False,"original_normalization_recomputed":False,
        "original_divisors_norms_intersections_or_shadow_claimed":False,
        "coefficient_or_data_file_written":False,
        "elapsed_seconds":time.monotonic()-STARTED,
    }
    payload = canonical(result)
    print("RANK2_FINITE_FIELD_QUOTIENT_API_RESULT "+payload,flush=True)
    print("RANK2_FINITE_FIELD_QUOTIENT_API_SHA256 "+hashlib.sha256(payload.encode()).hexdigest(),flush=True)


if __name__ == "__main__":
    main()
