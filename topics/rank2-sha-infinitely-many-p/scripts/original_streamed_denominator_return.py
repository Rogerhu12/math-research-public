#!/usr/bin/env sage-python
"""Complete same-MD return using streamed actual paired sources.

The original full Popov transcript and complete quotient construct H.
Every H row is divided completely and its coordinates are discarded.
Only actual rows of Y*MN are returned through that same transcript.
No universal H-to-MD matrix U or full coordinate matrix is materialized.
Only the two original direct endpoints may select this isolated method.
"""
import os
if (os.environ.get("GITHUB_ACTIONS") != "true" or
        os.environ.get("GITHUB_REPOSITORY") != "Rogerhu12/math-research-public"):
    raise SystemExit("Use only the named public research Actions.")

import ast
from copy import copy, deepcopy
import hashlib
import inspect
from pathlib import Path
import textwrap
import time
from types import FunctionType
from sage.all import matrix, vector, identity_matrix

import original_function_field_denominator_return as base
import original_cyclic_denominator_return as cyclic
import original_row_operation_right_return as replay

HERE = Path(__file__).resolve().parent
IMPLEMENTATION = "original-streamed-actual-source-denominator-return-v1"
PINNED = {
    "original_function_field_denominator_return.py":
        "0a1b6232348067cf9deb49498d97f9d32a0213dc3ef12d882d83ae35f00df5c4",
    "original_cyclic_denominator_return.py":
        "4ebbe8018347d9bf6269d6e0d83960224bb399fa5ae1998b7d91e3c1ba96fbf1",
    "original_row_operation_right_return.py":
        "ce7675e8b57fee62a2b5c7907a5cd5887759e4d72bc1e4117f04c4032e4dc225",
}
values, ideal_tools, norm_tools = base.values, base.ideal_tools, base.norm_tools
ORIGINAL_GRAPH = base.ORIGINAL_GRAPH
ORIGINAL_ZERO_POLES = base.ORIGINAL_ZERO_POLES
ORIGINAL_INTEGRAL_MULTIPLE = base.ORIGINAL_INTEGRAL_MULTIPLE
ORIGINAL_REVERSE = replay.reverse_right_return
SELECTED_GRAPH_LABELS = base.SELECTED_GRAPH_LABELS
SOURCE_DEPENDENCIES = tuple(dict.fromkeys((
    "original_streamed_denominator_return.py",
) + tuple(PINNED) + base.SOURCE_DEPENDENCIES + cyclic.SOURCE_DEPENDENCIES))
PREPARED_GRAPH = None
PREPARED_ZERO_POLES = None
PREPARED_REVERSE = None
PREPARATION = None
RETURN_AUDIT = []
OUTER_IDENTITY_AUDIT = []


class StreamBudget:
    """Actual work/storage limits, never a mathematical rank cutoff."""
    def __init__(self, cyclic_budget=None, max_returned_coefficients=32000000,
                 max_row_work_coefficients=32000000):
        if cyclic_budget is not None and not isinstance(cyclic_budget, cyclic.CyclicBudget):
            raise TypeError("Use the exact complete-work CyclicBudget or None.")
        self.cyclic = cyclic_budget or cyclic.CyclicBudget()
        self.max_returned_coefficients = int(max_returned_coefficients)
        self.max_row_work_coefficients = int(max_row_work_coefficients)
        if min(self.max_returned_coefficients,self.max_row_work_coefficients) <= 0:
            raise ValueError("Actual returned/source-row storage limits must be positive.")

    def receipt(self):
        return dict(cyclic=self.cyclic.receipt(),
            max_returned_coefficients=self.max_returned_coefficients,
            max_row_work_coefficients=self.max_row_work_coefficients,
            limits_are_actual_work_not_a_quotient_length_cutoff=True,
            final_canonical_X_may_exhaust_the_explicit_output_budget=True,
            total_process_peak_memory_bound_claimed=False)


def verify_source_pins():
    for name,expected in PINNED.items():
        assert hashlib.sha256((HERE/name).read_bytes()).hexdigest() == expected
    cyclic.verify_source_pins()
    assert replay.reverse_right_return is ORIGINAL_REVERSE
    assert values.OriginalTriangularIdealEngine.integral_fraction_multiple is ORIGINAL_INTEGRAL_MULTIPLE
    assert values.OriginalTriangularIdealEngine.zero_pole_ideals in (
        ORIGINAL_ZERO_POLES, _selected_zero_pole_ideals)
    return dict(PINNED)


def _row_cells(row):
    return sum(len(f.list()) for f in row)


def _row_matrix(row,R,n):
    row = vector(R,row)
    if len(row) != n:
        raise ValueError("Every original source coordinate is required.")
    return matrix(R,[row])


def _row_product(row,B,budget=None):
    R,n = B.base_ring(),int(B.nrows())
    row = vector(R,row)
    if len(row) != n:
        raise ValueError("A complete source row and multiplier have incompatible shapes.")
    if budget is not None:
        dr = max((int(f.degree()) for f in row),default=-1)
        db = max((int(f.degree()) for f in B.list()),default=-1)
        upper = 0 if dr < 0 or db < 0 else B.ncols()*(dr+db+1)
        if _row_cells(row)+upper > budget.max_row_work_coefficients:
            raise MemoryError("The next full single-row product exceeds its actual work budget.")
    answer = replay._product(matrix(R,[row]),B)
    assert answer.nrows() == 1 and answer.ncols() == B.ncols()
    if budget is not None and _row_cells(answer.row(0)) > budget.max_row_work_coefficients:
        raise MemoryError("The actual full source-row output exceeds its work budget.")
    return answer.row(0)


