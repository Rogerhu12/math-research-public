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
                                          selector_cache_mib=64):
    """Return (adapted_context, receipt), preserving the old public interface.

    The returned context has the same multiplication_matrix, multiply,
    product_coordinates, chart, and constant_extension APIs.  Both the
    original certificate and the original product-table objects are kept
    unchanged.  Its added APIs are:

      multiplication_matrix_with_certificate(x, infinity=False) -> (M, rec)
      coefficient_contraction_summary() -> complete running audit summary
      last_coefficient_contraction() -> the most recent exact operator rec

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
    for i in range(n):
        for j in range(i, n):
            m, row = (int(v) for v in positions[(i, j)])
            assert m == weights[i]+weights[j]
            assert 0 <= row < tables[m].nrows()
            assert row not in occupied[m]
            occupied[m].add(row)
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

        def multiply(x, y, infinity=False):
            polynomial_ring = infinity_ring if infinity else affine_ring
            return vector(polynomial_ring, y)*multiplication_matrix(x, infinity=infinity)

        def last_receipt():
            return None if state["last"] is None else dict(state["last"])

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
                "coefficient_contraction_summary":summary,
                "last_coefficient_contraction":last_receipt,
                "infinity_chart":infinity, "original_basis_weights":weights,
            }

        operations = {
            "constants":field, "dimension":n, "polynomial_ring":affine_ring,
            "affine_polynomial_ring":affine_ring, "infinity_polynomial_ring":infinity_ring,
            "unit":unit, "infinity_unit":infinity_unit,
            "product_coordinates":slow["product_coordinates"],
            "multiplication_matrix":multiplication_matrix, "multiply":multiply,
            "multiplication_matrix_with_certificate":multiplication_matrix_with_certificate,
            "chart":chart, "constant_extension":operations_over,
            "coefficient_contraction_summary":summary,
            "last_coefficient_contraction":last_receipt,
        }
        # This is compatibility, not a replacement for the complete exact
        # contraction performed for EVERY later (possibly dense) input.
        positive_indices = [i for i, d in enumerate(weights) if d > 0]
        low_index = min(positive_indices, key=lambda i: (weights[i], i))
        high_index = max(positive_indices, key=lambda i: (weights[i], i))
        assert low_index != high_index
        sparse_checks = []
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
        field_preflight = {
            "constant_field":field_record,
            "complete_original_API_comparisons":sparse_checks,
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
