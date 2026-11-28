#!/usr/bin/env sage-python
"""Isolated COMPLETE cyclic quotient return after the original Popov prefix.

No production binding is installed.  The input is the actual whole square
denominator matrix, in its unchanged original ring.  Its monic scalar content
is divided exactly and is restored to EVERY returned row and determinant.
The unchanged original Popov prefix supplies an actual coefficient transcript.
A native finite-field solve is attempted only for the COMPLETE quotient.
Failure of the last standard vector to generate that quotient returns to the
unchanged complete original algorithm on the ORIGINAL, undivided input.

The final certificate is still C P=H, U M=H, every original row modulo H,
monic complete HNF, and the full nonreduced determinant length.
"""
import os
if (os.environ.get("GITHUB_ACTIONS") != "true" or
        os.environ.get("GITHUB_REPOSITORY") != "Rogerhu12/math-research-public"):
    raise SystemExit("Use only the named public research Actions.")

from copy import copy
import hashlib
import inspect
from pathlib import Path
import time
from sage.all import identity_matrix, matrix, vector
from sage.version import version as SAGE_VERSION
import original_pair_reset_row_reduction as reference
import original_native_pair_reset as native_owner
import original_degree_bounded_row_reduction as descent
import original_ys_divisor_ideal_tools as ideal_tools
import original_row_operation_right_return as replay

HERE = Path(__file__).resolve().parent
IMPLEMENTATION = "original-complete-native-cyclic-quotient-and-content-return-v1"
PINNED = {
    "original_row_operation_right_return.py":
        "ce7675e8b57fee62a2b5c7907a5cd5887759e4d72bc1e4117f04c4032e4dc225",
    "original_native_pair_reset.py":
        "a270a003fbbe80d3cced1856fb19707ab83cb250bc57d2152da5583978fd7e28",
    "original_native_polynomial_rows.pyx":
        "c940f1759238103c85bf01bf22427394c87524eaf7ebe3f08488457447246922",
    "original_pair_reset_row_reduction.py":
        "ffa85755931dfb3b52e68a50981ad4db6b49714287efe92e0403922a8eef802f",
    "original_degree_bounded_row_reduction.py":
        "41be1b362e024ba847240c7bd928ae4e991b3c160d1c3556f7d8837d9b1788fa",
}
SOURCE_DEPENDENCIES = tuple(dict.fromkeys((
    "original_cyclic_denominator_return.py",
) + tuple(PINNED) + native_owner.SOURCE_DEPENDENCIES +
    replay.SOURCE_DEPENDENCIES))
REFERENCE_FUNCTION = reference.complete_pair_reset_row_hermite
NATIVE_PREPARE_FUNCTION = native_owner.prepare_backend
PREPARATION = None
GENERATED_SOURCE = None
NATIVE_MODULE = None


def verify_source_pins():
    if SAGE_VERSION != "10.6":
        raise RuntimeError("The isolated native implementation is fixed to Sage 10.6.")
    for name, expected in PINNED.items():
        assert hashlib.sha256((HERE/name).read_bytes()).hexdigest() == expected
    replay.verify_source_pins()
    assert reference.complete_pair_reset_row_hermite is REFERENCE_FUNCTION
    assert native_owner.prepare_backend is NATIVE_PREPARE_FUNCTION
    return dict(PINNED)


def prepare_backend():
    """Reproduce the pinned 19 replacements; compile declarations, not instances."""
    global PREPARATION, GENERATED_SOURCE, NATIVE_MODULE
    verify_source_pins()
    if PREPARATION is not None:
        return dict(PREPARATION)
    original_preparation = native_owner.prepare_backend()
    original = inspect.getsource(NATIVE_PREPARE_FUNCTION)
    old_name = "def prepare_backend():"
    new_name = "def isolated_generated_source_return():"
    stop = "    ast.parse(source)\n"
    replacement = "    return source, native\n"
    assert original.count(old_name) == original.count(stop) == 1
    changed = original.replace(old_name, new_name, 1).replace(stop, replacement, 1)
    inverse = changed.replace(replacement, stop, 1).replace(new_name, old_name, 1)
    assert inverse == original
    namespace = dict(vars(native_owner))
    namespace.update(PREPARED=None, PREPARATION=None)
    exec(compile(changed, "<original-native-source-return-only>", "exec"), namespace)
    generated, native = namespace["isolated_generated_source_return"]()
    actual = hashlib.sha256(generated.encode()).hexdigest()
    assert actual == original_preparation["exact_generated_function_sha256"]
    assert original_preparation["checked_text_replacement_count"] == 19
    GENERATED_SOURCE, NATIVE_MODULE = generated, native
    PREPARATION = dict(
        kind="isolated-pinned-native-source-and-coefficient-capture-preparation",
        original_native_preparation=original_preparation,
        generated_source_sha256=actual,
        inverse_prepare_source_text_verified=True,
        exactly_the_original_19_native_source_replacements=True,
        mathematical_instance_executed_by_this_preparation=False,
        original_reducer_and_native_prepare_functions_unchanged=True,
        cached_data_are_only_source_and_compiled_declarations=True)
    return dict(PREPARATION)


