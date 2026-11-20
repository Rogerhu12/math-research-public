#!/usr/bin/env sage-python
"""Construct the SAME full degree-204 divisor algebra from original sections.

This uses R917's authenticated and saturated complete M2(867), extended by
the SAME persistent PARI forms to Q^816.  Higher spaces consist of actual
products and are accepted only at the full Riemann--Roch dimension.
No eta48 normalization, reduced-point substitution or coefficient files.
"""
import os
if (os.environ.get("GITHUB_ACTIONS") != "true" or
        os.environ.get("GITHUB_REPOSITORY") != "Rogerhu12/math-research-public"):
    raise SystemExit("Run this mathematical producer only in the public research Actions.")

import argparse
import hashlib
import importlib.util
import sys
import time
from pathlib import Path
from sage.all import matrix, vector, set_random_seed
from sage.env import SAGE_VERSION
from section_quotient_algebra import (
    build_quotient, build_algebra, canonical, digest, matrix_digest,
    series_matrix, multiplication_by_section, vector_digest)
import section_quotient_algebra

HERE = Path(__file__).resolve().parent
STARTED = time.monotonic()
CURRENT_STAGE = "initialization"


def progress(stage, **kw):
    global CURRENT_STAGE
    CURRENT_STAGE = stage
    print("RANK2_SECTION_DS_STAGE " + canonical(dict(
        stage=stage, elapsed_seconds=time.monotonic()-STARTED, **kw)), flush=True)


def import_file(path, name):
    spec = importlib.util.spec_from_file_location(name, str(path))
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def default_scripts_directory():
    if (HERE / "original_pari_m2_basis.py").is_file():
        return HERE
    return Path(os.environ.get("GITHUB_WORKSPACE", ".")) / \
        "topics/rank2-sha-infinitely-many-p/scripts"


def label_original_ds_points(algebra, frobenius_context, rows1, series1,
                             frobenius_module):
    """Read the original complete M2 embedding on every nonreduced point.

    In the algebra model v -> v/h, [fi*fj]/[fj^2] is exactly fi/fj.
    Only the choice of j uses the residue field.  The inverse and all 120
    ratios are computed and checked in the entire four-dimensional local
    component, so the tangent/nilpotent information is retained.
    """
    k, n = algebra["constants"], int(algebra["dimension"])
    assert n == 204 and rows1.nrows() == len(series1) == 120
    source = algebra["source_quotient"]
    precision = int(source["sturm"])
    assert precision == 409
    decomposition = frobenius_context["decomposition"]
    assert decomposition is not None
    components = decomposition["components"]
    assert len(components) == 51
    F2 = frobenius_context["frobenius_matrix"]**2
    square_classes = source["project"](series_matrix(
        [(f*f).add_bigoh(precision) for f in series1], k, precision))
    numerator_cache = {}
    component_rows, local_records = [], []

    for index, component in enumerate(components):
        assert component["ambient_dimension"] == 4
        assert component["residue_degree"] == 2
        e, projector = component["idempotent"], component["projector_matrix"]
        local_squares = square_classes*projector
        residue_squares = local_squares*F2
        possible = [j for j in range(120) if not residue_squares.row(j).is_zero()]
        assert possible, "The complete original M2 sections must generate at every point."
        j = possible[0]
        denominator = local_squares.row(j)
        local_basis = matrix(k, list(component["residue_power_basis"].rows())+
                             list(component["nilradical_basis"].rows()))
        pivots = tuple(local_basis.pivots())
        assert len(pivots) == local_basis.nrows() == 4
        pivot_inverse = local_basis.matrix_from_columns(pivots).inverse()

        def local_coordinates(rows):
            coordinates = rows.matrix_from_columns(pivots)*pivot_inverse
            assert coordinates*local_basis == rows
            return coordinates

        denominator_matrix = algebra["multiplication_matrix"](denominator)
        local_multiplier = local_coordinates(local_basis*denominator_matrix)
        assert local_multiplier.rank() == 4
        local_unit = local_coordinates(matrix(k, [e])).row(0)
        inverse_coordinates = local_unit*local_multiplier.inverse()
        denominator_inverse = inverse_coordinates*local_basis
        assert denominator_inverse*denominator_matrix == e
        assert denominator_inverse*projector == denominator_inverse
        if j not in numerator_cache:
            numerator_cache[j] = source["project"](series_matrix(
                [(f*series1[j]).add_bigoh(precision) for f in series1],
                k, precision))
        local_numerators = numerator_cache[j]*projector
        ratios = local_numerators*algebra["multiplication_matrix"](denominator_inverse)
        assert ratios*projector == ratios
        assert ratios*denominator_matrix == local_numerators
        assert ratios.row(j) == e
        component_rows.append(ratios)
        local_records.append({
            "component_index":index,
            "original_M2_denominator_index":j,
            "complete_local_dimension":4,
            "actual_denominator_multiplication_rank":4,
            "inverse_verified_in_complete_nonreduced_component":True,
            "all_120_original_ratios_verified":True,
            "denominator_class_sha256":vector_digest(denominator),
            "complete_local_inverse_sha256":vector_digest(denominator_inverse),
            "complete_original_ratio_rows_sha256":matrix_digest(ratios)})
        progress("original DS full local projective ratios", component=index,
                 total_components=51, original_M2_denominator_index=j,
                 complete_local_dimension=4, original_coordinates=120)

    basis_id = matrix_digest(rows1[:, :205])
    labels, receipt = frobenius_module.label_closed_components(
        algebra, frobenius_context, component_rows,
        coordinate_basis_id=basis_id, progress=progress)
    labels["full_component_ratio_rows"] = component_rows
    labels["local_denominator_records"] = local_records
    receipt["ratio_construction"] = "([fi*fj]/h)/([fj^2]/h)=fi/fj in each complete local component"
    receipt["complete_local_ratio_checks"] = local_records
    receipt["same_original_M2_first_205_coefficients_sha256"] = basis_id
    return labels, receipt


