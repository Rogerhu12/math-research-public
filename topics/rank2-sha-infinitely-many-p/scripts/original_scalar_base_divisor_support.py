#!/usr/bin/env sage-python
"""Exact scalar-base divisor support in the original geometry entry only.

For a finite free A/k[t] and an ACTUAL ideal pi^m A, each local length is
m times the entire (possibly nonreduced) A/pi A local length.  The original
small residual algebra, residue fields, maximal ideals and registry remain.
This does not implement the general thick-local-ideal return interface.
"""
import os
if (os.environ.get("GITHUB_ACTIONS") != "true" or
        os.environ.get("GITHUB_REPOSITORY") != "Rogerhu12/math-research-public"):
    raise SystemExit("Use only the named public research Actions.")

import ast
from copy import copy
import hashlib
import inspect
import textwrap
from pathlib import Path
from types import FunctionType
import original_ys_geometry_transport as geometry
import original_ys_closed_point_tools as closed
import original_projector_hermite as projector
from original_ys_divisor_ideal_tools import (
    OriginalAffineIdealEngine, polynomial_digest, polynomial_matrix_digest)
from section_quotient_algebra import digest

HERE = Path(__file__).resolve().parent
PINNED = {
    "original_ys_geometry_transport.py": "cb39ebfb3b7adfa63c5d0ec2483354621938eb52381e957977f5e8f1544cd371",
    "original_ys_closed_point_tools.py": "7428cadb6b2179aebd547c749ec11ae46305476947aa443f7266e64d03ccc7bb",
    "original_projector_hermite.py": "545b330c4b7fb0c876e15f0ea6b94c9e35d29fdaf94b87707b3853dd33c32545",
    "original_ys_divisor_ideal_tools.py": "661075eecb9c7ba67da615c89fd3b7dbf2834b08ca8e1534c1713894dc1226d7",
}
SOURCE_DEPENDENCIES = tuple(dict.fromkeys(
    ("original_scalar_base_divisor_support.py",)+geometry.SOURCE_DEPENDENCIES+
    tuple(PINNED)))
ORIGINAL_GEOMETRY = geometry.prepare_original_ys_geometry_with_complete_transports
PREPARED = None
PREPARATION = None


def _whole_scalar_basis(engine, ideal):
    """Require equality of the ENTIRE actual HNF, before using its degree."""
    assert isinstance(engine, OriginalAffineIdealEngine)
    assert ideal.engine is engine
    n, R, H = engine.dimension, engine.R, ideal.basis
    assert n > 0 and H.base_ring() is R
    assert H.nrows() == H.ncols() == n and H.is_hermite()
    assert engine.identity.base_ring() is R
    assert engine.identity.nrows() == engine.identity.ncols() == n
    h = R(H[0, 0])
    assert h and h.leading_coefficient() == 1
    assert H == h*engine.identity, (
        "Scalar-base support requires the whole actual HNF h*I, not its determinant.")
    assert ideal.determinant == h**n
    assert ideal.length == n*int(h.degree())
    return h


def _point_data(fiber, component):
    engine = fiber.engine
    relative_degree = int(component["relative_residue_degree"])
    point_degree = int(fiber.pi.degree())*relative_degree
    native_field = component["residue_field"]
    assert closed.native_absolute_degree(native_field) == (
        closed.native_absolute_degree(engine.k)*point_degree)
    return {
        "degree_over_original_constants": point_degree,
        "degree_over_base_prime_residue": relative_degree,
        "base_prime_polynomial": fiber.pi,
        "base_residue_extension": fiber.base_extension,
        "native_residue_field": native_field,
        "native_residue_field_extension": component["residue_field_extension"],
        "original_constant_embedding": component["original_constant_embedding"],
        "reduce_integral_element": component["reduce_integral_element"],
        "actual_residue_coordinates_over_kpi": component["ambient_residue_coordinates"],
        "original_constants": engine.k,
    }