def verify_factored_identity(X,MD,Y,MN,budget=None,progress=None):
    """Exactly X*MD=Y*MN, evaluated on ALL rows without either full product."""
    R,n = MD.base_ring(),int(MD.nrows())
    if n <= 0 or MD.ncols() != n:
        raise ValueError("The actual denominator must retain its full square shape.")
    for A in (X,Y,MN):
        if A.base_ring() is not R or A.nrows() != n or A.ncols() != n:
            raise ValueError("The complete graph changed its original ring or shape.")
    last_report = time.monotonic()
    for i in range(n):
        if _row_product(X.row(i),MD,budget) != _row_product(Y.row(i),MN,budget):
            raise ArithmeticError("A complete original paired-source row failed X_i MD=(Y MN)_i.")
        if progress is not None and time.monotonic()-last_report >= 30:
            progress("all-row factored original graph identity advanced",
                     complete_rows_checked=i+1,complete_rows_total=n)
            last_report = time.monotonic()
    return True


class VerifiedTape:
    """Same-invocation immutable operation tuple; full checks at both ends."""
    def __init__(self,stream):
        if not isinstance(stream,replay.CompleteRowOperationStream) or not stream.sealed:
            raise ValueError("The actual complete coefficient transcript must be sealed.")
        stream.verify()
        self.stream,self.operations = stream,stream.operations
        self.record = deepcopy(stream.receipt())
        self.finished = False

    def check(self,stream):
        if (self.finished or stream is not self.stream or not stream.sealed or
                stream.operations is not self.operations):
            raise ValueError("The same-invocation complete operation tuple changed.")

    def finish(self):
        self.check(self.stream)
        self.stream.verify()
        assert self.stream.receipt() == self.record
        self.finished = True


def _checked_tape(stream,tape):
    if not isinstance(tape,VerifiedTape):
        raise ValueError("Use the same verified full operation tape.")
    tape.check(stream)


def _tape_receipt(stream,tape):
    _checked_tape(stream,tape)
    return deepcopy(tape.record)


def _inverse_source(source,changes):
    changed = source
    for old,new in changes:
        if changed.count(old) != 1:
            raise AssertionError("A pinned exact source replacement is no longer unique: "+old)
        changed = changed.replace(old,new,1)
    inverse = changed
    for old,new in reversed(changes):
        if inverse.count(new) != 1:
            raise AssertionError("An exact inverse source replacement is ambiguous.")
        inverse = inverse.replace(new,old,1)
    assert inverse == source
    return changed


def _prepare_rectangular_reverse():
    source = textwrap.dedent(inspect.getsource(ORIGINAL_REVERSE))
    changes = [
        ("def reverse_right_return(C, stream, progress=None):",
         "def rectangular_reverse_right_return(C, stream, progress=None, verified_tape=None):"),
        ("    stream.verify()\n","    _checked_tape(stream, verified_tape)\n"),
        ("    R, n = stream.R, stream.rank\n",
         "    R, n = stream.R, stream.rank\n    source_rows = int(C.nrows())\n"),
        ("if C.base_ring() is not R or C.nrows() != n or C.ncols() != n:",
         "if C.base_ring() is not R or source_rows <= 0 or C.ncols() != n:"),
        ("scratch_upper = n*sum(max(0, degree+1) for degree in output_degrees)",
         "scratch_upper = source_rows*sum(max(0, degree+1) for degree in output_degrees)"),
        ("scalar_updates += weight*n","scalar_updates += weight*source_rows"),
        ("assert U.base_ring() is R and U.nrows() == U.ncols() == n",
         "assert U.base_ring() is R and U.nrows() == source_rows and U.ncols() == n"),
        ('method="reverse chronological exact right multiplication by all original row operations",',
         'method="rectangular actual sources through all original reverse-right operations",'),
        ("rank=n, full_input_coordinate_sha256=",
         "rank=n, actual_source_rows=source_rows, universal_transform_materialized=False, full_input_coordinate_sha256="),
        ("full_returned_transform_sha256=","full_returned_actual_source_sha256="),
        ("complete_transcript=stream.receipt(), resource_budget=budget.receipt(),",
         "complete_transcript=_tape_receipt(stream, verified_tape), resource_budget=budget.receipt(),"),
    ]
    changed = _inverse_source(source,changes)
    ast.parse(changed)
    namespace = dict(vars(replay))
    namespace.update(_checked_tape=_checked_tape,_tape_receipt=_tape_receipt)
    exec(compile(changed,"<same-original-rectangular-reverse-right>","exec"),namespace)
    return namespace["rectangular_reverse_right_return"],dict(
        original_source_sha256=hashlib.sha256(source.encode()).hexdigest(),
        generated_source_sha256=hashlib.sha256(changed.encode()).hexdigest(),
        inverse_all_exact_replacements_verified=True,
        exact_replacement_count=len(changes),
        all_original_columns_and_simultaneous_Bezout_directions_retained=True,
        transcript_verified_whole_before_and_after_all_actual_source_rows=True,
        only_actual_source_row_count_changes_column_work_counts=True)