class CyclicBudget:
    """Work and storage limits, not a bound on a mathematical quotient length."""
    def __init__(self, max_native_cells=64000000,
                 max_estimated_field_operations=100000000000,
                 max_krylov_entry_updates=150000000,
                 max_popov_coordinate_steps=600000000,
                 max_coordinate_coefficients=32000000,
                 max_seconds=None, return_budget=None):
        self.max_native_cells = int(max_native_cells)
        self.max_estimated_field_operations = int(max_estimated_field_operations)
        self.max_krylov_entry_updates = int(max_krylov_entry_updates)
        self.max_popov_coordinate_steps = int(max_popov_coordinate_steps)
        self.max_coordinate_coefficients = int(max_coordinate_coefficients)
        self.max_seconds = None if max_seconds is None else float(max_seconds)
        self.return_budget = return_budget or replay.ReturnBudget(max_seconds=max_seconds)
        if min(self.max_native_cells, self.max_estimated_field_operations,
               self.max_krylov_entry_updates, self.max_popov_coordinate_steps,
               self.max_coordinate_coefficients) <= 0:
            raise ValueError("All explicit work limits must be positive.")
        if self.max_seconds is not None and self.max_seconds <= 0:
            raise ValueError("The elapsed-time budget must be positive.")

    def check_time(self, started):
        if self.max_seconds is not None and time.monotonic()-started > self.max_seconds:
            raise TimeoutError("The complete cyclic-return elapsed-time budget is exhausted.")

    def receipt(self):
        return dict(
            max_native_cells=self.max_native_cells,
            max_estimated_field_operations=self.max_estimated_field_operations,
            max_krylov_entry_updates=self.max_krylov_entry_updates,
            max_popov_coordinate_steps=self.max_popov_coordinate_steps,
            max_coordinate_coefficients=self.max_coordinate_coefficients,
            max_seconds=self.max_seconds, right_return=self.return_budget.receipt(),
            dimension_or_quotient_length_cutoff_used=False,
            estimate_does_not_bound_FFPACK_workspace_or_polynomial_outputs=True,
            total_process_peak_memory_bound_claimed=False)


def _progress(progress, stage, **data):
    if progress is not None:
        progress(stage, **data)


def _map_matrix(A, target_ring):
    if A.base_ring() is target_ring:
        return copy(A)
    k = target_ring.base_ring()
    return matrix(target_ring, A.nrows(), A.ncols(), [
        target_ring([k(c) for c in f.list()]) for f in A.list()])


def _whole_prime_admission(M):
    R, k = M.base_ring(), M.base_ring().base_ring()
    if int(k.cardinality()) == int(k.characteristic()):
        return M, dict(
            applied=False, already_original_prime_field=True,
            every_original_coefficient_retained=True)
    prime, attached, scalar, receipt = descent._entire_prime_subfield_inputs(M, None)
    if not receipt["applied"]:
        return None, receipt
    assert attached is None and scalar == k.one()
    assert _map_matrix(prime, R) == M
    return prime, receipt


