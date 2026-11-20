"""The six COMPLETE 306-dimensional cusp fibers of the original y_s map.

The authenticated two-chart normalization is specialized, with no plane-model
normalization and no deletion of nilpotents.  Each fiber is checked to be
Fp[nu]/(nu^289) x Fp x Fp16.  Actual Frobenius powers, primitive idempotents,
the entire length-289 local power basis, and all original 666 projective
coordinates remain in process.  Only their certificates and hashes are output.
"""
import os
if (os.environ.get("GITHUB_ACTIONS") != "true" or
        os.environ.get("GITHUB_REPOSITORY") != "Rogerhu12/math-research-public"):
    raise SystemExit("Run this mathematical helper only in public research Actions.")

import hashlib
from pathlib import Path
from sage.all import PolynomialRing, ZZ, identity_matrix, matrix, vector
from section_quotient_algebra import digest, matrix_digest, vector_digest
import finite_section_frobenius as residue_tools


def _progress(progress, stage, **record):
    if progress is not None:
        progress(stage, **record)


def _coordinates(basis, rows):
    k = basis.base_ring()
    assert rows.base_ring() == k and rows.ncols() == basis.ncols()
    pivots = tuple(basis.pivots())
    assert len(pivots) == basis.nrows()
    inverse = basis.matrix_from_columns(pivots).inverse()
    result = rows.matrix_from_columns(pivots)*inverse
    assert result*basis == rows
    return result


def _row_basis(rows):
    result = rows.row_space().basis_matrix()
    assert result.rank() == result.nrows()
    return result


def _specialize_chart(affine, value, infinity, progress, batch_size):
    """Specialize every actual product; no guessed local cusp model is used."""
    k = affine["constants"]
    n = int(affine["dimension"])
    assert n == 306 and int(k.cardinality()) == int(k.characteristic())
    weights = tuple(int(d) for d in affine["basis_weights"])
    blocks = affine["product_blocks"]
    recipes = affine["complete_product_recipes"]
    positions = affine["product_pair_positions"]
    chart = affine["chart"](infinity=infinity)
    scalar = k.zero() if infinity else k(value)
    label = "infinity" if infinity else str(int(value))
    pairs_by_weight = {}
    for pair, (weight, row) in positions.items():
        pairs_by_weight.setdefault(int(weight), []).append((int(row), pair))
    operators = [matrix(k, n, n) for _ in range(n)]
    records = []
    for weight in sorted(blocks):
        block = blocks[weight]
        ordered = sorted(pairs_by_weight[weight])
        assert [row for row, pair in ordered] == list(range(block.nrows()))
        transfer = matrix(k, len(recipes[weight]), n)
        for row, (basis_index, exponent) in enumerate(recipes[weight]):
            basis_index, exponent = int(basis_index), int(exponent)
            assert 0 <= exponent <= weight-weights[basis_index]
            if infinity:
                # c_i*c_j has coefficient s^(d_i+d_j-d_k-e); at s=0
                # retain exactly the weighted leading coefficient.
                coefficient = k.one() if exponent == weight-weights[basis_index] else k.zero()
            else:
                coefficient = scalar**exponent
            transfer[row, basis_index] = coefficient
        for start in range(0, block.nrows(), batch_size):
            end = min(start+batch_size, block.nrows())
            returned = block[start:end, :]*transfer
            for offset in range(end-start):
                i, j = ordered[start+offset][1]
                output = returned.row(offset)
                operators[i].set_row(j, output)
                operators[j].set_row(i, output)
        records.append({
            "product_weight":int(weight), "symmetric_pairs":int(block.nrows()),
            "actual_specialization_transfer_sha256":matrix_digest(transfer),
        })
        _progress(progress, "specialized complete original cusp fiber product block",
                  fiber=label, weight=int(weight), symmetric_pairs=int(block.nrows()))
    assert sum(block.nrows() for block in blocks.values()) == n*(n+1)//2
    unit = vector(k, [coefficient(scalar) for coefficient in chart["unit"]])
    I = identity_matrix(k, n)
    for i, operator in enumerate(operators):
        assert unit*operator == I.row(i)
        for j in range(i, n):
            assert operator.row(j) == operators[j].row(i)
    operators = tuple(operators)

    def multiplication_matrix(x):
        x = vector(k, x)
        assert len(x) == n
        nonzero = [(i, coefficient) for i, coefficient in enumerate(x) if coefficient]
        if not nonzero:
            return matrix(k, n, n)
        i, coefficient = nonzero[0]
        answer = operators[i] if coefficient == 1 else coefficient*operators[i]
        for i, coefficient in nonzero[1:]:
            answer = answer+coefficient*operators[i]
        return answer

    def multiply(x, y):
        return vector(k, y)*multiplication_matrix(x)

    def power(x, exponent):
        exponent = int(exponent)
        assert exponent >= 0
        answer = vector(k, unit)
        if not exponent:
            return answer
        operator = multiplication_matrix(x)
        if exponent <= 64:
            for _ in range(exponent):
                answer = answer*operator
            return answer
        while exponent:
            if exponent & 1:
                answer = answer*operator
            exponent >>= 1
            if exponent:
                operator = operator*operator
        return answer

    assert multiplication_matrix(unit) == I
    hashes = [matrix_digest(operator) for operator in operators]
    receipt = {
        "fiber":label, "infinity_chart":bool(infinity),
        "specialization_value_in_prime_field":int(scalar),
        "complete_dimension":n,
        "complete_symmetric_basis_products":n*(n+1)//2,
        "actual_specialization_blocks":records,
        "actual_multiplication_table_sha256":digest(hashes),
        "actual_unit_sha256":vector_digest(unit),
        "unit_verified_on_every_basis_element":True,
        "every_product_from_original_complete_normalization":True,
    }
    return {
        "constants":k, "dimension":n, "unit":unit,
        "multiplication_matrices":operators,
        "multiplication_matrix":multiplication_matrix,
        "multiply":multiply, "power":power,
        "fiber":label, "infinity_chart":bool(infinity),
        "specialization_value":scalar, "certificate":receipt,
    }, receipt


