#!/usr/bin/env sage-python
"""Recover the SAME original middle coordinate without a large field inverse.

This certifies only U after all original equations pass.  It does not claim
normalization, a full RR basis, either characteristic-zero map, or a shadow.
"""
import os
if (os.environ.get("GITHUB_ACTIONS") != "true" or
        os.environ.get("GITHUB_REPOSITORY") != "Rogerhu12/math-research-public"):
    raise SystemExit("Run this mathematical producer only in the public Actions.")

import argparse
import hashlib
import importlib.util
import time
from pathlib import Path
from sage.all import FunctionField, PolynomialRing, binomial, set_random_seed
from sage.env import SAGE_VERSION
import original_rr_primitive_algebra as original
from original_tadic_quotient import polynomial_api_preflight, recover_exact_quotient

HERE = Path(__file__).resolve().parent
GEOMETRY_PATH = HERE / "produce-r919-original-shadow-rr-tate19-geometry-first.py"
spec = importlib.util.spec_from_file_location("original_tadic_geometry", GEOMETRY_PATH)
geometry = importlib.util.module_from_spec(spec)
spec.loader.exec_module(geometry)
base = geometry.base
STARTED = time.monotonic()


def original_algebra(prime):
    k, Ks, polynomial, tate_certificate = geometry.direct_tate_atkin_polynomial(prime)
    K = FunctionField(k, "t_eta")
    t = K.gen()
    phi_s = Ks.hom([t+1/t])
    KJ = PolynomialRing(K, "J")
    p_t = KJ([t**(6*(24-i))*phi_s(ci)
              for i, ci in enumerate(polynomial.list())])
    assert p_t.degree() == 24 and p_t.leading_coefficient() == 1
    a = K(729)*t**12
    KX = PolynomialRing(K, "X")
    X = KX.gen()
    H = KX.zero()
    for i, ci in enumerate(p_t.list()):
        for j in range(i+1):
            H += ci*binomial(i, j)*a**j*X**(24+i-2*j)
    assert H.degree() == 48 and H.leading_coefficient() == 1
    separability = original.certify_separable_specialization(
        H, base.progress, "original eta degree48 for local quotient")
    base.progress("t-adic: original eta48 field construction start")
    B = K.extension(H, "T")
    T = B.gen()
    base.progress("t-adic: original eta48 field constructed")

    # H(T)=0 and H(0)!=0 give this inverse without a Euclidean algorithm.
    inverse_T = B.zero()
    for coefficient in reversed(H.list()[1:]):
        inverse_T = inverse_T*T + B(coefficient)
    inverse_T *= B(-K.one()/H[0])
    assert T*inverse_T == 1
    V = T*B(t**(-12))

    # These coefficient identities certify the ORIGINAL absolute Atkin maps.
    # They are exact identities in K[X], not specialization tests.
    sigma = K.hom([1/t])
    for i in range(49):
        assert H[48-i]*a**(48-i) == H[0]*H[i]
        assert sigma(H[48-i])*K(729)**(48-i) == sigma(H[0])*H[i]
    WT = B(a)*inverse_T
    W3T = B(729)*inverse_T
    assert WT*V == 729 and W3T*T == 729
    assert (WT*B(t**(-12)))*T == 729
    assert (W3T*B(t**12))*V == 729

    def atkin(value, switch_base):
        image = W3T if switch_base else WT
        out = B.zero()
        for coefficient in reversed(value.list()):
            out = out*image + B(sigma(coefficient) if switch_base else coefficient)
        return out

    base.progress("t-adic: both original Atkin substitutions certified",
                  eta48_polynomial_sha256=base.digest([str(c) for c in H.list()]),
                  generic_eta48_inverse_computed=False,
                  differential_inverse_computed=False)
    return K, B, T, V, atkin, tate_certificate, separability


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--prime", type=int, choices=(29, 41), default=29)
    parser.add_argument("--max-precision", type=int, default=4096)
    args = parser.parse_args()
    set_random_seed(20261120)
    polynomial_api_preflight()
    base.progress("t-adic: polynomial API preflight passed")
    terms, phi_hash = base.hecke17_level3()
    leading, constant, universal_certificate = original.universal_linear_remainder(
        args.prime, terms, base.progress)
    K, B, T, V, atkin, tate_certificate, separability = original_algebra(args.prime)
    A, shift_A = original.eta_scaled_evaluation(leading, B, T, base.progress, "linear leading")
    B0, shift_B = original.eta_scaled_evaluation(constant, B, T, base.progress, "linear constant")
    exponent = 12*(shift_A-shift_B)
    target = -B0*B(K.gen()**exponent)
    coordinates, quotient_certificate = recover_exact_quotient(
        B.polynomial(), A.list(), target.list(), base.progress, args.max_precision)
    U = B.zero()
    for coefficient in reversed(coordinates):
        U = U*T + B(coefficient)
    assert U != 0 and U != T and U != V
    base.progress("t-adic: first complete original Phi17 identity start")
    assert base.evaluate_phi(terms, T, U, B.zero()) == 0
    base.progress("t-adic: second complete original Phi17 identity start")
    assert base.evaluate_phi(terms, U, V, B.zero()) == 0
    base.progress("t-adic: first full original U Atkin identity start")
    assert atkin(U, False)*U == B(729)
    base.progress("t-adic: second full original U Atkin identity start")
    assert atkin(U, True)*U == B(729)
    base.progress("t-adic: same original U fully certified")
    dependencies = [GEOMETRY_PATH, HERE / "original_tadic_quotient.py",
                    HERE / "original_rr_primitive_algebra.py",
                    HERE / "produce-original-shadow-rr-eta48.py"]
    result = {
        "kind":"rank2_original_middle_coordinate_certificate",
        "status":"exact_original_U_only",
        "prime":args.prime,
        "function_field_degree":48,
        "field_model":"same original eta48 from the certified Tate quotient",
        "phi17_integer_terms_sha256":phi_hash,
        "direct_tate_certificate":tate_certificate,
        "eta48_separability":separability,
        "universal_linear_certificate":universal_certificate,
        "local_quotient_certificate":quotient_certificate,
        "eta_scaling_exponent":exponent,
        "both_complete_original_Phi17_identities":True,
        "both_original_U_Atkin_identities":True,
        "original_coordinates_sha256":base.hash_functions([T, U, V]),
        "original_U_sha256":base.hash_functions([U]),
        "rr_normalization_or_basis_claimed":False,
        "source":os.environ.get("RANK2_SOURCE_SHA"),
        "run_id":os.environ.get("RANK2_RUN_ID"),
        "sage_version":SAGE_VERSION,
        "script_sha256":hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "dependency_sha256":{p.name:hashlib.sha256(p.read_bytes()).hexdigest() for p in dependencies},
        "elapsed_seconds":time.monotonic()-STARTED}
    payload = base.canonical(result)
    print("RANK2_ORIGINAL_U_RESULT "+payload, flush=True)
    print("RANK2_ORIGINAL_U_SHA256 "+hashlib.sha256(payload.encode()).hexdigest(), flush=True)


if __name__ == "__main__":
    try:
        main()
    except Exception as exc:
        failed = base.CURRENT_STAGE
        base.progress("failed", failed_stage=failed,
                      exception_type=type(exc).__name__, message=str(exc))
        raise