def exact_scalar_content(M):
    """Return h,M0 with h the monic gcd of ALL entries and h M0=M."""
    R, n = M.base_ring(), int(M.nrows())
    replay._admit_ring(R)
    if n <= 0 or M.ncols() != n:
        raise ValueError("The complete original denominator must be square.")
    h = R.zero()
    inspected = 0
    for value in M.list():
        inspected += 1
        h = h.gcd(value)
        if h and h.degree() == 0:
            h = R.one()
            break
    if not h:
        raise ArithmeticError("The complete denominator is the zero matrix.")
    h = h.monic()
    entries = []
    for value in M.list():
        quotient, residual = value.quo_rem(h)
        if residual or h*quotient != value:
            raise ArithmeticError("The scalar content did not divide a complete input entry.")
        entries.append(quotient)
    M0 = matrix(R, n, n, entries)
    assert h*M0 == M
    return h, M0, dict(
        monic_content_sha256=ideal_tools.polynomial_digest(h),
        actual_content_degree=int(h.degree()),
        entries_examined_until_gcd_is_unit_or_all_entries=inspected,
        every_input_entry_divided_and_multiplied_back=True,
        quotient_original_ring_retained=True,
        original_rank=n, original_input_sha256=ideal_tools.polynomial_matrix_digest(M),
        whole_content_quotient_sha256=ideal_tools.polynomial_matrix_digest(M0),
        scalar_primary_thickness_not_discarded=True)


def captured_original(M, prefix_only, use_native, budget, progress=None, label=""):
    """Capture actual coefficients without modifying any original module function."""
    verify_source_pins()
    R, n = M.base_ring(), int(M.nrows())
    if prefix_only and not use_native:
        raise ValueError("The isolated prefix path is the exact original native prefix.")
    if use_native:
        prepare_backend()
        source = GENERATED_SOURCE
        old_name = "def _complete_native_pair_reset_row_hermite("
        namespace = dict(native_owner.PREPARED.__globals__)
    else:
        source = inspect.getsource(REFERENCE_FUNCTION)
        old_name = "def complete_pair_reset_row_hermite("
        namespace = dict(vars(reference))
    local_name = "def isolated_captured_original_reducer("
    record_tail = '        stream.update(b"\\n")\n'
    hook = (
        '        _capture_stream.append(kind, indices, tuple(\n'
        '            R(c) if R is original_ring else original_ring([\n'
        '                original_field(z) for z in R(c).list()])\n'
        '            for c in coefficients))\n')
    assert source.count(old_name) == source.count(record_tail) == 1
    changed = source.replace(old_name, local_name, 1)
    changed = changed.replace(record_tail, record_tail+hook, 1)
    inverse = changed.replace(record_tail+hook, record_tail, 1)
    inverse = inverse.replace(local_name, old_name, 1)
    assert inverse == source
    prefix_line = '    delta = popov(0, m, [0]*n, "whole unshifted Popov")\n'
    if prefix_only:
        assert changed.count(prefix_line) == 1
        prefix = changed.split(prefix_line, 1)[0]+prefix_line
        restored = prefix.replace(record_tail+hook, record_tail, 1)
        restored = restored.replace(local_name, old_name, 1)
        assert restored == source.split(prefix_line, 1)[0]+prefix_line
        suffix = (
            '    assert m == n\n'
            '    prime_P = matrix(R, [row.to_list() for row in current])\n'
            '    P = prime_P\n'
            '    if R is not original_ring:\n'
            '        P = matrix(original_ring,n,n,[original_ring([\n'
            '            original_field(c) for c in f.list()]) for f in P.list()])\n'
            '    assert P.base_ring() is original_ring\n'
            '    degrees = [int(P[j,j].degree()) for j in range(n)]\n'
            '    assert all(P[j,j] and P[j,j].leading_coefficient()==1 for j in range(n))\n'
            '    assert sum(degrees)==delta\n'
            '    assert all(not P[i,j] or P[i,j].degree()<degrees[j]\n'
            '               for i in range(n) for j in range(n) if i!=j)\n'
            '    return P,None,dict(operation_counts=dict(counts),\n'
            '        full_operation_stream_sha256=stream.hexdigest(),\n'
            '        determinant_degree=int(delta), phases=phase_records,\n'
            '        exact_prime_subfield_descent=field_descent,\n'
            '        full_column_reduced_original_popov_prefix=True),prime_P\n')
        executable = prefix+suffix
    else:
        executable = changed
    stream = replay.CompleteRowOperationStream(
        R, n, source_metadata=dict(
            actual_source_function_sha256=hashlib.sha256(source.encode()).hexdigest(),
            native=bool(use_native), complete_original_prefix_only=bool(prefix_only),
            inverse_coefficient_hook_text_verified=True,
            arithmetic_prefix_unchanged=True),
        budget=budget.return_budget)
    namespace["_capture_stream"] = stream
    namespace["_hermite_remainder_rows"] = ideal_tools._hermite_remainder_rows
    exec(compile(executable, "<isolated-actual-original-row-capture>", "exec"), namespace)
    answer = namespace["isolated_captured_original_reducer"](
        M, progress=progress, label=label)
    if prefix_only:
        if len(answer) != 4:
            raise RuntimeError("The verified native prefix unexpectedly used an uncaptured fallback.")
        P, attached, receipt, prime_P = answer
    else:
        P, attached, receipt = answer
        prime_P = None
    assert attached is None
    stream.seal()
    assert receipt["operation_counts"] == stream.counts
    assert receipt["full_operation_stream_sha256"] == stream.receipt()["operation_stream_sha256"]
    assert reference.complete_pair_reset_row_hermite is REFERENCE_FUNCTION
    assert native_owner.prepare_backend is NATIVE_PREPARE_FUNCTION
    receipt = dict(receipt)
    receipt.update(
        actual_coefficient_transcript_retained=True,
        record_hook_inverse_text_verified=True,
        complete_original_arithmetic_body_retained=not prefix_only,
        prefix_stopped_only_after_all_original_column_reductions=bool(prefix_only),
        current_remainder_function_is_used=True,
        executable_source_sha256=hashlib.sha256(executable.encode()).hexdigest())
    return P, stream, receipt, prime_P


