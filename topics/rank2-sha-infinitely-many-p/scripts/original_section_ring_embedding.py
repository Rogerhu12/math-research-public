"""Embed the original complete sections and maps in R925's two actual charts.

The small core needs only the certified original affine normalization.  The
map consumer additionally authenticates the SAME R917 basis and saturation
transform and uses the local input's exact quadratic constants and omega.
No independent quadratic field, root choice or function-field inverse is used.
"""
import os
if (os.environ.get("GITHUB_ACTIONS") != "true" or
        os.environ.get("GITHUB_REPOSITORY") != "Rogerhu12/math-research-public"):
    raise SystemExit("Run this mathematical helper only in the public research Actions.")

import hashlib
from pathlib import Path
from sage.all import QQ, PowerSeriesRing, LaurentSeriesRing, identity_matrix, matrix, vector
from section_quotient_algebra import canonical, digest, matrix_digest, vector_digest


def _progress(callback, stage, **record):
    if callback is not None:
        callback(stage, **record)


def finite_coordinates(value, field):
    """Coordinates in the caller's exact field presentation, never a new root."""
    value = field(value)
    degree = int(field.degree())
    assert degree in (1, 2)
    if degree == 1:
        return [int(value)]
    coefficients = [int(c) for c in value.polynomial().list()]
    assert len(coefficients) <= degree
    return coefficients+[0]*(degree-len(coefficients))


def polynomial_matrix_digest(rows):
    polynomial_ring = rows.base_ring()
    field = polynomial_ring.base_ring()
    output = hashlib.sha256()
    output.update(canonical({
        "encoding":"original-field-polynomial-matrix-v1",
        "prime":int(field.characteristic()), "constant_degree":int(field.degree()),
        "rows":int(rows.nrows()), "columns":int(rows.ncols()),
        "polynomial_order":"ascending base-parameter powers; fixed original field coordinates",
    }).encode())
    for row in rows.rows():
        output.update(b"\n")
        for value in row:
            output.update(canonical([finite_coordinates(c, field) for c in value.list()]).encode())
            output.update(b";")
    return output.hexdigest()


def polynomial_vector_digest(value):
    return polynomial_matrix_digest(matrix(value.base_ring(), [value]))


def _full_coordinate_reader(rows):
    field = rows.base_ring()
    pivots = tuple(rows.pivots())
    assert len(pivots) == rows.nrows()
    inverse = rows.matrix_from_columns(pivots).inverse()
    assert rows.matrix_from_columns(pivots)*inverse == identity_matrix(field, rows.nrows())
    pivot_set = set(pivots)
    nonpivots = tuple(i for i in range(rows.ncols()) if i not in pivot_set)
    reconstruction = inverse*rows.matrix_from_columns(nonpivots)

    def read(jets):
        assert jets.base_ring() == field and jets.ncols() == rows.ncols()
        entries = jets.matrix_from_columns(pivots)
        assert entries*reconstruction == jets.matrix_from_columns(nonpivots)
        return entries*inverse

    return read, {
        "complete_dimension":int(rows.nrows()),
        "complete_coefficient_count":int(rows.ncols()),
        "pivot_columns_sha256":digest(list(pivots)),
        "pivot_inverse_sha256":matrix_digest(inverse),
        "all_nonpivot_columns_checked":len(nonpivots),
        "nonpivot_reconstruction_sha256":matrix_digest(reconstruction),
        "full_basis_sha256":matrix_digest(rows),
    }


def _flat_to_polynomial_matrix(flat, recipes, operations, weights):
    polynomial_ring = operations["affine_polynomial_ring"]
    field = operations["constants"]
    T = polynomial_ring.gen()
    assert flat.ncols() == len(recipes)
    answer = matrix(polynomial_ring, flat.nrows(), 306)
    for index, coefficients in enumerate(flat.rows()):
        result = vector(polynomial_ring, 306)
        for coefficient, (basis_index, exponent) in zip(coefficients, recipes):
            if coefficient:
                result[int(basis_index)] += field(coefficient)*T**int(exponent)
        assert all(not f or int(f.degree())+int(weights[i]) <= 4
                   for i, f in enumerate(result))
        answer.set_row(index, result)
    return answer