def _frobenius_and_components(algebra, progress):
    """Actual Frobenius and all local algebras, including nilpotency 289."""
    k, n = algebra["constants"], int(algebra["dimension"])
    p, label = int(k.characteristic()), algebra["fiber"]
    assert n == 306 and p in (29, 41)
    I = identity_matrix(k, n)
    rows = []
    for i in range(n):
        rows.append(algebra["power"](I.row(i), p))
        if i % 24 == 23 or i+1 == n:
            _progress(progress, "actual cusp fiber Frobenius powers",
                      fiber=label, completed=i+1, total=n, prime=p)
    F = matrix(k, rows)
    F2, projection = F**2, F**16
    assert algebra["unit"]*F == algebra["unit"]
    actual_rank = int(F.rank())
    assert actual_rank == 17+(288//p+1)
    assert F2.rank() == projection.rank() == 18
    assert F2*projection == F2 and projection**2 == projection
    assert F**18 == F2
    characteristic = F.charpoly()
    X = characteristic.parent().gen()
    assert characteristic == X**288*(X-1)**2*(X**16-1)
    fixed_dimensions = []
    current = I
    for d in range(1, 17):
        current = current*F
        observed = n-int((current-I).rank())
        assert observed == 2+int(ZZ(d).gcd(16))
        fixed_dimensions.append({"power":d, "actual_fixed_dimension":observed})
    nilradical = projection.left_kernel().basis_matrix()
    assert nilradical.nrows() == 288 and (nilradical*F2).is_zero()
    assert (F-I).left_kernel().dimension() == 3
    _progress(progress, "full actual thick cusp Frobenius gates passed",
              fiber=label, dimension=n, rank_F=actual_rank,
              rank_F2=18, reduction_projection_power=16,
              nilradical_dimension=288)

    def local_progress(stage, **record):
        _progress(progress, stage, fiber=label, **record)

    fixed, idempotents, projectors, splits = residue_tools._split_fixed_algebra(
        algebra, F, local_progress)
    assert idempotents.nrows() == 3
    P = PolynomialRing(k, "X_original_cusp_residue")
    Z = P.gen()
    components, records = [], []
    for index, (e, projector) in enumerate(zip(idempotents.rows(), projectors)):
        ambient_dimension = int(projector.rank())
        reduced = _row_basis(projector*projection)
        degree = int(reduced.nrows())
        assert (ambient_dimension, degree) in ((289, 1), (1, 1), (16, 16))
        assert reduced*(F**degree) == reduced
        if degree == 1:
            alpha = vector(k, n)
        else:
            assert degree == 16
            alpha = next((candidate for candidate in reduced.rows()
                          if candidate*(F**8) != candidate), None)
            assert alpha is not None
        M_alpha = algebra["multiplication_matrix"](alpha)
        powers = [e]
        for _ in range(degree):
            powers.append(powers[-1]*M_alpha)
        residue_basis = matrix(k, powers[:degree])
        assert residue_basis.rank() == degree
        relation = _coordinates(residue_basis, matrix(k, [powers[degree]])).row(0)
        polynomial = Z**degree-sum((relation[j]*Z**j for j in range(degree)), P.zero())
        assert polynomial.is_irreducible()
        assert _coordinates(reduced, residue_basis).rank() == degree
        nil_basis = _row_basis(projector-projector*projection)
        assert nil_basis.nrows() == ambient_dimension-degree
        assert (nil_basis*F2).is_zero()
        nil_generator, local_powers, selected = None, None, None
        if ambient_dimension == 289:
            assert degree == 1 and nil_basis.nrows() == 288
            assert (projector*F).rank() == 288//p+1
            assert (projector*F2).rank() == 1
            # In the already genuine DVR fiber, N/N^2 is one-dimensional.
            # Some row of ANY full basis of N has parameter order one.
            # The following full-rank gate finds and certifies it without
            # mistaking the ramified base function for a local parameter.
            for candidate_index, candidate in enumerate(nil_basis.rows()):
                candidate_matrix = algebra["multiplication_matrix"](candidate)
                rank = int(candidate_matrix.rank())
                if rank == 288:
                    nil_generator, M_nil = candidate, candidate_matrix
                    selected = candidate_index
                    break
                if candidate_index % 16 == 15:
                    _progress(progress, "search actual heavy cusp parameter",
                              fiber=label, tried=candidate_index+1, bound=288)
            assert nil_generator is not None
            assert nil_generator*projector == nil_generator
            local_power_rows = [e]
            for _ in range(289):
                local_power_rows.append(local_power_rows[-1]*M_nil)
            assert not local_power_rows[288].is_zero()
            assert local_power_rows[289].is_zero()
            local_powers = matrix(k, local_power_rows[:289])
            assert local_powers.rank() == 289
            assert local_powers*projector == local_powers
            assert _coordinates(local_powers, nil_basis).rank() == 288
            _progress(progress, "complete heavy cusp local algebra certified",
                      fiber=label, local_dimension=289,
                      exact_nilpotence_index=289, full_power_basis_rank=289)
        else:
            assert nil_basis.nrows() == 0
            assert projector*projection == projector
        component = {
            "idempotent":e, "projector_matrix":projector,
            "ambient_dimension":ambient_dimension,
            "residue_degree":degree, "residue_polynomial":polynomial,
            "residue_generator":alpha, "residue_power_basis":residue_basis,
            "nilradical_basis":nil_basis, "nilradical_generator":nil_generator,
            "complete_local_power_basis":local_powers,
        }
        components.append(component)
        records.append({
            "component_index":index, "ambient_dimension":ambient_dimension,
            "residue_degree":degree,
            "fiber_ramification_index":ambient_dimension//degree,
            "residue_polynomial_coefficients_ascending":[int(c) for c in polynomial.list()],
            "residue_polynomial_irreducible":True,
            "actual_projector_rank":ambient_dimension,
            "idempotent_sha256":vector_digest(e),
            "complete_residue_power_basis_sha256":matrix_digest(residue_basis),
            "nilradical_dimension":int(nil_basis.nrows()),
            "full_nilradical_basis_sha256":matrix_digest(nil_basis),
            "heavy_parameter_selected_nil_basis_row":selected,
            "heavy_parameter_sha256":(vector_digest(nil_generator)
                                       if nil_generator is not None else None),
            "heavy_local_power_basis_sha256":(matrix_digest(local_powers)
                                               if local_powers is not None else None),
            "heavy_exact_nilpotence_index":289 if local_powers is not None else None,
        })
    assert sorted((c["ambient_dimension"], c["residue_degree"]) for c in components) == [
        (1, 1), (16, 16), (289, 1)]
    assert sum(c["ambient_dimension"] for c in components) == 306
    assert sum(c["residue_degree"] for c in components) == 18
    decomposition = {"components":components, "primitive_idempotents":idempotents,
                     "fixed_algebra_basis":fixed}
    context = {"frobenius_matrix":F, "reduction_projection":projection,
               "reduction_projection_power":16, "nilradical_basis":nilradical,
               "decomposition":decomposition}
    receipt = {
        "fiber":label, "prime":p, "actual_dimension":306,
        "actual_Frobenius_rank":actual_rank, "actual_Frobenius_squared_rank":18,
        "actual_nilradical_dimension":288,
        "actual_reduction_projection_power":16,
        "Frobenius_squared_not_assumed_idempotent":True,
        "actual_Frobenius_charpoly":"X^288*(X-1)^2*(X^16-1)",
        "actual_Frobenius_charpoly_sha256":digest([int(c) for c in characteristic.list()]),
        "actual_fixed_dimensions":fixed_dimensions,
        "F18_equals_F2_verified":True, "F16_is_actual_reduction_projection":True,
        "Frobenius_matrix_sha256":matrix_digest(F),
        "reduction_projection_sha256":matrix_digest(projection),
        "closed_components":records,
        "all_primitive_idempotents_orthogonal_and_complete":True,
        "actual_primitive_idempotents_sha256":matrix_digest(idempotents),
        "actual_fixed_algebra_splits":splits,
        "heavy_full_local_algebra_not_only_reduced_support":True,
        "all_geometric_points":18, "full_scheme_length":306,
    }
    return context, receipt


def _projective_labels(algebra, frobenius, section_context, progress):
    """All 666 original coordinates, including their length-289 local values."""
    k = algebra["constants"]
    n = int(algebra["dimension"])
    infinity = bool(algebra["infinity_chart"])
    key = ("original_Y_M2_infinity_coordinates" if infinity
           else "original_Y_M2_affine_coordinates")
    polynomial_rows = section_context[key]
    assert polynomial_rows.nrows() == 666 and polynomial_rows.ncols() == n
    assert polynomial_rows.base_ring().base_ring() == k
    scalar = algebra["specialization_value"]
    values = matrix(k, [[coefficient(scalar) for coefficient in row]
                        for row in polynomial_rows.rows()])
    projection = frobenius["reduction_projection"]
    full_rows = [values*component["projector_matrix"]
                 for component in frobenius["decomposition"]["components"]]
    reduced_rows = [rows*projection for rows in full_rows]
    for full, reduced in zip(full_rows, reduced_rows):
        assert full.nrows() == reduced.nrows() == 666
        assert reduced*projection == reduced
    # The existing canonical label routine only needs actual residue values.
    # Supply the correctly reduced rows, then retain the UNREDUCED rows in
    # exactly the same returned field and hash it accordingly.  F^degree by
    # itself would NOT kill nilpotents on the length-289 rational component.
    def local_progress(stage, **record):
        _progress(progress, stage, fiber=algebra["fiber"], **record)
    labels, receipt = residue_tools.label_closed_components(
        algebra, frobenius, reduced_rows,
        coordinate_basis_id=section_context["basis_id"], progress=local_progress)
    for index, (record, component, original_rows) in enumerate(zip(
            receipt["closed_point_labels"], labels["components"], full_rows)):
        assert component["reduced_coordinate_rows"] == reduced_rows[index]
        component["full_component_coordinate_rows"] = original_rows
        record["full_component_coordinate_rows_sha256"] = residue_tools.matrix_digest(original_rows)
        record["complete_local_scheme_length"] = int(
            frobenius["decomposition"]["components"][index]["ambient_dimension"])
        record["reduction_before_labeling_used_Frobenius_power"] = 16
    labels["full_component_ratio_rows"] = full_rows
    labels["all_original_Y_M2_fiber_values"] = values
    receipt["original_global_coordinate_count"] = 666
    receipt["global_frame"] = "J0=ys^4*J" if infinity else "J"
    receipt["full_666_coordinate_rows_preserved_on_heavy_component"] = True
    receipt["reduction_projection_power"] = 16
    receipt["all_original_Y_M2_fiber_values_sha256"] = matrix_digest(values)
    return labels, receipt


def build_original_ys_cusp_fibers(affine_context, section_context,
                                  progress=None, batch_size=64):
    """Read all six true fibers from one complete normalization process.

    section_context is the prime-field output of
    original_section_ring_embedding.build_original_y_section_basis.
    It supplies Fi/J and Fi/J0 for the SAME full 666 original M2 basis.
    """
    k = affine_context["constants"]
    assert int(k.cardinality()) == int(k.characteristic())
    assert int(k.characteristic()) in (29, 41)
    assert int(batch_size) > 0
    original_rows = affine_context["original_apery_context"]["original_M2_rows"]
    assert section_context["basis_id"] == matrix_digest(original_rows[:, :1225])
    fibers, receipts, all_point_ids = {}, [], []
    for value, infinity in ((0, False), (1, False), (-1, False),
                            (3, False), (-3, False), (0, True)):
        label = "infinity" if infinity else str(value)
        _progress(progress, "complete original cusp fiber start", fiber=label)
        algebra, specialization = _specialize_chart(
            affine_context, value, infinity, progress, int(batch_size))
        frobenius, frobenius_receipt = _frobenius_and_components(algebra, progress)
        labels, label_receipt = _projective_labels(
            algebra, frobenius, section_context, progress)
        ids = [component["point_id"] for component in labels["components"]]
        all_point_ids.extend(ids)
        fibers[label] = {"algebra":algebra, "frobenius":frobenius,
                         "original_point_labels":labels}
        receipts.append({"fiber":label, "specialization":specialization,
                         "actual_Frobenius_and_local_algebras":frobenius_receipt,
                         "original_666_projective_point_labels":label_receipt})
    assert len(all_point_ids) == len(set(all_point_ids)) == 18
    assert sum(record["actual_Frobenius_and_local_algebras"]["all_geometric_points"]
               for record in receipts) == 108
    assert sum(record["actual_Frobenius_and_local_algebras"]["full_scheme_length"]
               for record in receipts) == 1836
    all_components = [component for fiber in fibers.values()
                      for component in fiber["frobenius"]["decomposition"]["components"]]
    rational_count = sum(component["residue_degree"] == 1 for component in all_components)
    degree16_count = sum(component["residue_degree"] == 16 for component in all_components)
    heavy_count = sum(component["ambient_dimension"] == 289 and
                      component["residue_degree"] == 1 for component in all_components)
    different_degree = sum(component["ambient_dimension"]-component["residue_degree"]
                           for component in all_components)
    assert (rational_count, degree16_count, heavy_count, different_degree) == (12, 6, 6, 1728)
    receipt = {
        "kind":"rank2_original_Y_six_complete_cusp_fibers",
        "status":"all_six_original_cusp_fibers_with_full_length289_local_algebras",
        "prime":int(k.characteristic()), "level":3468,
        "original_base_function":"same y_s on X0(3468)",
        "all_fiber_labels":["0", "1", "-1", "3", "-3", "infinity"],
        "fiber_scheme_length":306, "actual_total_scheme_length":1836,
        "actual_total_geometric_cusp_count":108,
        "actual_prime_field_closed_point_count":18,
        "actual_rational_closed_cusps":rational_count,
        "actual_degree16_closed_cusps":degree16_count,
        "actual_heavy_rational_cusps":heavy_count,
        "actual_heavy_nilpotence_index":289,
        "actual_total_tame_different_degree":different_degree,
        "original_Y_M2_coordinate_basis_id":section_context["basis_id"],
        "all_original_closed_point_ids_distinct":True,
        "original_full_normalization_signature_sha256":affine_context["certificate"][
            "exact_multiplication_signature_sha256"],
        "fibers":receipts,
        "large_intersection_divisors_computed":False,
        "original_shadow_computed":False,
        "helper_sha256":hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
    }
    _progress(progress, "all original thick cusp fibers certified",
              fibers=6, geometric_cusps=108, closed_cusps=18,
              total_scheme_length=1836, heavy_local_length=289)
    return {"constants":k, "fibers":fibers,
            "original_normalization_context":affine_context,
            "original_section_context":section_context,
            "certificate":receipt}, receipt
