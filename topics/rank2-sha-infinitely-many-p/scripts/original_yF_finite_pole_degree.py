"""Read R927's two finite invariants in the SAME original reduction at 29.

Inputs are the in-process outputs of the complete original cube, DS and six
cusp builders.  The cube builder's actual returned receipt is mandatory:
its same-process mixed F kernel supplies the proved degree 180 premise.
The old full RF R6 kernel, not a selected or compact fraction, is consumed.

All 900 denominators are restricted to every actual DS residue factor.  The
restriction image is an ideal by R927's H1-vanishing argument; its equality
with the full product ideal is ALSO checked in exact original coordinates.
At the unique length-289 infinity component, the same kernel and same pi2
section pullback give the complete original RF value in the true local ring.
Only ranks, source records, finite readings and hashes leave the process.
"""
import os
if (os.environ.get("GITHUB_ACTIONS") != "true" or
        os.environ.get("GITHUB_REPOSITORY") != "Rogerhu12/math-research-public"):
    raise SystemExit("Run this mathematical helper only in public research Actions.")
if any(os.environ.get(key) for key in ("GH_TOKEN", "GITHUB_TOKEN", "RANK2_GITHUB_TOKEN")):
    raise SystemExit("Keep repository tokens on the host outside Sage.")

import hashlib
from pathlib import Path
from sage.all import QQ, PolynomialRing, identity_matrix, matrix, vector
import original_section_ring_embedding
import section_quotient_algebra
from section_quotient_algebra import digest, matrix_digest, vector_digest


SOURCE_DEPENDENCIES = (
    "original_yF_finite_pole_degree.py",
    "original_section_ring_embedding.py",
    "section_quotient_algebra.py",
)


def source_dependencies():
    """Direct source files; each upstream builder records its own full inputs."""
    return (Path(__file__), Path(original_section_ring_embedding.__file__),
            Path(section_quotient_algebra.__file__))


def _progress(callback, stage, **record):
    if callback is not None:
        callback(stage, **record)


def _same_base(first, second):
    """Exact source/basis identity; a digest is never used instead of equality."""
    fp = first["constants"]
    assert second["constants"] is fp and int(fp.cardinality()) == 29
    assert int(first["prime"]) == int(second["prime"]) == 29
    raw1 = matrix(QQ, [row[:205] for row in first["rational_source_owner"].columns])
    raw2 = matrix(QQ, [row[:205] for row in second["rational_source_owner"].columns])
    assert raw1.nrows() == 120 and raw1.ncols() == 205 and raw1 == raw2
    transform1, transform2 = (first["rational_basis_transform"],
                              second["rational_basis_transform"])
    assert transform1.nrows() == transform1.ncols() == 120
    assert transform1 == transform2
    common = min(int(first["q_precision"]), int(second["q_precision"]))
    assert common >= 409
    rows1, rows2 = (first["global_modular_form_jets"],
                    second["global_modular_form_jets"])
    assert rows1[:, :common] == rows2[:, :common]
    assert first["original_rr_jets"][:, :common] == second["original_rr_jets"][:, :common]
    assert all(first["original_denominator_q_series"][i] ==
               second["original_denominator_q_series"][i] for i in range(common))
    return {
        "same_exact_QQ_205_basis":True, "same_exact_saturation_transform":True,
        "all_common_modular_RR_and_S_coefficients_checked":common,
        "original_M2_basis_id":matrix_digest(rows1[:, :205]),
        "exact_QQ_205_basis_sha256":digest([[str(c) for c in row] for row in raw1.rows()]),
        "exact_saturation_transform_sha256":digest(
            [[str(c) for c in row] for row in transform1.rows()]),
        "all_common_modular_coefficients_sha256":matrix_digest(rows1[:, :common]),
    }


def _prime_coordinate_serial(coefficients, fp, field):
    """The existing row_serial convention, after actual descent to original Fp."""
    result = []
    for value in coefficients:
        coefficients_in_original_generator = value.polynomial().list()
        assert all(not c for c in coefficients_in_original_generator[1:])
        actual = (fp(coefficients_in_original_generator[0])
                  if coefficients_in_original_generator else fp.zero())
        assert field(actual) == value
        result.append([] if not actual else [int(actual)])
    return result