def _infinity_coordinates(value, section_power, operations, weights):
    """The SAME section divided by J0^m, where J0=t^4 J; no division in A."""
    power = int(section_power)
    assert power >= 0
    affine = operations["affine_polynomial_ring"]
    infinity = operations["infinity_polynomial_ring"]
    T, S = affine.gen(), infinity.gen()
    value = vector(affine, value)
    assert len(value) == 306
    shift = 4*power
    result = vector(infinity, 306)
    recovered = vector(affine, 306)
    for i, polynomial in enumerate(value):
        if not polynomial:
            continue
        assert int(polynomial.degree())+int(weights[i]) <= shift
        for exponent, coefficient in enumerate(polynomial.list()):
            if coefficient:
                new_exponent = shift-int(weights[i])-exponent
                assert new_exponent >= 0
                result[i] += coefficient*S**new_exponent
        for exponent, coefficient in enumerate(result[i].list()):
            if coefficient:
                recovered[i] += coefficient*T**(shift-int(weights[i])-exponent)
    assert recovered == value
    return result


def build_original_y_section_basis(affine_context, constants=None, progress=None):
    """Full 666 by 306 matrices F_i/J and F_i/J0 in the exact chosen constants.

    Default constants are the original prime field.  A caller may supply its
    already fixed quadratic field; only affine_context.constant_extension is
    used.  This core deliberately has no dependency on the F/P map recovery.
    """
    apery = affine_context["original_apery_context"]
    original = apery["original_Y_context"]
    fp = apery["constants"]
    field = fp if constants is None else constants
    assert affine_context["constants"] is fp
    assert int(fp.degree()) == 1
    assert int(field.characteristic()) == int(fp.characteristic())
    assert int(field.degree()) in (1, 2)
    operations = affine_context["constant_extension"](field)
    assert operations["constants"] is field
    weights = tuple(int(d) for d in apery["apery_weights"])
    original_rows = apery["original_M2_rows"]
    assert original_rows.nrows() == 666 and original_rows.ncols() >= 2453
    basis_id = matrix_digest(original_rows[:, :1225])
    recipes = tuple((int(i), int(j)) for i, j in apery["monomial_recipes"][4])
    target = apery["monomial_rows"][4]
    assert target.nrows() == 666 and target.ncols() == 1225
    reader, reader_receipt = _full_coordinate_reader(target)
    precision = int(apery["q_precision"])
    ring = PowerSeriesRing(fp, "u", default_prec=precision)
    laurent = LaurentSeriesRing(fp, "u", default_prec=precision)
    u = laurent.gen()
    normalized_inverse = ring(apery["inverse_J_over_u4"])
    assert normalized_inverse.precision_absolute() >= precision
    source_jets = []
    for row in original_rows.rows():
        genuine = laurent(ring(list(row)).add_bigoh(precision)*normalized_inverse)*u**-4
        assert genuine.valuation() >= -4
        assert genuine.precision_absolute() > 1220
        source_jets.append([genuine[i] for i in range(-4, 1221)])
    source_jets = matrix(fp, source_jets)
    flat = reader(source_jets)
    assert flat.nrows() == flat.ncols() == 666 and flat.rank() == 666
    assert flat*target == source_jets
    affine_rows = _flat_to_polynomial_matrix(flat, recipes, operations, weights)
    infinity_rows = matrix(operations["infinity_polynomial_ring"], [
        _infinity_coordinates(row, 1, operations, weights) for row in affine_rows.rows()])

    # Both global frames are themselves in the same original complete M2.
    J_coordinates = apery["J_coordinates"]
    J0_series = apery["t_series"]**4*apery["J_series"]
    assert J0_series.valuation() == 0
    assert J0_series.precision_absolute() >= precision
    J0_row = matrix(fp, [[J0_series[i] for i in range(precision)]])
    J0_coordinates = original["complete_membership_reader"](J0_row).row(0)
    assert J0_coordinates*original_rows == J0_row.row(0)
    affine_ring = operations["affine_polynomial_ring"]
    infinity_ring = operations["infinity_polynomial_ring"]
    T, S = affine_ring.gen(), infinity_ring.gen()
    assert vector(affine_ring, J_coordinates)*affine_rows == operations["unit"]
    assert vector(affine_ring, J0_coordinates)*affine_rows == T**4*operations["unit"]
    assert vector(infinity_ring, J0_coordinates)*infinity_rows == operations["infinity_unit"]
    assert vector(infinity_ring, J_coordinates)*infinity_rows == S**4*operations["infinity_unit"]

    def y_section_coordinates(coefficients):
        coefficients = vector(affine_ring, [field(c) for c in coefficients])
        assert len(coefficients) == 666
        return coefficients*affine_rows

    receipt = {
        "kind":"rank2_original_Y_complete_M2_ring_embedding",
        "status":"all_666_original_sections_in_both_actual_charts",
        "prime":int(fp.characteristic()), "constant_degree":int(field.degree()),
        "exact_original_affine_constant_extension_api":True,
        "original_Y_M2_coordinate_basis_id":basis_id,
        "complete_original_Y_M2_dimension":666,
        "complete_W4_window_inclusive":[-4, 1220],
        "complete_W4_coefficient_count":1225,
        "complete_W4_reader":reader_receipt,
        "actual_full_change_of_basis_rank":666,
        "full_original_M2_over_J_jets_sha256":matrix_digest(source_jets),
        "full_original_M2_flat_coordinates_sha256":matrix_digest(flat),
        "original_Y_M2_affine_coordinates_sha256":polynomial_matrix_digest(affine_rows),
        "original_Y_M2_infinity_coordinates_sha256":polynomial_matrix_digest(infinity_rows),
        "original_J_coordinates_sha256":vector_digest(J_coordinates),
        "original_J0_coordinates_sha256":vector_digest(J0_coordinates),
        "J0_same_complete_M2_membership_coefficients":precision,
        "both_original_frame_units_verified":True,
        "infinity_section_formula":"F_i/J0; J0=ys^4*J; same shift 4",
        "helper_sha256":hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
    }
    context = {
        "kind":"rank2_original_Y_complete_M2_ring_embedding_context",
        "constants":field, "original_fp":fp, "operations":operations,
        "original_affine_context":affine_context,
        "original_Y_context":original,
        "basis_id":basis_id,
        "coordinate_basis_id":basis_id,
        "original_Y_M2_coordinate_basis_id":basis_id,
        "original_Y_M2_flat_coordinates":flat,
        "original_Y_M2_affine_coordinates":affine_rows,
        "original_Y_M2_infinity_coordinates":infinity_rows,
        "original_J_coordinates":J_coordinates,
        "original_J0_coordinates":J0_coordinates,
        "section_from_Y_coordinates":y_section_coordinates,
        "section_infinity_coordinates":lambda value, power: _infinity_coordinates(
            value, power, operations, weights),
        "certificate":receipt,
    }
    _progress(progress, "all original Y M2 sections embedded in both charts",
              dimension=666, module_rank=306, constant_degree=int(field.degree()),
              original_basis_id=basis_id)
    return context, receipt