def verify_forward_transcript(M,P,stream,budget,progress=None):
    """Replay every actual original row operation on M; never form E."""
    R,n = M.base_ring(),int(M.nrows())
    if P.base_ring() is not R or P.nrows() != n or P.ncols() != n:
        raise ValueError("The complete recorded intermediate changed its original shape.")
    stream.verify()
    if stream.R is not R or stream.rank != n:
        raise ValueError("The complete operation stream belongs to another original module.")
    prime,admission = cyclic._whole_prime_admission(M)
    use_native = prime is not None
    if use_native:
        cyclic.prepare_backend()
        PR,pk = prime.base_ring(),prime.base_ring().base_ring()
        rows = [cyclic.NATIVE_MODULE.NativePolynomialRow(PR,row) for row in prime.rows()]
        def coefficient(f):
            answer = PR([pk(c) for c in f.list()])
            assert R([R.base_ring()(c) for c in answer.list()]) == f
            return answer
        def row_degree(row):
            return int(row.degree(0))
    else:
        rows = [copy(M.row(i)) for i in range(n)]
        coefficient = R
        def row_degree(row):
            return max((int(f.degree()) for f in row),default=-1)
    degrees = [row_degree(row) for row in rows]
    live = sum(n*max(0,d+1) for d in degrees)
    peak = live
    max_work = budget.cyclic.return_budget.max_work_coefficients
    if live > max_work:
        raise MemoryError("The full forward transcript input exceeds its explicit coefficient envelope.")
    started = time.monotonic()
    last = started
    for step,(kind,inds,coeffs) in enumerate(stream.operations,1):
        budget.cyclic.check_time(started)
        if kind == "swap":
            i,j = inds
            rows[i],rows[j] = rows[j],rows[i]
            degrees[i],degrees[j] = degrees[j],degrees[i]
        else:
            c = tuple(coefficient(f) for f in coeffs)
            if kind == "add":
                i,j = inds
                affected = (i,)
                upper = (max(degrees[i],int(c[0].degree())+degrees[j])
                         if degrees[j] >= 0 else degrees[i],)
            elif kind == "scale":
                i = inds[0]
                affected,upper = (i,),(degrees[i],)
            else:
                i,j = inds
                def td(f,d):
                    return -1 if not f or d < 0 else int(f.degree())+d
                affected = (i,j)
                upper = (max(td(c[0],degrees[i]),td(c[1],degrees[j])),
                         max(td(c[2],degrees[i]),td(c[3],degrees[j])))
            scratch = n*sum(max(0,d+1) for d in upper)
            if live+scratch > max_work:
                raise MemoryError("The actual forward operation exceeds its explicit coefficient envelope.")
            peak = max(peak,live+scratch)
            old_cells = sum(n*max(0,degrees[i]+1) for i in affected)
            if kind == "add":
                if use_native:
                    rows[i].add_scaled(rows[j],c[0])
                else:
                    rows[i] = rows[i]+c[0]*rows[j]
            elif kind == "scale":
                if use_native:
                    rows[i].scale(c[0])
                else:
                    rows[i] = c[0]*rows[i]
            else:
                old_i,old_j = rows[i],rows[j]
                if use_native:
                    rows[i] = cyclic.NATIVE_MODULE.linear_combination(c[0],old_i,c[1],old_j)
                    rows[j] = cyclic.NATIVE_MODULE.linear_combination(c[2],old_i,c[3],old_j)
                else:
                    rows[i],rows[j] = c[0]*old_i+c[1]*old_j,c[2]*old_i+c[3]*old_j
            for i in affected:
                degrees[i] = row_degree(rows[i])
            live += sum(n*max(0,degrees[i]+1) for i in affected)-old_cells
        if progress is not None and time.monotonic()-last >= 30:
            progress("whole original forward coefficient transcript advanced",
                operations_completed=step,operations_total=len(stream.operations),
                explicit_polynomial_coefficient_envelope=live)
            last = time.monotonic()
    for i,row in enumerate(rows):
        actual = row.to_list() if use_native else list(row)
        restored = vector(R,[R([R.base_ring()(c) for c in f.list()]) for f in actual])
        if restored != P.row(i):
            raise ArithmeticError("The actual full coefficient transcript does not return P=E*M.")
    stream.verify()
    return dict(
        method="all actual original row operations replayed forward on every original coordinate",
        original_input_sha256=ideal_tools.polynomial_matrix_digest(M),
        complete_recorded_basis_sha256=ideal_tools.polynomial_matrix_digest(P),
        complete_transcript=stream.receipt(),whole_prime_admission=admission,
        actual_operation_count=len(stream.operations),complete_P_equals_E_M=True,
        E_or_any_universal_transform_materialized=False,
        explicit_peak_coefficient_envelope=peak,
        elapsed_seconds=time.monotonic()-started)