def _authenticate(cube, ds, cusps, cube_receipt):
    assert cube["kind"] == "rank2_original_cube_section_fractions_context"
    assert int(cube["prime"]) == 29
    fp, field = cube["original_fp"], cube["constants"]
    assert int(fp.cardinality()) == 29 and int(field.cardinality()) == 29**2
    assert ds["constants"] is cusps["constants"] is fp
    assert cube["original_omega_codec"].fp is fp
    assert cube["original_omega_codec"].field is field
    omega = cube["original_omega"]
    assert cube["original_omega_codec"].omega == omega
    assert omega**2+omega+1 == 0 and omega**29 != omega
    maps = cube["map_context"]
    assert cube["original_map_sections_context"] is maps
    assert maps["constants"] is field and maps["original_fp"] is fp
    assert cube["original_r917_context"] is maps["original_r917_context"]
    assert maps["original_omega"] == omega
    assert cube_receipt["kind"] == "rank2_original_cube_section_fractions"
    assert int(cube_receipt["prime"]) == 29
    map_receipt = cube_receipt["same_authenticated_F_and_P_source"]
    assert map_receipt["kind"] == "rank2_original_map_section_fractions"
    assert int(map_receipt["prime"]) == 29
    assert map_receipt["first_original_source"] == maps["first_certificate"]["source"]
    assert map_receipt["first_original_run"] == maps["first_certificate"]["run_id"]
    assert map_receipt["packet_original_source"] == maps["packet_certificate"]["source"]
    assert map_receipt["packet_original_run"] == maps["packet_certificate"]["run_id"]
    mixed = map_receipt["F"]
    assert int(mixed["weight"]) == 4 and int(mixed["last_index"]) == 1428
    assert int(mixed["nullity"]) == 144 and int(mixed["rank"]) == 1116
    assert mixed["same_original_ratio_identified_by_R881"] is True
    assert (int(mixed["numerator_section_power"]),
            int(mixed["denominator_recipe_section_power"]),
            int(mixed["denominator_S_power"])) == (5, 2, 3)
    for key, hash_key in (("numerator_coordinates", "numerator_coordinates_sha256"),
                          ("denominator_recipe_coordinates", "denominator_recipe_coordinates_sha256")):
        assert digest(_prime_coordinate_serial(maps["F"][key], fp, field)) == mixed[hash_key]
    # This is R927's exact RR calculation from the actual whole mixed kernel.
    assert 144 > 85
    residual_vF_degree = 2*204+1-85-int(mixed["nullity"])
    assert residual_vF_degree == 180

    RF = cube["RF"]
    assert int(RF["section_power"]) == 6 and RF["original_coordinate"] == "RF"
    kernel = RF["full_kernel_coordinates"]
    assert kernel.base_ring() is fp and kernel.nrows() == 900 and kernel.ncols() == 2280
    record = RF["certificate"]
    assert record == cube_receipt["original_RF_complete_low_kernel"]
    assert int(record["same_complete_section_dimension"]) == 1140
    assert int(record["actual_complete_kernel_dimension"]) == 900
    assert record["full_low_window_inclusive"] == [0, 2312]
    assert record["both_entire_kernel_projections_injective"] is True
    assert record["all_original_equations_returned"] is True
    assert matrix_digest(kernel) == record["entire_kernel_real_component_sha256"]
    assert matrix_digest(matrix(fp, 900, 2280)) == record["entire_kernel_omega_component_sha256"]
    identity = RF["complete_global_identity"]
    assert identity == cube_receipt["original_RF_full_global_cube_identity"]
    assert identity["original_global_identity_certified"] is True
    assert identity["full_original_BF_S_cubed_retained"] is True
    assert identity["all_coefficients_zero"] is True
    assert identity["full_checked_regular_coefficients_inclusive"] == [0, 6940]
    assert int(identity["complete_global_zero_degree_bound"]) == 6936
    assert 900 > 85
    RF_pole_degree = 6*204+1-85-int(kernel.nrows())
    assert RF_pole_degree == 240
    recipes = tuple(tuple(int(i) for i in row) for row in cube["complete_product_recipes"][6])
    assert len(recipes) == len(set(recipes)) == 1140
    assert all(len(row) == 6 and all(0 <= i < 120 for i in row) for row in recipes)
    r6_receipt = cube_receipt["complete_R6_source"]
    assert r6_receipt["same_genuine_original_M2_products"] is True
    assert int(r6_receipt["actual_complete_dimension"]) == 1140
    assert int(r6_receipt["complete_Sturm_coefficients"]) == 1225
    assert digest(recipes) == r6_receipt["new_recipes_sha256"]
    assert digest(cube["complete_product_recipes"]) == cube_receipt["complete_product_recipes_sha256"]
    base = cube["original_r917_context"]
    high = cube["extended_original_M2_rows"]
    common = int(base["q_precision"])
    assert high.nrows() == 120 and high.ncols() >= 6941
    assert high[:, :common] == base["global_modular_form_jets"][:, :common]
    ds_auth = _same_base(ds["original_r917_context"], base)
    assert ds["original_point_labels"]["coordinate_basis_id"] == ds_auth["original_M2_basis_id"]

    affine, core = cusps["original_normalization_context"], cusps["original_section_context"]
    assert core["original_affine_context"] is affine
    assert affine["constants"] is core["constants"] is core["original_fp"] is fp
    original_y = affine["original_apery_context"]["original_Y_context"]
    assert core["original_Y_context"] is original_y
    _, y_auth = original_section_ring_embedding._authenticate_same_base(original_y, maps)
    assert core["basis_id"] == matrix_digest(original_y["global_modular_form_jets"][:, :1225])
    assert core["certificate"]["both_original_frame_units_verified"] is True
    cusp_receipt = cusps["certificate"]
    assert cusp_receipt["kind"] == "rank2_original_Y_six_complete_cusp_fibers"
    assert int(cusp_receipt["actual_total_scheme_length"]) == 1836
    assert int(cusp_receipt["actual_total_geometric_cusp_count"]) == 108
    assert int(cusp_receipt["actual_prime_field_closed_point_count"]) == 18
    assert int(cusp_receipt["actual_heavy_nilpotence_index"]) == 289
    assert set(cusps["fibers"]) == {"0", "1", "-1", "3", "-3", "infinity"}
    assert cusp_receipt["original_Y_M2_coordinate_basis_id"] == core["basis_id"]
    assert cusp_receipt["original_full_normalization_signature_sha256"] == affine["certificate"][
        "exact_multiplication_signature_sha256"]
    return fp, recipes, kernel, {
        "same_process_cube_receipt_sha256":digest(cube_receipt),
        "same_process_mixed_F_kernel_receipt_sha256":digest(mixed),
        "actual_mixed_F_kernel_dimension":144,
        "actual_RF_complete_kernel_dimension":900,
        "actual_RF_complete_kernel_sha256":matrix_digest(kernel),
        "degree_D_prime_from_RR":residual_vF_degree,
        "degree_RF_poles_from_RR":RF_pole_degree,
        "RR_premise":"R927: h0>genus kills H1 for the complete projected section space",
        "original_cube_global_identity_sha256":digest(identity),
        "same_original_DS_source":ds_auth, "same_original_Y_source":y_auth,
        "original_Y_M2_basis_id":core["basis_id"],
        "original_normalization_signature_sha256":affine["certificate"][
            "exact_multiplication_signature_sha256"],
        "all_six_original_cusp_fibers_receipt_sha256":digest(cusp_receipt),
        "original_omega_retained_without_new_field_or_root":True,
        "original_omega_coordinates":[int(c) for c in omega.polynomial().list()],
        "first_authenticated_source":maps["first_certificate"]["source"],
        "first_authenticated_run":maps["first_certificate"]["run_id"],
        "packet_authenticated_source":maps["packet_certificate"]["source"],
        "packet_authenticated_run":maps["packet_certificate"]["run_id"],
    }


