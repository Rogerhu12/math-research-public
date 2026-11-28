#!/usr/bin/env sage-python
"""Public small software check of complete reverse-right polynomial returns.

Only this checker captures a pinned original function's actual coefficients.
The old source file, module functions and production bindings are unchanged.
No original rank-306 geometric computation is performed by this request.
"""
import os
if (os.environ.get("GITHUB_ACTIONS") != "true" or
        os.environ.get("GITHUB_REPOSITORY") != "Rogerhu12/math-research-public"):
    raise SystemExit("Use only the named public research Actions.")

from copy import copy
import hashlib
import inspect
import json
from pathlib import Path
import time
from sage.all import GF, PolynomialRing, identity_matrix, matrix
from sage.version import version as SAGE_VERSION
import original_pair_reset_row_reduction as reference
import original_polynomial_row_reduction as old_division
import original_complete_quadratic_returns as complete_returns
import original_ys_divisor_ideal_tools as ideal_tools
import original_row_operation_right_return as replay

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
    "section_quotient_algebra.py": "4c66da67ab76a61c075367a9a23801b726ebaa6ed098226dd943a708020a0536"
}
ORIGINAL_FUNCTION = reference.complete_pair_reset_row_hermite
ORIGINAL_DIVISION = old_division.full_polynomial_left_division
ORIGINAL_REDUCTION = old_division.complete_row_hermite
TOTAL_SECONDS = 420
STARTED = time.monotonic()


def check_time():
    if time.monotonic()-STARTED >= TOTAL_SECONDS:
        raise TimeoutError("The fixed small-software budget was exhausted.")


def progress(stage, **data):
    check_time()
    print("RANK2_ROW_OPERATION_RIGHT_RETURN_STAGE "+
          ideal_tools.canonical(dict(stage=stage, **data)), flush=True)


def verify_pins():
    if SAGE_VERSION != "10.6":
        raise RuntimeError("This software check uses the fixed Sage 10.6 image.")
    for name, expected in PINNED.items():
        assert hashlib.sha256((HERE/name).read_bytes()).hexdigest() == expected
    replay.verify_source_pins()
    assert reference.complete_pair_reset_row_hermite is ORIGINAL_FUNCTION
    assert old_division.full_polynomial_left_division is ORIGINAL_DIVISION
    assert old_division.complete_row_hermite is ORIGINAL_REDUCTION
    return dict(PINNED)


def captured_original(M, prefix_only):
    """Insert one data hook into record(); execute the exact pinned source.

    In prefix mode the body stops only AFTER the original complete, sorted,
    column-reduced unshifted Popov stage.  In full mode no arithmetic source
    statement is added, deleted or changed.  No original module is rebound.
    """
    verify_pins()
    R, n = M.base_ring(), int(M.nrows())
    stream = replay.CompleteRowOperationStream(
        R, n, source_metadata=dict(
            source_file="original_pair_reset_row_reduction.py",
            source_sha256=PINNED["original_pair_reset_row_reduction.py"],
            source_function="complete_pair_reset_row_hermite",
            original_complete_popov_prefix_only=bool(prefix_only),
            one_actual_coefficient_record_hook=True),
        budget=replay.ReturnBudget(max_seconds=90))
    original_source = inspect.getsource(ORIGINAL_FUNCTION)
    original_name = "def complete_pair_reset_row_hermite("
    local_name = "def captured_complete_pair_reset_row_hermite("
    assert original_source.count(original_name) == 1
    record_tail = '        stream.update(b"\\n")\n'
    hook = (
        '        _capture_stream.append(kind, indices, tuple(\n'
        '            R(c) if R is original_ring else original_ring([\n'
        '                original_field(z) for z in R(c).list()])\n'
        '            for c in coefficients))\n')
    assert original_source.count(record_tail) == 1
    changed = original_source.replace(original_name, local_name, 1)
    changed = changed.replace(record_tail, record_tail+hook, 1)
    inverse = changed.replace(record_tail+hook, record_tail, 1)
    inverse = inverse.replace(local_name, original_name, 1)
    assert inverse == original_source
    prefix_line = '    delta = popov(0, m, [0]*n, "whole unshifted Popov")\n'
    if prefix_only:
        assert changed.count(prefix_line) == 1
        prefix = changed.split(prefix_line, 1)[0]+prefix_line
        restored_prefix = prefix.replace(record_tail+hook, record_tail, 1)
        restored_prefix = restored_prefix.replace(local_name, original_name, 1)
        assert restored_prefix == original_source.split(prefix_line, 1)[0]+prefix_line
        suffix = (
            '    assert m == n\n'
            '    P = matrix(R, current)\n'
            '    if R is not original_ring:\n'
            '        P = matrix(original_ring, n, n, [original_ring([\n'
            '            original_field(c) for c in f.list()]) for f in P.list()])\n'
            '    assert P.base_ring() is original_ring\n'
            '    pivot_degrees = [int(P[j,j].degree()) for j in range(n)]\n'
            '    assert all(P[j,j] and P[j,j].leading_coefficient() == 1 for j in range(n))\n'
            '    assert sum(pivot_degrees) == delta\n'
            '    assert all(not P[i,j] or P[i,j].degree() < pivot_degrees[j]\n'
            '               for i in range(n) for j in range(n) if i != j)\n'
            '    return P, None, dict(operation_counts=dict(counts),\n'
            '        full_operation_stream_sha256=stream.hexdigest(),\n'
            '        determinant_degree=int(delta), exact_prime_subfield_descent=field_descent,\n'
            '        full_column_reduced_original_popov_prefix=True,\n'
            '        original_prefix_inverse_text_verified=True)\n')
        executable = prefix+suffix
    else:
        executable = changed
    namespace = dict(vars(reference))
    namespace["_capture_stream"] = stream
    exec(compile(executable, "<pinned-original-row-operation-capture>", "exec"),
         namespace)
    P, attached, receipt = namespace["captured_complete_pair_reset_row_hermite"](
        M, progress=progress, label="small exact actual-coefficient transcript")
    assert attached is None
    stream.seal()
    assert receipt["operation_counts"] == stream.counts
    assert receipt["full_operation_stream_sha256"] == stream.receipt()["operation_stream_sha256"]
    assert reference.complete_pair_reset_row_hermite is ORIGINAL_FUNCTION
    assert old_division.full_polynomial_left_division is ORIGINAL_DIVISION
    assert old_division.complete_row_hermite is ORIGINAL_REDUCTION
    return P, stream, receipt


