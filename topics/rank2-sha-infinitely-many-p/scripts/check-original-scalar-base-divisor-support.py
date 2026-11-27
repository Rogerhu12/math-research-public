#!/usr/bin/env sage-python
"""Small full software checks for the scalar-base support reader.

All fixtures are finite free, genuinely nonreduced algebras of rank nine.
The reference is the unchanged general thick original decomposition.  This
does not construct the original curve, run a geometric source, or save data.
"""
import os
if (os.environ.get("GITHUB_ACTIONS") != "true" or
        os.environ.get("GITHUB_REPOSITORY") != "Rogerhu12/math-research-public"):
    raise SystemExit("Use only the named public research Actions.")

import hashlib
import json
import time
from pathlib import Path
from sage.all import GF, PolynomialRing, matrix, vector, identity_matrix
import original_scalar_base_divisor_support as support
import original_ys_closed_point_tools as closed
from original_ys_divisor_ideal_tools import (
    OriginalAffineIdeal, OriginalAffineIdealEngine,
    polynomial_matrix_digest, finite_field_coordinates, field_description)

HERE = Path(__file__).resolve().parent
STARTED = time.monotonic()


def canonical(value):
    return json.dumps(value, sort_keys=True, separators=(",", ":"))


def quiet(*args, **kwargs):
    pass


