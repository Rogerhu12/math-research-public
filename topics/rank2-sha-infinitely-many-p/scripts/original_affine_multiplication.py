"""Complete multiplication of the ORIGINAL filtered Y normalization ring.

Input is the authenticated full colon/Apéry context of R925, not arbitrary
Laurent strings.  Every computed basis product is returned through its full
global pole-degree window.  The resulting k[t] structure constants give the
actual integral closure A = Gamma(Y minus pole(t), O).  A second k[s] chart,
s = 1/t, is obtained by the proved weighted coefficient reversal.

All symmetric product coordinates are stored as small-prime-field matrices,
grouped by pole weight.  Polynomial matrices are constructed on demand; the
helper does not create tens of millions of polynomial objects up front.
No mathematical execution is permitted outside the public research Actions.
"""
import os
if (os.environ.get("GITHUB_ACTIONS") != "true" or
        os.environ.get("GITHUB_REPOSITORY") != "Rogerhu12/math-research-public"):
    raise SystemExit("Run this mathematical helper only in the public research Actions.")

import hashlib
from pathlib import Path
from sage.all import PolynomialRing, identity_matrix, matrix, vector
from section_quotient_algebra import canonical, digest, matrix_digest, vector_digest


def _progress(progress, stage, **record):
    if progress is not None:
        progress(stage, **record)


def _jet_row(series, weight, k):
    """Read every TRUE Laurent coefficient; an unknown tail is never zero-filled."""
    weight = int(weight)
    assert weight >= 0
    last = 305*weight
    assert series.precision_absolute() > last, (
        "Insufficient actual Laurent precision", weight,
        str(series.precision_absolute()), last)
    assert series.valuation() >= -weight, (
        "A supposed W_n function has a larger original cusp pole", weight)
    return vector(k, [series[j] for j in range(-weight, last+1)])


def _coordinate_reader(rows, recipes, weight, k):
    """The caller has proved these are the complete ORIGINAL W_weight basis."""
    weight = int(weight)
    assert rows.base_ring() == k
    assert rows.ncols() == 306*weight+1
    assert rows.nrows() == len(recipes)
    pivots = tuple(rows.pivots())
    assert len(pivots) == rows.nrows()
    inverse = rows.matrix_from_columns(pivots).inverse()
    assert rows.matrix_from_columns(pivots)*inverse == identity_matrix(k, rows.nrows())
    nonpivots = tuple(j for j in range(rows.ncols()) if j not in set(pivots))
    reconstruction = inverse*rows.matrix_from_columns(nonpivots)

    def read(jets):
        assert jets.base_ring() == k and jets.ncols() == rows.ncols()
        entries = jets.matrix_from_columns(pivots)
        assert entries*reconstruction == jets.matrix_from_columns(nonpivots), (
            "A proposed original product failed its COMPLETE global zero bound", weight)
        answer = entries*inverse
        # Pivot coefficients return identically by the exact inverse; all
        # other Laurent coefficients were checked above, with no truncation.
        return answer

    certificate = {
        "pole_weight":weight, "complete_dimension":int(rows.nrows()),
        "complete_Laurent_window_inclusive":[-weight, 305*weight],
        "full_jet_coefficients":306*weight+1,
        "monomial_recipes_sha256":digest([[int(i), int(j)] for i, j in recipes]),
        "complete_monomial_rows_sha256":matrix_digest(rows),
        "full_pivot_columns_sha256":digest(list(pivots)),
        "full_pivot_inverse_sha256":matrix_digest(inverse),
        "remaining_complete_window_columns":len(nonpivots),
    }
    return read, certificate