def _ds_residue_codec(ds, progress):
    """An actual product coordinate isomorphism, returned to all 204 columns."""
    fp = ds["constants"]
    assert int(ds["dimension"]) == 204
    F = ds["frobenius_context"]["frobenius_matrix"]
    P = F**2
    assert F**3 == F and P**2 == P and P.rank() == 102
    components = ds["frobenius_context"]["decomposition"]["components"]
    labels = ds["original_point_labels"]["components"]
    assert len(components) == len(labels) == 51
    pieces, bases, quadratic, records = [], [], [], []
    projector_sum = matrix(fp, 204, 204)
    for i, component in enumerate(components):
        assert int(component["ambient_dimension"]) == 4
        assert int(component["residue_degree"]) == 2
        e, alpha = component["idempotent"], component["residue_generator"]
        R, M = component["residue_power_basis"], component["projector_matrix"]
        assert R.nrows() == 2 and R.ncols() == 204
        assert R.row(0) == e and R.row(1) == alpha and R*P == R and R*M == R
        polynomial = component["residue_polynomial"]
        assert polynomial.degree() == 2 and polynomial[2] == 1
        c0, c1 = fp(polynomial[0]), fp(polynomial[1])
        assert ds["multiply"](alpha, alpha) == -c0*e-c1*alpha
        pivots = tuple(R.pivots())
        assert len(pivots) == 2
        inverse = R.matrix_from_columns(pivots).inverse()
        projected = P*M
        C = projected.matrix_from_columns(pivots)*inverse
        assert C*R == projected
        pieces.append(C)
        bases.extend(R.rows())
        quadratic.append((int(c0), int(c1)))
        projector_sum += M
        records.append({"component_index":i, "residue_degree":2,
                        "point_id":labels[i]["point_id"],
                        "residue_polynomial_ascending":[int(c0), int(c1), 1],
                        "actual_power_basis_sha256":matrix_digest(R),
                        "actual_residue_projection_sha256":matrix_digest(C),
                        "all_204_return_coordinates_verified":True})
    assert projector_sum == identity_matrix(fp, 204)
    C = pieces[0]
    for piece in pieces[1:]:
        C = C.augment(piece)
    R = matrix(fp, bases)
    assert C.nrows() == 204 and C.ncols() == 102
    assert R*C == identity_matrix(fp, 102) and C*R == P
    unit = vector(fp, [a for _ in range(51) for a in (1, 0)])
    assert ds["unit"]*C == unit and unit*R == ds["unit"]
    _progress(progress, "same DS complete residue product codec", original_dimension=204,
              reduced_dimension=102, all_original_degree_two_components=51)
    return {"reduction_projection":P, "to_product":C, "from_product":R,
            "quadratic_coefficients":tuple(quadratic), "unit":unit}, records