class StreamedDenominatorSession:
    """Same actual MD/P/H/tape, with only source rows retained for reverse return."""
    def __init__(self,budget=None):
        if budget is not None and not isinstance(budget,StreamBudget):
            raise TypeError("Use an actual StreamBudget or None.")
        self.budget = budget or StreamBudget()
        self.input_object = self.input_snapshot = None
        self.M0 = self.P0 = self.P = self.prime_P = self.H = self.H0 = None
        self.h = self.stream = self.tape = self.native_rows = None
        self.image_receipt = self.division_receipt = None
        self.image_calls = self.division_calls = 0
        self.coordinate_steps = self.coordinate_cells_max = 0
        self.coordinate_row_count = 0

    def _prime_coordinate_component(self,source):
        PR,n = self.prime_P.base_ring(),int(self.prime_P.nrows())
        source = vector(PR,source)
        if source.is_zero():
            return vector(PR,n)
        current = cyclic.NATIVE_MODULE.NativePolynomialRow(PR,source)
        coefficients = [PR.zero() for unused in range(n)]
        degrees = [int(self.prime_P[j,j].degree()) for j in range(n)]
        live = 0
        shifts = [0]*n
        while not current.is_zero():
            self.budget.cyclic.check_time(self.started)
            d,j = current.leading(0,shifts)
            if d < degrees[j]:
                raise ArithmeticError("A complete actual source has a nonzero Popov remainder.")
            quotient,residual = current[j].quo_rem(self.prime_P[j,j])
            assert quotient
            old = len(coefficients[j].list())
            coefficients[j] += quotient
            live += len(coefficients[j].list())-old
            work = live+n*(d+1)
            if work > self.budget.cyclic.max_coordinate_coefficients:
                raise MemoryError("The actual single-row Popov coordinate budget is exhausted.")
            self.coordinate_cells_max = max(self.coordinate_cells_max,work)
            current.add_scaled(self.native_rows[j],-quotient)
            assert current[j] == residual and current.leading(0,shifts) < (d,j)
            self.coordinate_steps += 1
            if self.coordinate_steps > self.budget.cyclic.max_popov_coordinate_steps:
                raise TimeoutError("The complete actual-source Popov work budget is exhausted.")
        return vector(PR,coefficients)

    def coordinate_row(self,source):
        """Return the full original-field coordinates in P0, then check them."""
        R,n = self.P0.base_ring(),int(self.P0.nrows())
        source = vector(R,source)
        if len(source) != n:
            raise ValueError("The complete source row lost original coordinates.")
        if self.prime_P is None:
            C = norm_tools._whole_hermite_coordinates(
                self.P0,matrix(R,[source])).row(0)
        else:
            PR,pk = self.prime_P.base_ring(),self.prime_P.base_ring().base_ring()
            k = R.base_ring()
            degree = int(k.degree())
            components = [[] for unused in range(degree)]
            for f in source:
                coefficient_parts = [[] for unused in range(degree)]
                for z in f.list():
                    parts = [pk(z)] if degree == 1 else list(z.polynomial())
                    if len(parts) > degree:
                        raise ArithmeticError("The actual finite-field basis changed.")
                    parts += [pk.zero()]*(degree-len(parts))
                    assert k(z) == sum((k(parts[j])*k.gen()**j for j in range(degree)),k.zero())
                    for j in range(degree):
                        coefficient_parts[j].append(pk(parts[j]))
                for j in range(degree):
                    components[j].append(PR(coefficient_parts[j]))
            coordinate_parts = [self._prime_coordinate_component(row) for row in components]
            C = vector(R,[
                sum((R([k(c) for c in coordinate_parts[j][i].list()])*k.gen()**j
                     for j in range(degree)),R.zero()) for i in range(n)])
        if _row_product(C,self.P0,self.budget) != source:
            raise ArithmeticError("The full original-field coordinate return C_row*P0=source failed.")
        self.coordinate_row_count += 1
        return C

    def certify_image(self,progress=None):
        """All H rows in P plus all MD rows in H; coordinates never accumulate."""
        R,n = self.P0.base_ring(),int(self.P0.nrows())
        if not self.H.is_hermite() or self.H.base_ring() is not R:
            raise ValueError("The candidate is not the complete original Hermite basis.")
        determinant = R.one()
        row_returns = []
        last_report = time.monotonic()
        for i in range(n):
            if not self.H[i,i] or self.H[i,i].leading_coefficient() != 1:
                raise ValueError("Every complete Hermite pivot must be monic and nonzero.")
            determinant *= self.H[i,i]
            source = vector(R,[f.quo_rem(self.h)[0] for f in self.H.row(i)])
            if any(f.quo_rem(self.h)[1] for f in self.H.row(i)):
                raise ArithmeticError("A full Hermite row omitted an original content factor.")
            C = self.coordinate_row(source)
            if _row_product(C,self.P,self.budget) != self.H.row(i):
                raise ArithmeticError("A complete H-row return against the undivided P failed.")
            row_returns.append(ideal_tools.element_digest(C))
            del C
            if progress is not None and time.monotonic()-last_report >= 30:
                progress("complete H rows streamed through the same original P",
                         complete_rows_checked=i+1,complete_rows_total=n,
                         actual_full_coordinate_steps=self.coordinate_steps)
                last_report = time.monotonic()
        if not ideal_tools._hermite_remainder_rows(self.input_snapshot,self.H).is_zero():
            raise ArithmeticError("An original MD row has nonzero remainder against complete H.")
        expected = self.expected_length
        if int(determinant.degree()) != expected:
            raise ArithmeticError("The original complete nonreduced determinant length changed.")
        return determinant,dict(
            every_H_row_divided_completely_in_original_P=True,
            complete_H_row_coordinate_sha256=row_returns,
            each_H_coordinate_row_discarded_before_the_next=True,
            every_original_MD_row_has_zero_full_Hermite_remainder=True,
            current_dynamic_original_remainder_used=True,
            complete_monic_determinant_sha256=ideal_tools.polynomial_digest(determinant),
            full_quotient_length=expected,
            both_polynomial_row_module_inclusions_verified=True,
            full_coordinate_matrix_materialized=False,
            universal_full_transform_materialized=False)

    def image(self,rows,attached=None,progress=None,label="complete original denominator image"):
        if attached is not None:
            raise ValueError("This entry admits only the entire unattached MD image.")
        if self.image_calls or self.input_object is not None:
            raise ValueError("A streamed denominator session is single use.")
        verify_source_pins()
        R,k,n = base._admit_square_polynomial_matrix(rows)
        report = progress or base._report
        self.started = time.monotonic()
        before = copy(rows)
        before.set_immutable()
        mutable = bool(rows.is_mutable())
        h,M0,content = cyclic.exact_scalar_content(rows)
        prime,admission = cyclic._whole_prime_admission(M0)
        attempt = dict(prime_admission=admission)
        fallback = prime is None
        if not fallback:
            P0,stream,prefix,prime_P = cyclic.captured_original(
                M0,prefix_only=True,use_native=True,budget=self.budget.cyclic,
                progress=report,label=label+": complete original Popov prefix")
            Hprime,attempt0 = cyclic.native_complete_cyclic_candidate(
                prime_P,self.budget.cyclic,progress=report,started=self.started)
            attempt.update(attempt0,original_complete_popov_receipt=prefix)
            fallback = Hprime is None
            if not fallback:
                H0 = cyclic._map_matrix(Hprime,R)
                H = h*H0
                expected = n*int(h.degree())+int(prefix["determinant_degree"])
                full = None
                del Hprime
            else:
                del P0,stream,prime_P
        if fallback:
            # Exactly the old complete algorithm on the ORIGINAL undivided MD.
            original_prime,old_admission = cyclic._whole_prime_admission(rows)
            H0,stream,full,unused = cyclic.captured_original(
                rows,prefix_only=False,use_native=original_prime is not None,
                budget=self.budget.cyclic,progress=report,
                label=label+": unchanged full original fallback")
            M0,P0,H,h,prime_P = rows,H0,H0,R.one(),None
            expected = int(full["determinant_degree"])
            attempt["fallback_whole_prime_admission"] = old_admission
        forward = verify_forward_transcript(
            M0,P0,stream,self.budget,progress=report)
        assert rows == before and bool(rows.is_mutable()) == mutable
        self.input_object,self.input_snapshot = rows,before
        self.M0,self.P0,self.prime_P,self.H0,self.H = M0,P0,prime_P,H0,H
        self.P = h*P0
        assert rows == h*M0
        self.h,self.stream,self.expected_length = h,stream,expected
        self.tape = VerifiedTape(stream)
        for A in (self.P0,self.P,self.H0,self.H):
            if A is not rows:
                A.set_immutable()
        if prime_P is not None:
            prime_P.set_immutable()
            self.native_rows = [
                cyclic.NATIVE_MODULE.NativePolynomialRow(prime_P.base_ring(),row)
                for row in prime_P.rows()]
        determinant,certificate = self.certify_image(progress=report)
        phases = [] if full is None else [
            deepcopy(phase) for phase in full["phases"]
            if phase["phase"] == "whole unshifted tail reset after certified gcd pair"]
        self.image_receipt = dict(
            method="whole cyclic/content image or unchanged full fallback, streamed H-row certificates",
            implementation=IMPLEMENTATION,label=label,original_shape=[n,n],full_rank=n,
            route="unchanged complete original fallback" if fallback else "complete cyclic quotient with exact scalar-content restoration",
            original_rows_sha256=ideal_tools.polynomial_matrix_digest(before),
            complete_hermite_basis_sha256=ideal_tools.polynomial_matrix_digest(H),
            complete_recorded_P_sha256=ideal_tools.polynomial_matrix_digest(self.P),
            full_monic_determinant_sha256=ideal_tools.polynomial_digest(determinant),
            determinant_degree=expected,full_quotient_length=expected,
            content=content,actual_content_restoration_used=not fallback,
            fallback_uses_exact_original_undivided_MD=fallback,
            actual_scalar_content_restoration_degree=0 if fallback else int(h.degree()),
            full_transcript_forward_return=forward,cyclic_attempt=attempt,
            exact_undivided_content_identity_MD_equals_h_M0=True,
            scalar_commutes_with_every_recorded_polynomial_operation=True,
            complete_undivided_P_equals_E_MD=True,
            fallback_full_reducer_receipt=full,complete_image_certificate=certificate,
            attached_block=False,complete_cyclic_route_succeeded=not fallback,
            old_complete_reducer_executed_for_this_image=fallback,
            old_tail_reset_algorithm_executed_for_this_image=bool(phases),
            actual_old_tail_reset_phase_count=len(phases),
            actual_old_tail_reset_phase_records=phases,
            old_transposed_attached_hermite_reduction_executed=False,
            official_function_field_hnf_executed_for_this_image=False,
            universal_full_transform_materialized=False,
            whole_coordinate_matrix_materialized=False,
            actual_H_coordinate_row_count=n,
            all_original_rows_columns_and_nilpotents_retained=True,
            original_input_and_mutability_unchanged=True,
            resource_budget=self.budget.receipt(),
            image_elapsed_seconds=time.monotonic()-self.started)
        self.image_calls = 1
        report("complete streamed original denominator image certified",
            label=label,full_rank=n,full_quotient_length=expected,
            route=self.image_receipt["route"],universal_transform_materialized=False)
        return H,None,deepcopy(self.image_receipt)

    def divide_factored(self,MD,Y,MN,progress=None,label="all actual paired numerators"):
        if (self.image_calls != 1 or self.division_calls or self.input_object is None or
                MD is not self.input_object or MD != self.input_snapshot):
            raise ValueError("Use exactly this unchanged same-call MD once.")
        R,n = MD.base_ring(),int(MD.nrows())
        if (ideal_tools.polynomial_matrix_digest(self.H) != self.image_receipt["complete_hermite_basis_sha256"] or
                ideal_tools.polynomial_matrix_digest(self.P) != self.image_receipt["complete_recorded_P_sha256"]):
            raise ValueError("The same-call complete P/H objects were replaced or changed.")
        for A in (Y,MN):
            if A.base_ring() is not R or A.nrows() != n or A.ncols() != n:
                raise ValueError("Both actual full source factors must keep the original ring and shape.")
        if not Y.is_hermite() or any(not Y[j,j] for j in range(n)):
            raise ValueError("Keep the entire original canonical denominator preimage Y.")
        prepare_source_bindings()
        report = progress or base._report
        self.tape.check(self.stream)
        per_source_updates = sum(
            dict(swap=0,add=1,scale=1,bezout=4)[kind]
            for kind,unused_indices,unused_coefficients in self.tape.operations)
        planned_reverse_updates = n*per_source_updates
        if planned_reverse_updates > self.budget.cyclic.return_budget.max_scalar_column_updates:
            raise MemoryError("All actual source returns exceed the complete-graph reverse-work budget.")
        actual_reverse_updates = 0
        X = matrix(R,n,n,0)
        row_records = []
        accumulated = 0
        last_report = time.monotonic()
        for i in range(n):
            self.budget.cyclic.check_time(self.started)
            W = _row_product(Y.row(i),MN,self.budget)
            reduced = []
            for f in W:
                q,r = f.quo_rem(self.h)
                if r:
                    raise ArithmeticError("An actual paired source omits an original content factor.")
                reduced.append(q)
            C = self.coordinate_row(reduced)
            if _row_product(C,self.P,self.budget) != W:
                raise ArithmeticError("The full actual source return C_W P=W failed.")
            Xrow_matrix,reverse = PREPARED_REVERSE(
                matrix(R,[C]),self.stream,progress=report,verified_tape=self.tape)
            actual_reverse_updates += reverse["actual_scalar_column_updates"]
            assert reverse["actual_scalar_column_updates"] == per_source_updates
            assert actual_reverse_updates <= planned_reverse_updates
            Xrow = Xrow_matrix.row(0)
            cells = _row_cells(Xrow)
            if accumulated+cells > self.budget.max_returned_coefficients:
                raise MemoryError("The actual final canonical X exceeds its explicit output budget.")
            if _row_product(Xrow,MD,self.budget) != W:
                raise ArithmeticError("The full actual source return X_i MD=(Y MN)_i failed.")
            accumulated += cells
            X.set_row(i,Xrow)
            row_records.append(dict(
                original_source_row=i,
                complete_W_row_sha256=ideal_tools.element_digest(W),
                complete_C_W_row_sha256=ideal_tools.element_digest(C),
                complete_X_row_sha256=ideal_tools.element_digest(Xrow),
                complete_C_W_P_equals_W=True,complete_X_MD_equals_W=True,
                reverse_right_return=reverse))
            del C,W,Xrow_matrix
            if time.monotonic()-last_report >= 30:
                report("complete actual paired source rows returned",
                       complete_rows_finished=i+1,complete_rows_total=n,
                       actual_returned_X_polynomial_cells=accumulated,
                       actual_complete_coordinate_steps=self.coordinate_steps)
                last_report = time.monotonic()
        assert X.nrows() == X.ncols() == n
        assert actual_reverse_updates == planned_reverse_updates
        assert MD == self.input_snapshot
        self.tape.finish()
        self.division_receipt = dict(
            method="same complete P=E*MD, factored actual W_i=(Y*MN)_i, C_i*P=W_i, X_i=C_i*E",
            implementation=IMPLEMENTATION,reduction=None,
            same_complete_denominator_image_receipt_sha256=ideal_tools.digest(self.image_receipt),
            original_denominator_sha256=ideal_tools.polynomial_matrix_digest(MD),
            complete_recorded_P_sha256=self.image_receipt["complete_recorded_P_sha256"],
            actual_source_Y_sha256=ideal_tools.polynomial_matrix_digest(Y),
            actual_source_MN_sha256=ideal_tools.polynomial_matrix_digest(MN),
            complete_returned_X_sha256=ideal_tools.polynomial_matrix_digest(X),
            original_source_row_count=n,all_actual_source_row_returns=row_records,
            actual_returned_X_polynomial_cells=accumulated,
            maximum_actual_prime_component_coordinate_work_cells=(
                self.coordinate_cells_max if self.prime_P is not None else None),
            coordinate_work_measurement_scope=(
                "one native prime component: current residual plus its coordinates"
                if self.prime_P is not None else "native prime component counter not used on full fallback"),
            combined_quadratic_coordinate_or_total_process_peak_claimed=False,
            planned_complete_graph_reverse_scalar_updates=planned_reverse_updates,
            actual_complete_graph_reverse_scalar_updates=actual_reverse_updates,
            complete_graph_reverse_scalar_update_budget=(
                self.budget.cyclic.return_budget.max_scalar_column_updates),
            actual_complete_coordinate_steps=self.coordinate_steps,
            full_Y_times_MN_materialized=False,
            universal_full_transform_materialized=False,
            whole_coordinate_matrix_materialized=False,
            every_source_row_returned_against_original_denominator=True,
            full_actual_coefficient_transcript_verified_at_both_ends=True,
            same_actual_MD_P_H_and_transcript_used_for_every_source=True,
            unique_X_from_original_nonsingular_MD=True,
            old_transposed_attached_hermite_reduction_executed=False,
            cross_call_solved_image_or_transform_reused=False,
            original_complete_nonreduced_graph_retained=True)
        self.division_calls = 1
        return X,deepcopy(self.division_receipt)

    def release(self):
        self.input_object = self.input_snapshot = None
        self.M0 = self.P0 = self.P = self.prime_P = self.H = self.H0 = None
        self.h = self.stream = self.tape = self.native_rows = None