class SoftwareFiniteFreeEngine(OriginalAffineIdealEngine):
    """Only a software fixture; inherited complete ideal algorithms are real."""

    def __init__(self, infinity_chart=False):
        # Deliberately do not invoke the production constructor's rank-306
        # admission assertion.  This separate fixture is not an original chart.
        self.k = GF(29**2, "software_original_a")
        eta = self.k.multiplicative_generator()
        assert eta**((self.k.cardinality()-1)//2) == -1
        self.R = PolynomialRing(self.k, "software_t")
        t = self.R.gen()
        self.P = PolynomialRing(self.R, "software_x")
        x = self.P.gen()
        w = x-eta*t
        # At each t=0 and t=1 the full local dimensions are 2,3,4,
        # with residue degrees 1,1,2.  The t*(t-1) term deforms the
        # thick algebra, so this is not just a constant-product mock.
        self.F = (w**2*(w-1)**3*(w**2-eta)**2 + t*(t-1)*w).monic()
        self.dimension = int(self.F.degree())
        assert self.dimension == 9 and self.F.leading_coefficient() == 1
        self.infinity_chart = bool(infinity_chart)
        self.progress = quiet
        self.kernel_method = "hermite"
        self.identity = identity_matrix(self.R, self.dimension)
        self.unit = vector(self.R, [1]+[0]*(self.dimension-1))
        self.preflight = None
        self.started = time.monotonic()

        def product(left, right):
            a, b = self.element(left), self.element(right)
            polynomial = (self.P(list(a))*self.P(list(b))).quo_rem(self.F)[1]
            answer = vector(self.R, [polynomial[i] for i in range(self.dimension)])
            assert self.P(list(answer)) == polynomial
            return answer

        def operator(value):
            return matrix(self.R, [
                product(value, self.identity.row(j)) for j in range(self.dimension)])

        self.chart = {
            "constants": self.k, "polynomial_ring": self.R,
            "dimension": self.dimension, "infinity_chart": self.infinity_chart,
            "unit": self.unit, "multiply": product, "multiplication_matrix": operator,
            "software_fixture_not_original_geometry": True,
        }
        assert self.multiplication_matrix(self.unit) == self.identity
        self.fixture_eta = eta


def compare_point(actual, reference, engine):
    assert actual["identity"] == reference["identity"]
    assert actual["maximal_ideal"].basis == reference["maximal_ideal"].basis
    assert actual["degree_over_original_constants"] == reference["degree_over_original_constants"]
    assert actual["degree_over_base_prime_residue"] == reference["degree_over_base_prime_residue"]
    assert actual["base_prime_polynomial"] == reference["base_prime_polynomial"]
    assert actual["original_constants"] is reference["original_constants"] is engine.k
    fa, fr = actual["native_residue_field"], reference["native_residue_field"]
    assert field_description(fa) == field_description(fr)
    assert closed.native_absolute_degree(fa) == (
        closed.native_absolute_degree(engine.k)*actual["degree_over_original_constants"])
    # Compare ALL original ambient coordinates and the complete constant
    # power basis in the native residue coordinates, not just field degrees.
    for row in engine.identity.rows():
        va = actual["reduce_integral_element"](row)
        vr = reference["reduce_integral_element"](row)
        assert finite_field_coordinates(va, fa) == finite_field_coordinates(vr, fr)
    for j in range(closed.native_absolute_degree(engine.k)):
        value = engine.k.gen()**j
        va = actual["original_constant_embedding"](value)
        vr = reference["original_constant_embedding"](value)
        assert finite_field_coordinates(va, fa) == finite_field_coordinates(vr, fr)


def run_case(engine, h, session, registry, reference_registry, name, boundary=False):
    h = engine.R(h).monic()
    actual_ideal = engine.ideal_from_rows(h*engine.identity, "software actual "+name)
    assert actual_ideal.basis == h*engine.identity
    assert actual_ideal.determinant == h**engine.dimension
    old_points, old_receipt = closed.decompose_complete_ideal(
        engine, actual_ideal, reference_registry, label="software reference "+name,
        only_infinity_boundary=boundary, progress=quiet)
    new_points, new_receipt = session.decompose(
        engine, actual_ideal, registry, label="software scalar "+name,
        only_infinity_boundary=boundary, progress=quiet)
    assert new_receipt["complete_length"] == old_receipt["complete_degree"]
    assert new_receipt["all_nonreduced_intersection_lengths_retained"]
    assert not new_receipt["thick_local_hermite_ideals_materialized"]
    assert not new_receipt["general_thick_local_ideal_interface_claimed"]
    assert len(new_points) == len(old_points)
    old_by_fingerprint = {}
    for old in old_points:
        key = old["point"]["fingerprint"]
        assert key not in old_by_fingerprint
        old_by_fingerprint[key] = old
    matched = []
    for new in new_points:
        old = old_by_fingerprint[new["point"]["fingerprint"]]
        compare_point(new["point"], old["point"], engine)
        assert new["intersection_multiplicity"] == old["intersection_multiplicity"]
        assert new["full_local_k_length"] == old["full_local_k_length"]
        assert old["full_local_primary_ideal"].length == new["full_local_k_length"]
        assert old["full_local_primary_ideal"].receipt[
            "both_polynomial_row_module_inclusions_verified"]
        assert "full_local_primary_ideal" not in new
        assert "full_local_quotient" not in new
        assert "idempotent_in_complete_primary_quotient" not in new
        matched.append((
            new["point"]["degree_over_original_constants"],
            new["intersection_multiplicity"], new["full_local_k_length"]))
    assert sum(p["full_local_k_length"] for p in new_points) == new_receipt["complete_length"]
    nonreduced_dimensions = []
    for record in new_receipt["base_prime_components"]:
        dims = sorted(c["entire_nonreduced_fiber_local_dimension"]
                      for c in record["components"])
        degrees = sorted(c["relative_residue_degree"] for c in record["components"])
        assert dims == [2, 3, 4]
        assert degrees == [1, 1, 2]
        nonreduced_dimensions.append(dims)
    return new_points, {
        "case": name, "input_full_hnf_sha256": polynomial_matrix_digest(actual_ideal.basis),
        "only_infinity_boundary": boundary,
        "complete_length": new_receipt["complete_length"],
        "complete_point_length_records": sorted(matched),
        "entire_nonreduced_fiber_dimensions": nonreduced_dimensions,
        "all_reference_point_maximal_hnfs_equal": True,
        "all_reference_thick_local_lengths_equal": True,
        "all_ambient_residue_coordinates_and_original_constants_equal": True,
        "new_general_local_ideal_return_not_claimed": True,
        "reused_fiber_count": sum(
            bool(x["same_engine_and_full_prime_fiber_reused"])
            for x in new_receipt["base_prime_components"]),
        "reference_receipt_sha256": hashlib.sha256(canonical(old_receipt).encode()).hexdigest(),
        "filtration_receipt_sha256": hashlib.sha256(canonical(new_receipt).encode()).hexdigest(),
    }


def main():
    preparation = support.prepare_source_bindings()
    generic_before = closed.decompose_complete_ideal
    primary_before = closed.decompose_complete_primary_block
    original_geometry = support.ORIGINAL_GEOMETRY
    binding = support.bind_original_geometry_support()
    assert binding["original_geometry_module_binding_replaced"]
    assert closed.decompose_complete_ideal is generic_before
    assert closed.decompose_complete_primary_block is primary_before
    assert support.geometry.prepare_original_ys_geometry_with_complete_transports is (
        support.prepare_original_ys_geometry_with_scalar_base_support)
    again = support.bind_original_geometry_support()
    assert again["already_bound"]
    # The exact prepared body is audited without calling geometry.
    runner1, isolated1 = support._new_geometry_runner()
    runner2, isolated2 = support._new_geometry_runner()
    assert runner1.__code__ is runner2.__code__ is support.PREPARED.__code__
    assert runner1.__globals__ is not runner2.__globals__
    assert runner1.__globals__["_scalar_base_support_only"].__self__ is isolated1
    assert runner2.__globals__["_scalar_base_support_only"].__self__ is isolated2
    assert isolated1 is not isolated2 and isolated1.calls == isolated2.calls == []
    assert runner1.__globals__["decompose_complete_ideal"] is generic_before
    assert original_geometry.__globals__["decompose_complete_ideal"] is generic_before
    assert isolated1.expected_dimension == 306
    assert len(isolated1.allowed_labels) == 4

    engine = SoftwareFiniteFreeEngine()
    t = engine.R.gen()
    identity = {"software_fixture": "full_nonreduced_finite_free_rank_nine",
                "actual_base_field": field_description(engine.k)}
    registry = closed.OriginalClosedPointRegistry(identity)
    reference_registry = closed.OriginalClosedPointRegistry(identity)
    session = support.ScalarBaseSupportSession(expected_dimension=9)
    checks, previous_points = [], {}
    for m in (1, 2, 3):
        points, record = run_case(
            engine, t**m, session, registry, reference_registry, "thickness_"+str(m))
        if previous_points:
            for item in points:
                assert previous_points[item["point"]["fingerprint"]] is item["point"]
        previous_points = {item["point"]["fingerprint"]: item["point"] for item in points}
        assert sorted((x["point"]["degree_over_original_constants"],
                       x["intersection_multiplicity"], x["full_local_k_length"])
                      for x in points) == sorted([(1, 2*m, 2*m), (1, 3*m, 3*m), (2, 2*m, 4*m)])
        checks.append(record)

    points, record = run_case(
        engine, t**2*(t-1)**3, session, registry, reference_registry, "two_distinct_base_primes")
    assert record["complete_length"] == 45 and len(points) == 6
    checks.append(record)
    # Caller-owned item dictionaries are fresh; changing one must not alter
    # any cached whole fiber, multiplicity, or later support return.
    points[0]["intersection_multiplicity"] = -12345
    repeated, record = run_case(
        engine, t**2*(t-1)**3, session, registry, reference_registry, "repeat_after_item_mutation")
    assert all(x["intersection_multiplicity"] > 0 for x in repeated)
    assert record["reused_fiber_count"] == 2
    checks.append(record)

    infinity_engine = SoftwareFiniteFreeEngine(infinity_chart=True)
    s = infinity_engine.R.gen()
    points, record = run_case(
        infinity_engine, s**3*(s-1)**2, session, registry, reference_registry,
        "whole_infinity_boundary", boundary=True)
    assert record["complete_length"] == 27
    assert all(x["point"]["infinity_chart"] for x in points)
    checks.append(record)
    points, record = run_case(
        engine, engine.R.one(), session, registry, reference_registry, "complete_unit_ideal")
    assert not points and record["complete_length"] == 0
    checks.append(record)

    # Same determinant and total degree as t^2 I, but an unequal complete
    # HNF.  This must be refused before a residual algebra is consulted.
    H = (t**2*engine.identity).copy()
    H[0, 0], H[1, 1] = t**3, t
    fake = OriginalAffineIdeal(engine, H, t**(2*engine.dimension),
                               {"software_deliberate_non_scalar_input": True})
    assert H.is_hermite() and H.det() == fake.determinant
    refused = []
    before_fibers, before_calls = len(session._fibers), len(session.calls)
    try:
        session.decompose(engine, fake, registry, label="software false scalar", progress=quiet)
    except AssertionError as exc:
        refused.append(str(exc))
    else:
        raise AssertionError("Same determinant was incorrectly accepted as scalar ideal equality.")
    assert refused == [
        "Scalar-base support requires the whole actual HNF h*I, not its determinant."]
    assert len(session._fibers) == before_fibers and len(session.calls) == before_calls

    try:
        session.decompose(infinity_engine, infinity_engine.unit_ideal(), registry,
                          label="software overlapping reciprocal chart", progress=quiet)
    except AssertionError as exc:
        overlap_refused = str(exc)
    else:
        raise AssertionError("The entire reciprocal chart was accepted as disjoint support.")
    assert overlap_refused == (
        "The reciprocal chart overlaps the finite chart; keep only s=0.")

    files = tuple(dict.fromkeys((Path(__file__).name,)+support.SOURCE_DEPENDENCIES))
    report = {
        "kind": "original-scalar-base-support-software-check",
        "status": "PASS",
        "source": os.environ["RANK2_SOURCE_SHA"],
        "run_id": os.environ["RANK2_RUN_ID"],
        "run_attempt": os.environ["RANK2_RUN_ATTEMPT"],
        "root_readme_blob": os.environ["RANK2_ROOT_README_SHA"],
        "topic_readme_blob": os.environ["RANK2_TOPIC_README_SHA"],
        "source_file_sha256": {
            name: hashlib.sha256((HERE/name).read_bytes()).hexdigest() for name in files},
        "preparation": preparation, "binding": binding,
        "checks": checks,
        "same_determinant_non_scalar_hnf_refused": True,
        "reciprocal_chart_overlap_refused": True,
        "actual_original_native_residue_maps_compared_on_all_coordinates": True,
        "same_point_objects_reused_across_scalar_thicknesses": True,
        "current_selected_original_residual_class_used": True,
        "no_cross_geometry_session_cache": True,
        "generic_decomposer_and_return_schema_unchanged": True,
        "original_geometric_computation_executed": False,
        "original_mathematical_acceptance_claimed": False,
        "data_artifact_written": False,
        "elapsed_seconds": time.monotonic()-STARTED,
    }
    payload = canonical(report)
    print("RANK2_SCALAR_BASE_SUPPORT_API_RESULT "+payload, flush=True)
    print("RANK2_SCALAR_BASE_SUPPORT_API_SHA256 "+
          hashlib.sha256(payload.encode()).hexdigest(), flush=True)


if __name__ == "__main__":
    main()