class ScalarBaseSupportSession:
    """Process-local complete fibers; one session belongs to one geometry call."""

    def __init__(self, expected_dimension=None, allowed_labels=None):
        self.expected_dimension = expected_dimension
        self.allowed_labels = None if allowed_labels is None else frozenset(allowed_labels)
        self.registry = None
        self._fibers = []
        self.calls = []

    def _fiber(self, engine, primary, pi, progress):
        for saved in self._fibers:
            if saved["engine"] is engine and saved["pi"] == pi:
                fiber = saved["fiber"]
                assert saved["ring"] is engine.R and saved["constants"] is engine.k
                assert saved["infinity_chart"] == engine.infinity_chart
                assert saved["selected_class"] is closed.OriginalSmallResidualAlgebra
                assert fiber.engine is engine and fiber.pi == pi
                assert fiber.dimension == engine.dimension
                assert fiber.relations.nrows() == 0
                assert fiber.specialize_matrix(primary.basis).is_zero()
                idempotents, splitting = fiber.primitive_idempotents()
                assert idempotents == saved["idempotent_snapshot"]
                assert splitting == saved["splitting"]
                return saved, True
        selected_class = closed.OriginalSmallResidualAlgebra
        # This is the CURRENT original class, including the production
        # complete linear-fiber and native residue-field bindings.
        fiber = selected_class(engine, primary, pi, progress=progress)
        assert fiber.engine is engine and fiber.pi == pi
        assert fiber.dimension == engine.dimension
        assert fiber.relations.nrows() == 0
        assert fiber.specialize_matrix(primary.basis).is_zero()
        frobenius = fiber.certify_frobenius()
        idempotents, splitting = fiber.primitive_idempotents()
        assert splitting["all_idempotents_orthogonal_and_sum_to_one"]
        snapshot = copy(idempotents)
        snapshot.set_immutable()
        components = tuple(
            fiber.residue_component(e, j) for j, e in enumerate(idempotents.rows()))
        assert sum(int(c["small_local_dimension"]) for c in components) == fiber.dimension
        assert sum(int(c["relative_residue_degree"]) for c in components) == (
            fiber.reduced_basis.nrows())
        for c in components:
            d, f = int(c["small_local_dimension"]), int(c["relative_residue_degree"])
            assert d >= f > 0 and d % f == 0
        saved = {
            "engine": engine, "ring": engine.R, "constants": engine.k,
            "infinity_chart": engine.infinity_chart,
            "pi": engine.R(pi.list()), "selected_class": selected_class,
            "fiber": fiber, "frobenius": frobenius,
            "splitting": splitting, "idempotent_snapshot": snapshot,
            "components": components,
        }
        self._fibers.append(saved)
        return saved, False

    def decompose(self, engine, ideal, registry, label="original scalar-base support",
                  only_infinity_boundary=False, progress=None):
        """Only support, actual residue maps and WHOLE multiplicities are returned."""
        progress = progress or closed._progress
        assert isinstance(registry, closed.OriginalClosedPointRegistry)
        if self.registry is None:
            self.registry = registry
        assert registry is self.registry
        assert ideal.engine is engine
        if self.expected_dimension is not None:
            assert engine.dimension == self.expected_dimension
        if self.allowed_labels is not None:
            assert label in self.allowed_labels
        boundary_receipt = None
        if only_infinity_boundary:
            assert engine.infinity_chart
            # Keep the original entire boundary computation and its HNF.
            target, boundary_receipt = engine.infinity_boundary(ideal)
        else:
            assert not engine.infinity_chart, (
                "The reciprocal chart overlaps the finite chart; keep only s=0.")
            target = ideal
        h = _whole_scalar_basis(engine, target)
        n = engine.dimension
        factors = [(engine.R(pi).monic(), int(m)) for pi, m in h.factor()]
        factor_product = engine.R.one()
        for pi, m in factors:
            assert m > 0 and pi.degree() > 0 and pi.is_irreducible()
            factor_product *= pi**m
        assert factor_product == h
        results, primary_records = [], []
        accounted = 0
        for factor_index, (pi, m) in enumerate(factors):
            primary_label = label + ": scalar base-prime " + str(factor_index)
            # Preserve the actual original primary-block constructor and all
            # its complete row returns.  No field-rank surrogate is accepted.
            primary, primary_receipt = engine.primary_block(
                target, pi, primary_label + ": whole original primary block")
            assert _whole_scalar_basis(engine, primary) == pi**m
            assert primary_receipt["norm_exponent"] == m*n
            assert primary.length == m*n*int(pi.degree())
            saved, reused = self._fiber(engine, primary, pi, progress)
            fiber = saved["fiber"]
            component_records = []
            primary_length = 0
            for j, component in enumerate(saved["components"]):
                d = int(component["small_local_dimension"])
                f = int(component["relative_residue_degree"])
                assert d > 0 and f > 0 and d % f == 0
                maximal = projector.complete_residue_maximal_ideal(
                    fiber, component, primary_label + ": actual maximal ideal " + str(j))
                assert maximal.engine is engine
                assert maximal.receipt["complete_original_residue_kernel"]
                assert maximal.receipt["both_polynomial_row_module_inclusions_verified"]
                assert maximal.length == int(pi.degree())*f
                # The actual pi^m module lies in this exact residue kernel.
                assert (fiber.specialize_matrix(primary.basis)*
                        component["ambient_residue_coordinates"]).is_zero()
                point, new_point = registry.register(
                    engine, maximal, _point_data(fiber, component))
                local_length = m*int(pi.degree())*d
                multiplicity = m*(d//f)
                assert local_length == multiplicity*point["degree_over_original_constants"]
                primary_length += local_length
                results.append({
                    "point": point,
                    "intersection_multiplicity": multiplicity,
                    "full_local_k_length": local_length,
                    "new_point_registered": new_point,
                    "length_method": "entire_pi_adic_filtration_of_actual_scalar_ideal",
                })
                component_records.append({
                    "component_index": j, "point_fingerprint": point["fingerprint"],
                    "full_maximal_ideal_sha256": polynomial_matrix_digest(maximal.basis),
                    "degree_over_original_constants": point["degree_over_original_constants"],
                    "relative_residue_degree": f,
                    "entire_nonreduced_fiber_local_dimension": d,
                    "scalar_thickness": m,
                    "full_local_k_length": local_length,
                    "actual_intersection_multiplicity": multiplicity,
                    "original_residue_component": component["receipt"],
                    "new_point_registered": new_point,
                })
            assert primary_length == primary.length
            accounted += primary_length
            primary_records.append({
                "label": primary_label, "primary": primary_receipt,
                "actual_scalar_primary_hnf_sha256": polynomial_matrix_digest(primary.basis),
                "scalar_thickness": m,
                "complete_primary_length": primary_length,
                "small_residual_frobenius": saved["frobenius"],
                "primitive_idempotent_split": saved["splitting"],
                "same_engine_and_full_prime_fiber_reused": reused,
                "components": component_records,
                "thick_local_hermite_ideals_materialized": False,
                "length_proof": "each_pi_filtration_layer_is_the_entire_A_mod_pi_component",
            })
            progress("complete original scalar-base support certified",
                     label=primary_label, full_quotient_length=primary_length,
                     scalar_thickness=m, closed_component_count=len(component_records),
                     all_nonreduced_fiber_dimensions_retained=True,
                     thick_local_hermite_ideals_materialized=False)
        assert accounted == target.length
        receipt = {
            "label": label,
            "method": "exact_scalar_base_filtration_with_original_full_residue_fields",
            "input_actual_hnf_sha256": polynomial_matrix_digest(ideal.basis),
            "target_actual_hnf_sha256": polynomial_matrix_digest(target.basis),
            "target_scalar_sha256": polynomial_digest(h),
            "target_determinant_sha256": polynomial_digest(target.determinant),
            "original_infinity_boundary": boundary_receipt,
            "whole_actual_hnf_equals_scalar_times_identity": True,
            "complete_length": accounted,
            "complete_degree": accounted,
            "closed_component_count": len(results),
            "actual_closed_point_count": len(results),
            "base_prime_factor_count": len(factors),
            "whole_original_infinity_fiber": bool(only_infinity_boundary),
            "all_closed_points_accounted": True,
            "complete_thick_length_identity_checked": True,
            "all_original_closed_points_accounted": True,
            "all_nonreduced_intersection_lengths_retained": True,
            "all_original_constant_embeddings_preserved": True,
            "point_identity_uses_complete_maximal_ideal_in_same_original_basis": True,
            "all_small_idempotents_orthogonal_and_sum_to_one": True,
            "thick_local_hermite_ideals_materialized": False,
            "general_thick_local_ideal_interface_claimed": False,
            "local_fraction_values_or_elliptic_trace_claimed": False,
            "base_prime_components": primary_records,
        }
        self.calls.append({
            "label": label, "infinity_chart": engine.infinity_chart,
            "only_infinity_boundary": bool(only_infinity_boundary),
            "complete_length": accounted, "receipt_sha256": digest(receipt),
        })
        return results, receipt


def _unbound_support(*args, **kwargs):
    raise AssertionError("A geometry call must install its own scalar-support session.")


def prepare_source_bindings():
    global PREPARED, PREPARATION
    for name, expected in PINNED.items():
        assert hashlib.sha256((HERE/name).read_bytes()).hexdigest() == expected
    if PREPARED is not None:
        return dict(PREPARATION)
    source = textwrap.dedent(inspect.getsource(ORIGINAL_GEOMETRY))
    old_name = "def prepare_original_ys_geometry_with_complete_transports("
    new_name = "def _prepare_geometry_with_scalar_base_support("
    old_call = "points,record = decompose_complete_ideal("
    new_call = "points,record = _scalar_base_support_only("
    assert source.count(old_name) == source.count(old_call) == 1
    generated = source.replace(old_name, new_name, 1).replace(old_call, new_call, 1)
    assert generated.count(new_call) == 1
    assert old_call not in generated
    assert generated.replace(new_name, old_name, 1).replace(new_call, old_call, 1) == source
    ast.parse(generated)
    namespace = dict(ORIGINAL_GEOMETRY.__globals__)
    namespace["_scalar_base_support_only"] = _unbound_support
    exec(compile(generated, str(HERE/"original_scalar_base_divisor_support.py")+
                 ":prepared-original-geometry", "exec"), namespace)
    PREPARED = namespace["_prepare_geometry_with_scalar_base_support"]
    assert PREPARED.__defaults__ == ORIGINAL_GEOMETRY.__defaults__
    assert PREPARED.__closure__ is None
    assert namespace["decompose_complete_ideal"] is (
        ORIGINAL_GEOMETRY.__globals__["decompose_complete_ideal"])
    PREPARATION = {
        "original_geometry_source_sha256": hashlib.sha256(source.encode()).hexdigest(),
        "prepared_geometry_source_sha256": hashlib.sha256(generated.encode()).hexdigest(),
        "only_body_change_is_one_support_call": True,
        "original_general_decomposer_binding_unchanged": True,
        "original_geometry_gates_and_return_object_unchanged": True,
        "pinned_source_sha256": dict(PINNED),
    }
    return dict(PREPARATION)


def _new_geometry_runner():
    """Construct the isolated runner without executing any geometry."""
    prepare_source_bindings()
    session = ScalarBaseSupportSession(
        expected_dimension=306,
        allowed_labels=("all original cusps:positive", "all original cusps:negative",
                        "all original cubic branching:positive",
                        "all original cubic branching:negative"))
    namespace = dict(PREPARED.__globals__)
    namespace["_scalar_base_support_only"] = session.decompose
    runner = FunctionType(PREPARED.__code__, namespace, PREPARED.__name__,
                          PREPARED.__defaults__, PREPARED.__closure__)
    runner.__kwdefaults__ = PREPARED.__kwdefaults__
    assert runner.__globals__["decompose_complete_ideal"] is (
        ORIGINAL_GEOMETRY.__globals__["decompose_complete_ideal"])
    return runner, session


def prepare_original_ys_geometry_with_scalar_base_support(
        six, progress=None, kernel_method="minimal"):
    runner, session = _new_geometry_runner()
    result = runner(six, progress=progress, kernel_method=kernel_method)
    assert len(session.calls) == 8
    context, receipt = result
    assert context["six"] is six and context["certificate"] is receipt
    assert receipt["original_geometric_cusp_count"] == 108
    assert receipt["original_cubic_ramified_geometric_count"] == 54
    return result


def bind_original_geometry_support():
    """Call before any producer captures the original geometry callable."""
    preparation = prepare_source_bindings()
    selected = prepare_original_ys_geometry_with_scalar_base_support
    current = geometry.prepare_original_ys_geometry_with_complete_transports
    already = current is selected
    assert already or current is ORIGINAL_GEOMETRY
    if not already:
        geometry.prepare_original_ys_geometry_with_complete_transports = selected
    assert geometry.prepare_original_ys_geometry_with_complete_transports is selected
    return {
        "original_geometry_module_binding_replaced": not already,
        "already_bound": already,
        "general_decompose_complete_ideal_unchanged": True,
        "general_primary_decomposer_and_producer_schema_unchanged": True,
        "per_geometry_session_no_cross_engine_or_registry_alias": True,
        "production_must_bind_before_triangular_producer_import": True,
        "preparation": preparation,
    }