def prepare_source_bindings():
    global PREPARED_GRAPH,PREPARED_ZERO_POLES,PREPARED_REVERSE,PREPARATION
    verify_source_pins()
    if PREPARATION is not None:
        return deepcopy(PREPARATION)
    backend = cyclic.prepare_backend()
    reverse,reverse_receipt = _prepare_rectangular_reverse()
    source = textwrap.dedent(inspect.getsource(ORIGINAL_GRAPH))
    changes = [
        ("HD, attached, denominator_receipt = complete_row_hermite(",
         "HD, attached, denominator_receipt = _streamed_image("),
        ("X, paired_receipt = full_polynomial_left_division(\n        MD, Y*MN,",
         "X, paired_receipt = _streamed_factored_division(\n        MD, Y, MN,"),
        ("    assert X*MD == Y*MN\n",
         "    assert _streamed_full_identity(X, MD, Y, MN)\n"),
    ]
    changed = _inverse_source(source,changes)
    ast.parse(changed)
    namespace = dict(ORIGINAL_GRAPH.__globals__)
    exec(compile(changed,"<original-complete-graph-factored-return>","exec"),namespace)
    graph = namespace["complete_paired_fraction_graph"]
    outer = textwrap.dedent(inspect.getsource(ORIGINAL_ZERO_POLES))
    outer_changes = [
        ("    assert X*MD == Y*MN\n",
         "    assert _streamed_outer_identity(X, MD, Y, MN, label, self)\n"),
    ]
    outer_changed = _inverse_source(outer,outer_changes)
    ast.parse(outer_changed)
    namespace = dict(ORIGINAL_ZERO_POLES.__globals__)
    exec(compile(outer_changed,"<original-zero-poles-complete-rowwise-identity>","exec"),namespace)
    outer_function = namespace["zero_pole_ideals"]
    PREPARED_REVERSE,PREPARED_GRAPH,PREPARED_ZERO_POLES = reverse,graph,outer_function
    PREPARATION = dict(
        implementation=IMPLEMENTATION,pinned_source_sha256=dict(PINNED),
        original_complete_cyclic_backend_preparation=backend,
        rectangular_reverse_source=reverse_receipt,
        original_graph_function_sha256=hashlib.sha256(source.encode()).hexdigest(),
        prepared_graph_function_sha256=hashlib.sha256(changed.encode()).hexdigest(),
        original_zero_poles_function_sha256=hashlib.sha256(outer.encode()).hexdigest(),
        prepared_zero_poles_function_sha256=hashlib.sha256(outer_changed.encode()).hexdigest(),
        graph_exact_replacement_count=3,outer_exact_replacement_count=1,
        inverse_all_graph_and_outer_replacements_recover_original_sources=True,
        full_preimage_and_both_original_ideal_from_rows_calls_unchanged=True,
        both_full_graph_identities_checked_on_every_original_row=True,
        original_general_functions_and_old_F_y_source_unchanged=True,
        cached_objects_are_only_source_and_compiled_declarations=True,
        mathematical_instance_executed_by_preparation=False)
    return deepcopy(PREPARATION)


