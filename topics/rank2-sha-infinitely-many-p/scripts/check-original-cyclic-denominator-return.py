#!/usr/bin/env sage-python
"""Fixed public software check of complete cyclic quotient and content returns.

This is an isolated software check, not an original geometric rank-306 run.
All native matrices represent the complete standard-monomial quotient.
Every result is compared with the unchanged original whole algorithm and
Sage 10.6's complete polynomial HNF transformation, including ALL entries.
"""
import os
if (os.environ.get("GITHUB_ACTIONS") != "true" or
        os.environ.get("GITHUB_REPOSITORY") != "Rogerhu12/math-research-public"):
    raise SystemExit("Use only the named public research Actions.")

from copy import copy
import hashlib
from pathlib import Path
import time
from sage.all import GF, PolynomialRing, identity_matrix, matrix
from sage.version import version as SAGE_VERSION
import original_pair_reset_row_reduction as reference
import original_native_pair_reset as native_owner
import original_polynomial_row_reduction as old_division
import original_complete_quadratic_returns as complete_returns
import original_ys_divisor_ideal_tools as ideal_tools
import original_row_operation_right_return as replay
import original_cyclic_denominator_return as candidate

HERE = Path(__file__).resolve().parent
PINNED = {
    "original_affine_fast_operations.py": "1e0ffc3533022e17ca3da39e6cdd85997425f1150f6bb943d8e9a500e632c67b",
    "original_affine_multiplication.py": "ff55083ab0e25d6b44991b64fa9cdc63d397842add1c474459e42986437e65a2",
    "original_complete_quadratic_polynomials.pyx": "7742254770d03bbdab649902e4a9faf92dc7e82c0fb360d279b496b7eb7ed917",
    "original_complete_quadratic_returns.py": "7da06cd12f35f7f2b98bf0c2c247c2732c838924c5497d3b8755b34932ce6d09",
    "original_degree_bounded_row_reduction.py": "41be1b362e024ba847240c7bd928ae4e991b3c160d1c3556f7d8837d9b1788fa",
    "original_pair_reset_row_reduction.py": "ffa85755931dfb3b52e68a50981ad4db6b49714287efe92e0403922a8eef802f",
    "original_polynomial_row_reduction.py": "9e3413176d9cce5fa00836ee05ea450483c60a786407b40fcef2ae226f009936",
    "original_projector_hermite.py": "545b330c4b7fb0c876e15f0ea6b94c9e35d29fdaf94b87707b3853dd33c32545",
    "original_ys_artinian_norm_tools.py": "f604ae5f862519f5ccdce609a78ef05866fd85ae81ea699fb1de06f47b550714",
    "original_ys_closed_point_tools.py": "7428cadb6b2179aebd547c749ec11ae46305476947aa443f7266e64d03ccc7bb",
    "original_ys_divisor_ideal_tools.py": "661075eecb9c7ba67da615c89fd3b7dbf2834b08ca8e1534c1713894dc1226d7",
    "original_ys_integral_image_tools.py": "268ae368f0aea343b1490d2245d19475e82c193a3dd4f2e0cc747aec49ff86c0",
    "original_ys_local_value_tools.py": "566f231e614f4b961cbd695318a159ee92b08a99de2da6f4c8786474e832b5a1",
    "original_ys_scalar_colon_tools.py": "b643b02deb3948d352a3fc252008f9fb939bef5083184f7c9cc85653ef3a8436",
    "section_quotient_algebra.py": "4c66da67ab76a61c075367a9a23801b726ebaa6ed098226dd943a708020a0536",
    "original_native_pair_reset.py": "a270a003fbbe80d3cced1856fb19707ab83cb250bc57d2152da5583978fd7e28",
    "original_native_polynomial_rows.pyx": "c940f1759238103c85bf01bf22427394c87524eaf7ebe3f08488457447246922",
    "original_row_operation_right_return.py": "ce7675e8b57fee62a2b5c7907a5cd5887759e4d72bc1e4117f04c4032e4dc225",
    "original_cyclic_denominator_return.py": "4ebbe8018347d9bf6269d6e0d83960224bb399fa5ae1998b7d91e3c1ba96fbf1"
}