def _authenticate_same_base(original_y, maps):
    """Check the genuine rational basis, the exact saturation and all common jets."""
    base = original_y["original_base_context"]
    other = maps["original_r917_context"]
    fp = base["constants"]
    assert int(fp.degree()) == 1 and other["constants"] is fp
    assert int(base["prime"]) == int(other["prime"]) == int(maps["prime"])
    q1, q2 = int(base["q_precision"]), int(other["q_precision"])
    common = min(q1, q2)
    assert common >= 205
    raw1 = matrix(QQ, [row[:205] for row in base["rational_source_owner"].columns])
    raw2 = matrix(QQ, [row[:205] for row in other["rational_source_owner"].columns])
    assert raw1.nrows() == 120 and raw1.ncols() == 205
    assert raw1 == raw2
    change1, change2 = base["rational_basis_transform"], other["rational_basis_transform"]
    assert change1.nrows() == change1.ncols() == 120 and change1 == change2
    rows1, rows2 = base["global_modular_form_jets"], other["global_modular_form_jets"]
    assert rows1[:, :common] == rows2[:, :common]
    assert base["original_rr_jets"][:, :common] == other["original_rr_jets"][:, :common]
    S1, S2 = base["original_denominator_q_series"], other["original_denominator_q_series"]
    assert all(S1[i] == S2[i] for i in range(common))
    field = maps["constants"]
    assert all(field(S1[i]) == maps["original_S_series"][i] for i in range(common))
    return base, {
        "same_genuine_R917_M2_basis":True,
        "same_exact_QQ_205_prefix":True,
        "same_exact_saturation_transform":True,
        "same_full_common_modular_and_RR_jets":common,
        "same_original_S_on_all_common_coefficients":True,
        "original_M2_basis_id":matrix_digest(rows1[:, :205]),
        "exact_QQ_205_input_sha256":digest([[str(c) for c in row] for row in raw1.rows()]),
        "exact_QQ_saturation_transform_sha256":digest([[str(c) for c in row] for row in change1.rows()]),
        "full_common_reduced_M2_sha256":matrix_digest(rows1[:, :common]),
    }