def paired_graph_with_streamed_sources(MN,MD,progress=None,
        label="whole original paired fraction graph",budget=None):
    prepare_source_bindings()
    session = StreamedDenominatorSession(budget)
    namespace = dict(ORIGINAL_GRAPH.__globals__)
    original_preimage = namespace["complete_triangular_preimage"]
    original_division = namespace["full_polynomial_left_division"]
    original_hermite = namespace["complete_row_hermite"]
    namespace.update(_streamed_image=session.image,
        _streamed_factored_division=session.divide_factored,
        _streamed_full_identity=lambda X,M,Y,N:verify_factored_identity(
            X,M,Y,N,session.budget,progress=progress or base._report))
    runner = FunctionType(PREPARED_GRAPH.__code__,namespace,PREPARED_GRAPH.__name__,
                          PREPARED_GRAPH.__defaults__,PREPARED_GRAPH.__closure__)
    try:
        X,Y,receipt = runner(MN,MD,progress=progress,label=label)
        assert session.image_calls == session.division_calls == 1
        assert receipt["full_paired_numerator_division"] == session.division_receipt
        assert ORIGINAL_GRAPH.__globals__["complete_triangular_preimage"] is original_preimage
        assert ORIGINAL_GRAPH.__globals__["full_polynomial_left_division"] is original_division
        assert ORIGINAL_GRAPH.__globals__["complete_row_hermite"] is original_hermite
        RETURN_AUDIT.append(dict(
            label=label,original_shape=list(session.image_receipt["original_shape"]),
            original_denominator_sha256=receipt["denominator_operator_sha256"],
            original_numerator_sha256=receipt["numerator_operator_sha256"],
            complete_denominator_image_receipt_sha256=ideal_tools.digest(session.image_receipt),
            same_denominator_paired_division_receipt_sha256=ideal_tools.digest(session.division_receipt),
            paired_numerator_projection_sha256=receipt["paired_numerator_projection_sha256"],
            paired_denominator_projection_sha256=receipt["paired_denominator_projection_sha256"],
            actual_route=session.image_receipt["route"],
            old_complete_denominator_reducer_executed=session.image_receipt[
                "old_complete_reducer_executed_for_this_image"],
            actual_old_tail_reset_phase_count=session.image_receipt["actual_old_tail_reset_phase_count"],
            same_MD_P_H_actual_transcript_and_every_C_W_X_return=True,
            full_Y_MN_or_universal_U_materialized=False,
            full_matrix_or_mathematical_result_cached_in_audit=False))
        return X,Y,receipt
    finally:
        session.release()