def _validate_prime_popov(P):
    R, k = P.base_ring(), P.base_ring().base_ring()
    n = int(P.nrows())
    if n <= 0 or P.ncols() != n or int(k.cardinality()) != int(k.characteristic()):
        raise ValueError("Use the entire prime-field square original Popov basis.")
    if int(k.characteristic()) not in (29, 41):
        raise ValueError("The fixed native fields are the original 29 and 41 fields.")
    degrees = []
    for j in range(n):
        if not P[j,j] or P[j,j].leading_coefficient() != 1:
            raise ValueError("Every original Popov pivot must be monic and nonzero.")
        d = int(P[j,j].degree())
        degrees.append(d)
        for i in range(n):
            if i != j and P[i,j] and P[i,j].degree() >= d:
                raise ValueError("The complete original Popov column is not reduced.")
    for i in range(n):
        lead = max(((int(P[i,j].degree()),j) for j in range(n) if P[i,j]),
                   default=(-1,-1))
        if lead != (degrees[i],i):
            raise ValueError("The full original row leading positions are not the sorted pivots.")
    return degrees


def _native_matrix(k, rows, columns):
    A = matrix(k, rows, columns, 0, sparse=False, implementation="linbox-float")
    if type(A).__name__ != "Matrix_modn_dense_float":
        raise RuntimeError("The fixed Sage 10.6 packed prime-field backend changed.")
    return A