ORIGINAL_FUNCTION = reference.complete_pair_reset_row_hermite
ORIGINAL_NATIVE_PREPARE = native_owner.prepare_backend
ORIGINAL_DIVISION = old_division.full_polynomial_left_division
ORIGINAL_REDUCTION = old_division.complete_row_hermite
ORIGINAL_CANDIDATE = candidate.native_complete_cyclic_candidate
TOTAL_SECONDS = 420
STARTED = time.monotonic()


def check_time():
    if time.monotonic()-STARTED >= TOTAL_SECONDS:
        raise TimeoutError("The fixed complete-cyclic software-check budget was exhausted.")


def progress(stage, **data):
    check_time()
    print("RANK2_CYCLIC_DENOMINATOR_RETURN_STAGE "+
          ideal_tools.canonical(dict(stage=stage, **data)), flush=True)


def verify_pins():
    if SAGE_VERSION != "10.6":
        raise RuntimeError("Use the fixed Sage 10.6 image.")
    for name,expected in PINNED.items():
        assert hashlib.sha256((HERE/name).read_bytes()).hexdigest() == expected
    candidate.verify_source_pins()
    assert reference.complete_pair_reset_row_hermite is ORIGINAL_FUNCTION
    assert native_owner.prepare_backend is ORIGINAL_NATIVE_PREPARE
    assert old_division.full_polynomial_left_division is ORIGINAL_DIVISION
    assert old_division.complete_row_hermite is ORIGINAL_REDUCTION
    assert candidate.native_complete_cyclic_candidate is ORIGINAL_CANDIDATE
    return dict(PINNED)


def precondition(H,a):
    """Known full unimodular row changes; no source row or column is omitted."""
    M = copy(H)
    n,t = int(M.nrows()),M.base_ring().gen()
    if n >= 2:
        M.swap_rows(0,n-1)
        M.rescale_row(0,a)
        M.add_multiple_of_row(1,0,t**2+1)
        M.add_multiple_of_row(0,n-1,t+a+1)
    else:
        M.rescale_row(0,a)
    return M


def known_cyclic_H(R,n,q):
    """An explicit complete quotient, retaining every repeated factor of q."""
    t = R.gen()
    H = copy(identity_matrix(R,n))
    H[n-1,n-1] = q
    for i in range(n-1):
        H[i,n-1] = (t**(i+1)+(i+2)*t+i+1) % q
    assert H.is_hermite()
    return H


