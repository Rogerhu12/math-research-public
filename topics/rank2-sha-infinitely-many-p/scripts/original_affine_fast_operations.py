"""Exact native-Fp contraction of the ORIGINAL 306-dimensional ring table.

This is an operation adapter for an already authenticated complete context
from original_affine_multiplication.py.  It neither computes a new function
field nor changes any original structure constant.  In particular it uses
no Laurent coefficients and loses no precision.

For a fixed output row j and input weight a, all structure constants for
the ACTUALLY NONZERO input coordinates are a single selected prime-field
matrix S_(j,a).  The prime-field coefficient matrices of x are multiplied
by S_(j,a) in native finite-field arithmetic.  Strictly zero input rows
are omitted before any native table copy; all original recipe columns stay.
Every resulting recipe coefficient is shifted by its EXACT table exponent
(or the proved weighted reverse exponent in the infinity chart).  Only then
is each of the 306^2 output polynomials constructed once.  All of its
coefficients are split back and compared to the complete contraction.

The caller's actual quadratic field is split in the basis 1, field.gen().
No field or root of unity is constructed here.  Structure constants lie in
the prime field, so the two coefficient components contract independently.

Vector products use the exact unordered original pair coefficients instead
of constructing an operator: C_ii=x_i*y_i and C_ij=x_i*y_j+x_j*y_i.  Pair
rows and polynomial degrees are streamed in bounded native-Fp blocks.  The
actual caller-generator square handles quadratic coefficient products; the
same original recipe scatter handles both weighted charts.  Every returned
product coefficient is split back and checked against the entire result.

The full mathematical correctness is the coefficient identity in the
companion note original-affine-fast-operations-proof.md; finite sparse
comparisons are additional compatibility checks, not its proof.
"""
import os
if (os.environ.get("GITHUB_ACTIONS") != "true" or
        os.environ.get("GITHUB_REPOSITORY") != "Rogerhu12/math-research-public"):
    raise SystemExit("Run this mathematical helper only in the public research Actions.")

import hashlib
from pathlib import Path
from sage.all import PolynomialRing, identity_matrix, matrix, vector
from section_quotient_algebra import canonical, digest


def _progress(progress, stage, **record):
    if progress is not None:
        progress(stage, **record)


def _prime_matrix_hash(value):
    """Exact streamed byte encoding, valid for the ORIGINAL primes 29 and 41."""
    k = value.base_ring()
    prime = int(k.characteristic())
    assert prime in (29, 41) and int(k.cardinality()) == prime
    output = hashlib.sha256()
    output.update(canonical({
        "encoding":"small-prime-matrix-row-bytes-v1", "prime":prime,
        "rows":int(value.nrows()), "columns":int(value.ncols()),
    }).encode())
    for j in range(value.nrows()):
        output.update(bytes(int(c) for c in value.row(j)))
    return output.hexdigest()