def native_complete_cyclic_candidate(P, budget, progress=None, started=None):
    """Return full H0 or a concrete failure of the LAST-vector cyclic test.

    The quotient basis has one coordinate for EVERY standard monomial.
    No annihilator, radical, residue field, or partial quotient is substituted.
    """
    started = time.monotonic() if started is None else started
    degrees = _validate_prime_popov(P)
    R, k, n = P.base_ring(), P.base_ring().base_ring(), int(P.nrows())
    delta = sum(degrees)
    common = dict(
        complete_quotient_dimension=delta, complete_column_degrees=degrees,
        chosen_generator_original_column=n-1,
        all_nonreduced_standard_monomials_retained=True,
        original_input_or_quotient_changed_for_cyclicity=False)
    if delta == 0:
        assert P == identity_matrix(R,n)
        return identity_matrix(R,n), dict(
            common, route="zero complete quotient", cyclic=True,
            complete_krylov_rank=0, native_dense_solve_executed=False)
    positive = [j for j,d in enumerate(degrees) if d]
    q = len(positive)
    cells = 3*delta*delta+delta*q+4*delta*n+4*delta+q
    field_work = delta**3+delta*delta*(q+n)
    entry_updates = delta*delta+delta*n+delta*q
    estimates = dict(
        estimated_explicit_native_cells=cells,
        estimated_explicit_native_coefficient_bytes=4*cells,
        estimated_field_operation_work=field_work,
        estimated_krylov_entry_updates=entry_updates,
        native_element_bytes=4,
        FFPACK_internal_workspace_and_polynomial_matrices_excluded=True)
    common.update(estimates)
    if (cells > budget.max_native_cells or
            field_work > budget.max_estimated_field_operations or
            entry_updates > budget.max_krylov_entry_updates):
        return None, dict(
            common, route="native candidate declined by explicit work budget",
            cyclic=None, native_dense_solve_executed=False,
            fallback_requires_unchanged_original_input=True)
    offsets, next_offset = [], 0
    for d in degrees:
        offsets.append(next_offset)
        next_offset += d
    assert next_offset == delta
    boundary = _native_matrix(k,delta,q)
    shifts = []
    for j in positive:
        shifts.extend((offsets[j]+a,offsets[j]+a+1) for a in range(degrees[j]-1))
    for col,j in enumerate(positive):
        for i in range(n):
            tail = P[j,i]-(R.gen()**degrees[j] if i == j else R.zero())
            if tail and tail.degree() >= degrees[i]:
                raise ArithmeticError("A whole Popov boundary image left the standard monomial basis.")
            for a,coefficient in enumerate(tail.list()):
                if coefficient:
                    boundary[offsets[i]+a,col] = -coefficient

    def normal_unit_vector(j):
        out = vector(k,delta)
        if type(out).__name__ != "Vector_modn_dense":
            raise RuntimeError("The fixed native prime-field vector backend changed.")
        if degrees[j]:
            out[offsets[j]] = k.one()
        else:
            assert P[j,j] == 1
            for i in range(n):
                if i != j:
                    for a,coefficient in enumerate(P[j,i].list()):
                        if coefficient:
                            assert a < degrees[i]
                            out[offsets[i]+a] = -coefficient
        return out

    def multiply_t(x):
        tails = vector(k,[x[offsets[j]+degrees[j]-1] for j in positive])
        out = boundary*tails
        for source,target in shifts:
            out[target] += x[source]
        return out

    K = _native_matrix(k,delta,delta)
    x = normal_unit_vector(n-1)
    report_at = time.monotonic()
    for j in range(delta):
        budget.check_time(started)
        K.set_column(j,x)
        x = multiply_t(x)
        now = time.monotonic()
        if now-report_at >= 30:
            _progress(progress,"complete native quotient Krylov columns advanced",
                      columns_completed=j+1,complete_quotient_dimension=delta)
            report_at = now
    targets = _native_matrix(k,delta,n)
    targets.set_column(0,x)
    for i in range(n-1):
        targets.set_column(i+1,normal_unit_vector(i))
    augmented = copy(K.augment(targets))
    _progress(progress,"complete native quotient augmented solve starts",
              complete_quotient_dimension=delta,original_rank=n,
              native_matrix_class=type(augmented).__name__,**estimates)
    before = time.monotonic()
    augmented.echelonize(algorithm="linbox_noefd")
    budget.check_time(started)
    pivots = tuple(int(j) for j in augmented.pivots())
    rank_K = sum(j < delta for j in pivots)
    if rank_K != delta:
        return None, dict(
            common, route="last original basis vector is not cyclic",
            cyclic=False, complete_krylov_rank=rank_K,
            augmented_rank=len(pivots), native_dense_solve_executed=True,
            native_matrix_class=type(K).__name__,
            native_echelon_algorithm="linbox_noefd",
            elapsed_native_echelon_seconds=time.monotonic()-before,
            all_delta_krylov_columns_checked=True,
            fallback_requires_unchanged_original_input=True)
    assert pivots == tuple(range(delta))
    solution = augmented.matrix_from_rows_and_columns(
        range(delta),range(delta,delta+n))
    if K*solution != targets:
        raise ArithmeticError("The COMPLETE native Krylov coordinate return failed.")
    t = R.gen()
    H = copy(identity_matrix(R,n))
    for i in range(n-1):
        H[i,n-1] = -R(list(solution.column(i+1)))
    H[n-1,n-1] = t**delta-R(list(solution.column(0)))
    assert H.is_hermite()
    assert H[n-1,n-1].degree() == delta
    assert all(H[i,i] == 1 for i in range(n-1))
    return H, dict(
        common, route="complete native cyclic quotient", cyclic=True,
        complete_krylov_rank=rank_K, augmented_rank=len(pivots),
        all_delta_krylov_columns_checked=True,
        complete_K_times_solution_equals_all_targets=True,
        native_dense_solve_executed=True,
        native_matrix_class=type(K).__name__,
        native_echelon_algorithm="linbox_noefd",
        full_minimal_polynomial_sha256=ideal_tools.polynomial_digest(H[n-1,n-1]),
        complete_prime_H_candidate_sha256=ideal_tools.polynomial_matrix_digest(H),
        every_original_basis_vector_returned_as_generator_or_target=True,
        elapsed_native_echelon_seconds=time.monotonic()-before)