def build_original_ds_section_algebra(prime=29, q_precision=817,
                                     max_unit_trials=64, batch_size=128,
                                     scripts_directory=None,
                                     with_frobenius=False):
    prime, q_precision = int(prime), int(q_precision)
    max_unit_trials, batch_size = int(max_unit_trials), int(batch_size)
    assert prime in (29, 41) and q_precision >= 817
    assert max_unit_trials > 0 and batch_size > 0
    scripts = Path(scripts_directory or default_scripts_directory()).resolve()
    sys.path.insert(0, str(scripts))
    r917_path = scripts / "produce-r917-original-global-rr-q-lattice.py"
    r917 = import_file(r917_path, "original_ds_r917_source")
    products_path = scripts / "original_shadow_coordinate_tools.py"
    products = import_file(products_path, "original_ds_complete_products")
    set_random_seed(20261120)

    original, original_receipt = r917.build_original_global_rr_q_lattice(
        prime, q_precision)
    k = original["constants"]
    rows1 = original["global_modular_form_jets"]
    assert rows1.nrows() == 120 and rows1.ncols() == q_precision
    progress("same complete saturated M2 expanded", prime=prime,
             precision=q_precision,
             original_space_receipt_sha256=digest(original_receipt))
    recipes, series = products.complete_product_recipes(
        {"constants":k}, [list(row) for row in rows1.rows()], 4, q_precision)
    spaces = {m:series_matrix(series[m], k, q_precision) for m in range(1, 5)}
    assert spaces[1] == rows1
    full_space_receipts = []
    for m in range(1, 5):
        expected = 204*m-84
        assert spaces[m].nrows() == expected
        full_space_receipts.append({
            "power":m, "weight":2*m, "complete_dimension":expected,
            "complete_rank_source":("same R917 saturated full M2" if m == 1
                                    else "same complete actual-product rank selector"),
            "full_sturm_coefficients":204*m+1,
            "retained_q_precision":q_precision,
            "actual_product_recipes_sha256":digest(recipes[m]),
            "complete_rows_sha256":matrix_digest(spaces[m])})
    S = original["original_denominator_q_series"]
    assert S[0] == 1
    ideal2 = series_matrix([(S*f).add_bigoh(q_precision) for f in series[1]],
                           k, q_precision)
    ideal4 = series_matrix([(S*f).add_bigoh(q_precision) for f in series[3]],
                           k, q_precision)
    source = build_quotient(spaces[2], ideal2, 409, "M4 / (S M2)", progress)
    target = build_quotient(spaces[4], ideal4, 817, "M8 / (S M6)", progress)
    assert source["quotient_dimension"] == target["quotient_dimension"] == 204

    # This bounded deterministic search is an execution budget, not a
    # mathematical test for the existence of a trivializing section.
    set_random_seed(20261120)
    unit_trials = []
    selected = None
    n = source["quotient_dimension"]
    for trial in range(max_unit_trials):
        coefficients = vector(k, n)
        if trial == 0:
            coefficients[0] = 1
            method = "first actual quotient lift"
        else:
            coefficients = vector(k, [k.random_element() for _ in range(n)])
            method = "fixed-seed dense prime-field combination"
        h = coefficients*source["lift_rows"]
        H, h_record = multiplication_by_section(source, target, h, progress,
                                               batch_size=batch_size)
        unit_trials.append({"trial":trial+1, "method":method,
                            "rank":h_record["rank"],
                            "h_quotient_coordinates_sha256":vector_digest(coefficients),
                            "h_row_sha256":h_record["h_row_sha256"]})
        progress("original DS unit-section trial", **unit_trials[-1])
        if h_record["rank"] == n:
            selected = h, H, h_record
            break
    if selected is None:
        raise ArithmeticError(
            "Bounded unit-section search exhausted; no nonexistence claim.")
    h, H, h_record = selected
    algebra, algebra_receipt = build_algebra(
        source, target, h, progress, batch_size=batch_size,
        precomputed_h=(H, h_record))
    algebra["original_r917_context"] = original
    algebra["complete_section_spaces"] = spaces
    algebra["complete_section_series"] = series
    algebra["original_S"] = S

    dependencies = [r917_path, scripts / "original_pari_m2_basis.py",
                    products_path, Path(section_quotient_algebra.__file__)]
    frobenius_receipt = None
    point_label_receipt = None
    if with_frobenius:
        import finite_section_frobenius
        frobenius_context, frobenius_receipt = finite_section_frobenius.inspect_frobenius(
            algebra, expected="ds", progress=progress)
        algebra["frobenius_context"] = frobenius_context
        point_labels, point_label_receipt = label_original_ds_points(
            algebra, frobenius_context, rows1, series[1], finite_section_frobenius)
        algebra["original_point_labels"] = point_labels
        dependencies.append(Path(finite_section_frobenius.__file__))

    result = {
        "kind":"rank2_original_DS_section_algebra_certificate",
        "status":("exact_original_full_DS_algebra_with_frobenius"
                  if with_frobenius else "exact_original_full_DS_algebra"),
        "level":867, "prime":prime, "genus":85,
        "original_divisor":"DS = div_L(S), S=(3E2(Q^3)-E2(Q))/2",
        "original_divisor_degree":204, "all_geometric_cusps_retained":36,
        "same_original_global_model_as_R917":True,
        "nonreduced_divisor_structure_retained":True,
        "q_precision":q_precision,
        "original_complete_M2_receipt":original_receipt,
        "complete_product_spaces":full_space_receipts,
        "original_S_sha256":digest([int(S[j]) for j in range(q_precision)]),
        "unit_section_search":{"seed":20261120,
                               "maximum_trials":max_unit_trials,
                               "trials":unit_trials,
                               "budget_exhaustion_is_not_nonexistence":True},
        "finite_algebra":algebra_receipt,
        "frobenius":frobenius_receipt,
        "original_M2_projective_point_labels":point_label_receipt,
        "all_original_closed_points_labeled_in_same_global_embedding":point_label_receipt is not None,
        "complete_closed_point_decomposition_computed":bool(
            frobenius_receipt and frobenius_receipt.get("decomposition")),
        "closed_point_decomposition_requires_separate_complete_receipt":not bool(
            frobenius_receipt and frobenius_receipt.get("decomposition")),
        "eta48_normalization_claimed":False,
        "original_maps_or_shadow_claimed":False,
        "scope":"Exact Gamma(DS,O_DS) via complete original sections and a unit on all DS; further map evaluation remains separate.",
        "source":os.environ.get("RANK2_SOURCE_SHA"),
        "run_id":os.environ.get("RANK2_RUN_ID", os.environ.get("GITHUB_RUN_ID")),
        "run_attempt":os.environ.get("RANK2_RUN_ATTEMPT"),
        "sage_version":SAGE_VERSION,
        "image":os.environ.get("RANK2_IMAGE"),
        "script_sha256":hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "dependency_sha256":{path.name:hashlib.sha256(path.read_bytes()).hexdigest()
                             for path in dependencies},
        "readme_blobs":{"README.md":os.environ.get("RANK2_ROOT_README_SHA"),
                        "topic":os.environ.get("RANK2_TOPIC_README_SHA")},
        "elapsed_seconds":time.monotonic()-STARTED,
    }
    return algebra, result


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--prime", type=int, choices=(29, 41), default=29)
    parser.add_argument("--q-precision", type=int, default=817)
    parser.add_argument("--max-unit-trials", type=int, default=64)
    parser.add_argument("--batch-size", type=int, default=128)
    parser.add_argument("--scripts-directory", default=str(default_scripts_directory()))
    parser.add_argument("--with-frobenius", action="store_true")
    args = parser.parse_args()
    algebra, result = build_original_ds_section_algebra(
        prime=args.prime, q_precision=args.q_precision,
        max_unit_trials=args.max_unit_trials, batch_size=args.batch_size,
        scripts_directory=args.scripts_directory,
        with_frobenius=args.with_frobenius)
    globals()["ORIGINAL_DS_SECTION_ALGEBRA_CONTEXT"] = algebra
    payload = canonical(result)
    print("RANK2_SECTION_DS_RESULT " + payload, flush=True)
    print("RANK2_SECTION_DS_SHA256 " + hashlib.sha256(payload.encode()).hexdigest(), flush=True)


if __name__ == "__main__":
    try:
        main()
    except Exception as exc:
        failed = CURRENT_STAGE
        progress("failed", failed_stage=failed,
                 exception_type=type(exc).__name__, message=str(exc))
        raise