def build_original_section_ring_embedding(affine_context, map_sections_context,
                                          progress=None, with_map_fractions=True):
    """Embed original products and F/P same-degree fractions for j=1,2,4.

    context.section_coordinates(power, recipes, coefficients, j) returns the
    actual pulled-back section divided by J^power.  Every recipe is a tuple
    of indices of the SAME original 120-dimensional M2 basis.  The j^power
    logarithmic differential multiplier is already included and never dropped.
    """
    maps = map_sections_context
    assert maps["kind"] == "rank2_original_map_section_fractions_context"
    field, local = maps["constants"], maps["local_context"]
    fp = affine_context["constants"]
    prime = int(fp.characteristic())
    assert field is local["constants"]
    assert int(field.characteristic()) == prime and int(field.degree()) == 2
    omega = maps["original_omega"]
    assert omega.parent() is field and omega == local["omega"]
    assert omega != 1 and omega**2+omega+1 == 0
    assert tuple(maps["sigma_a_index"]) == tuple(local["sigma_a_index"])
    original_y = affine_context["original_apery_context"]["original_Y_context"]
    base, source_receipt = _authenticate_same_base(original_y, maps)
    core, core_receipt = build_original_y_section_basis(affine_context, field, progress)
    operations = core["operations"]
    polynomial_ring = operations["affine_polynomial_ring"]
    weights = tuple(int(d) for d in affine_context["basis_weights"])
    flat = core["original_Y_M2_flat_coordinates"]
    recipes4 = affine_context["original_apery_context"]["monomial_recipes"][4]
    original_rows = original_y["global_modular_form_jets"]
    base_rows = base["global_modular_form_jets"]
    base_S_coordinates = original_y["original_base_S_coordinates"]
    pulls, S_pullbacks, pull_records = {}, {}, []
    for j in (1, 2, 4):
        item = original_y["degeneracy_maps"][j]
        assert int(item["differential_multiplier"]) == j
        coordinates = item["full_M2_pullback_coordinates"]
        assert coordinates.nrows() == 120 and coordinates.ncols() == 666
        faithful_pullback = matrix(fp, 120, 1225, lambda i, n:
            fp(j)*base_rows[i, n//j] if n % j == 0 else fp.zero())
        assert item["full_M2_pullback_jets"][:, :1225] == faithful_pullback
        assert coordinates*original_rows[:, :1225] == faithful_pullback
        pull_flat = coordinates*flat
        pulls[j] = _flat_to_polynomial_matrix(pull_flat, recipes4, operations, weights)
        S_coordinates = item["pulled_S_coordinates"]
        assert base_S_coordinates*coordinates == S_coordinates
        S_pullbacks[j] = vector(polynomial_ring, base_S_coordinates)*pulls[j]
        assert S_pullbacks[j] == core["section_from_Y_coordinates"](S_coordinates)
        assert not S_pullbacks[j].is_zero()
        pull_records.append({
            "degeneracy_exponent":j,
            "actual_original_M2_rows":120,
            "logarithmic_differential_multiplier":j,
            "complete_M2_membership_window_inclusive":[0, 1224],
            "same_original_basis_with_all_multiplier_factors":True,
            "actual_Y_coordinates_sha256":matrix_digest(coordinates),
            "actual_pulled_jets_sha256":matrix_digest(faithful_pullback),
            "actual_pulled_section_over_J_sha256":polynomial_matrix_digest(pulls[j]),
            "actual_pulled_S_over_J_sha256":polynomial_vector_digest(S_pullbacks[j]),
        })
    assert S_pullbacks[2] == core["section_from_Y_coordinates"](
        original_y["degeneracy_maps"][2]["pulled_S_coordinates"])

    multiplier_cache, conversion_records = {}, []

    def scalar(coefficient):
        if hasattr(coefficient, "parent"):
            parent = coefficient.parent()
            if hasattr(parent, "characteristic") and int(parent.characteristic()) == prime:
                if int(parent.cardinality()) == prime**2:
                    assert parent is field, "A different quadratic presentation is not the original constants."
                else:
                    assert int(parent.cardinality()) == prime
        return field(coefficient)

    def checked_weight(value, bound):
        assert len(value) == 306 and value.base_ring() is polynomial_ring
        assert all(not p or int(p.degree())+weights[i] <= int(bound)
                   for i, p in enumerate(value))
        return value

    def basis_multiplier(j, index):
        key = (int(j), int(index))
        if key not in multiplier_cache:
            multiplier_cache[key] = operations["multiplication_matrix"](pulls[j].row(index))
            assert operations["unit"]*multiplier_cache[key] == pulls[j].row(index)
            _progress(progress, "original section multiplier retained",
                      degeneracy_exponent=int(j), original_M2_index=int(index))
        return multiplier_cache[key]

    def horner(power, terms, j):
        if not terms:
            return vector(polynomial_ring, 306)
        if power == 0:
            assert all(recipe == () for recipe in terms)
            return sum(terms.values(), field.zero())*operations["unit"]
        if power == 1:
            result = vector(polynomial_ring, 306)
            for recipe, coefficient in terms.items():
                assert len(recipe) == 1
                result += coefficient*pulls[j].row(recipe[0])
            return checked_weight(result, 4)
        groups = {}
        for recipe, coefficient in terms.items():
            head, tail = recipe[0], recipe[1:]
            group = groups.setdefault(head, {})
            group[tail] = group.get(tail, field.zero())+coefficient
        result = vector(polynomial_ring, 306)
        for head in sorted(groups):
            tail_value = horner(power-1, groups[head], j)
            if not tail_value.is_zero():
                result += tail_value*basis_multiplier(j, head)
        return checked_weight(result, 4*power)

    def section_coordinates(power, recipes, coefficients, j):
        power, j = int(power), int(j)
        assert power >= 0 and j in (1, 2, 4)
        recipes = tuple(tuple(int(i) for i in recipe) for recipe in recipes)
        coefficients = tuple(scalar(c) for c in coefficients)
        assert len(recipes) == len(coefficients)
        assert all(len(recipe) == power and all(0 <= i < 120 for i in recipe)
                   for recipe in recipes)
        terms = {}
        for recipe, coefficient in zip(recipes, coefficients):
            if coefficient:
                recipe = tuple(sorted(recipe))
                terms[recipe] = terms.get(recipe, field.zero())+coefficient
        terms = {recipe:c for recipe, c in terms.items() if c}
        answer = checked_weight(horner(power, terms, j), 4*power)
        record = {
            "section_power":power, "degeneracy_exponent":j,
            "actual_recipe_count":len(recipes), "nonzero_merged_terms":len(terms),
            "differential_multiplier_before_reduction":j**power,
            "actual_global_expression":"pi_j^*(sum c_recipe product f_i) / J^power",
            "same_original_120_M2_basis_authenticated":True,
            "complete_original_multiplication_used":True,
            "polynomial_weight_bound_checked":4*power,
            "recipes_sha256":digest([list(recipe) for recipe in recipes]),
            "coefficients_in_original_field_sha256":digest([
                finite_coordinates(c, field) for c in coefficients]),
            "actual_normalization_coordinates_sha256":polynomial_vector_digest(answer),
        }
        conversion_records.append(record)
        _progress(progress, "actual original homogeneous section embedded",
                  section_power=power, degeneracy_exponent=j,
                  original_recipe_count=len(recipes), same_differential_multiplier=j**power)
        return answer

    def same_degree_fraction(numerator, denominator, power, label=None):
        power = int(power)
        numerator = checked_weight(vector(polynomial_ring, numerator), 4*power)
        denominator = checked_weight(vector(polynomial_ring, denominator), 4*power)
        assert not numerator.is_zero() and not denominator.is_zero()
        infinity_numerator = _infinity_coordinates(numerator, power, operations, weights)
        infinity_denominator = _infinity_coordinates(denominator, power, operations, weights)
        record = {
            "label":label, "same_section_power":power,
            "common_infinity_shift":4*power,
            "same_original_fraction_on_both_charts":True,
            "numerator_nonzero":True, "denominator_nonzero":True,
            "function_field_inverse_used":False,
            "numerator_sha256":polynomial_vector_digest(numerator),
            "denominator_sha256":polynomial_vector_digest(denominator),
            "infinity_numerator_sha256":polynomial_vector_digest(infinity_numerator),
            "infinity_denominator_sha256":polynomial_vector_digest(infinity_denominator),
        }
        return {
            "numerator":numerator, "denominator":denominator,
            "infinity_numerator":infinity_numerator,
            "infinity_denominator":infinity_denominator,
            "section_power":power, "common_infinity_shift":4*power,
            "certificate":record,
        }

    def coefficient_frobenius(value):
        return vector(polynomial_ring, [
            polynomial_ring([c**prime for c in p.list()]) for p in value])

    F, P, fraction_records = {}, {i:{} for i in (0, 1, 2)}, []
    if with_map_fractions:
        actual_recipes = maps["complete_RR_product_recipes"]
        for j in (1, 2, 4):
            first = maps["F"]
            a, b = int(first["numerator_power"]), int(first["denominator_recipe_power"])
            assert int(first["denominator_S_power"]) == 3 and a == b+3
            numerator = section_coordinates(a, actual_recipes[a], first["numerator_coordinates"], j)
            denominator = section_coordinates(b, actual_recipes[b], first["denominator_recipe_coordinates"], j)
            # This exact S^3 is part of the ORIGINAL same-degree denominator.
            # It is not canceled using residues or norms at its zero divisor.
            M_S = operations["multiplication_matrix"](S_pullbacks[j])
            assert operations["unit"]*M_S == S_pullbacks[j]
            for power in range(1, 4):
                denominator = checked_weight(denominator*M_S, 4*(b+power))
                assert not denominator.is_zero()
            F[j] = same_degree_fraction(numerator, denominator, a, "original v_F; pi_%d" % j)
            F[j]["certificate"].update({
                "original_fraction":"A_F/(B_F*S^3)",
                "denominator_recipe_power":b, "explicit_original_S_power":3,
                "differential_factor_numerator_and_denominator":j**a,
            })
            fraction_records.append(F[j]["certificate"])
            for index in (0, 1):
                item = maps["P"][index]
                power = int(item["section_power"])
                numerator = section_coordinates(power, actual_recipes[power], item["numerator_coordinates"], j)
                denominator = section_coordinates(power, actual_recipes[power], item["denominator_coordinates"], j)
                P[index][j] = same_degree_fraction(
                    numerator, denominator, power, "original Y_%d; pi_%d" % (index, j))
                P[index][j]["certificate"].update({
                    "original_embedding":index, "degeneracy_exponent":j,
                    "same_original_S_power_cancels_only_in_ratio":power,
                    "differential_factor_both_sides":j**power,
                })
                fraction_records.append(P[index][j]["certificate"])
            # The original third embedding is exact CONSTANT conjugation of
            # the second.  The original Artin permutation is kept separately.
            for key in ("numerator_coordinates", "denominator_coordinates"):
                assert tuple(maps["P"][2][key]) == tuple(c**prime for c in maps["P"][1][key])
            power = int(maps["P"][2]["section_power"])
            assert power == int(maps["P"][1]["section_power"])
            P[2][j] = same_degree_fraction(
                coefficient_frobenius(P[1][j]["numerator"]),
                coefficient_frobenius(P[1][j]["denominator"]),
                power, "original Y_2; pi_%d" % j)
            P[2][j]["certificate"].update({
                "original_embedding":2, "degeneracy_exponent":j,
                "source":"constant Frobenius of original embedding 1 on the fixed Fp structure constants",
                "same_original_P2_section_coefficients_verified":True,
                "original_Artin_operator_unchanged":True,
            })
            fraction_records.append(P[2][j]["certificate"])

    receipt = {
        "kind":"rank2_original_section_ring_embedding",
        "status":"same_original_sections_and_requested_map_fractions_in_both_charts",
        "prime":prime, "constant_degree":2,
        "exact_local_constant_field_reused":True,
        "original_omega_coordinates":finite_coordinates(omega, field),
        "original_constant_modulus":"omega^2+omega+1",
        "original_sigma_a_index":[int(i) for i in maps["sigma_a_index"]],
        "same_original_base_source":source_receipt,
        "complete_Y_section_embedding":core_receipt,
        "three_actual_degeneracies":pull_records,
        "generic_section_conversions":conversion_records,
        "original_map_fraction_records":fraction_records,
        "F_and_P_fractions_built":bool(with_map_fractions),
        "original_cube_roots_claimed":False,
        "original_complete_divisors_claimed":False,
        "original_shadow_claimed":False,
        "first_authenticated_source":maps["first_certificate"]["source"],
        "first_authenticated_run":maps["first_certificate"]["run_id"],
        "packet_authenticated_source":maps["packet_certificate"]["source"],
        "packet_authenticated_run":maps["packet_certificate"]["run_id"],
        "helper_sha256":hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
    }
    context = {
        "kind":"rank2_original_section_ring_embedding_context",
        "constants":field, "original_fp":fp, "original_omega":omega,
        "sigma_a_index":tuple(maps["sigma_a_index"]),
        "operations":operations,
        "section_basis_context":core,
        "basis_id":core["coordinate_basis_id"],
        "coordinate_basis_id":core["coordinate_basis_id"],
        "original_Y_M2_coordinate_basis_id":core["coordinate_basis_id"],
        "original_Y_M2_affine_coordinates":core["original_Y_M2_affine_coordinates"],
        "original_Y_M2_infinity_coordinates":core["original_Y_M2_infinity_coordinates"],
        "original_map_sections_context":maps,
        "original_affine_context":affine_context,
        "base_M2_pullback_coordinates":pulls,
        "original_S_pullback_coordinates":S_pullbacks,
        "original_SY_coordinates":S_pullbacks[2],
        "rho_fraction_pairs":{j:(S_pullbacks[j], S_pullbacks[2]) for j in (1, 2, 4)},
        "section_coordinates":section_coordinates,
        "same_degree_fraction":same_degree_fraction,
        "section_infinity_coordinates":core["section_infinity_coordinates"],
        "section_from_Y_coordinates":core["section_from_Y_coordinates"],
        "F":F, "P":P,
        "actual_multiplier_cache":multiplier_cache,
        "conversion_records":conversion_records,
        "certificate":receipt,
    }
    _progress(progress, "original section and map embedding complete",
              actual_degeneracies=3, original_quadratic_constants=True,
              original_fraction_count=len(fraction_records))
    return context, receipt