def complete_popov_coordinates(P,H,budget,progress=None,started=None):
    """Integral whole Popov division; no one-step companion assumption."""
    started = time.monotonic() if started is None else started
    prepare_backend()
    degrees = _validate_prime_popov(P)
    R, n = P.base_ring(), int(P.nrows())
    if H.base_ring() is not R or H.nrows() != n or H.ncols() != n:
        raise ValueError("The complete coordinate target changed its original prime ring or shape.")
    rows = [NATIVE_MODULE.NativePolynomialRow(R,row) for row in P.rows()]
    coordinates = []
    coordinate_cells, steps = 0, 0
    shifts = [0]*n
    last_report = time.monotonic()
    for source in H.rows():
        current = NATIVE_MODULE.NativePolynomialRow(R,source)
        coefficients = [R.zero() for unused in range(n)]
        live_cells = 0
        while not current.is_zero():
            budget.check_time(started)
            d,j = current.leading(0,shifts)
            if d < degrees[j]:
                raise ArithmeticError("A complete target has a nonzero Popov remainder.")
            quotient,residual = current[j].quo_rem(P[j,j])
            assert quotient
            old_length = len(coefficients[j].list())
            coefficients[j] += quotient
            live_cells += len(coefficients[j].list())-old_length
            if coordinate_cells+live_cells+n*(d+1) > budget.max_coordinate_coefficients:
                raise MemoryError("The actual complete Popov coordinate work budget is exhausted.")
            current.add_scaled(rows[j],-quotient)
            assert current[j] == residual
            assert current.leading(0,shifts) < (d,j)
            steps += 1
            if steps > budget.max_popov_coordinate_steps:
                raise TimeoutError("The complete Popov division step budget is exhausted.")
            now = time.monotonic()
            if now-last_report >= 30:
                _progress(progress,"complete original Popov coordinates advanced",
                          complete_rows_finished=len(coordinates),
                          complete_rows_total=n,actual_full_row_division_steps=steps)
                last_report = now
        coordinates.append(coefficients)
        coordinate_cells += live_cells
    C = matrix(R,coordinates)
    if replay._product(C,P) != H:
        raise ArithmeticError("The entire prime Popov coordinate return C P=H failed.")
    return C,dict(
        method="complete leading-term Popov division using full native polynomial rows",
        complete_rows_divided=n,actual_full_row_division_steps=steps,
        actual_coordinate_polynomial_cells=coordinate_cells,
        complete_C_P_equals_H=True,
        all_complete_target_remainders_are_zero=True,
        fraction_field_or_denominator_clearing_used=False,
        one_step_companion_division_assumed=False)


def _fallback_original(M,reason,budget,progress,started,label,content_receipt,attempt):
    """Same original M, same full reducer, same current remainder; no changed input."""
    prime,admission = _whole_prime_admission(M)
    H,stream,captured,unused = captured_original(
        M,prefix_only=False,use_native=prime is not None,budget=budget,
        progress=progress,label=label+": unchanged complete original fallback")
    I = identity_matrix(M.base_ring(),M.nrows())
    U,verification = replay.restore_complete_denominator_transform(
        M,H,H,I,stream,progress=progress)
    budget.check_time(started)
    return H,U,dict(
        implementation=IMPLEMENTATION,route="unchanged complete original fallback",
        fallback_reason=reason,cyclic_attempt=attempt,content=content_receipt,
        fallback_original_input_sha256=ideal_tools.polynomial_matrix_digest(M),
        fallback_did_not_use_content_quotient_or_change_generator=True,
        fallback_whole_prime_admission=admission,
        fallback_full_reducer_receipt=captured,complete_verification=verification,
        actual_content_restoration_used=False,
        original_complete_quotient_and_all_nilpotents_retained=True,
        production_binding_changed=False,performance_improvement_claimed=False,
        resource_budget=budget.receipt(),elapsed_seconds=time.monotonic()-started)


