#!/usr/bin/env sage-python
"""Constructed complete two-chart ideal and primitive zero/pole API fixtures."""
import os
if (os.environ.get("GITHUB_ACTIONS") != "true" or
        os.environ.get("GITHUB_REPOSITORY") != "Rogerhu12/math-research-public"):
    raise SystemExit("Run mathematical computations only in the public research Actions.")

import ast
import hashlib
import json
import time
from pathlib import Path
from sage.all import GF, PolynomialRing, diagonal_matrix, identity_matrix, matrix, vector
from sage.env import SAGE_VERSION
from section_quotient_algebra import canonical, digest
from original_ys_divisor_ideal_tools import OriginalAffineIdeal, polynomial_matrix_digest
import original_w_ideal_transport as transport

HERE = Path(__file__).resolve().parent
ROOT, TOPIC = HERE.parents[2], HERE.parent
REQUEST = TOPIC/"ci/original-whole-w-ideal-api-request.json"
WORKFLOW = ROOT/".github/workflows/rank2-sha-whole-w-ideal-api.yml"
IMAGE = "sagemath/sagemath@sha256:19995db6194f4a4bab18ce9a88556fd15b9ed5e916b4504fefe618a7796ddbdb"
SOURCE_FILES = tuple(dict.fromkeys((
    "check-original-whole-w-ideal-api.py",
)+transport.SOURCE_DEPENDENCIES))
assert len(SOURCE_FILES) == len(set(SOURCE_FILES))
STARTED = time.monotonic()


def complete_mixed_two_chart_case():
    k = GF(29)
    R, S = PolynomialRing(k, "constructed_xi"), PolynomialRing(k, "constructed_s")
    t, s = R.gen(), S.gen()
    half, third, fifth, seventh = (k(a)**(-1) for a in (2, 3, 5, 7))
    irreducible = t*t-2
    transformed_irreducible = t*t-10*t-7
    assert irreducible.is_irreducible() and transformed_irreducible.is_irreducible()
    # Two components of a CONSTRUCTED product curve, with the same fixed
    # constant change of basis. The first has full multiplicity 289 at
    # source infinity, plus a nonsplit degree-two point of multiplicity 3.
    # W must move infinity to xi=1 and source xi=0 to target xi=-3.
    f1 = t**5*(t-1)**2*(t+3)**4*(t-2)**2*irreducible**3
    f2 = t**2*(t-1)**4*(t-7)
    g1 = s**289*(s-1)**2*(s+third)**4*(s-half)**2*(s*s-half)**3
    g2 = s*(s-1)**4*(s-seventh)
    U_R, U_S = matrix(R, [[1, 2], [1, 3]]), matrix(S, [[1, 2], [1, 3]])
    H, source_H = transport._checked_hnf(
        diagonal_matrix(R, [f1, f2])*U_R, label="constructed full finite source")
    H0, source_H0 = transport._checked_hnf(
        diagonal_matrix(S, [g1, g2])*U_S, label="constructed full other-chart source")
    C, D = identity_matrix(R, 2), identity_matrix(S, 2)
    images, receipt = transport._complete_pair_bases(
        H, H0, (0, 0), C, D, label="constructed mixed two-chart whole transport")
    expected_f1 = t**4*(t-1)**289*(t+3)**5*(t-5)**2*transformed_irreducible**3
    expected_f2 = (t-1)*(t+3)**2*(t-5*third)
    reciprocal_transformed = s*s+10*seventh*s-seventh
    expected_g1 = s**2*(s-1)**289*(s+third)**5*(s-fifth)**2*reciprocal_transformed**3
    expected_g2 = s**4*(s-1)*(s+third)**2*(s-3*fifth)
    expected, unused = transport._checked_hnf(
        diagonal_matrix(R, [expected_f1, expected_f2])*U_R,
        label="independent complete expected finite image")
    expected0, unused = transport._checked_hnf(
        diagonal_matrix(S, [expected_g1, expected_g2])*U_S,
        label="independent complete expected other-chart image")
    assert images[False] == expected and images[True] == expected0
    assert receipt["finite"]["complete_missing_fibre_length"] == 290
    assert receipt["infinity"]["complete_missing_fibre_length"] == 7
    returned, return_receipt = transport._complete_pair_bases(
        images[False], images[True], (0, 0), C, D,
        label="constructed full inverse W on both original source modules")
    assert returned[False] == H and returned[True] == H0
    assert transport._determinant_of_hermite(images[False]).degree() == 310
    assert transport._linear_order(transport._determinant_of_hermite(images[True]), s) == 6
    assert transport._determinant_of_hermite(H).degree() == 26
    assert transport._linear_order(transport._determinant_of_hermite(H0), s) == 290
    return dict(
        constructed_coordinate_rank=2, constructed_constant_prime=29,
        full_projective_length=316, mixed_complete_source_HNF=True,
        whole_multiplicity_289_and_nonsplit_degree_two_thickness_three_retained=True,
        entire_missing_finite_fibre_length=290, entire_missing_other_fibre_length=7,
        both_complete_expected_target_HNFs_returned=True,
        every_original_source_returned_after_W_squared=True,
        first_complete_two_chart_transport=receipt,
        inverse_complete_two_chart_transport=return_receipt,
        original_Y_or_306_dimensional_normalization_generated=False)