def _selected_endpoint_graph(MN,MD,progress=None,label="whole original paired fraction graph"):
    if label in SELECTED_GRAPH_LABELS:
        return paired_graph_with_streamed_sources(MN,MD,progress=progress,label=label)
    return ORIGINAL_GRAPH(MN,MD,progress=progress,label=label)


def _outer_identity(X,MD,Y,MN,label,engine):
    verify_factored_identity(X,MD,Y,MN,progress=engine.progress)
    OUTER_IDENTITY_AUDIT.append(dict(
        label=label,all_original_rows=int(MD.nrows()),
        actual_engine_object_id=id(engine),actual_infinity_chart=bool(engine.infinity_chart),
        original_denominator_sha256=ideal_tools.polynomial_matrix_digest(MD),
        original_numerator_sha256=ideal_tools.polynomial_matrix_digest(MN),
        paired_X_sha256=ideal_tools.polynomial_matrix_digest(X),
        canonical_Y_sha256=ideal_tools.polynomial_matrix_digest(Y),
        complete_identity_rechecked_after_both_original_ideals=True,
        whole_product_materialized=False))
    return True


def _selected_zero_pole_ideals(self,numerator,denominator,label="original function"):
    if label+": complete zero/pole graph" not in SELECTED_GRAPH_LABELS:
        return ORIGINAL_ZERO_POLES(self,numerator,denominator,label=label)
    prepare_source_bindings()
    namespace = dict(ORIGINAL_ZERO_POLES.__globals__)
    namespace.update(complete_paired_fraction_graph=_selected_endpoint_graph,
                     _streamed_outer_identity=_outer_identity)
    runner = FunctionType(PREPARED_ZERO_POLES.__code__,namespace,
        PREPARED_ZERO_POLES.__name__,PREPARED_ZERO_POLES.__defaults__,
        PREPARED_ZERO_POLES.__closure__)
    return runner(self,numerator,denominator,label=label)