def complete_cyclic_denominator_return(M,progress=None,label="original whole denominator",
                                      budget=None):
    """Return H,U,receipt for the entire original square denominator image."""
    verify_source_pins()
    if budget is None:
        budget = CyclicBudget()
    if not isinstance(budget,CyclicBudget):
        raise TypeError("Use an explicit complete-work CyclicBudget.")
    started = time.monotonic()
    R, n = M.base_ring(), int(M.nrows())
    replay._admit_ring(R)
    if n <= 0 or M.ncols() != n:
        raise ValueError("Use the actual entire square full-rank denominator image.")
    before = copy(M)
    before.set_immutable()
    mutable = bool(M.is_mutable())
    h,M0,content = exact_scalar_content(M)
    prime_input,admission = _whole_prime_admission(M0)
    if prime_input is None:
        result = _fallback_original(
            M,"complete scalar-content quotient does not descend to the original prime field",
            budget,progress,started,label,content,dict(prime_admission=admission))
    else:
        prepare_backend()
        P0,stream,prefix,prime_P = captured_original(
            M0,prefix_only=True,use_native=True,budget=budget,
            progress=progress,label=label+": original complete Popov prefix")
        assert _map_matrix(prime_P,R) == P0
        Hprime,attempt = native_complete_cyclic_candidate(
            prime_P,budget,progress=progress,started=started)
        attempt.update(
            original_complete_popov_receipt=prefix,
            exact_whole_prime_admission=admission,
            actual_prefix_stream_sha256=stream.receipt()["operation_stream_sha256"])
        if Hprime is None:
            result = _fallback_original(
                M,attempt["route"],budget,progress,started,label,content,attempt)
        else:
            Cprime,division = complete_popov_coordinates(
                prime_P,Hprime,budget,progress=progress,started=started)
            C = _map_matrix(Cprime,R)
            H0 = _map_matrix(Hprime,R)
            P,H = h*P0,h*H0
            assert C*P == H
            U,verification = replay.restore_complete_denominator_transform(
                M,P,H,C,stream,progress=progress)
            delta0 = int(prefix["determinant_degree"])
            expected_length = n*int(h.degree())+delta0
            assert int(verification["full_quotient_length"]) == expected_length
            assert H.is_hermite()
            determinant0 = R.one()
            for j in range(n):
                determinant0 *= H0[j,j]
            determinant = h**n*determinant0
            assert ideal_tools.polynomial_digest(determinant) == verification[
                "full_monic_determinant_sha256"]
            result = H,U,dict(
                implementation=IMPLEMENTATION,route="complete cyclic quotient with exact scalar-content restoration",
                content=content,cyclic_attempt=attempt,
                complete_popov_coordinate_return=division,
                complete_verification=verification,
                full_original_length=n*int(h.degree())+delta0,
                scalar_content_length_contribution=n*int(h.degree()),
                quotient_after_exact_content_division_length=delta0,
                full_determinant_content_factor_restored=True,
                actual_content_restoration_used=True,
                common_content_multiplied_into_every_returned_P_and_H_row=True,
                original_complete_quotient_and_all_nilpotents_retained=True,
                production_binding_changed=False,performance_improvement_claimed=False,
                resource_budget=budget.receipt(),
                preparation=dict(PREPARATION),
                elapsed_seconds=time.monotonic()-started)
    H,U,receipt = result
    assert M == before and bool(M.is_mutable()) == mutable
    assert H.base_ring() is R and U.base_ring() is R
    assert reference.complete_pair_reset_row_hermite is REFERENCE_FUNCTION
    assert native_owner.prepare_backend is NATIVE_PREPARE_FUNCTION
    receipt.update(
        original_input_values_and_mutability_unchanged=True,
        original_functions_and_production_bindings_unchanged=True,
        all_original_rows_columns_and_nilpotents_preserved=True,
        isolated_module_caches_only_source_and_compiled_declarations=True,
        no_mathematical_outputs_written_or_saved_for_later_runs=True,
        existing_complete_return_transient_representation_cache_retained=True)
    return H,U,receipt
