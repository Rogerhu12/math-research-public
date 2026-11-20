#!/usr/bin/env sage-python
"""Original T/U/V on the whole nonreduced DS via complete M6 fractions.

R924 Appendix A: the complete 222-dimensional fraction kernel restricts
surjectively to the 102-dimensional reduced divisor.  The prescribed value
b/f_j^3=1 chooses an actual denominator unit on every full local component.
All values are then read in Gamma(DS,O), retaining both nilpotent directions.
No higher section space than the same R4 is constructed or assumed.
"""
import os
if (os.environ.get("GITHUB_ACTIONS") != "true" or
        os.environ.get("GITHUB_REPOSITORY") != "Rogerhu12/math-research-public"):
    raise SystemExit("Run this mathematical producer only in the public research Actions.")

import argparse
import hashlib
import importlib.util
import time
from pathlib import Path
from sage.all import PolynomialRing, PowerSeriesRing, identity_matrix, matrix, vector
from sage.env import SAGE_VERSION
from section_quotient_algebra import (
    canonical, digest, matrix_digest, vector_digest, series_matrix,
    multiplication_by_section)
import section_quotient_algebra

HERE = Path(__file__).resolve().parent
STARTED = time.monotonic()
CURRENT_STAGE = "initialization"


def progress(stage, **kw):
    global CURRENT_STAGE
    CURRENT_STAGE = stage
    print("RANK2_DS_TUV_STAGE "+canonical(dict(
        stage=stage, elapsed_seconds=time.monotonic()-STARTED, **kw)), flush=True)


def import_file(filename, name):
    path = HERE / filename
    spec = importlib.util.spec_from_file_location(name, str(path))
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def coordinate_reader(basis):
    """Coordinates in a complete independent row basis, with full return."""
    k = basis.base_ring()
    pivots = tuple(basis.pivots())
    assert len(pivots) == basis.nrows()
    inverse = basis.matrix_from_columns(pivots).inverse()

    def read(rows):
        assert rows.base_ring() == k and rows.ncols() == basis.ncols()
        coordinates = rows.matrix_from_columns(pivots)*inverse
        assert coordinates*basis == rows
        return coordinates

    return read


def local_inverse(algebra, component, value):
    """Invert only after proving full rank on the entire four-dimensional factor."""
    k = algebra["constants"]
    e = component["idempotent"]
    assert value*component["projector_matrix"] == value
    basis = matrix(k, list(component["residue_power_basis"].rows())+
                      list(component["nilradical_basis"].rows()))
    assert basis.nrows() == 4
    read = coordinate_reader(basis)
    M = algebra["multiplication_matrix"](value)
    local_M = read(basis*M)
    assert local_M.rank() == 4
    inverse = (read(matrix(k, [e])).row(0)*local_M.inverse())*basis
    assert inverse*M == e
    assert inverse*component["projector_matrix"] == inverse
    return inverse


def prepare_original_frames(algebra):
    """Reuse each original M2 projective frame and its full local unit."""
    k = algebra["constants"]
    n = int(algebra["dimension"])
    assert n == 204
    rows1 = algebra["complete_section_spaces"][1]
    series1 = algebra["complete_section_series"][1]
    labels = algebra["original_point_labels"]
    assert labels["coordinate_basis_id"] == matrix_digest(rows1[:, :205])
    records = labels["local_denominator_records"]
    frobenius = algebra["frobenius_context"]
    components = frobenius["decomposition"]["components"]
    assert len(records) == len(components) == 51
    F2 = frobenius["frobenius_matrix"]**2
    source = algebra["source_quotient"]
    squares = source["project"](series_matrix(
        [(f*f).add_bigoh(409) for f in series1], k, 409))
    frames = []
    for index, (component, record) in enumerate(zip(components, records)):
        assert record["component_index"] == index
        assert component["residue_degree"] == 2 and component["ambient_dimension"] == 4
        j = int(record["original_M2_denominator_index"])
        e = component["idempotent"]
        u = squares.row(j)*component["projector_matrix"]
        assert not (u*F2).is_zero()
        inverse_u = local_inverse(algebra, component, u)
        inverse_square = algebra["multiply"](inverse_u, inverse_u)
        normalizer = algebra["multiplication_matrix"](inverse_square)
        assert algebra["multiply"](u, u)*normalizer == e
        read_residue = coordinate_reader(component["residue_power_basis"])
        one_coordinates = read_residue(matrix(k, [e])).row(0)
        assert list(one_coordinates) == [k.one(), k.zero()]
        frames.append({
            "component":component, "original_M2_index":j,
            "normalizer_matrix":normalizer,
            "residue_reader":read_residue,
            "residue_unit_coordinates":one_coordinates,
            "point_id":labels["components"][index]["point_id"],
            "local_unit_square":u,
        })
    return frames, F2