def build_original_affine_fast_operations(affine_context, progress=None,
                                          selector_cache_mib=64,
                                          vector_pair_batch_size=128,
                                          vector_degree_block_size=32):
    """Return (adapted_context, receipt), preserving the old public interface.

    The returned context has the same multiplication_matrix, multiply,
    product_coordinates, chart, and constant_extension APIs.  Both the
    original certificate and the original product-table objects are kept
    unchanged.  Its added APIs are:

      multiplication_matrix_with_certificate(x, infinity=False) -> (M, rec)
      multiply_with_certificate(x, y, infinity=False) -> (xy, rec)
      coefficient_contraction_summary() -> complete running audit summary
      last_coefficient_contraction() -> the most recent exact operator rec
      last_direct_product() -> the most recent exact vector-product rec

    The same additions are present in constant_extension(field) and chart.
    Every standard multiplication_matrix call also performs and records the
    whole coefficient return.  The summary commits to ALL operator receipts
    by an ordered SHA-256 stream; it never treats sparse checks as coverage
    of later dense inputs.

    Only selected native Fp matrices are cached.  A conservative 8-byte per
    entry accounting plus row/object allowance enforces the configured
    retained payload budget.  A first-fit cache avoids full-scan LRU churn;
    sparse compatibility probes do not populate it.  Uncached selectors
    contain ONLY the actual nonzero input coordinates, are made at most
    once per (j, weight) per operator, and are shared by every input degree,
    both field components, and all recipe shifts.  Dense full-weight groups
    still reuse their entire group selector; partial groups have distinct
    exact coordinate-tuple cache keys, within the same bounded budget.
    """
    n = int(affine_context["dimension"])
    k = affine_context["constants"]
    prime = int(k.characteristic())
    assert n == 306 and prime in (29, 41)
    assert int(k.cardinality()) == prime
    assert affine_context["kind"] == "rank2_original_Y_complete_affine_multiplication_context"
    original_certificate = affine_context["certificate"]
    assert original_certificate["every_product_full_global_zero_bound_checked"] is True
    assert original_certificate["complete_original_infinity_chart"] is True
    assert original_certificate["complete_symmetric_basis_product_count"] == n*(n+1)//2
    original_signature = original_certificate["exact_multiplication_signature_sha256"]
    vector_pair_batch_size = int(vector_pair_batch_size)
    vector_degree_block_size = int(vector_degree_block_size)
    assert vector_pair_batch_size > 0 and vector_degree_block_size > 0
    weights = tuple(int(d) for d in affine_context["basis_weights"])
    assert len(weights) == n and weights.count(0) == 1
    assert min(weights) == 0 and max(weights) <= 4 and sum(weights) == 864
    tables = affine_context["product_blocks"]
    positions = affine_context["product_pair_positions"]
    recipes = {
        int(m):tuple((int(i), int(e)) for i, e in rs)
        for m, rs in affine_context["complete_product_recipes"].items()
    }
    weight_indices = {
        a:tuple(i for i, d in enumerate(weights) if d == a)
        for a in sorted(set(weights))
    }
    weight_column_indices = {
        a:{i:column for column, i in enumerate(indices)}
        for a, indices in weight_indices.items()
    }
    assert len(positions) == n*(n+1)//2
    occupied = {int(m):set() for m in tables}
    pairs_by_weight = {int(m):[] for m in tables}
    for i in range(n):
        for j in range(i, n):
            m, row = (int(v) for v in positions[(i, j)])
            assert m == weights[i]+weights[j]
            assert 0 <= row < tables[m].nrows()
            assert row not in occupied[m]
            occupied[m].add(row)
            pairs_by_weight[m].append((i, j, row))
    for m, table in tables.items():
        m = int(m)
        assert table.base_ring() == k and table.ncols() == len(recipes[m])
        assert occupied[m] == set(range(table.nrows()))
        assert set(recipes[m]) == {
            (i, e) for i in range(n) for e in range(m-weights[i]+1)
        }
        assert len(recipes[m]) == len(set(recipes[m]))

    # All selector provenance is fixed once, independently of any target x.
    selector_rows = {}
    selector_provenance = []
    for j in range(n):
        for a, indices in weight_indices.items():
            m = a+weights[j]
            rows = tuple(int(positions[(min(i, j), max(i, j))][1]) for i in indices)
            assert all(int(positions[(min(i, j), max(i, j))][0]) == m for i in indices)
            assert len(rows) == len(set(rows))
            selector_rows[(j, a)] = (m, rows)
            selector_provenance.append([j, a, m, list(indices), list(rows)])
    selector_provenance_sha256 = digest(selector_provenance)
    del selector_provenance

    # plans[m, infinity] contains one 306-column selection for each output
    # exponent.  The last (appended) column is zero.  The disjoint selections
    # consume EVERY original recipe column exactly once, in either chart.
    plans = {}
    plan_provenance = []
    for m in sorted(tables):
        column_of = {pair:column for column, pair in enumerate(recipes[m])}
        zero_column = len(recipes[m])
        for infinity in (False, True):
            current, consumed = [], []
            for shift in range(m+1):
                columns = []
                for output_index in range(n):
                    exponent = m-weights[output_index]-shift if infinity else shift
                    column = column_of.get((output_index, exponent), zero_column)
                    columns.append(column)
                    if column != zero_column:
                        consumed.append(column)
                if any(column != zero_column for column in columns):
                    current.append((shift, tuple(columns)))
            assert sorted(consumed) == list(range(len(recipes[m])))
            plans[(m, infinity)] = tuple(current)
            plan_provenance.append([
                m, infinity, [[shift, list(columns)] for shift, columns in current]
            ])
    complete_recipe_scatter_sha256 = digest(plan_provenance)
    del plan_provenance

    cache_limit = int(selector_cache_mib)*1024*1024
    assert cache_limit >= 0
    selector_cache, field_contexts = {}, {}
    state = {
        "cache_accounted_bytes":0, "selector_cache_hits":0,
        "selector_copies":0, "selector_copied_prime_entries":0,
        "strict_zero_selector_prime_entries_omitted":0, "operator_calls":0,
        "complete_output_prime_coefficients_verified":0,
        "native_prime_matrix_contractions":0,
        "native_contracted_prime_entries":0,
        "field_preflights":[], "last":None,
        "receipt_stream":hashlib.sha256(),
        "direct_product_calls":0, "direct_product_receipt_stream":hashlib.sha256(),
        "direct_last":None, "direct_input_pair_products":0,
        "direct_native_matrix_contractions":0, "direct_contracted_prime_entries":0,
        "direct_output_prime_coefficients_verified":0,
    }

    def selected_table(j, a, indices, retain):
        # The coefficient reader has proved that every omitted input
        # polynomial is identically zero.  Do NOT copy the full weight
        # group before selecting these rows: a single basis input must
        # select a single original product-table row for each j.
        key = (j, a, indices)
        if key in selector_cache:
            state["selector_cache_hits"] += 1
            return selector_cache[key]
        m, full_rows = selector_rows[(j, a)]
        rows = tuple(full_rows[weight_column_indices[a][i]] for i in indices)
        selected = tables[m].matrix_from_rows(rows)
        assert selected.nrows() == len(indices)
        assert selected.ncols() == len(recipes[m])
        state["selector_copies"] += 1
        state["selector_copied_prime_entries"] += selected.nrows()*selected.ncols()
        state["strict_zero_selector_prime_entries_omitted"] += (
            len(weight_indices[a])-len(indices))*selected.ncols()
        # Sage's original small-prime dense backends use at most 8 bytes
        # per numeric entry; the additional allowance covers row/object
        # bookkeeping.  No polynomial objects are cached here.
        accounted = 8*selected.nrows()*selected.ncols()+64*(selected.nrows()+16)
        if retain and state["cache_accounted_bytes"]+accounted <= cache_limit:
            selector_cache[key] = selected
            state["cache_accounted_bytes"] += accounted
        return selected

    def summary():
        return {
            "kind":"rank2_original_affine_complete_coefficient_contraction_summary",
            "original_multiplication_signature_sha256":original_signature,
            "original_tables_preserved_by_object_identity":True,
            "operator_calls":state["operator_calls"],
            "native_prime_matrix_contractions":state["native_prime_matrix_contractions"],
            "native_contracted_prime_entries":state["native_contracted_prime_entries"],
            "complete_output_prime_coefficients_verified":state[
                "complete_output_prime_coefficients_verified"],
            "all_operator_receipts_ordered_sha256":state["receipt_stream"].hexdigest(),
            "selector_provenance_sha256":selector_provenance_sha256,
            "complete_recipe_scatter_sha256":complete_recipe_scatter_sha256,
            "selector_cache_limit_bytes":cache_limit,
            "selector_cache_accounted_bytes":state["cache_accounted_bytes"],
            "cached_selector_count":len(selector_cache),
            "selector_cache_hits":state["selector_cache_hits"],
            "selector_native_copies":state["selector_copies"],
            "selector_copied_prime_entries":state["selector_copied_prime_entries"],
            "strict_zero_selector_prime_entries_omitted":state[
                "strict_zero_selector_prime_entries_omitted"],
            "field_preflights":[dict(record) for record in state["field_preflights"]],
            "direct_product_calls":state["direct_product_calls"],
            "all_direct_product_receipts_ordered_sha256":state[
                "direct_product_receipt_stream"].hexdigest(),
            "direct_input_pair_products":state["direct_input_pair_products"],
            "direct_native_matrix_contractions":state["direct_native_matrix_contractions"],
            "direct_contracted_prime_entries":state["direct_contracted_prime_entries"],
            "direct_output_prime_coefficients_verified":state[
                "direct_output_prime_coefficients_verified"],
            "direct_pair_batch_size":vector_pair_batch_size,
            "direct_degree_block_size":vector_degree_block_size,
            "no_new_Laurent_or_q_coefficients_used":True,
            "precision_loss":0,
        }

    def operations_over(field):
        key = id(field)
        if key in field_contexts:
            assert field_contexts[key]["constants"] is field
            return field_contexts[key]
        assert field.is_field() and int(field.characteristic()) == prime
        cardinality = int(field.cardinality())
        assert cardinality in (prime, prime**2)
        field_degree = 1 if cardinality == prime else 2
        generator = field.gen() if field_degree == 2 else None
        affine_ring = PolynomialRing(field, "t_original_ys")
        infinity_ring = PolynomialRing(field, "s_original_inverse_ys")
        slow = (affine_context if field is k else
                affine_context["constant_extension"](field))
        unit = vector(affine_ring, slow["unit"])
        infinity_unit = vector(infinity_ring, slow["infinity_unit"])
        constant_splits, constant_joins = {}, {}

        def split_constant(value):
            value = field(value)
            if value in constant_splits:
                return constant_splits[value]
            if field_degree == 1:
                first = k(value)
                assert field(first) == value
                parts = (first,)
            else:
                coefficients = value.polynomial().list()
                assert len(coefficients) <= 2
                first = k(coefficients[0]) if coefficients else k.zero()
                second = k(coefficients[1]) if len(coefficients) > 1 else k.zero()
                assert field(first)+field(second)*generator == value
                parts = (first, second)
            constant_splits[value] = parts
            constant_joins[parts] = value
            return parts

        def join_constant(parts):
            # At most p^2 tiny constants are retained, not any polynomial
            # table.  The first occurrence verifies the original-field
            # inverse conversion; all later occurrences reuse that exact
            # field element and its already checked coordinates.
            parts = tuple(parts)
            if parts not in constant_joins:
                value = field(parts[0])
                if field_degree == 2:
                    value += field(parts[1])*generator
                assert split_constant(value) == parts
            return constant_joins[parts]

        field_record = {
            "prime":prime, "constant_field_degree":field_degree,
            "caller_field_description":str(field),
            "coefficient_basis":"1" if field_degree == 1 else "1, caller_field.gen()",
            "caller_field_object_preserved":True,
            "new_constant_field_constructed":False,
        }
        if field_degree == 2:
            field_record.update({
                "caller_generator_name":str(generator),
                "caller_generator_square_prime_coordinates":[
                    int(c) for c in split_constant(generator**2)
                ],
            })

        def coefficient_groups(x):
            """Complete polynomial coefficients, split in the caller's basis."""
            groups, records, consumed = {}, [], set()
            nonzero_count = sum(bool(value) for value in x)
            for a, full_indices in weight_indices.items():
                indices = tuple(i for i in full_indices if x[i])
                omitted = tuple(i for i in full_indices if not x[i])
                assert all(x[i].is_zero() for i in omitted)
                if not indices:
                    continue
                degree = max(int(x[i].degree()) for i in indices)
                assert degree >= 0
                consumed.update(indices)
                entries = [[k.zero()] *((degree+1)*len(indices))
                           for _ in range(field_degree)]
                for column, i in enumerate(indices):
                    for exponent, coefficient in enumerate(x[i].list()):
                        for component, value in enumerate(split_constant(coefficient)):
                            entries[component][exponent*len(indices)+column] = value
                components = tuple(matrix(k, degree+1, len(indices), row) for row in entries)
                active = tuple(c for c in range(field_degree) if not components[c].is_zero())
                assert active
                groups[a] = (degree, indices, components, active)
                records.append({
                    "input_weight":a, "input_basis_indices":list(indices),
                    "strictly_zero_input_basis_indices_omitted":list(omitted),
                    "polynomial_degree":degree,
                    "complete_prime_component_sha256":[_prime_matrix_hash(c) for c in components],
                })
            assert consumed == {i for i in range(n) if x[i]}
            return groups, records, nonzero_count

        def row_polynomials_and_return(coefficient_matrices, polynomial_ring):
            """Construct each polynomial once, then verify EVERY coefficient."""
            length = coefficient_matrices[0].nrows()
            assert all(c.nrows() == length and c.ncols() == n for c in coefficient_matrices)
            transposed = [c.transpose() for c in coefficient_matrices]
            answer = []
            for output_index in range(n):
                if field_degree == 1:
                    coefficients = [join_constant((c,)) for c in transposed[0].row(output_index)]
                else:
                    coefficients = [join_constant((a, b)) for a, b in zip(
                        transposed[0].row(output_index), transposed[1].row(output_index))]
                answer.append(polynomial_ring(coefficients))
            # This return is intentionally independent of the shift/scatter
            # loop.  No degree is sampled and no unknown tail is padded.
            # These are exact POLYNOMIALS; zero padding above their degree is
            # an algebraic equality, not a power-series precision assertion.
            returned_entries = [[k.zero()] *(n*length) for _ in range(field_degree)]
            for output_index, value in enumerate(answer):
                assert value.degree() < length or value.is_zero()
                for exponent, coefficient in enumerate(value.list()):
                    for component, c in enumerate(split_constant(coefficient)):
                        returned_entries[component][exponent*n+output_index] = c
            returned = tuple(matrix(k, length, n, entries) for entries in returned_entries)
            assert all(actual == expected for actual, expected in zip(returned, coefficient_matrices))
            return vector(polynomial_ring, answer), returned

        def multiplication_matrix_with_certificate(x, infinity=False):
            infinity = bool(infinity)
            polynomial_ring = infinity_ring if infinity else affine_ring
            x = vector(polynomial_ring, x)
            assert len(x) == n
            groups, input_records, nonzero_count = coefficient_groups(x)
            max_input_weighted_degree = max(
                (degree+a for a, (degree, _, _, _) in groups.items()), default=-1)
            answer = matrix(polynomial_ring, n, n)
            contraction_hash = hashlib.sha256()
            output_hash = hashlib.sha256()
            output_hash.update(canonical({
                "encoding":"original-polynomial-operator-prime-components-v1",
                "field":field_record, "infinity":infinity, "dimension":n,
            }).encode())
            contractions = contracted_entries = checked_coefficients = 0
            retain_selectors = nonzero_count >= max(2, n//4)
            for j in range(n):
                # A degree bound for every output column; the sharper
                # individual bound subtracts the output basis weight.
                bound = max(0, max_input_weighted_degree+weights[j])
                accumulators = [matrix(k, bound+1, n) for _ in range(field_degree)]
                for a, (degree, indices, components, active) in groups.items():
                    m = a+weights[j]
                    selector = selected_table(j, a, indices, retain_selectors)
                    assert selector.nrows() == components[0].ncols()
                    for component in active:
                        contracted = components[component]*selector
                        assert contracted.nrows() == degree+1
                        assert contracted.ncols() == len(recipes[m])
                        contractions += 1
                        contracted_entries += contracted.nrows()*contracted.ncols()
                        contraction_hash.update(canonical({
                            "output_row":j, "input_weight":a, "product_weight":m,
                            "prime_component":component,
                            "complete_contraction_sha256":_prime_matrix_hash(contracted),
                        }).encode())
                        padded = contracted.augment(matrix(k, degree+1, 1))
                        for shift, columns in plans[(m, infinity)]:
                            selected = padded.matrix_from_columns(columns)
                            assert selected.nrows() == degree+1 and selected.ncols() == n
                            assert shift+degree <= bound
                            for exponent in range(degree+1):
                                target = exponent+shift
                                accumulators[component].set_row(
                                    target, accumulators[component].row(target)+selected.row(exponent))
                polynomial_row, returned = row_polynomials_and_return(accumulators, polynomial_ring)
                for output_index, value in enumerate(polynomial_row):
                    if value:
                        assert value.degree() <= max_input_weighted_degree+weights[j]-weights[output_index]
                answer.set_row(j, polynomial_row)
                checked_coefficients += field_degree*(bound+1)*n
                output_hash.update(canonical({
                    "row":j, "degree_bound":bound,
                    "complete_prime_component_sha256":[_prime_matrix_hash(c) for c in returned],
                }).encode())
                if j+1 in (64, 128, 192, 256):
                    _progress(progress, "complete native original operator rows",
                              completed=j+1, total=n, infinity_chart=infinity,
                              constant_field_degree=field_degree,
                              input_nonzero_coordinates=nonzero_count)
            state["operator_calls"] += 1
            record = {
                "kind":"rank2_original_affine_exact_coefficient_contraction",
                "operator_call":state["operator_calls"],
                "original_multiplication_signature_sha256":original_signature,
                "constant_field":field_record, "infinity_chart":infinity,
                "operator_dimension":n, "input_nonzero_coordinates":nonzero_count,
                "maximum_input_weighted_degree":max_input_weighted_degree,
                "input_complete_coefficient_groups_sha256":digest(input_records),
                "native_prime_matrix_contractions":contractions,
                "native_contracted_prime_entries":int(contracted_entries),
                "all_native_contractions_sha256":contraction_hash.hexdigest(),
                "complete_output_prime_coefficients_verified":int(checked_coefficients),
                "complete_output_coefficients_sha256":output_hash.hexdigest(),
                "selector_provenance_sha256":selector_provenance_sha256,
                "complete_recipe_scatter_sha256":complete_recipe_scatter_sha256,
                "every_original_recipe_column_consumed_exactly_once_per_contraction":True,
                "only_identically_zero_input_coordinate_rows_omitted":True,
                "no_full_weight_table_copy_for_sparse_inputs":True,
                "every_returned_polynomial_coefficient_checked":True,
                "original_field_split_and_recombination_checked":True,
                "both_weighted_chart_rules_used_without_table_change":True,
                "precision_loss":0, "random_or_sampled_verification":False,
            }
            state["native_prime_matrix_contractions"] += contractions
            state["native_contracted_prime_entries"] += contracted_entries
            state["complete_output_prime_coefficients_verified"] += checked_coefficients
            state["last"] = record
            state["receipt_stream"].update(canonical(record).encode())
            state["receipt_stream"].update(b"\n")
            _progress(progress, "complete original operator contraction certified",
                      operator_call=record["operator_call"], infinity_chart=infinity,
                      constant_field_degree=field_degree,
                      input_nonzero_coordinates=nonzero_count,
                      checked_prime_coefficients=int(checked_coefficients),
                      complete_output_coefficients_sha256=record["complete_output_coefficients_sha256"])
            return answer, record

        def multiplication_matrix(x, infinity=False):
            return multiplication_matrix_with_certificate(x, infinity=infinity)[0]

        def multiply_with_certificate(x, y, infinity=False):
            """Exact unordered-pair contraction, without a polynomial operator.

            Every needed coefficient of C_ij=x_i*y_j+x_j*y_i (i<j),
            C_ii=x_i*y_i is computed in the caller's exact constants.
            Prime-field row blocks contract against the SAME original table
            rows; all recipe columns are scattered in the actual chart.
            Only the final n coordinate-output polynomials are constructed;
            intermediate exact Fp pair-coefficient polynomials are streamed
            in bounded batches, never assembled into a polynomial operator.
            """
            infinity = bool(infinity)
            polynomial_ring = infinity_ring if infinity else affine_ring
            x, y = vector(polynomial_ring, x), vector(polynomial_ring, y)
            assert len(x) == len(y) == n
            xgroups, xrecords, xn = coefficient_groups(x)
            ygroups, yrecords, yn = coefficient_groups(y)
            square = x == y
            wx = max((degree+a for a, (degree, _, _, _) in xgroups.items()), default=-1)
            wy = max((degree+a for a, (degree, _, _, _) in ygroups.items()), default=-1)
            bound = max(0, wx+wy) if xn and yn else 0
            accumulators = [matrix(k, bound+1, n) for _ in range(field_degree)]
            prime_polynomials = PolynomialRing(k, "q_original_direct_product")
            zero_parts = tuple(prime_polynomials.zero() for _ in range(field_degree))

            def split_polynomials(groups):
                parts = [zero_parts for _ in range(n)]
                for _, (degree, indices, components, _) in groups.items():
                    for column, i in enumerate(indices):
                        parts[i] = tuple(prime_polynomials(list(component.column(column)))
                                         for component in components)
                        assert all(p.degree() <= degree for p in parts[i])
                return parts

            xparts = split_polynomials(xgroups)
            yparts = xparts if square else split_polynomials(ygroups)
            generator_square = (split_constant(generator**2)
                                if field_degree == 2 else None)
            pair_polynomial_products = 0

            def constant_field_polynomial_product(left, right):
                nonlocal pair_polynomial_products
                pair_polynomial_products += 1
                if field_degree == 1:
                    return (left[0]*right[0],)
                # The three exact native Fp products are Karatsuba's identity.
                # gamma^2=u+v*gamma is read from the CALLER'S actual generator.
                p00, p11 = left[0]*right[0], left[1]*right[1]
                middle = (left[0]+left[1])*(right[0]+right[1])-p00-p11
                u, v = generator_square
                return (p00+u*p11, middle+v*p11)

            contraction_hash = hashlib.sha256()
            pair_source_hash = hashlib.sha256()
            contractions = contracted_entries = active_pairs = zero_pairs = batches = 0
            eligible_pairs = 0
            peak_selector_entries = peak_input_block_entries = peak_contracted_entries = 0
            maximum_retained_pair_polynomial_coefficients = 0

            def consume_batch(m, batch):
                nonlocal contractions, contracted_entries, batches
                nonlocal peak_selector_entries, peak_input_block_entries, peak_contracted_entries
                nonlocal maximum_retained_pair_polynomial_coefficients
                assert 0 < len(batch) <= vector_pair_batch_size
                row_indices = tuple(row for i, j, row, parts in batch)
                assert len(row_indices) == len(set(row_indices))
                selector = tables[m].matrix_from_rows(row_indices)
                assert selector.nrows() == len(batch) and selector.ncols() == len(recipes[m])
                peak_selector_entries = max(peak_selector_entries, selector.nrows()*selector.ncols())
                length = 1+max(int(p.degree()) for _, _, _, parts in batch for p in parts if p)
                assert length >= 1
                maximum_retained_pair_polynomial_coefficients = max(
                    maximum_retained_pair_polynomial_coefficients,
                    sum(len(p.list()) for _, _, _, parts in batch for p in parts))
                pair_source_hash.update(canonical({
                    "weight":m, "original_pairs_and_rows":[[i,j,row] for i,j,row,_ in batch],
                    "all_selected_original_table_entries_sha256":_prime_matrix_hash(selector),
                    "full_pair_polynomial_length":length,
                }).encode())
                pair_source_hash.update(b"\n")
                for start in range(0, length, vector_degree_block_size):
                    height = min(vector_degree_block_size, length-start)
                    for component in range(field_degree):
                        coefficients = matrix(k, height, len(batch),
                            lambda r, c: batch[c][3][component][start+r])
                        peak_input_block_entries = max(peak_input_block_entries,
                                                       coefficients.nrows()*coefficients.ncols())
                        coefficient_hash = _prime_matrix_hash(coefficients)
                        if coefficients.is_zero():
                            contraction_hash.update(canonical({
                                "weight":m, "degree_start":start, "degree_length":height,
                                "component":component, "input_sha256":coefficient_hash,
                                "exact_zero_block_omitted":True,
                            }).encode())
                            contraction_hash.update(b"\n")
                            continue
                        contracted = coefficients*selector
                        assert contracted.nrows() == height and contracted.ncols() == len(recipes[m])
                        contractions += 1
                        contracted_entries += contracted.nrows()*contracted.ncols()
                        peak_contracted_entries = max(peak_contracted_entries,
                                                       contracted.nrows()*contracted.ncols())
                        contraction_hash.update(canonical({
                            "weight":m, "degree_start":start, "degree_length":height,
                            "component":component, "input_sha256":coefficient_hash,
                            "complete_contraction_sha256":_prime_matrix_hash(contracted),
                        }).encode())
                        contraction_hash.update(b"\n")
                        padded = contracted.augment(matrix(k, height, 1))
                        for shift, columns in plans[(m, infinity)]:
                            selected = padded.matrix_from_columns(columns)
                            assert selected.nrows() == height and selected.ncols() == n
                            for local in range(height):
                                target = start+local+shift
                                if target > bound:
                                    # The per-pair filtration bound forces these
                                    # exact coefficients to be zero; no tail is dropped.
                                    assert selected.row(local).is_zero()
                                else:
                                    accumulators[component].set_row(target,
                                        accumulators[component].row(target)+selected.row(local))
                batches += 1
                if batches % 32 == 0:
                    _progress(progress, "complete direct original pair batches",
                              batches=batches, native_contractions=contractions,
                              infinity_chart=infinity, constant_field_degree=field_degree)

            for m, pairs in pairs_by_weight.items():
                batch = []
                for i, j, row in pairs:
                    forward = bool(x[i]) and bool(y[j])
                    backward = i != j and bool(x[j]) and bool(y[i])
                    if not forward and not backward:
                        continue
                    eligible_pairs += 1
                    if square:
                        assert forward and (i == j or backward)
                        parts = constant_field_polynomial_product(xparts[i], xparts[j])
                        if i != j:
                            parts = tuple(2*p for p in parts)
                    else:
                        parts = (constant_field_polynomial_product(xparts[i], yparts[j])
                                 if forward else zero_parts)
                        if backward:
                            other = constant_field_polynomial_product(xparts[j], yparts[i])
                            parts = tuple(a+b for a, b in zip(parts, other))
                    if not any(parts):
                        zero_pairs += 1
                        continue
                    assert m == weights[i]+weights[j]
                    assert all(p.degree()+m <= bound for p in parts if p)
                    active_pairs += 1
                    batch.append((i, j, row, parts))
                    if len(batch) == vector_pair_batch_size:
                        consume_batch(m, batch)
                        batch = []
                if batch:
                    consume_batch(m, batch)
            assert eligible_pairs == active_pairs+zero_pairs
            assert eligible_pairs <= min(xn*yn, n*(n+1)//2)
            if not xn or not yn:
                assert eligible_pairs == 0 and all(a.is_zero() for a in accumulators)
            answer, returned = row_polynomials_and_return(accumulators, polynomial_ring)
            for i, value in enumerate(answer):
                if value:
                    assert value.degree() <= wx+wy-weights[i]
            state["direct_product_calls"] += 1
            checked = field_degree*(bound+1)*n
            record = {
                "kind":"rank2_original_affine_exact_direct_vector_product",
                "direct_product_call":state["direct_product_calls"],
                "original_multiplication_signature_sha256":original_signature,
                "constant_field":field_record, "infinity_chart":infinity,
                "module_dimension":n, "left_nonzero_coordinates":xn,
                "right_nonzero_coordinates":yn, "complete_vectors_equal":square,
                "maximum_left_weighted_degree":wx, "maximum_right_weighted_degree":wy,
                "complete_output_degree_bound":bound,
                "left_full_coefficient_groups_sha256":digest(xrecords),
                "right_full_coefficient_groups_sha256":digest(yrecords),
                "eligible_original_unordered_pairs":eligible_pairs,
                "nonzero_pair_coefficient_polynomials":active_pairs,
                "identically_zero_pair_coefficient_polynomials_omitted":zero_pairs,
                "exact_original_constant_field_polynomial_products":pair_polynomial_products,
                "all_actual_pair_sources_sha256":pair_source_hash.hexdigest(),
                "native_pair_batches":batches,
                "native_prime_matrix_contractions":contractions,
                "native_contracted_prime_entries":int(contracted_entries),
                "all_complete_contractions_sha256":contraction_hash.hexdigest(),
                "complete_output_prime_coefficients_verified":checked,
                "complete_output_prime_component_sha256":[_prime_matrix_hash(c) for c in returned],
                "complete_recipe_scatter_sha256":complete_recipe_scatter_sha256,
                "every_original_recipe_column_scattered_exactly_once_per_contraction":True,
                "every_output_coefficient_returned_to_original_field_components":True,
                "both_original_weighted_charts_preserved":True,
                "new_constant_field_or_root_chosen":False,
                "polynomial_multiplication_matrix_constructed":False,
                "number_of_output_polynomials_constructed":n,
                "pair_batch_size":vector_pair_batch_size,
                "degree_block_size":vector_degree_block_size,
                "peak_selected_table_prime_entries":peak_selector_entries,
                "peak_input_block_prime_entries":peak_input_block_entries,
                "peak_contracted_block_prime_entries":peak_contracted_entries,
                "maximum_retained_pair_polynomial_coefficients":maximum_retained_pair_polynomial_coefficients,
                "persistent_pair_selector_cache_created":False,
                "precision_loss":0, "random_or_sampled_verification":False,
            }
            state["direct_input_pair_products"] += pair_polynomial_products
            state["direct_native_matrix_contractions"] += contractions
            state["direct_contracted_prime_entries"] += contracted_entries
            state["direct_output_prime_coefficients_verified"] += checked
            state["direct_last"] = record
            state["direct_product_receipt_stream"].update(canonical(record).encode())
            state["direct_product_receipt_stream"].update(b"\n")
            _progress(progress, "complete original direct product certified",
                      direct_product_call=record["direct_product_call"], infinity_chart=infinity,
                      left_nonzero_coordinates=xn, right_nonzero_coordinates=yn,
                      complete_vectors_equal=square, active_original_pairs=active_pairs,
                      checked_prime_coefficients=checked,
                      polynomial_multiplication_matrix_constructed=False)
            return answer, record

        def multiply(x, y, infinity=False):
            return multiply_with_certificate(x, y, infinity=infinity)[0]

        def last_receipt():
            return None if state["last"] is None else dict(state["last"])

        def last_direct_receipt():
            return None if state["direct_last"] is None else dict(state["direct_last"])

        def chart(infinity=False):
            infinity = bool(infinity)
            polynomial_ring = infinity_ring if infinity else affine_ring
            selected_unit = infinity_unit if infinity else unit
            return {
                "constants":field, "polynomial_ring":polynomial_ring,
                "dimension":n, "unit":selected_unit,
                "multiplication_matrix":lambda x: multiplication_matrix(x, infinity=infinity),
                "multiplication_matrix_with_certificate":lambda x: multiplication_matrix_with_certificate(x, infinity=infinity),
                "multiply":lambda x, y: multiply(x, y, infinity=infinity),
                "multiply_with_certificate":lambda x, y: multiply_with_certificate(x, y, infinity=infinity),
                "coefficient_contraction_summary":summary,
                "last_coefficient_contraction":last_receipt,
                "last_direct_product":last_direct_receipt,
                "infinity_chart":infinity, "original_basis_weights":weights,
            }

        operations = {
            "constants":field, "dimension":n, "polynomial_ring":affine_ring,
            "affine_polynomial_ring":affine_ring, "infinity_polynomial_ring":infinity_ring,
            "unit":unit, "infinity_unit":infinity_unit,
            "product_coordinates":slow["product_coordinates"],
            "multiplication_matrix":multiplication_matrix, "multiply":multiply,
            "multiplication_matrix_with_certificate":multiplication_matrix_with_certificate,
            "multiply_with_certificate":multiply_with_certificate,
            "chart":chart, "constant_extension":operations_over,
            "coefficient_contraction_summary":summary,
            "last_coefficient_contraction":last_receipt,
            "last_direct_product":last_direct_receipt,
        }
        # This is compatibility, not a replacement for the complete exact
        # contraction performed for EVERY later (possibly dense) input.
        positive_indices = [i for i, d in enumerate(weights) if d > 0]
        low_index = min(positive_indices, key=lambda i: (weights[i], i))
        high_index = max(positive_indices, key=lambda i: (weights[i], i))
        assert low_index != high_index
        sparse_checks, direct_checks = [], []
        for infinity in (False, True):
            ring = infinity_ring if infinity else affine_ring
            parameter = ring.gen()
            selected_unit = infinity_unit if infinity else unit
            actual, record = multiplication_matrix_with_certificate(selected_unit, infinity=infinity)
            old = slow["multiplication_matrix"](selected_unit, infinity=infinity)
            assert actual == old == identity_matrix(ring, n)
            sparse_checks.append({
                "infinity_chart":infinity, "case":"the actual original scalar unit",
                "complete_operator_sha256":record["complete_output_coefficients_sha256"],
                "all_306_by_306_entries_agree_with_original_API":True,
            })
            unit_product, direct_record = multiply_with_certificate(
                selected_unit, selected_unit, infinity=infinity)
            assert unit_product == selected_unit
            direct_checks.append({
                "infinity_chart":infinity, "case":"the same actual unit squared",
                "complete_direct_product_receipt_sha256":digest(direct_record),
                "all_306_coordinates_equal_the_original_operator_product":True,
            })
            sparse = vector(ring, n)
            gamma = generator if field_degree == 2 else field.one()
            sparse[low_index] = gamma+(gamma+1)*parameter**2
            sparse[high_index] = (gamma+2)-gamma*parameter**3
            actual, record = multiplication_matrix_with_certificate(sparse, infinity=infinity)
            old = slow["multiplication_matrix"](sparse, infinity=infinity)
            assert actual == old
            sparse_checks.append({
                "infinity_chart":infinity,
                "case":"two actual basis coordinates, with degrees 2 and 3",
                "basis_indices":[low_index, high_index],
                "complete_operator_sha256":record["complete_output_coefficients_sha256"],
                "all_306_by_306_entries_agree_with_original_API":True,
            })
            # These are extra whole-API comparisons using the operator just
            # authenticated above.  The coefficient formula, full source-row
            # selection and complete return prove ALL later direct products.
            other = vector(ring, [gamma+field(i+1)*parameter for i in range(n)])
            for name, right in (("two-coordinate times all-coordinate polynomial vector", other),
                                ("the same two-coordinate polynomial vector squared", sparse)):
                actual_product, direct_record = multiply_with_certificate(
                    sparse, right, infinity=infinity)
                assert actual_product == right*actual
                direct_checks.append({
                    "infinity_chart":infinity, "case":name,
                    "complete_direct_product_receipt_sha256":digest(direct_record),
                    "all_306_coordinates_equal_the_original_operator_product":True,
                    "previously_authenticated_operator_reused":True,
                })
        field_preflight = {
            "constant_field":field_record,
            "complete_original_API_comparisons":sparse_checks,
            "complete_direct_product_API_comparisons":direct_checks,
            "random_tests_used":False,
        }
        state["field_preflights"].append(field_preflight)
        operations["fast_field_preflight"] = field_preflight
        field_contexts[key] = operations
        return operations

    base_operations = operations_over(k)
    receipt = {
        "kind":"rank2_original_affine_native_coefficient_operation_adapter",
        "status":"complete_exact_coefficient_adapter_and_sparse_API_compatibility_verified",
        "original_multiplication_signature_sha256":original_signature,
        "original_complete_multiplication_certificate_preserved":True,
        "original_product_table_objects_preserved":True,
        "module_dimension":n, "prime":prime,
        "basis_weight_counts":{str(a):len(indices) for a, indices in weight_indices.items()},
        "selector_provenance_sha256":selector_provenance_sha256,
        "complete_recipe_scatter_sha256":complete_recipe_scatter_sha256,
        "selector_cache_limit_bytes":cache_limit,
        "no_polynomial_structure_table_cache":True,
        "sparse_inputs_copy_only_actual_nonzero_coordinate_rows":True,
        "every_later_operator_performs_full_coefficient_return":True,
        "every_later_direct_vector_product_performs_full_coefficient_return":True,
        "multiply_uses_complete_original_unordered_pair_contraction":True,
        "vector_product_constructs_no_polynomial_multiplication_matrix":True,
        "direct_vector_pair_batch_size":vector_pair_batch_size,
        "direct_vector_degree_block_size":vector_degree_block_size,
        "direct_pair_selector_cache_created":False,
        "no_new_Laurent_or_q_coefficients_used":True, "precision_loss":0,
        "initial_prime_field_preflight":dict(base_operations["fast_field_preflight"]),
        "initial_coefficient_contraction_summary":summary(),
        "helper_sha256":hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "original_large_intersection_divisors_computed":False,
        "original_shadow_computed":False,
    }
    adapted = dict(affine_context)
    adapted.update(base_operations)
    adapted.update({
        "operations":base_operations,
        "original_multiplication_context":affine_context,
        "fast_operations_certificate":receipt,
        "constant_extension":operations_over,
    })
    assert adapted["product_blocks"] is tables
    assert adapted["product_pair_positions"] is positions
    assert adapted["certificate"] is original_certificate
    _progress(progress, "complete original fast operation adapter verified",
              module_rank=n, prime=prime,
              original_multiplication_signature_sha256=original_signature,
              selector_cache_limit_bytes=cache_limit,
              precision_loss=0)
    return adapted, receipt