def compare_complete(M,name,wanted,expected_content=None,budget=None):
    check_time()
    snapshot = copy(M)
    snapshot.set_immutable()
    mutable = bool(M.is_mutable())
    old_H,attached,old_receipt = ORIGINAL_FUNCTION(
        M,progress=progress,label=name+": unchanged original entire HNF")
    assert attached is None
    official_H,official_U = copy(M).hermite_form(
        transformation=True,include_zero_rows=False)
    assert official_H == old_H and official_U*M == old_H
    H,U,receipt = candidate.complete_cyclic_denominator_return(
        M,progress=progress,label=name,
        budget=budget or candidate.CyclicBudget(max_seconds=120))
    assert H == old_H and U == official_U and U*M == H
    assert ideal_tools._hermite_remainder_rows(M,H).is_zero()
    verification = receipt["complete_verification"]
    assert verification["full_monic_determinant_sha256"] == old_receipt[
        "full_monic_determinant_sha256"]
    assert verification["full_quotient_length"] == old_receipt["determinant_degree"]
    assert verification["complete_coordinate_return_C_P_equals_H"]
    assert verification["complete_original_transform_return_U_M_equals_H"]
    assert verification["both_polynomial_row_module_inclusions_verified"]
    if wanted == "cyclic":
        assert receipt["route"] == "complete cyclic quotient with exact scalar-content restoration"
        assert receipt["cyclic_attempt"]["cyclic"] is True
        assert receipt["cyclic_attempt"]["complete_krylov_rank"] == receipt[
            "quotient_after_exact_content_division_length"]
    elif wanted == "noncyclic":
        assert receipt["route"] == "unchanged complete original fallback"
        attempt = receipt["cyclic_attempt"]
        assert attempt["cyclic"] is False
        assert attempt["complete_krylov_rank"] < attempt["complete_quotient_dimension"]
        assert receipt["fallback_original_input_sha256"] == ideal_tools.polynomial_matrix_digest(M)
    elif wanted == "nonprime":
        assert receipt["route"] == "unchanged complete original fallback"
        assert not receipt["cyclic_attempt"]["prime_admission"]["applied"]
        assert receipt["fallback_original_input_sha256"] == ideal_tools.polynomial_matrix_digest(M)
    elif wanted == "budget":
        assert receipt["route"] == "unchanged complete original fallback"
        assert receipt["cyclic_attempt"]["cyclic"] is None
        assert receipt["fallback_original_input_sha256"] == ideal_tools.polynomial_matrix_digest(M)
    else:
        raise AssertionError("Unknown fixed expected route.")
    if expected_content is not None:
        assert receipt["content"]["monic_content_sha256"] == ideal_tools.polynomial_digest(
            expected_content.monic())
        assert receipt["content"]["actual_content_degree"] == expected_content.degree()
    assert M == snapshot and bool(M.is_mutable()) == mutable
    assert H.base_ring() is M.base_ring() and U.base_ring() is M.base_ring()
    verify_pins()
    result = dict(
        name=name,rank=int(M.nrows()),
        original_constant_degree=int(M.base_ring().base_ring().degree()),
        characteristic=int(M.base_ring().base_ring().characteristic()),
        expected_and_actual_route=wanted,
        complete_original_M_sha256=ideal_tools.polynomial_matrix_digest(M),
        complete_H_sha256=ideal_tools.polynomial_matrix_digest(H),
        complete_U_sha256=ideal_tools.polynomial_matrix_digest(U),
        full_quotient_length=verification["full_quotient_length"],
        complete_H_and_U_equal_to_both_original_and_official_returns=True,
        full_original_remainders_and_all_matrix_entries_verified=True,
        original_input_values_and_mutability_unchanged=True,
        original_functions_unchanged=True,
        native_complete_return_bound=bool(complete_returns.BOUND),
        complete_candidate_receipt=receipt)
    return result,(M,H,U,receipt)


def rejected(name,callback):
    check_time()
    try:
        callback()
    except (AssertionError,ArithmeticError,ValueError,TypeError,RuntimeError,
            AttributeError,MemoryError,TimeoutError) as error:
        return dict(name=name,exception=type(error).__name__,rejected=True)
    raise AssertionError("An invalid complete cyclic return was accepted: "+name)