def original_m6_fraction_kernel(rows3, exponent, integral_eta, name):
    """Keep the ENTIRE original (a,b) kernel on 0..918+exponent."""
    k = rows3.base_ring()
    precision = rows3.ncols()
    assert rows3.nrows() == 528
    length = 919+int(exponent)
    assert precision >= length
    ring = PolynomialRing(k, "Q_original_fraction")
    Q = ring.gen()
    basis = [ring(list(row)) for row in rows3.rows()]
    coefficients = [k.zero() for _ in range(length)]
    for j in range((length-1)//exponent+1):
        coefficients[exponent*j] = k(integral_eta[j])
    tau = ring(coefficients)
    assert tau[0] == 1
    negative = [-(tau*b).truncate(length) for b in basis]
    equations = matrix(k, [
        [b[j-exponent] if j >= exponent else k.zero() for j in range(length)]
        for b in basis] + [
        [b[j] for j in range(length)] for b in negative])
    assert equations.nrows() == 1056 and equations.ncols() == length
    progress("complete original M6 fraction kernel start", function=name,
             unknowns=1056, checked_coefficients=length, original_pole_degree=306)
    kernel = equations.left_kernel().basis_matrix()
    assert kernel.nrows() == 222
    assert kernel*equations == 0
    first, second = kernel[:, :528], kernel[:, 528:]
    assert first.rank() == second.rank() == 222
    progress("complete original M6 fraction kernel certified", function=name,
             actual_kernel_dimension=222, full_pole_bound=918,
             checked_shifted_last=918+exponent)
    receipt = {
        "original_function":name, "eta_substitution_exponent":int(exponent),
        "complete_M6_dimension":528,
        "section_bundle_degree":612, "original_complete_pole_degree":306,
        "complete_difference_pole_bound":918,
        "checked_shifted_coefficients_inclusive":[0, 918+int(exponent)],
        "actual_full_fraction_kernel_dimension":222,
        "entire_kernel_residual_verified":True,
        "both_full_kernel_projections_injective":True,
        "equations_sha256":matrix_digest(equations),
        "complete_fraction_kernel_sha256":matrix_digest(kernel),
        "original_shifted_eta_jets_sha256":digest([int(tau[j]) for j in range(length)])}
    return {"kernel":kernel, "equations":equations, "tau":tau,
            "ring":ring, "Q":Q, "length":length, "receipt":receipt}


def read_one_original_function(algebra, frames, F2, H_inverse,
                               fraction, name, exponent):
    """Prescribe all reduced denominator values, then divide on full DS."""
    k, n = algebra["constants"], int(algebra["dimension"])
    rows3 = algebra["complete_section_spaces"][3]
    series1 = algebra["complete_section_series"][1]
    target = algebra["target_quotient"]
    kernel = fraction["kernel"]
    denominator_rows = kernel[:, 528:]*rows3
    ring = PowerSeriesRing(k, "Q_DS_read", default_prec=817)
    denominator_series = [ring(list(row[:817])).add_bigoh(817)
                          for row in denominator_rows.rows()]
    section_cache = {}

    def denominator_products(j):
        if j not in section_cache:
            f = ring([series1[j][i] for i in range(817)]).add_bigoh(817)
            jets = series_matrix([(b*f).add_bigoh(817) for b in denominator_series], k, 817)
            # This is exactly b*f_j/h^2 in Gamma(DS,O).
            section_cache[j] = target["project"](jets)*H_inverse
        return section_cache[j]

    blocks = []
    for index, frame in enumerate(frames):
        normalized = denominator_products(frame["original_M2_index"])*frame["normalizer_matrix"]
        reduced = normalized*F2
        block = frame["residue_reader"](reduced)
        assert block.nrows() == 222 and block.ncols() == 2
        blocks.append(block)
        if index % 12 == 11 or index == len(frames)-1:
            progress("original denominator complete residue restriction", function=name,
                     completed_components=index+1, total_components=51)
    restriction = matrix(k, 222, 102, lambda i, j: blocks[j//2][i, j % 2])
    selected_rows = tuple(restriction.transpose().pivots())
    assert len(selected_rows) == 102
    minor = restriction.matrix_from_rows(selected_rows)
    assert minor.nrows() == minor.ncols() == 102
    rhs = vector(k, [c for frame in frames for c in frame["residue_unit_coordinates"]])
    solution_selected = rhs*minor.inverse()
    solution = vector(k, 222)
    for j, row in enumerate(selected_rows):
        solution[row] = solution_selected[j]
    assert solution*restriction == rhs
    coefficients = solution*kernel
    assert coefficients*fraction["equations"] == 0
    a_coordinates = vector(k, coefficients[:528])
    b_coordinates = vector(k, coefficients[528:])
    a_row, b_row = a_coordinates*rows3, b_coordinates*rows3
    P, Q, tau = fraction["ring"], fraction["Q"], fraction["tau"]
    a, b = P(list(a_row)), P(list(b_row))
    assert a and b
    assert (Q**exponent*a-tau*b).truncate(fraction["length"]) == 0
    assert int(b.valuation())-int(a.valuation()) == exponent
    assert a[int(a.valuation())] == b[int(b.valuation())]

    a_series = ring(list(a_row[:817])).add_bigoh(817)
    numerator_cache = {}
    all_a, all_b = vector(k, n), vector(k, n)
    local_denominators = []
    for frame in frames:
        j = frame["original_M2_index"]
        if j not in numerator_cache:
            f = ring([series1[j][i] for i in range(817)]).add_bigoh(817)
            jets = series_matrix([(a_series*f).add_bigoh(817)], k, 817)
            numerator_cache[j] = (target["project"](jets)*H_inverse).row(0)
        local_a = numerator_cache[j]*frame["normalizer_matrix"]
        local_b = (solution*denominator_products(j))*frame["normalizer_matrix"]
        e = frame["component"]["idempotent"]
        projector = frame["component"]["projector_matrix"]
        assert local_a*projector == local_a and local_b*projector == local_b
        assert local_b*F2 == e
        all_a += local_a
        all_b += local_b
        local_denominators.append(local_b)
    assert all_b*F2 == algebra["unit"]
    denominator_matrix = algebra["multiplication_matrix"](all_b)
    assert denominator_matrix.rank() == n == 204
    inverse_matrix = denominator_matrix.inverse()
    assert denominator_matrix*inverse_matrix == identity_matrix(k, n)
    value = all_a*inverse_matrix
    assert value*denominator_matrix == all_a
    # The eta functions have zeros and poles only at cusps; DS is disjoint
    # from the entire cusp divisor, so their complete DS values are units.
    value_matrix = algebra["multiplication_matrix"](value)
    assert value_matrix.rank() == 204
    if name == "T":
        assert value == -k(27)*algebra["unit"]

    local_values, local_records = [], []
    for index, frame in enumerate(frames):
        local_value = value*frame["component"]["projector_matrix"]
        residue = frame["residue_reader"](matrix(k, [local_value*F2]))
        local_values.append(local_value)
        local_records.append({"component_index":index,
            "original_point_id_sha256":frame["point_id"],
            "original_M2_frame_index":frame["original_M2_index"],
            "complete_local_value_sha256":vector_digest(local_value),
            "residue_coordinates_sha256":matrix_digest(residue),
            "normalized_denominator_residue_is_one":True})
    receipt = dict(fraction["receipt"],
        actual_complete_residue_restriction_rank=102,
        prescribed_residue_values="b/f_j^3=1 at each of all 51 quadratic closed points",
        remaining_affine_solution_dimension=120,
        complete_restriction_matrix_sha256=matrix_digest(restriction),
        chosen_restriction_minor_rows_sha256=digest(list(selected_rows)),
        chosen_full_kernel_combination_sha256=vector_digest(solution),
        chosen_fraction_coordinates_sha256=vector_digest(coefficients),
        all_prescribed_residue_values_verified=True,
        actual_full_DS_denominator_multiplication_rank=204,
        full_DS_denominator_multiplication_sha256=matrix_digest(denominator_matrix),
        complete_nonreduced_division_verified=True,
        actual_original_value_multiplication_rank=204,
        original_T_equals_minus_27_on_full_DS=(name == "T"),
        full_original_value_sha256=vector_digest(value),
        full_original_multiplication_matrix_sha256=matrix_digest(value_matrix),
        normalized_numerator_sha256=vector_digest(all_a),
        normalized_denominator_sha256=vector_digest(all_b),
        original_numerator_jets_sha256=vector_digest(a_row),
        original_denominator_jets_sha256=vector_digest(b_row),
        complete_point_values=local_records)
    progress("same original eta function read on all nonreduced DS", function=name,
             complete_fraction_kernel=222, complete_residue_restriction=102,
             actual_full_denominator_unit_rank=204,
             full_value_sha256=receipt["full_original_value_sha256"])
    context = {"fraction":fraction, "restriction_matrix":restriction,
               "kernel_combination":solution,
               "numerator_coordinates":a_coordinates,
               "denominator_coordinates":b_coordinates,
               "numerator_jets":a_row, "denominator_jets":b_row,
               "normalized_numerator":all_a, "normalized_denominator":all_b,
               "local_denominators":local_denominators,
               "value":value, "multiplication_matrix":value_matrix,
               "complete_local_values":local_values,
               "certificate":receipt}
    return context, receipt


def build_original_ds_tuv_values(prime=29, q_precision=1208):
    prime, q_precision = int(prime), int(q_precision)
    assert prime in (29, 41) and q_precision >= 1208
    ds_module = import_file("produce-original-ds-section-algebra.py", "original_ds_for_tuv_values")
    eta_module = import_file("produce-original-tuv-section-fractions.py", "original_eta_for_ds_values")
    algebra, ds_receipt = ds_module.build_original_ds_section_algebra(
        prime=prime, q_precision=q_precision, with_frobenius=True)
    rows3 = algebra["complete_section_spaces"][3]
    assert rows3.nrows() == 528 and rows3.ncols() == q_precision
    assert rows3[:, :613].rank() == 528
    H, h_record = multiplication_by_section(
        algebra["source_quotient"], algebra["target_quotient"],
        algebra["h_row"], progress)
    assert h_record["matrix_sha256"] == algebra["certificate"]["h_multiplier"]["matrix_sha256"]
    H_inverse = H.inverse()
    assert matrix_digest(H_inverse) == algebra["certificate"]["h_multiplier_inverse_sha256"]
    frames, F2 = prepare_original_frames(algebra)
    integral_eta = eta_module.original_eta_unit(q_precision)
    functions, cases = {}, []
    for name, exponent in (("T", 1), ("U", 17), ("V", 289)):
        fraction = original_m6_fraction_kernel(rows3, exponent, integral_eta, name)
        functions[name], receipt = read_one_original_function(
            algebra, frames, F2, H_inverse, fraction, name, exponent)
        cases.append(receipt)
    assert functions["T"]["value"] == -algebra["constants"](27)*algebra["unit"]
    dependencies = [Path(ds_module.__file__), Path(eta_module.__file__),
                    Path(section_quotient_algebra.__file__),
                    HERE / "finite_section_frobenius.py",
                    HERE / "produce-r917-original-global-rr-q-lattice.py",
                    HERE / "original_pari_m2_basis.py",
                    HERE / "original_shadow_coordinate_tools.py"]
    receipt = {
        "kind":"rank2_original_full_DS_TUV_values_certificate",
        "status":"all_three_original_eta_functions_read_on_complete_nonreduced_DS",
        "prime":prime, "level":867, "q_precision":q_precision,
        "original_DS_degree":204, "all_original_closed_components":51,
        "complete_nonreduced_local_dimensions":[4]*51,
        "same_DS_source_receipt_sha256":digest(ds_receipt),
        "same_DS_multiplication_table_sha256":algebra["certificate"]["multiplication_table_sha256"],
        "same_original_M2_coordinate_basis_id":algebra["original_point_labels"]["coordinate_basis_id"],
        "same_full_M6_rows_sha256":matrix_digest(rows3),
        "same_full_M6_product_recipes_sha256":
            ds_receipt["complete_product_spaces"][2]["actual_product_recipes_sha256"],
        "same_H_inverse_sha256":matrix_digest(H_inverse),
        "each_function_uses_its_own_complete_kernel_and_denominator":True,
        "no_section_space_above_R4_used":True,
        "cases":cases,
        "original_T_equals_minus_27_on_entire_DS":True,
        "original_maps_or_shadow_claimed":False,
        "source":os.environ.get("RANK2_SOURCE_SHA"),
        "run_id":os.environ.get("RANK2_RUN_ID", os.environ.get("GITHUB_RUN_ID")),
        "run_attempt":os.environ.get("RANK2_RUN_ATTEMPT"),
        "sage_version":SAGE_VERSION, "image":os.environ.get("RANK2_IMAGE"),
        "script_sha256":hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "dependency_sha256":{path.name:hashlib.sha256(path.read_bytes()).hexdigest()
                             for path in dependencies},
        "readme_blobs":{"README.md":os.environ.get("RANK2_ROOT_README_SHA"),
                        "topic":os.environ.get("RANK2_TOPIC_README_SHA")},
        "elapsed_seconds":time.monotonic()-STARTED,
    }
    context = {"kind":"rank2_original_full_DS_TUV_values_context",
               "constants":algebra["constants"], "original_DS_algebra":algebra,
               "DS_source_receipt":ds_receipt, "original_frames":frames,
               "same_H_inverse":H_inverse, "functions":functions,
               "q_precision":q_precision}
    return context, receipt


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--prime", type=int, choices=(29, 41), default=29)
    parser.add_argument("--q-precision", type=int, default=1208)
    args = parser.parse_args()
    context, receipt = build_original_ds_tuv_values(args.prime, args.q_precision)
    globals()["ORIGINAL_FULL_DS_TUV_VALUES_CONTEXT"] = context
    payload = canonical(receipt)
    print("RANK2_DS_TUV_RESULT "+payload, flush=True)
    print("RANK2_DS_TUV_SHA256 "+hashlib.sha256(payload.encode()).hexdigest(), flush=True)


if __name__ == "__main__":
    try:
        main()
    except Exception as exc:
        failed = CURRENT_STAGE
        progress("failed", failed_stage=failed,
                 exception_type=type(exc).__name__, message=str(exc))
        raise