def complete_unit_pair_case():
    k = GF(29)
    R, S = PolynomialRing(k, "constructed_unit_xi"), PolynomialRing(k, "constructed_unit_s")
    I, I0 = identity_matrix(R, 1), identity_matrix(S, 1)
    result, receipt = transport._complete_pair_bases(
        I, I0, (0,), I, I0, label="constructed empty divisor on both whole charts")
    assert result[False] == I and result[True] == I0
    assert receipt["finite"]["complete_missing_fibre_length"] == 0
    assert receipt["infinity"]["complete_missing_fibre_length"] == 0
    # Reuse the ACTUAL production formatter on the genuine constructed
    # constant function 1 on both P1 charts. No fake rank-306 identity exists.
    charts, gates = {}, {}
    for flag, ring in ((False, R), (True, S)):
        engine = ConstructedRankOneEngine(ring)
        engine.infinity_chart = flag
        whole = OriginalAffineIdeal(
            engine, result[flag], ring.one(),
            dict(constructed_rank_one_complete_unit_ideal=True))
        charts[flag] = {"positive":whole, "negative":whole}
        gates["infinity" if flag else "finite"] = (
            transport.verify_complete_original_zero_pole_pair(
                engine, whole, whole, [ring.one()], [ring.one()],
                label="constructed whole constant function on its actual chart"))
    for sign in ("positive", "negative"):
        charts[True][sign+"_boundary"] = charts[True][sign]
        gates[sign+"_infinity_boundary"] = dict(
            constructed_rank_one_complete_unit_boundary=True,
            full_quotient_length=0, complete_primary_block=True,
            full_returned_unit_HNF_sha256=polynomial_matrix_digest(result[True]))
    packed = transport.assemble_complete_principal_divisor_records(
        charts, gates, operation="W", label="constructed complete unit principal divisor")
    assert {"False", "True", "positive_infinity_boundary",
            "negative_infinity_boundary"} <= set(packed)
    for flag, chart_name in ((False, "finite"), (True, "infinity")):
        assert packed[str(flag)]["complete_transported_primitive_fraction_gates"] is gates[chart_name]
        assert packed[str(flag)]["zero_ideal"] is charts[flag]["positive"].receipt
        assert packed[str(flag)]["pole_ideal"] is charts[flag]["negative"].receipt
        assert "kernel" not in packed[str(flag)]
    for sign in ("positive", "negative"):
        assert packed[sign+"_infinity_boundary"] is gates[sign+"_infinity_boundary"]
    return dict(empty_divisor_and_zero_primary_exponent_passed=True,
                unchanged_consumer_records_False_and_True_paths_returned=True,
                original_both_boundary_record_keys_returned=True,
                actual_production_formatter_used_on_verified_rank_one_unit_parts=True,
                direct_graph_computation_not_falsely_claimed=True,
                complete_both_chart_returns=receipt)


class ConstructedRankOneEngine:
    """Only k[t] on a constructed P1 chart; never an original-Y engine."""
    def __init__(self, R):
        self.R, self.k, self.dimension = R, R.base_ring(), 1
        self.identity, self.unit = identity_matrix(R, 1), vector(R, [1])
        self.infinity_chart = False

    def element(self, value):
        row = vector(self.R, value)
        assert len(row) == 1
        return row

    def multiplication_matrix(self, value):
        return matrix(self.R, [[self.element(value)[0]]])