def precondition(H, a):
    """Explicit unimodular source; not a surrogate geometric input."""
    M = copy(H)
    n, t = int(M.nrows()), M.base_ring().gen()
    if n >= 2:
        M.swap_rows(0, n-1)
        M.rescale_row(0, a)
        M.add_multiple_of_row(1, 0, t**2+1)
        M.add_multiple_of_row(0, n-1, t+a+1)
    return M


def compare_complete(M, name, prefix_only=True):
    check_time()
    before = copy(M)
    before.set_immutable()
    mutable = bool(M.is_mutable())
    H, attached, old_receipt = ORIGINAL_FUNCTION(
        M, progress=progress, label=name+": unchanged original whole HNF")
    assert attached is None
    official_H, official_U = copy(M).hermite_form(
        transformation=True, include_zero_rows=False)
    assert official_H == H and official_U*M == H
    P, stream, captured = captured_original(M, prefix_only)
    if prefix_only:
        C, division = ORIGINAL_DIVISION(
            P, H, progress=progress, label=name+": unchanged full polynomial coordinates")
        assert division["every_source_row_returned_against_original_denominator"]
    else:
        assert P == H
        C, division = identity_matrix(M.base_ring(), M.nrows()), None
    U, receipt = replay.restore_complete_denominator_transform(
        M, P, H, C, stream, progress=progress)
    assert U == official_U and U*M == H and C*P == H
    assert M == before and bool(M.is_mutable()) == mutable
    assert int(receipt["full_quotient_length"]) == int(old_receipt["determinant_degree"])
    assert receipt["full_monic_determinant_sha256"] == old_receipt["full_monic_determinant_sha256"]
    assert receipt["both_polynomial_row_module_inclusions_verified"]
    assert reference.complete_pair_reset_row_hermite is ORIGINAL_FUNCTION
    result = dict(
        name=name, rank=int(M.nrows()), field_degree=int(M.base_ring().base_ring().degree()),
        characteristic=int(M.base_ring().base_ring().characteristic()),
        full_quotient_length=receipt["full_quotient_length"],
        complete_original_M_sha256=ideal_tools.polynomial_matrix_digest(M),
        complete_P_sha256=ideal_tools.polynomial_matrix_digest(P),
        complete_H_sha256=ideal_tools.polynomial_matrix_digest(H),
        complete_C_sha256=ideal_tools.polynomial_matrix_digest(C),
        complete_U_sha256=ideal_tools.polynomial_matrix_digest(U),
        captured_actual_operation_counts=dict(stream.counts),
        actual_full_transcript_sha256=stream.receipt()["operation_stream_sha256"],
        original_prime_descent_applied=bool(captured["exact_prime_subfield_descent"]["applied"]),
        whole_popov_prefix_only=bool(prefix_only),
        complete_reference_H_and_U_equal=True,
        complete_C_P_and_U_M_and_original_remainders_verified=True,
        original_input_values_and_mutability_unchanged=True,
        original_functions_unchanged=True,
        native_complete_return_bound=bool(complete_returns.BOUND),
        right_return=receipt["right_return"])
    return result, (M, P, H, C, stream, U)


