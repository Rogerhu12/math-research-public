#!/usr/bin/env sage-python
"""The original T3(Q), T3(Q^17), T3(Q^289) as exact section fractions.

The functions are globally known eta quotients, with pole degree 306 each.
Complete section spaces and the degree-714 zero bound certify identification;
the finite q expansion is not used to invent a modular function.
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
from sage.all import ZZ, PolynomialRing, matrix, vector
from sage.env import SAGE_VERSION
from original_shadow_coordinate_tools import complete_product_recipes
from section_quotient_algebra import canonical, digest, matrix_digest, series_matrix

HERE = Path(__file__).resolve().parent
STARTED = time.monotonic()
CURRENT_STAGE = "initialization"


def progress(stage, **kw):
    global CURRENT_STAGE
    CURRENT_STAGE = stage
    print("RANK2_SECTION_TUV_STAGE "+canonical(dict(
        stage=stage, elapsed_seconds=time.monotonic()-STARTED, **kw)), flush=True)


def original_eta_unit(precision):
    """Compute integral Q*T3(Q) before reduction; never divide by p in Fp."""
    sigma = [ZZ.zero() for _ in range(precision)]
    for d in range(1, precision):
        for j in range(d, precision, d):
            sigma[j] += d
    logarithmic = [ZZ.zero()] + [
        -12*sigma[j] + (36*sigma[j//3] if j % 3 == 0 else 0)
        for j in range(1, precision)]
    coefficients = [ZZ.one()]
    for n in range(1, precision):
        numerator = sum((logarithmic[j]*coefficients[n-j]
                         for j in range(1, n+1)), ZZ.zero())
        quotient, remainder = numerator.quo_rem(ZZ(n))
        assert remainder == 0
        coefficients.append(quotient)
    assert coefficients[:4] == [1, -12, 54, -76]
    return coefficients


def build_original_tuv_section_fractions(prime=29, q_precision=1005):
    prime, q_precision = int(prime), int(q_precision)
    assert prime in (29, 41) and q_precision >= 1004
    path = HERE / "produce-r917-original-global-rr-q-lattice.py"
    spec = importlib.util.spec_from_file_location("tuv_original_r917", path)
    r917 = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(r917)
    original, original_receipt = r917.build_original_global_rr_q_lattice(prime, q_precision)
    k = original["constants"]
    rows1 = original["global_modular_form_jets"]
    recipes, series = complete_product_recipes(
        {"constants":k}, [list(row) for row in rows1.rows()], 2, q_precision)
    rows2 = series_matrix(series[2], k, q_precision)
    assert rows2.nrows() == 324 and rows2[:, :409].rank() == 324
    R = PolynomialRing(k, "Q")
    Q = R.gen()
    basis = [R(list(row)) for row in rows2.rows()]
    integral_eta = original_eta_unit(q_precision)
    progress("same complete M4 and original eta units ready", prime=prime,
             q_precision=q_precision, full_dimension=324)
    functions = {}
    cases = []
    for name, exponent in (("T", 1), ("U", 17), ("V", 289)):
        length = 715 + exponent
        assert length <= q_precision
        tau_coefficients = [k.zero() for _ in range(length)]
        for j in range((length-1)//exponent+1):
            tau_coefficients[exponent*j] = k(integral_eta[j])
        tau = R(tau_coefficients)
        assert tau[0] == 1
        negative_products = [-(tau*basis_i).truncate(length) for basis_i in basis]
        equations = matrix(k, [
            [basis_i[j-exponent] if j >= exponent else k.zero()
             for j in range(length)] for basis_i in basis] + [
            [product[j] for j in range(length)] for product in negative_products])
        assert equations.nrows() == 648 and equations.ncols() == length
        progress("original TUV complete section kernel start", function=name,
                 original_pole_degree=306, complete_pole_bound=714,
                 rows=length, unknowns=648)
        kernel = equations.left_kernel().basis_matrix()
        assert kernel.nrows() >= 18
        assert kernel*equations == 0
        coefficients = kernel.row(0)
        first_denominator = next(i for i in range(324, 648) if coefficients[i])
        coefficients /= coefficients[first_denominator]
        assert coefficients*equations == 0
        numerator_coordinates = vector(k, coefficients[:324])
        denominator_coordinates = vector(k, coefficients[324:])
        assert not denominator_coordinates.is_zero()
        numerator_row = numerator_coordinates*rows2
        denominator_row = denominator_coordinates*rows2
        A, B = R(list(numerator_row)), R(list(denominator_row))
        assert A and B
        assert (Q**exponent*A-tau*B).truncate(length) == 0
        assert int(B.valuation())-int(A.valuation()) == exponent
        assert A[int(A.valuation())] == B[int(B.valuation())]
        record = {
            "name":name, "original_function":"T3(Q^%d)" % exponent,
            "original_infinity_pole_order":exponent,
            "original_complete_pole_degree":306,
            "numerator_denominator_bundle":"same full M4(867), or both divided by S^2",
            "numerator_denominator_section_degree":408,
            "complete_difference_pole_bound":714,
            "checked_shifted_coefficients_inclusive":[0, 714+exponent],
            "complete_kernel_dimension":int(kernel.nrows()),
            "complete_kernel_residual_verified":True,
            "exact_global_eta_identity_certified_by_pole_bound":True,
            "actual_numerator_infinity_order":int(A.valuation()),
            "actual_denominator_infinity_order":int(B.valuation()),
            "original_leading_coefficient":1,
            "full_equation_matrix_sha256":matrix_digest(equations),
            "complete_kernel_sha256":matrix_digest(kernel),
            "chosen_coordinates_sha256":digest([int(c) for c in coefficients]),
            "actual_numerator_jets_sha256":digest([int(c) for c in numerator_row]),
            "actual_denominator_jets_sha256":digest([int(c) for c in denominator_row]),
            "original_shifted_eta_jets_sha256":digest([int(tau[j]) for j in range(length)])}
        functions[name] = {"numerator_coordinates":numerator_coordinates,
                           "denominator_coordinates":denominator_coordinates,
                           "complete_fraction_kernel":kernel,
                           "numerator_jets":numerator_row,
                           "denominator_jets":denominator_row,
                           "certificate":record}
        cases.append(record)
        progress("same original TUV function globally identified", function=name,
                 kernel_dimension=int(kernel.nrows()),
                 full_pole_bound=714, checked_shifted_last=714+exponent)
    dependencies = [path, HERE / "original_pari_m2_basis.py",
                    HERE / "original_shadow_coordinate_tools.py",
                    HERE / "section_quotient_algebra.py"]
    result = {
        "kind":"rank2_original_TUV_section_fraction_certificate",
        "status":"all_three_original_global_eta_functions_identified",
        "level":867, "prime":prime, "q_precision":q_precision,
        "same_original_Q_parameter":True,
        "original_complete_M2_receipt":original_receipt,
        "same_complete_M4_product_recipes_sha256":digest(recipes[2]),
        "same_complete_M4_jets_sha256":matrix_digest(rows2),
        "integer_eta_unit_sha256":digest([str(c) for c in integral_eta]),
        "cases":cases,
        "eta48_coordinate_model_claimed":False,
        "original_maps_or_shadow_claimed":False,
        "source":os.environ.get("RANK2_SOURCE_SHA"),
        "run_id":os.environ.get("RANK2_RUN_ID", os.environ.get("GITHUB_RUN_ID")),
        "run_attempt":os.environ.get("RANK2_RUN_ATTEMPT"),
        "sage_version":SAGE_VERSION,
        "image":os.environ.get("RANK2_IMAGE"),
        "readme_blobs":{"README.md":os.environ.get("RANK2_ROOT_README_SHA"),
                        "topic":os.environ.get("RANK2_TOPIC_README_SHA")},
        "script_sha256":hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "dependency_sha256":{p.name:hashlib.sha256(p.read_bytes()).hexdigest() for p in dependencies},
        "elapsed_seconds":time.monotonic()-STARTED}
    context = {"kind":"rank2_original_TUV_section_fractions", "constants":k,
               "original_r917_context":original, "complete_m4_rows":rows2,
               "complete_m4_recipes":recipes[2], "functions":functions,
               "q_precision":q_precision}
    return context, result


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--prime", type=int, choices=(29, 41), default=29)
    parser.add_argument("--q-precision", type=int, default=1005)
    args = parser.parse_args()
    context, result = build_original_tuv_section_fractions(args.prime, args.q_precision)
    globals()["ORIGINAL_TUV_SECTION_FRACTIONS"] = context
    payload = canonical(result)
    print("RANK2_SECTION_TUV_RESULT "+payload, flush=True)
    print("RANK2_SECTION_TUV_SHA256 "+hashlib.sha256(payload.encode()).hexdigest(), flush=True)


if __name__ == "__main__":
    try:
        main()
    except Exception as exc:
        failed = CURRENT_STAGE
        progress("failed", failed_stage=failed,
                 exception_type=type(exc).__name__, message=str(exc))
        raise