def main():
    verify_pins()
    preparation = candidate.prepare_backend()
    assert preparation["exactly_the_original_19_native_source_replacements"]
    fp = GF(29)
    Rmod = PolynomialRing(fp,"cyclic_return_modulus")
    k = GF(29**2,"cyclic_return_a",modulus=Rmod.gen()**2-2)
    a = k.gen()
    R = PolynomialRing(k,"cyclic_return_t")
    t = R.gen()
    checks,refusals = [],[]

    # This full Popov basis is not HNF.  The cyclic candidate must construct
    # genuinely nonidentity complete coordinates and the same U as the oracle.
    first = matrix(R,[[t,1],[1,t]])
    row,saved = compare_complete(first,"full Popov to complete cyclic quotient","cyclic",
                                 expected_content=R.one())
    assert not first.is_hermite()
    assert row["complete_candidate_receipt"]["complete_popov_coordinate_return"][
        "actual_full_row_division_steps"] > 0
    checks.append(row)

    H = known_cyclic_H(R,4,t**7)
    immutable = precondition(H,k(3))
    immutable.set_immutable()
    row,unused = compare_complete(
        immutable,"cyclic nilpotent quotient with immutable original input","cyclic",
        expected_content=R.one())
    assert row["full_quotient_length"] == 7
    checks.append(row)

    h = (t-a)**2*(t+1)**3
    H = known_cyclic_H(R,3,t**5*(t-1)**3)
    content_input = h*precondition(H,k(2))
    row,content_data = compare_complete(
        content_input,"genuine quadratic scalar content fully restored","cyclic",
        expected_content=h)
    assert any(c not in fp for c in h.list())
    assert row["complete_candidate_receipt"]["scalar_content_length_contribution"] == 3*h.degree()
    assert row["complete_candidate_receipt"]["quotient_after_exact_content_division_length"] == 8
    checks.append(row)

    h0 = (t-a)**4
    unit_quotient = h0*precondition(identity_matrix(R,4),k(2))
    row,unused = compare_complete(
        unit_quotient,"nonreduced scalar thickness over a unit quotient","cyclic",
        expected_content=h0)
    assert row["complete_candidate_receipt"]["cyclic_attempt"]["route"] == "zero complete quotient"
    assert row["full_quotient_length"] == 4*h0.degree()
    checks.append(row)

    # The module may be cyclic abstractly, but its ACTUAL last basis vector
    # need not generate it.  There is no search for a more convenient input.
    noncyclic_generator = matrix(R,[[t**2,0],[0,(t-1)**2]])
    row,unused = compare_complete(
        noncyclic_generator,"last original vector fails despite coprime factors","noncyclic",
        expected_content=R.one())
    assert row["complete_candidate_receipt"]["cyclic_attempt"]["complete_krylov_rank"] == 2
    checks.append(row)

    noncyclic_module = matrix(R,[[t**2,0,0],[0,t**2,0],[0,0,1]])
    row,unused = compare_complete(
        precondition(noncyclic_module,k(2)),"entire noncyclic nonreduced quotient","noncyclic",
        expected_content=R.one())
    assert row["complete_candidate_receipt"]["cyclic_attempt"]["complete_krylov_rank"] == 0
    checks.append(row)

    nonprime_H = matrix(R,[[(t-a)**2,t+a],[0,(t-a-1)**3]])
    row,nonprime_data = compare_complete(
        precondition(nonprime_H,a+1),"unsupported actual nonprime quotient uses full original fallback",
        "nonprime",expected_content=R.one())
    checks.append(row)

    fp41 = GF(41)
    R41 = PolynomialRing(fp41,"cyclic_return_s")
    s = R41.gen()
    row,unused = compare_complete(
        precondition(known_cyclic_H(R41,3,(s+1)**4*(s-2)**2),fp41(3)),
        "native complete quotient in the second original prime","cyclic",
        expected_content=R41.one())
    checks.append(row)

    Rp = PolynomialRing(fp,"cyclic_return_prime_t")
    z = Rp.gen()
    row,unused = compare_complete(
        precondition(known_cyclic_H(Rp,2,(z**2+2)**3),fp(2)),
        "native prime coefficients with repeated polynomial factor","cyclic",
        expected_content=Rp.one())
    checks.append(row)

    h1 = (t-a)**6
    row,unused = compare_complete(
        matrix(R,[[3*h1]]),"rank one keeps all original content and constant unit","cyclic",
        expected_content=h1)
    assert row["full_quotient_length"] == 6
    checks.append(row)

    row,unused = compare_complete(
        first,"explicit native allocation budget returns to the same entire input","budget",
        expected_content=R.one(),budget=candidate.CyclicBudget(
            max_native_cells=1,max_seconds=120))
    checks.append(row)

    # A balanced complete nilpotent quotient exercises the native path on
    # all 96 dimensions.  Relations t^12 e_i=e_(i-1) make the ORIGINAL
    # last basis vector cyclic; t^96 is retained, not reduced to t.
    balanced = matrix(R,8,8)
    for i in range(8):
        balanced[i,i] = t**12
        if i:
            balanced[i,i-1] = -1
    row,unused = compare_complete(
        precondition(balanced,k(2)),"balanced 96-dimensional complete nilpotent Krylov module",
        "cyclic",expected_content=R.one())
    assert row["full_quotient_length"] == 96
    assert row["complete_candidate_receipt"]["cyclic_attempt"]["complete_krylov_rank"] == 96
    checks.append(row)

    # Install the ACTUAL current native complete-return wrapper.  Neither
    # original reduction nor integral division is replaced by this candidate.
    binding = complete_returns.bind_original_returns()
    assert complete_returns.BOUND
    assert ideal_tools._hermite_remainder_rows is complete_returns.complete_remainder_rows
    row,unused = compare_complete(
        content_data[0],"current native product and remainder wrapper on the cyclic route",
        "cyclic",expected_content=h)
    checks.append(row)
    row,unused = compare_complete(
        nonprime_data[0],"current native wrapper with unchanged full nonprime fallback",
        "nonprime",expected_content=R.one())
    checks.append(row)

    refusals.append(rejected("rectangular original input",
        lambda: candidate.complete_cyclic_denominator_return(matrix(R,2,3))))
    refusals.append(rejected("zero complete denominator",
        lambda: candidate.complete_cyclic_denominator_return(matrix(R,2,2))))
    refusals.append(rejected("singular complete denominator",
        lambda: candidate.complete_cyclic_denominator_return(matrix(R,[[t,1],[t,1]]))))
    Rwrong = PolynomialRing(GF(31),"wrong_cyclic_t")
    refusals.append(rejected("wrong original characteristic",
        lambda: candidate.complete_cyclic_denominator_return(identity_matrix(Rwrong,2))))
    refusals.append(rejected("nonpositive explicit work budget",
        lambda: candidate.CyclicBudget(max_native_cells=0)))
    refusals.append(rejected("wrong budget object",
        lambda: candidate.complete_cyclic_denominator_return(first,budget={})))
    refusals.append(rejected("unsupported attached input",
        lambda: candidate.complete_cyclic_denominator_return(first,attached=identity_matrix(R,2))))
    # The native quotient validator must not treat arbitrary weak Popov or
    # same-determinant matrices as the column-reduced original basis.
    weak = matrix(Rp,[[z,0],[z,z**2]])
    refusals.append(rejected("weak Popov without full column reduction",
        lambda: candidate.native_complete_cyclic_candidate(weak,candidate.CyclicBudget())))
    unsorted = matrix(Rp,[[0,z],[z,0]])
    refusals.append(rejected("unsorted original pivot positions",
        lambda: candidate.native_complete_cyclic_candidate(unsorted,candidate.CyclicBudget())))
    nonmonic = matrix(Rp,[[2*z,0],[0,z]])
    refusals.append(rejected("nonmonic complete Popov pivots",
        lambda: candidate.native_complete_cyclic_candidate(nonmonic,candidate.CyclicBudget())))
    refusals.append(rejected("nonprime field passed to native full quotient",
        lambda: candidate.native_complete_cyclic_candidate(
            matrix(R,[[t-a,0],[0,t-a]]),candidate.CyclicBudget())))
    Pdiv = matrix(Rp,[[z,0],[0,z]])
    refusals.append(rejected("complete target not in full Popov module",
        lambda: candidate.complete_popov_coordinates(
            Pdiv,identity_matrix(Rp,2),candidate.CyclicBudget())))
    Rother = PolynomialRing(fp,"other_cyclic_parameter")
    refusals.append(rejected("coordinate target in a different original ring",
        lambda: candidate.complete_popov_coordinates(
            Pdiv,identity_matrix(Rother,2),candidate.CyclicBudget())))

    # Inject a mathematically false full candidate only into this isolated
    # new entry point.  Exact polynomial coordinate verification must reject;
    # all pinned original functions and source files remain untouched.
    def bad_same_det():
        def changed(P,budget,progress=None,started=None):
            H,receipt = ORIGINAL_CANDIDATE(P,budget,progress=progress,started=started)
            assert H is not None and H.nrows() == 2 and H[1,1].degree() > 0
            H = copy(H)
            H[0,1] += 1
            assert H.is_hermite()
            return H,receipt
        candidate.native_complete_cyclic_candidate = changed
        try:
            return candidate.complete_cyclic_denominator_return(first)
        finally:
            candidate.native_complete_cyclic_candidate = ORIGINAL_CANDIDATE
    refusals.append(rejected("same determinant but wrong complete cyclic candidate",bad_same_det))
    def bad_rank_only():
        def changed(P,budget,progress=None,started=None):
            return identity_matrix(P.base_ring(),P.nrows()),dict(
                route="deliberately false rank-only test candidate",cyclic=True)
        candidate.native_complete_cyclic_candidate = changed
        try:
            return candidate.complete_cyclic_denominator_return(first)
        finally:
            candidate.native_complete_cyclic_candidate = ORIGINAL_CANDIDATE
    refusals.append(rejected("rank-only candidate cannot bypass full module return",bad_rank_only))
    def insufficient_coordinate_budget():
        return candidate.complete_cyclic_denominator_return(first,
            budget=candidate.CyclicBudget(max_coordinate_coefficients=1))
    refusals.append(rejected("actual polynomial coordinate work budget",insufficient_coordinate_budget))
    def insufficient_right_budget():
        return candidate.complete_cyclic_denominator_return(first,budget=candidate.CyclicBudget(
            return_budget=replay.ReturnBudget(max_work_coefficients=1)))
    refusals.append(rejected("actual reverse-right full coefficient budget",insufficient_right_budget))

    verify_pins()
    assert len(checks) == 14 and len(refusals) == 17
    source_files = tuple(dict.fromkeys((
        Path(__file__).name,"check-original-complete-quadratic-api.py",
    )+tuple(PINNED)+candidate.SOURCE_DEPENDENCIES))
    hashes = {name:hashlib.sha256((HERE/name).read_bytes()).hexdigest()
              for name in source_files}
    result = dict(
        kind="original-complete-cyclic-denominator-return-software-check",status="PASS",
        source=os.environ["RANK2_SOURCE_SHA"],run_id=os.environ["RANK2_RUN_ID"],
        run_attempt=os.environ["RANK2_RUN_ATTEMPT"],
        root_readme_blob=os.environ["RANK2_ROOT_README_SHA"],
        topic_readme_blob=os.environ["RANK2_TOPIC_README_SHA"],
        source_file_sha256=hashes,preparation=preparation,
        checks=checks,refusals=refusals,
        complete_comparison_count=len(checks),rejection_count=len(refusals),
        source_capture_uses_exact_original_19_native_replacements=True,
        actual_polynomial_operation_coefficients_retained=True,
        all_complete_Krylov_coordinates_and_original_matrix_returns_checked=True,
        scalar_content_and_every_nonreduced_length_restored=True,
        failed_cyclic_test_uses_unchanged_original_full_input=True,
        current_native_complete_return_binding=binding,
        original_functions_and_production_source_files_unchanged=True,
        original_geometric_input_executed=False,
        rank_306_or_delta_3670_performance_improvement_claimed=False,
        total_process_peak_memory_bound_claimed=False,
        resource_limits_are_not_mathematical_dimension_cutoffs=True,
        data_artifact_written=False,elapsed_seconds=time.monotonic()-STARTED)
    payload = ideal_tools.canonical(result)
    print("RANK2_CYCLIC_DENOMINATOR_RETURN_API_RESULT "+payload,flush=True)
    print("RANK2_CYCLIC_DENOMINATOR_RETURN_API_SHA256 "+
          hashlib.sha256(payload.encode()).hexdigest(),flush=True)


if __name__ == "__main__":
    main()