def _quad_product(left, right, quadratics):
    answer = []
    for i, (c0, c1) in enumerate(quadratics):
        a, b, c, d = left[2*i], left[2*i+1], right[2*i], right[2*i+1]
        answer.extend(((a*c-c0*b*d) % 29, (a*d+b*c-c1*b*d) % 29))
    return tuple(answer)


def _read_e(ds, recipes, kernel, progress):
    fp = ds["constants"]
    source = ds["source_quotient"]
    assert int(source["full_dimension"]) == 324
    assert int(source["quotient_dimension"]) == int(ds["dimension"]) == 204
    assert int(source["sturm"]) == 409
    assert ds["certificate"]["h_multiplier"]["unit_on_complete_divisor"] is True
    assert int(ds["certificate"]["h_multiplier"]["rank"]) == 204
    assert source["project"](matrix(fp, [list(ds["h_row"])] )).row(0) == ds["unit"]
    codec, component_records = _ds_residue_codec(ds, progress)
    rows = ds["original_r917_context"]["global_modular_form_jets"]
    pair_keys = sorted({tuple(sorted(recipe[j:j+2]))
                        for recipe in recipes for j in (0, 2, 4)})
    polynomial_ring = PolynomialRing(fp, "Q_original_DS_pairs")
    basis = [polynomial_ring(list(row[:409])) for row in rows.rows()]
    pair_values, pair_classes = {}, []
    for start in range(0, len(pair_keys), 128):
        keys = pair_keys[start:start+128]
        products = [(basis[i]*basis[j]).truncate(409) for i, j in keys]
        complete_jets = matrix(fp, [[value[n] for n in range(409)] for value in products])
        actual_classes = source["project"](complete_jets)
        reduced = actual_classes*codec["to_product"]
        assert reduced*codec["from_product"] == actual_classes*codec["reduction_projection"]
        pair_classes.extend(actual_classes.rows())
        for key, value in zip(keys, reduced.rows()):
            pair_values[key] = tuple(int(c) for c in value)
        _progress(progress, "all original R2 pair restrictions returned", completed=start+len(keys),
                  total=len(pair_keys), full_global_membership_coefficients=409)
    values = []
    for recipe in recipes:
        factors = [pair_values[tuple(sorted(recipe[j:j+2]))] for j in (0, 2, 4)]
        values.append(_quad_product(_quad_product(factors[0], factors[1],
                      codec["quadratic_coefficients"]), factors[2], codec["quadratic_coefficients"]))
    evaluation = matrix(fp, values)
    assert evaluation.nrows() == 1140 and evaluation.ncols() == 102
    denominators = kernel[:, 1140:]*evaluation
    assert denominators.nrows() == 900 and denominators.ncols() == 102
    image = denominators.row_space().basis_matrix()
    active_columns = []
    for i, record in enumerate(component_records):
        component_values = denominators[:, 2*i:2*i+2]
        rank = int(component_values.rank())
        assert rank in (0, 2)
        if rank:
            active_columns.extend((2*i, 2*i+1))
        record.update(actual_all_900_denominator_residue_rank=rank,
                      original_RF_regular=bool(rank),
                      complete_denominator_residues_sha256=matrix_digest(component_values))
    expected = identity_matrix(fp, 102).matrix_from_rows(active_columns)
    assert image == expected
    e = int(image.nrows())
    assert e == len(active_columns) and 0 <= e <= 102 and e % 2 == 0
    receipt = {
        "e":e, "definition":"degree of the original RF-regular subset of Z_ell",
        "frame":"the actual h^3 on the complete original DS",
        "actual_DS_dimension":204, "actual_reduced_dimension":102,
        "all_original_closed_components":51, "all_original_residue_degrees":2,
        "full_original_RF_denominator_rows":900, "full_original_R6_recipes":1140,
        "actual_original_R2_pair_count":len(pair_keys),
        "each_R2_pair_global_membership_coefficients":409,
        "actual_full_restriction_image_rank":e,
        "all_51_factor_images_are_zero_or_the_whole_actual_residue_field":True,
        "complete_image_equals_full_product_ideal_verified":True,
        "rank_as_ideal_basis":"R927: deg(M_R(-Z_ell))=882>168 gives full restriction surjectivity",
        "H1_vanishing_degree":882, "canonical_degree":168,
        "actual_reduction_projection_sha256":matrix_digest(codec["reduction_projection"]),
        "actual_product_codec_sha256":matrix_digest(codec["to_product"]),
        "actual_product_return_sha256":matrix_digest(codec["from_product"]),
        "original_R2_pair_classes_sha256":matrix_digest(matrix(fp, pair_classes)),
        "all_original_R6_reduced_values_sha256":matrix_digest(evaluation),
        "all_900_denominator_reduced_values_sha256":matrix_digest(denominators),
        "complete_regular_support_ideal_basis_sha256":matrix_digest(image),
        "all_closed_components":component_records,
        "R6_nonreduced_values_computed":False,
        "actual_reduced_values_returned_to_complete_204_coordinate_algebra":True,
    }
    _progress(progress, "original e completely read", e=e, active_closed_components=e//2,
              all_denominator_rows=900, full_ideal_equality=True)
    return {"e":e, "residue_codec":codec, "R6_reduced_values":evaluation,
            "full_denominator_reduced_values":denominators,
            "regular_support_ideal_basis":image}, receipt