def rejected(name, callback):
    check_time()
    try:
        callback()
    except (AssertionError, ArithmeticError, ValueError, TypeError,
            RuntimeError, AttributeError, MemoryError, TimeoutError) as error:
        return dict(name=name, exception=type(error).__name__, rejected=True)
    raise AssertionError("An invalid complete return was accepted: "+name)


def main():
    verify_pins()
    fp = GF(29)
    P0 = PolynomialRing(fp, "right_return_modulus")
    k = GF(29**2, "right_return_a", modulus=P0.gen()**2-2)
    a = k.gen()
    R = PolynomialRing(k, "right_return_t")
    t = R.gen()
    checks, refusals = [], []

    # This is genuinely column-reduced Popov but not Hermite.  Thus C != I
    # and this case detects confusing a Popov basis with the HNF.
    M = matrix(R, [[t, 1], [1, t]])
    row, data = compare_complete(M, "full Popov is not Hermite")
    assert not M.is_hermite() and data[3] != identity_matrix(R, 2)
    checks.append(row)

    H = matrix(R, 4, 4)
    for i in range(4):
        H[i,i] = (t-a)**(2+i%2)
        for j in range(i+1, 4):
            H[i,j] = (a+i+j)*t+(j+1)
    assert H.is_hermite()
    M = precondition(H, a+1)
    M.set_immutable()
    row, saved = compare_complete(M, "nonprime nonreduced immutable source")
    assert any(c not in fp for f in M.list() for c in f.list())
    checks.append(row)

    q = t**2-a
    assert q.is_irreducible()
    Hq = matrix(R, [[q**2, t+a], [0, q**3]])
    row, unused = compare_complete(precondition(Hq, a), "repeated irreducible primary thickness")
    checks.append(row)

    Mp = precondition(matrix(R, [[t**2+1, 1, t],
                                [0, (t-1)**3, 1], [0, 0, t+2]]), k(2))
    row, unused = compare_complete(Mp, "entire prime-field descent returned to original ring")
    assert row["original_prime_descent_applied"]
    checks.append(row)

    k41 = GF(41**2, "right_return_b")
    b = k41.gen()
    R41 = PolynomialRing(k41, "right_return_s")
    s = R41.gen()
    H41 = matrix(R41, [[(s-b)**2, s+b, b],
                       [0, (s-b-1)**3, s+1], [0, 0, s**2+b]])
    row, unused = compare_complete(precondition(H41, b), "second original quadratic field")
    checks.append(row)

    Rp = PolynomialRing(fp, "right_return_prime_t")
    z = Rp.gen()
    row, unused = compare_complete(
        precondition(matrix(Rp, [[z**2, z+1], [0, (z-1)**3]]), fp(3)),
        "actual prime coefficient ring")
    checks.append(row)

    row, unused = compare_complete(precondition(identity_matrix(R, 3), a+1),
                                   "unit determinant full source")
    assert row["full_quotient_length"] == 0
    checks.append(row)

    # Its first whole Popov basis already has column degrees (2,2,2);
    # the original first-column gcd is 1, while no single entry is a unit.
    # Therefore the unchanged original full reducer must really record a
    # simultaneous determinant-one Bezout block.
    Mb = matrix(R, [[t**2+1, 1, 1], [t, t**2, 1], [t+1, 1, t**2+2]])
    row, unused = compare_complete(Mb, "actual original simultaneous Bezout coefficients",
                                   prefix_only=False)
    assert row["captured_actual_operation_counts"]["bezout"] > 0
    checks.append(row)

    # Repeat a complete nonprime return after the ACTUAL native wrapper is
    # installed, including its current dynamic remainder entry point.
    binding = complete_returns.bind_original_returns()
    assert complete_returns.BOUND
    row, data = compare_complete(saved[0], "current native full-return binding")
    checks.append(row)
    M, P, H, C, stream, U = data
    assert ideal_tools._hermite_remainder_rows is complete_returns.complete_remainder_rows

    def wrong_P():
        wrong = copy(P)
        wrong[0,0] += 1
        return replay.restore_complete_denominator_transform(M, wrong, H, C, stream)
    refusals.append(rejected("changed complete recorded intermediate", wrong_P))
    def wrong_M():
        wrong = copy(M)
        wrong[0,0] += 1
        return replay.restore_complete_denominator_transform(wrong, P, H, C, stream)
    refusals.append(rejected("changed complete original denominator", wrong_M))
    def wrong_C():
        wrong = copy(C)
        wrong[0,0] += 1
        return replay.restore_complete_denominator_transform(M, P, H, wrong, stream)
    refusals.append(rejected("changed complete coordinate matrix", wrong_C))
    def same_det_wrong_H():
        wrong = copy(H)
        wrong[0,1] += 1
        assert wrong.is_hermite()
        assert all(wrong[j,j] == H[j,j] for j in range(H.nrows()))
        return replay.restore_complete_denominator_transform(M, P, wrong, C, stream)
    refusals.append(rejected("same determinant but changed full Hermite module", same_det_wrong_H))
    refusals.append(rejected("wrong complete rank",
        lambda: replay.reverse_right_return(C.matrix_from_rows([0]), stream)))
    Rother = PolynomialRing(k, "wrong_right_return_variable")
    refusals.append(rejected("different original polynomial ring",
        lambda: replay.reverse_right_return(identity_matrix(Rother, M.nrows()), stream)))
    unsealed = replay.CompleteRowOperationStream(R, M.nrows())
    refusals.append(rejected("unsealed coefficient transcript",
        lambda: replay.reverse_right_return(C, unsealed)))
    refusals.append(rejected("nonunit row scale",
        lambda: replay.CompleteRowOperationStream(R, 2).append("scale", (0,), (t,))))
    refusals.append(rejected("wrong simultaneous Bezout determinant",
        lambda: replay.CompleteRowOperationStream(R, 2).append("bezout", (0,1), (1,0,0,2))))
    refusals.append(rejected("two-row operation with a repeated index",
        lambda: replay.CompleteRowOperationStream(R, 2).append("add", (0,0), (1,))))
    def altered_sealed():
        bad = replay.CompleteRowOperationStream(R, 2)
        bad.append("add", (0,1), (t,))
        bad.seal()
        bad.operations = (("add", (0,1), (t+1,)),)
        return replay.reverse_right_return(identity_matrix(R, 2), bad)
    refusals.append(rejected("coefficient change after sealing", altered_sealed))
    def false_empty_prefix():
        bad = replay.CompleteRowOperationStream(R, M.nrows()).seal()
        return replay.restore_complete_denominator_transform(M, P, H, C, bad)
    assert P != M
    refusals.append(rejected("false same-ring transcript with no recorded operations",
                            false_empty_prefix))
    def inadequate_budget():
        bad = replay.CompleteRowOperationStream(R, 2,
            budget=replay.ReturnBudget(max_work_coefficients=1)).seal()
        return replay.reverse_right_return(identity_matrix(R, 2), bad)
    refusals.append(rejected("actual work budget is insufficient", inadequate_budget))

    verify_pins()
    source_files = tuple(dict.fromkeys((
        Path(__file__).name, "check-original-complete-quadratic-api.py",
        "original_row_operation_right_return.py",
    ) + tuple(PINNED)))
    hashes = {name:hashlib.sha256((HERE/name).read_bytes()).hexdigest()
              for name in source_files}
    result = dict(
        kind="original-row-operation-right-return-software-check", status="PASS",
        source=os.environ["RANK2_SOURCE_SHA"], run_id=os.environ["RANK2_RUN_ID"],
        run_attempt=os.environ["RANK2_RUN_ATTEMPT"],
        root_readme_blob=os.environ["RANK2_ROOT_README_SHA"],
        topic_readme_blob=os.environ["RANK2_TOPIC_README_SHA"],
        source_file_sha256=hashes, checks=checks, refusals=refusals,
        complete_matrix_comparison_count=len(checks), rejection_count=len(refusals),
        source_record_hook_inverse_verified=True,
        original_full_reducer_and_division_functions_unchanged=True,
        actual_coefficients_retained_not_reconstructed_from_digests=True,
        native_complete_return_binding=binding,
        original_geometric_input_executed=False,
        rank_306_performance_improvement_claimed=False,
        total_process_peak_memory_bound_claimed=False,
        resource_budget_is_not_a_dimension_or_quotient_length_cutoff=True,
        data_artifact_written=False, elapsed_seconds=time.monotonic()-STARTED)
    payload = ideal_tools.canonical(result)
    print("RANK2_ROW_OPERATION_RIGHT_RETURN_API_RESULT "+payload, flush=True)
    print("RANK2_ROW_OPERATION_RIGHT_RETURN_API_SHA256 "+
          hashlib.sha256(payload.encode()).hexdigest(), flush=True)


if __name__ == "__main__":
    main()