def primitive_zero_pole_case():
    k, R = GF(29), None
    R = PolynomialRing(k, "constructed_fraction_parameter")
    t, engine = R.gen(), ConstructedRankOneEngine(R)
    z, p = (t-2)**3, (t+1)**2
    common = (t*t-2)**2*(t-2)
    N, D = common*z, common*p

    def ideal(f):
        f = f.monic()
        return OriginalAffineIdeal(engine, matrix(R, [[f]]), f,
                                   dict(constructed_rank_one_fixture=True))

    Z, P = ideal(z), ideal(p)
    good = transport.verify_complete_original_zero_pole_pair(
        engine, Z, P, [N], [D], label="constructed genuine common-zero fraction")
    extra = (t-3)**2
    bad_Z, bad_P = ideal(extra*z), ideal(extra*p)
    # The image equation alone REALLY holds for this wrong pair.
    assert bad_Z.basis*engine.multiplication_matrix([D]) == (
        bad_P.basis*engine.multiplication_matrix([N]))
    common_rejected = False
    try:
        transport.verify_complete_original_zero_pole_pair(
            engine, bad_Z, bad_P, [N], [D],
            label="constructed extra common ideal must be rejected")
    except AssertionError:
        common_rejected = True
    assert common_rejected
    wrong_order_rejected = False
    try:
        transport.verify_complete_original_zero_pole_pair(
            engine, Z, ideal(t+1), [N], [D],
            label="constructed coprime but wrong pole order must be rejected")
    except AssertionError:
        wrong_order_rejected = True
    assert wrong_order_rejected
    return dict(
        actual_common_zeros_in_both_displayed_polynomials_retained=True,
        correct_primitive_positive_and_negative_pair_accepted=good,
        extra_common_ideal_passes_image_equation_but_is_rejected_by_unit_sum=True,
        coprime_pair_with_wrong_local_order_rejected_by_complete_image_gate=True,
        original_Y_function_or_shadow_generated=False)


def main():
    raw = REQUEST.read_bytes()
    request = json.loads(raw)
    assert request == {
        "schema":"rank2-original-whole-w-ideal-api/v1",
        "checks":["whole-two-chart-mixed-sources", "multiplicity-289",
                  "nonsplit-degree-two-thickness-three", "whole-W-squared-return",
                  "empty-divisor", "primitive-zero-pole-double-gate"],
        "original_geometry":False,
    }
    assert len(raw) <= 4096 and SAGE_VERSION == "10.6"
    assert os.environ["RANK2_IMAGE"] == IMAGE
    source = os.environ["RANK2_SOURCE_SHA"]
    assert len(source) == 40 and all(c in "0123456789abcdef" for c in source)
    assert os.environ["RANK2_RUN_ID"].isdecimal()
    assert os.environ["RANK2_RUN_ATTEMPT"].isdecimal()
    for name in SOURCE_FILES:
        ast.parse((HERE/name).read_text(encoding="utf-8"), filename=name)
    files = [HERE/name for name in SOURCE_FILES]+[
        REQUEST, WORKFLOW, ROOT/"README.md", TOPIC/"README.md"]
    manifest = dict(
        source=source, run_id=os.environ["RANK2_RUN_ID"],
        run_attempt=os.environ["RANK2_RUN_ATTEMPT"], image=IMAGE,
        sage_version=SAGE_VERSION, request=request,
        request_sha256=hashlib.sha256(raw).hexdigest(),
        source_sha256={str(p.relative_to(ROOT)):hashlib.sha256(p.read_bytes()).hexdigest()
                       for p in files},
        readme_blobs={"root":os.environ["RANK2_ROOT_README_SHA"],
                      "topic":os.environ["RANK2_TOPIC_README_SHA"]},
        source_mount_read_only=True, Sage_network_mode="none",
        original_geometric_input_generated=False)
    print("RANK2_WHOLE_W_IDEAL_API_MANIFEST "+canonical(manifest), flush=True)
    mixed = complete_mixed_two_chart_case()
    unit = complete_unit_pair_case()
    primitive = primitive_zero_pole_case()
    result = dict(
        kind="rank2_original_whole_W_ideal_API",
        status="constructed_complete_thick_sources_and_primitive_fraction_gates_passed",
        source=source, run_id=os.environ["RANK2_RUN_ID"],
        run_attempt=os.environ["RANK2_RUN_ATTEMPT"], image=IMAGE,
        sage_version=SAGE_VERSION, manifest_sha256=digest(manifest),
        complete_mixed_two_chart_case=mixed, complete_unit_pair=unit,
        complete_primitive_zero_pole_pair=primitive,
        all_source_ASTs_checked=True, source_file_count=len(SOURCE_FILES),
        original_306_W_matrix_divisors_intersections_or_shadow_computed=False,
        coefficient_or_data_file_written=False,
        elapsed_seconds=time.monotonic()-STARTED)
    payload = canonical(result)
    print("RANK2_WHOLE_W_IDEAL_API_RESULT "+payload, flush=True)
    print("RANK2_WHOLE_W_IDEAL_API_SHA256 "+hashlib.sha256(payload.encode()).hexdigest(),
          flush=True)


if __name__ == "__main__":
    main()