def _unit_inverse_truncated(value, length, progress):
    ring = value.parent()
    assert value[0]
    inverse = ring(1/value[0])
    precision = 1
    records = []
    while precision < length:
        precision = min(2*precision, length)
        inverse = (inverse*(2-value*inverse)).truncate(precision)
        assert (value*inverse).truncate(precision) == ring.one()
        records.append(precision)
        _progress(progress, "same heavy cusp denominator unit inverse", checked_coefficients=precision)
    assert (value*inverse).truncate(length) == ring.one()
    return inverse, records


def _read_z(cusps, recipes, kernel, progress):
    fp = cusps["constants"]
    core = cusps["original_section_context"]
    original_y = core["original_Y_context"]
    fiber = cusps["fibers"]["infinity"]
    algebra, frobenius = fiber["algebra"], fiber["frobenius"]
    assert algebra["constants"] is fp and int(algebra["dimension"]) == 306
    assert algebra["fiber"] == "infinity" and algebra["infinity_chart"] is True
    assert algebra["specialization_value"] == 0
    assert int(frobenius["reduction_projection_power"]) == 16
    components = frobenius["decomposition"]["components"]
    assert sorted((int(c["ambient_dimension"]), int(c["residue_degree"]))
                  for c in components) == [(1, 1), (16, 16), (289, 1)]
    heavy_indices = [i for i, c in enumerate(components) if int(c["ambient_dimension"]) == 289]
    assert len(heavy_indices) == 1
    index = heavy_indices[0]
    heavy = components[index]
    e, projector = heavy["idempotent"], heavy["projector_matrix"]
    power_basis = heavy["complete_local_power_basis"]
    parameter = heavy["nilradical_generator"]
    assert power_basis.nrows() == 289 and power_basis.ncols() == 306
    assert power_basis.row(0) == e and power_basis.row(1) == parameter
    assert power_basis*projector == power_basis
    M_parameter = algebra["multiplication_matrix"](parameter)
    shifted = matrix(fp, list(power_basis.rows()[1:])+[vector(fp, 306)])
    assert power_basis*M_parameter == shifted
    pivots = tuple(power_basis.pivots())
    assert len(pivots) == 289
    inverse = power_basis.matrix_from_columns(pivots).inverse()
    assert power_basis.matrix_from_columns(pivots)*inverse == identity_matrix(fp, 289)
    assert not power_basis.row(288).is_zero()

    labels = fiber["original_point_labels"]
    assert labels["coordinate_basis_id"] == core["basis_id"]
    full_Y_values = labels["all_original_Y_M2_fiber_values"]
    assert full_Y_values.nrows() == 666 and full_Y_values.ncols() == 306
    actual_specialized = matrix(fp, [[value(fp.zero()) for value in row]
                                     for row in core["original_Y_M2_infinity_coordinates"].rows()])
    assert full_Y_values == actual_specialized
    assert vector(fp, core["original_J0_coordinates"])*full_Y_values == algebra["unit"]
    assert labels["components"][index]["full_component_coordinate_rows"] == full_Y_values*projector
    point_id = labels["components"][index]["point_id"]

    pull = original_y["degeneracy_maps"][2]
    assert int(pull["differential_multiplier"]) == 2
    coordinates = pull["full_M2_pullback_coordinates"]
    assert coordinates.nrows() == 120 and coordinates.ncols() == 666
    base_rows = original_y["original_base_context"]["global_modular_form_jets"]
    faithful = matrix(fp, 120, 1225,
                      lambda i, n: fp(2)*base_rows[i, n//2] if n % 2 == 0 else fp.zero())
    assert coordinates*original_y["global_modular_form_jets"][:, :1225] == faithful
    assert pull["full_M2_pullback_jets"][:, :1225] == faithful
    pulled_values = coordinates*full_Y_values
    local_values = pulled_values*projector
    local_coordinates = local_values.matrix_from_columns(pivots)*inverse
    assert local_coordinates*power_basis == local_values
    assert local_coordinates.nrows() == 120 and local_coordinates.ncols() == 289
    ring = PolynomialRing(fp, "nu_original_heavy_infinity")
    section_values = [ring(list(row)) for row in local_coordinates.rows()]
    cache = {():ring.one()}

    def product(recipe):
        if recipe not in cache:
            cache[recipe] = (product(recipe[:-1])*section_values[recipe[-1]]).truncate(289)
        return cache[recipe]

    values = []
    for i, recipe in enumerate(recipes):
        value = product(recipe)
        values.append([value[j] for j in range(289)])
        if i % 128 == 127 or i+1 == len(recipes):
            _progress(progress, "original R6 on the complete heavy cusp", completed=i+1,
                      total=len(recipes), local_length=289, preserved_degeneracy_multiplier=2**6)
    evaluation = matrix(fp, values)
    denominator_residues = kernel[:, 1140:]*evaluation.column(0)
    assert len(denominator_residues) == 900
    selected = next((i for i, value in enumerate(denominator_residues) if value), None)
    z, j, local_RF, selected_pair, unit_inverse, inverse_steps = 0, None, None, None, None, []
    if selected is not None:
        row = kernel.row(selected)
        Nrow = vector(fp, row[:1140])*evaluation
        Drow = vector(fp, row[1140:])*evaluation
        N, D = ring(list(Nrow)), ring(list(Drow))
        assert D[0] == denominator_residues[selected] and D[0]
        unit_inverse, inverse_steps = _unit_inverse_truncated(D, 289, progress)
        value = (N*unit_inverse).truncate(289)
        assert (D*value).truncate(289) == N
        Nambient, Dambient = Nrow*power_basis, Drow*power_basis
        inverse_ambient = vector(fp, [unit_inverse[t] for t in range(289)])*power_basis
        value_row = vector(fp, [value[t] for t in range(289)])
        local_RF = value_row*power_basis
        assert algebra["multiply"](Dambient, inverse_ambient) == e
        assert algebra["multiply"](Dambient, local_RF) == Nambient
        j = next((i for i, coefficient in enumerate(value_row) if coefficient), None)
        assert j is not None, "All 289 coefficients vanish; the proved 192 bound rejects this reading."
        assert 0 <= j <= 192 and j % 4 == 0
        z = j//2
        selected_pair = {"kernel_row_index":selected, "numerator":Nrow,
                         "denominator":Drow, "inverse":unit_inverse,
                         "RF_value":value_row, "RF_ambient_value":local_RF}
    assert 0 <= z <= 96 and z % 2 == 0
    receipt = {
        "z":z, "definition":"positive RF zero order at the unique base T-pole of order 289",
        "original_heavy_infinity_point_id":point_id,
        "complete_heavy_local_length":289, "actual_residue_degree":1,
        "actual_full_local_power_basis_rank":289,
        "actual_parameter_relation":"nu^289=0, nu^288!=0; all consecutive powers returned",
        "actual_complete_power_basis_sha256":matrix_digest(power_basis),
        "actual_parameter_sha256":vector_digest(parameter),
        "actual_local_coordinate_inverse_sha256":matrix_digest(inverse),
        "original_Y_coordinate_count":666, "original_base_coordinate_count":120,
        "original_Y_basis_id":core["basis_id"],
        "original_full_Y_fiber_values_sha256":matrix_digest(full_Y_values),
        "same_pi2_complete_1225_coefficients_returned":True,
        "same_pi2_pullback_coordinates_sha256":matrix_digest(coordinates),
        "same_pi2_original_M2_local_values_sha256":matrix_digest(local_coordinates),
        "original_frame":"J0=ys^4*J; pi2^*D/J0^6 and pi2^*N/J0^6",
        "frame_unit_returned_in_complete_fiber":True,
        "full_degeneracy_multiplier_preserved":2**6,
        "all_original_R6_local_values_sha256":matrix_digest(evaluation),
        "all_900_denominator_residues_sha256":vector_digest(denominator_residues),
        "all_900_denominator_residues_checked":True,
        "all_denominators_vanish_in_residue":selected is None,
        "regularity_test_basis":"complete H0(L^6(-Pole RF)) is globally generated, degree 984",
        "selected_original_kernel_row":selected,
        "selected_paired_numerator_sha256":(vector_digest(selected_pair["numerator"])
                                               if selected_pair is not None else None),
        "selected_denominator_sha256":(vector_digest(selected_pair["denominator"])
                                          if selected_pair is not None else None),
        "actual_unit_inverse_checked_precisions":inverse_steps,
        "complete_ambient_unit_inverse_and_value_returned":selected is not None,
        "complete_original_RF_local_coefficients_sha256":(vector_digest(selected_pair["RF_value"])
                                                            if selected_pair is not None else None),
        "actual_local_RF_first_nonzero_index":j,
        "ramification_index_pi2_at_this_original_cusp":2,
        "proved_first_nonzero_index_bound_if_regular":192,
        "z_reading":("RF has a pole by the whole denominator system, hence z=0"
                     if selected is None else "z=first_nonzero_index/2 in the complete original local ring"),
    }
    _progress(progress, "original z completely read", z=z, selected_kernel_row=selected,
              original_point_id=point_id, local_RF_first_nonzero_index=j,
              full_local_length=289)
    return {"z":z, "original_component":heavy, "original_point_id":point_id,
            "base_M2_local_values":local_coordinates, "R6_local_values":evaluation,
            "all_denominator_residues":denominator_residues,
            "selected_pair":selected_pair}, receipt


def build_original_first_pole_degree(cube_context, ds_context, cusp_context,
                                    progress=None, *, cube_receipt):
    """Return (context, receipt), with exact e, z and dF at the original r=29.

    cube_context,cube_receipt are BOTH returns of the original cube builder.
    ds_context is the complete DS algebra with with_frobenius=True.
    cusp_context is the complete all-six output of build_original_ys_cusp_fibers,
    made using the original Fp normalization and full 666-section core.
    No upstream algebra is reconstructed or replaced inside this helper.
    """
    _progress(progress, "authenticate original finite pole-degree inputs")
    fp, recipes, kernel, authentication = _authenticate(
        cube_context, ds_context, cusp_context, cube_receipt)
    e_context, e_receipt = _read_e(ds_context, recipes, kernel, progress)
    z_context, z_receipt = _read_z(cusp_context, recipes, kernel, progress)
    e, z = int(e_context["e"]), int(z_context["z"])
    dF = 2160+9*(e-z)
    assert 1296 <= dF <= 3078 and dF % 18 == 0 and dF != 2256
    assert (dF < 2256) == (e-z <= 10)
    assert (dF > 2256) == (e-z >= 12)
    receipt = {
        "kind":"rank2_original_yF_finite_pole_degree",
        "status":"same_original_e_z_and_exact_yF_degree_read",
        "prime":29, "base_level":867, "Y_level":3468,
        "authentication":authentication,
        "e":e, "z":z, "dF":dF,
        "formula":"dF=2160+9*(e-z)", "theory":"R927 sections 6 and 7",
        "e_reading":e_receipt, "z_reading":z_receipt,
        "dF_is_divisible_by_18":True, "dF_ne_2256":True,
        "original_packet_degree_for_comparison":2256,
        "dF_less_than_original_packet_degree":dF < 2256,
        "original_consumer_branch":"F_first" if dF < 2256 else "P_first",
        "all_actual_original_contexts_retained":True,
        "same_original_quadratic_constants_and_omega_retained":True,
        "complete_global_pole_ideals_computed":False,
        "four_intersection_ideals_computed":False,
        "original_shadow_computed":False,
        "ordinary_or_infinitely_many_primes_claimed":False,
        "all_large_matrices_and_local_values_kept_in_process_only":True,
        "source_dependencies":[path.name for path in source_dependencies()],
        "dependency_sha256":{path.name:hashlib.sha256(path.read_bytes()).hexdigest()
                              for path in source_dependencies()},
    }
    context = {"kind":"rank2_original_yF_finite_pole_degree_context",
               "constants":fp, "cube_context":cube_context,
               "DS_context":ds_context, "cusp_context":cusp_context,
               "e_context":e_context, "z_context":z_context,
               "e":e, "z":z, "dF":dF, "certificate":receipt}
    _progress(progress, "complete original yF finite pole degree", e=e, z=z, dF=dF,
              original_consumer_branch=receipt["original_consumer_branch"])
    return context, receipt