def bind_original_streamed_denominator_return():
    preparation = prepare_source_bindings()
    old_graph = values.complete_paired_fraction_graph
    old_outer = values.OriginalTriangularIdealEngine.zero_pole_ideals
    if old_graph not in (ORIGINAL_GRAPH,base._selected_endpoint_graph,_selected_endpoint_graph):
        raise AssertionError("Refuse an unrecognized complete graph binding.")
    if old_outer not in (ORIGINAL_ZERO_POLES,_selected_zero_pole_ideals):
        raise AssertionError("Refuse an unrecognized original zero/pole method.")
    already = old_graph is _selected_endpoint_graph and old_outer is _selected_zero_pole_ideals
    values.complete_paired_fraction_graph = _selected_endpoint_graph
    values.OriginalTriangularIdealEngine.zero_pole_ideals = _selected_zero_pole_ideals
    assert values.OriginalTriangularIdealEngine.integral_fraction_multiple is ORIGINAL_INTEGRAL_MULTIPLE
    return dict(kind="original-selected-endpoint-streamed-actual-source-binding",
        implementation=IMPLEMENTATION,already_bound=already,
        graph_reference_replaced=old_graph is not _selected_endpoint_graph,
        selected_outer_identity_method_replaced=old_outer is not _selected_zero_pole_ideals,
        selected_complete_graph_labels=list(SELECTED_GRAPH_LABELS),
        all_other_graphs_and_zero_pole_labels_use_exact_original_functions=True,
        actual_old_F_y_attached_Hermite_route_retained=True,
        original_complete_preimage_ideal_and_general_division_apis_unchanged=True,
        scalar_primary_and_all_unselected_engine_method_bodies_unchanged=True,
        preparation=preparation)


def denominator_return_audit():
    return deepcopy(RETURN_AUDIT)


def outer_identity_audit():
    return deepcopy(OUTER_IDENTITY_AUDIT)