def build_original_affine_multiplication(apery_context, progress=None,
                                         batch_size=64):
    """Return the full two-chart multiplication context and its exact receipt.

    Required original producer keys:
      constants, t_series, apery_weights, apery_laurent_series,
      apery_coordinates, monomial_recipes, monomial_rows, q_precision.

    monomial_recipes[n] consists of (basis_index, t_exponent).  Each matching
    row has coefficients u^-n, ..., u^(305*n), and is an ACTUAL global
    t^exponent*b_basis_index.  The producer has already certified the complete
    colon kernels and the 306-element filtered free basis.  This helper
    checks the entire input-return again and certifies every basis product.

    Matrix convention: y * multiplication_matrix(x) represents y*x.
    The first chart uses b_i over k[t]; the infinity chart uses
    c_i=t^(-weight_i)*b_i over k[s].
    """
    k = apery_context["constants"]
    assert int(k.cardinality()) == int(k.characteristic())
    prime = int(k.characteristic())
    assert prime in (29, 41)
    t = apery_context["t_series"]
    basis = tuple(apery_context["apery_laurent_series"])
    weights = tuple(int(d) for d in apery_context["apery_weights"])
    coordinates = apery_context["apery_coordinates"]
    monomial_recipes = apery_context["monomial_recipes"]
    monomial_rows = apery_context["monomial_rows"]
    q_precision = int(apery_context["q_precision"])
    batch_size = int(batch_size)
    n = 306
    assert len(basis) == len(weights) == n
    assert coordinates.base_ring() == k
    assert coordinates.nrows() == n and coordinates.ncols() == 666
    assert 0 <= min(weights) <= max(weights) <= 4
    assert weights.count(0) == 1 and sum(weights) == 864
    assert q_precision >= 2453 and batch_size > 0
    assert t.valuation() == -1 and t[-1] == -k.one()
    for i, b in enumerate(basis):
        assert b.parent().base_ring() == k
        assert b.valuation() >= -weights[i]
        assert b.precision_absolute() >= q_precision-4

    # Read each complete original filtered space.  Returning the actual
    # Laurent functions makes the matrix input independently reviewable.
    readers, reader_records = {}, []
    recipe_positions = {}
    powers_t = [t.parent().one()]
    for j in range(1, 9):
        powers_t.append(powers_t[-1]*t)
    for m in range(9):
        recipes = tuple((int(i), int(j)) for i, j in monomial_recipes[m])
        expected_recipes = {(i, j) for i in range(n)
                            for j in range(m-weights[i]+1)}
        assert len(recipes) == len(set(recipes))
        assert set(recipes) == expected_recipes
        rows = monomial_rows[m]
        assert rows.nrows() == sum(max(0, m-d+1) for d in weights)
        if m >= 4:
            assert rows.nrows() == 306*m-558
        for index, (i, j) in enumerate(recipes):
            actual = basis[i]*powers_t[j]
            assert rows.row(index) == _jet_row(actual, m, k)
        reader, record = _coordinate_reader(rows, recipes, m, k)
        readers[m] = reader
        recipe_positions[m] = {pair:j for j, pair in enumerate(recipes)}
        reader_records.append(record)
        _progress(progress, "complete original filtered multiplication source", **record)

    pairs_by_weight = {m:[] for m in range(9)}
    for i in range(n):
        for j in range(i, n):
            pairs_by_weight[weights[i]+weights[j]].append((i, j))

    tables, pair_positions, table_records = {}, {}, []
    for m in range(9):
        pairs = pairs_by_weight[m]
        recipes = tuple((int(i), int(j)) for i, j in monomial_recipes[m])
        if not pairs:
            continue
        table = matrix(k, len(pairs), len(recipes))
        for start in range(0, len(pairs), batch_size):
            batch = pairs[start:start+batch_size]
            product_jets = matrix(k, [_jet_row(basis[i]*basis[j], m, k)
                                      for i, j in batch])
            returned = readers[m](product_jets)
            for offset, pair in enumerate(batch):
                table.set_row(start+offset, returned.row(offset))
                pair_positions[pair] = (m, start+offset)
            done = min(start+batch_size, len(pairs))
            if done == len(pairs) or (start//batch_size) % 16 == 0:
                _progress(progress, "actual original affine basis products",
                          pole_weight=m, completed=done, total=len(pairs),
                          complete_Laurent_coefficients=306*m+1)
        tables[m] = table
        record = {
            "product_pole_weight":m, "symmetric_basis_pair_count":len(pairs),
            "complete_target_dimension":len(recipes),
            "all_products_global_identity_verified":True,
            "pairs_sha256":digest([[i, j] for i, j in pairs]),
            "actual_product_coordinates_sha256":matrix_digest(table),
        }
        table_records.append(record)
        _progress(progress, "complete original product-weight block certified", **record)

    assert len(pair_positions) == n*(n+1)//2
    assert sum(t.nrows() for t in tables.values()) == n*(n+1)//2
    zero_index = weights.index(0)
    one = t.parent().one()
    unit_read = readers[0](matrix(k, [_jet_row(one, 0, k)])).row(0)
    recipes_zero = tuple((int(i), int(j)) for i, j in monomial_recipes[0])
    assert recipes_zero == ((zero_index, 0),)
    assert len(unit_read) == 1 and unit_read[0]
    unit_scalar = unit_read[0]

    # The actual scalar multiple of the sole weight-zero generator is the
    # global unit, whether or not the producer normalized that generator.
    for i in range(n):
        key = (min(i, zero_index), max(i, zero_index))
        m, row = pair_positions[key]
        expected = vector(k, tables[m].ncols())
        expected[recipe_positions[m][(i, 0)]] = 1
        assert unit_scalar*tables[m].row(row) == expected

    def operations_over(field):
        """Use the caller's EXACT original Fp or Fp2 constants, never a new root."""
        assert field.is_field() and int(field.characteristic()) == prime
        assert int(field.cardinality()) in (prime, prime**2)
        affine_polynomials = PolynomialRing(field, "t_original_ys")
        infinity_polynomials = PolynomialRing(field, "s_original_inverse_ys")
        T, S = affine_polynomials.gen(), infinity_polynomials.gen()
        unit_affine = vector(affine_polynomials, n)
        unit_infinity = vector(infinity_polynomials, n)
        unit_affine[zero_index] = field(unit_scalar)
        unit_infinity[zero_index] = field(unit_scalar)

        def product_coordinates(i, j, infinity=False):
            """Return the EXACT coefficients of one true (possibly base-changed) product."""
            i, j = int(i), int(j)
            assert 0 <= i < n and 0 <= j < n
            pair = (min(i, j), max(i, j))
            m, row = pair_positions[pair]
            polynomial_ring = infinity_polynomials if infinity else affine_polynomials
            parameter = S if infinity else T
            answer = vector(polynomial_ring, n)
            coefficients = tables[m].row(row)
            for coefficient, (b, exponent) in zip(coefficients, monomial_recipes[m]):
                if not coefficient:
                    continue
                b, exponent = int(b), int(exponent)
                assert 0 <= exponent <= weights[i]+weights[j]-weights[b]
                output_exponent = (weights[i]+weights[j]-weights[b]-exponent
                                   if infinity else exponent)
                assert output_exponent >= 0
                answer[b] += field(coefficient)*parameter**output_exponent
            return answer

        def multiplication_matrix(x, infinity=False):
            """A 306 x 306 polynomial operator, made only when actually needed."""
            polynomial_ring = infinity_polynomials if infinity else affine_polynomials
            x = vector(polynomial_ring, x)
            assert len(x) == n
            nonzero = [(i, coefficient) for i, coefficient in enumerate(x) if coefficient]
            answer = matrix(polynomial_ring, n, n)
            for j in range(n):
                row = vector(polynomial_ring, n)
                for i, coefficient in nonzero:
                    row += coefficient*product_coordinates(i, j, infinity=infinity)
                answer.set_row(j, row)
            return answer

        def multiply(x, y, infinity=False):
            polynomial_ring = infinity_polynomials if infinity else affine_polynomials
            return vector(polynomial_ring, y)*multiplication_matrix(x, infinity=infinity)

        def chart(infinity=False):
            """Plain one-chart interface for the complete polynomial ideal tools."""
            use_infinity = bool(infinity)
            polynomial_ring = infinity_polynomials if use_infinity else affine_polynomials
            selected_unit = unit_infinity if use_infinity else unit_affine

            def chart_matrix(x):
                return multiplication_matrix(x, infinity=use_infinity)

            def chart_multiply(x, y):
                return multiply(x, y, infinity=use_infinity)

            return {
                "constants":field, "polynomial_ring":polynomial_ring,
                "dimension":n, "unit":selected_unit,
                "multiplication_matrix":chart_matrix, "multiply":chart_multiply,
                "infinity_chart":use_infinity,
                "original_basis_weights":weights,
            }

        # These complete checks exercise both actual chart APIs.  The
        # characteristic-p field is unchanged unless the caller supplies
        # its already fixed quadratic field, containing its original omega.
        assert multiplication_matrix(unit_affine) == identity_matrix(affine_polynomials, n)
        assert multiplication_matrix(unit_infinity, infinity=True) == identity_matrix(infinity_polynomials, n)
        return {
            "constants":field, "dimension":n,
            "polynomial_ring":affine_polynomials,
            "affine_polynomial_ring":affine_polynomials,
            "infinity_polynomial_ring":infinity_polynomials,
            "unit":unit_affine, "infinity_unit":unit_infinity,
            "product_coordinates":product_coordinates,
            "multiplication_matrix":multiplication_matrix, "multiply":multiply,
            "chart":chart,
        }

    operations = operations_over(k)
    signature = {
        "prime":prime, "original_level":3468, "original_genus":559,
        "normalization_module_rank":306, "pole_divisor_degree":306,
        "basis_weights":list(weights),
        "original_apery_coordinates_sha256":matrix_digest(coordinates),
        "complete_weighted_readers":reader_records,
        "complete_product_blocks":table_records,
        "unit_basis_index":zero_index, "unit_scalar":int(unit_scalar),
    }
    receipt = dict(signature,
        kind="rank2_original_Y_complete_affine_multiplication",
        status="all_true_basis_products_and_both_normalization_charts_certified",
        q_precision=q_precision,
        complete_symmetric_basis_product_count=n*(n+1)//2,
        every_product_full_global_zero_bound_checked=True,
        polynomial_coefficient_degree_bounds_checked=True,
        original_unit_verified_on_every_basis_element=True,
        complete_original_infinity_chart=True,
        infinity_chart_formula="c_i=t^(-d_i)b_i; coefficient s^(d_i+d_j-d_k)*m_ij^k(1/s)",
        infinity_fiber_dimension=306,
        infinity_fiber_local_decomposition_computed=False,
        original_large_intersection_divisors_computed=False,
        original_shadow_computed=False,
        exact_multiplication_signature_sha256=digest(signature),
        helper_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest())
    _progress(progress, "complete original two-chart normalization multiplication",
              module_rank=306, symmetric_products=n*(n+1)//2,
              signature_sha256=receipt["exact_multiplication_signature_sha256"])
    context = {
        "kind":"rank2_original_Y_complete_affine_multiplication_context",
        **operations,
        "original_apery_context":apery_context,
        "basis_weights":weights, "basis_laurent_series":basis,
        "product_blocks":tables, "product_pair_positions":pair_positions,
        "complete_product_recipes":monomial_recipes,
        "constant_extension":operations_over,
        "certificate":receipt,
    }
    return context, receipt
