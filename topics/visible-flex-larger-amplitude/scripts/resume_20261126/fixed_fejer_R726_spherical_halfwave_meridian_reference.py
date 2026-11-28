#!/usr/bin/env python3
"""Fixed supported unit-meridian reference for the complete outer SO(3) space.

The exact boundary is the independent R726 shortest spherical interpolation.
Its complete three-coordinate mean and both angular jets are solved again from
that actual boundary function. The R711 scalar amplitude, opposite R724 paired
halfwaves, and complete fixed-epsilon R725 three-piece C3 cutoff are retained.
Old Euclidean boundary roots, R709 ball potentials and R722 posterior formulas
are not inherited; R726 existence and uniqueness remain conditional until paid.
The original unit meridian outside two fixed supports is unchanged.
Each physical halfwave has six exact pieces; the auxiliary amplitude rule
still uses all twelve original R711 pieces. Three mean variables and one amplitude are determined at each
fixed material-chart angle.  This provider is frozen from the predeclared fixed Fejer
reference core and its complete working height.  It never consumes the current outer free vector.

The working mean equations, complete positive quadratures, scalar carriers,
normalizations and angular jets are evaluated only in public Actions.
Returned working values are not continuous/root/rounding/geometry certificates.
"""
from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction as F
from functools import cmp_to_key
import hashlib
import inspect
import json
import math
import os
from pathlib import Path
import time

import numpy as np

SCHEMA = "complete-fixed-fejer-R726-spherical-boundary-paired-halfwave-meridian-seed-reference-v1"
ORIGINAL_REFERENCE_SCHEMA = "R690-fixed-fejer-axisymmetric-SO3-reference-input-v1"
ORIGINAL_REFERENCE_SHA = "e7175f591a14844331b55c9c09cc6d0ff25f1e2f390706c951f9b6a6008322cb"
MEAN_KERNEL_SCHEMA = "complete-R726-spherical-boundary-paired-halfwave-seed-working-mean-and-angular-jets-v1"
MEAN_KERNEL_SHA = "2513e4b0b8e6f895e4b9a53da2d938bb109937a3ab577e09c67558e37d128d23"
DEFAULT_SUPPORT = (("1/32", "15/32"), ("17/32", "31/32"))

BOUNDARY_CUTOFF_EPSILON = "1/8"
BOUNDARY_CUTOFF_SCHEMA = "complete-fixed-width-three-piece-C3-boundary-cutoff-v1"


def _flat_cutoff_polynomial_jets(t, epsilon):
    """Exact arithmetic for Fraction inputs; working arithmetic for float inputs."""
    zero, one = t*0, t*0+1
    if t <= zero:
        return zero, zero, zero, zero
    if t >= one:
        return one, zero, zero, zero
    denominator = one-epsilon
    if epsilon <= t <= one-epsilon:
        return (t-epsilon/2)/denominator, one/denominator, zero, zero
    reflected = t > one-epsilon
    u = (one-t)/epsilon if reflected else t/epsilon
    G = (u*u*u*u)*(5+u*(-6+2*u))/2
    S = u*u*u*(10+u*(-15+6*u))
    S1 = 30*u*u*(one-u)*(one-u)
    S2 = 60*u*(one-u)*(one-2*u)
    value = epsilon*G/denominator
    first = S/denominator
    second = S1/(epsilon*denominator)
    third = S2/(epsilon*epsilon*denominator)
    if reflected:
        return one-value, first, -second, third
    return value, first, second, third


def boundary_cutoff_exact_jets(t):
    """R725 value and first three normalized-coordinate derivatives, all exact."""
    t = exact_fraction(t, "boundary cutoff coordinate")
    return _flat_cutoff_polynomial_jets(t, F(BOUNDARY_CUTOFF_EPSILON))


def boundary_cutoff_working_jets(t):
    """The same complete three pieces, with explicit working float arithmetic."""
    t = float(t)
    if not math.isfinite(t) or not 0. <= t <= 1.:
        raise ValueError("Use a finite complete boundary cutoff coordinate in [0,1]")
    result = _flat_cutoff_polynomial_jets(t, float(F(BOUNDARY_CUTOFF_EPSILON)))
    if (len(result) != 4 or any(not math.isfinite(v) for v in result)
            or not 0. <= result[0] <= 1. or result[1] < 0):
        raise ValueError("A complete boundary cutoff jet is nonfinite or outside its working range")
    return tuple(float(v) for v in result)


def boundary_cutoff_definition(support, central):
    """Complete fixed-rational three-piece law and every exact physical cut."""
    epsilon = F(BOUNDARY_CUTOFF_EPSILON)
    support = tuple(tuple(F(v) for v in pair) for pair in support)
    central = tuple(tuple(F(v) for v in pair) for pair in central)
    if (epsilon != F(1,8) or len(support) != 2 or len(central) != 2
            or any(len(pair) != 2 for pair in support+central)):
        raise ValueError("This source fixes the complete R725 cutoff at epsilon=1/8")
    edges = (F(0), epsilon, F(1)-epsilon, F(1))
    layers = []
    for index, ((left, right), (ca, cb)) in enumerate(zip(support, central)):
        if not left < ca < cb < right:
            raise ValueError("Every complete original boundary and central interval is required")
        for side, a, b, orientation in (("left", left, ca, 1), ("right", cb, right, -1)):
            physical = tuple(a+(b-a)*v for v in edges)
            layers.append(dict(support_index=index, side=side,
                exact_relative_interval=[str(a),str(b)],
                exact_relative_piece_edges=[str(v) for v in physical],
                exact_relative_internal_cuts=[str(v) for v in physical[1:-1]],
                original_interval_normalized_piece_edges=[str(v) for v in edges],
                cutoff_coordinate="t" if orientation == 1 else "1-t",
                odd_material_derivative_orientation=orientation,
                physical_piece_count=3,
                branches_in_increasing_material_order=(
                    ["left-polynomial","affine","right-reflection"] if orientation == 1 else
                    ["right-reflection","affine","left-polynomial"])))
    return dict(schema=BOUNDARY_CUTOFF_SCHEMA, proof_result="R725",
        exact_epsilon=str(epsilon), epsilon_is_a_fixed_source_parameter=True,
        epsilon_depends_on_angle_mean_direction_or_outer_point=False,
        accurate_law="C=epsilon*G(t/epsilon)/(1-epsilon); (t-epsilon/2)/(1-epsilon); 1-epsilon*G((1-t)/epsilon)/(1-epsilon)",
        exact_G_ascending_coefficients=["0","0","0","0","5/2","-3","1"],
        exact_velocity_S5_ascending_coefficients=["0","0","0","10","-15","6"],
        exact_normalized_piece_edges=[str(v) for v in edges],
        constant_extension_outside_unit_interval=True,
        piecewise_polynomial_degree=[6,1,6],
        matching_material_derivative_order=3,
        fourth_material_derivative_continuity_claimed=False,
        exact_cut_values_and_first_three_normalized_jets=[
            [str(v) for v in boundary_cutoff_exact_jets(t)] for t in edges],
        exact_first_derivative_peak=str(F(1)/(1-epsilon)),
        exact_derivative_integral="1", exact_value_integral="1/2",
        four_boundary_layers=layers, complete_physical_boundary_piece_count=12,
        complete_new_internal_boundary_cut_count=8,
        original_central_halfwave_profile_changed=False,
        original_bubble_gamma_and_raw_defect_lift_changed=False,
        working_arithmetic="binary64 evaluation of this complete exact-rational law",
        working_rounding_or_integration_error_enclosed=False)


def require_actions():
    if (os.environ.get("GITHUB_ACTIONS") != "true"
            or os.environ.get("GITHUB_REPOSITORY") != "Rogerhu12/math-research-public"):
        raise RuntimeError("Scientific paired-halfwave reference evaluation requires public repository Actions")


def sha(path):
    h = hashlib.sha256()
    with Path(path).open("rb") as stream:
        for block in iter(lambda: stream.read(1 << 20), b""):
            h.update(block)
    return h.hexdigest()


def canonical(value):
    return hashlib.sha256(json.dumps(value, sort_keys=True, separators=(",", ":"),
        allow_nan=False).encode()).hexdigest()


def array_sha(value):
    value = np.ascontiguousarray(value)
    h = hashlib.sha256(str(value.dtype).encode())
    h.update(json.dumps(list(value.shape)).encode())
    h.update(value.tobytes())
    return h.hexdigest()


def array_record(value):
    value = np.ascontiguousarray(value)
    return dict(shape=list(value.shape), dtype=str(value.dtype), sha256=array_sha(value))


def file_record(path):
    path = Path(path).resolve()
    return dict(path=str(path), bytes=path.stat().st_size, sha256=sha(path))


def write_json(path, value):
    path = Path(path)
    temporary = path.with_name(path.name+".partial")
    temporary.write_text(json.dumps(value, indent=2, allow_nan=False)+"\n")
    temporary.replace(path)


def exact_fraction(value, name):
    if not isinstance(value, (str, F)):
        raise ValueError(name+" must be an exact rational string or Fraction")
    result = F(value)
    if isinstance(value, str) and str(result) != value:
        raise ValueError(name+" must use the canonical Fraction spelling")
    return result


def positive_integer(value, name):
    if isinstance(value, (bool, np.bool_)) or int(value) != value or int(value) < 1:
        raise ValueError(name+" must be a positive integer")
    return int(value)


@dataclass(frozen=True)
class SeedParameters:
    support_intervals: tuple = DEFAULT_SUPPORT
    relative_boundary_total_length: str = "1/16"
    profile_delta: str = "1/128"
    radial_quadrature_order: int = 8
    profile_quadrature_order: int = 16
    mean_maxiter: int = 128
    mean_tolerance: float = 2.e-12
    scalar_iterations: int = 64
    mean_backtracks: int = 24
    mean_armijo: float = 1.e-4
    boundary_cutoff_epsilon: str = BOUNDARY_CUTOFF_EPSILON

    def definitions(self):
        support = tuple(tuple(exact_fraction(x, "support endpoint") for x in pair)
                        for pair in self.support_intervals)
        if (len(support) != 2 or any(len(pair) != 2 for pair in support)
                or not F(0) < support[0][0] < support[0][1] < support[1][0] < support[1][1] < F(1)):
            raise ValueError("Use two complete disjoint strictly interior support intervals")
        if support != tuple(tuple(F(x) for x in pair) for pair in DEFAULT_SUPPORT):
            raise ValueError("This complete first seed uses the two original wide-control support endpoints")
        cutoff_epsilon = exact_fraction(self.boundary_cutoff_epsilon, "boundary cutoff epsilon")
        if cutoff_epsilon != F(BOUNDARY_CUTOFF_EPSILON):
            raise ValueError("This complete source fixes boundary cutoff epsilon=1/8")
        boundary = exact_fraction(self.relative_boundary_total_length, "boundary total length")
        profile_delta = exact_fraction(self.profile_delta, "smooth-triangle profile delta")
        if not F(0) < profile_delta < F(1, 8):
            raise ValueError("Keep the exact twelve-piece smooth-triangle profile_delta in (0,1/8)")
        if not F(0) < boundary < 2*min(right-left for left, right in support):
            raise ValueError("Each support must retain a positive central interval")
        delta = boundary/(2*len(support))
        central = tuple((left+delta, right-delta) for left, right in support)
        if any(not left < a < b < right
               for (left, right), (a, b) in zip(support, central)):
            raise ValueError("Every boundary layer and central interval must have positive exact length")
        if central[0][1]-central[0][0] != central[1][1]-central[1][0]:
            raise ValueError("The two complete paired-halfwave central lengths must be exactly equal")
        ints = {name: positive_integer(getattr(self, name), name) for name in (
            "radial_quadrature_order", "profile_quadrature_order", "mean_maxiter",
            "scalar_iterations", "mean_backtracks")}
        tolerance, armijo = float(self.mean_tolerance), float(self.mean_armijo)
        if not math.isfinite(tolerance) or tolerance <= 0:
            raise ValueError("Use a finite positive physical mean tolerance")
        if not math.isfinite(armijo) or not 0 < armijo < 1:
            raise ValueError("Use a finite mean Armijo coefficient in (0,1)")
        return support, central, boundary, delta, profile_delta, ints, tolerance, armijo


class SeedReferenceFailure(RuntimeError):
    def __init__(self, message, record):
        super().__init__(message)
        self.record = record


def _S5(t):
    return t*t*t*(10.+t*(-15.+6.*t))


def _S5_prime(t):
    return 30.*t*t*(1.-t)*(1.-t)


def _profile(t, profile_delta, kernel):
    """Use the same full R711 evaluator as the bound complete mean rule."""
    return kernel.smooth_triangle_value_and_derivative(t, profile_delta)


def paired_halfwave_definition(central, profile_delta):
    """Exact complete radial profile; no numerical mean or field evaluation."""
    central = tuple(tuple(F(v) for v in pair) for pair in central)
    delta = F(profile_delta)
    if (len(central) != 2 or any(len(pair) != 2 for pair in central)
            or not F(0) < delta < F(1, 8)
            or not F(0) < central[0][1]-central[0][0]
            or central[0][1]-central[0][0] != central[1][1]-central[1][0]):
        raise ValueError("The paired halfwaves require two complete equal positive central intervals")
    edges = (F(0), 2*delta, F(1,2)-2*delta, F(1,2),
             F(1,2)+2*delta, F(1)-2*delta, F(1))
    if any(a >= b for a, b in zip(edges, edges[1:])):
        raise ValueError("Every one of the six exact halfwave pieces is required")
    return dict(schema="complete-equal-central-intervals-paired-halfwave-profile-v1",
        auxiliary_profile="the original complete R711 h_delta on [0,1]",
        auxiliary_mean_kernel_source_sha256=MEAN_KERNEL_SHA,
        auxiliary_mean_rule_piece_count=12,
        physical_central_interval_count=2, physical_piece_count_per_interval=6,
        complete_physical_pair_piece_count=12,
        exact_profile_delta=str(delta),
        exact_normalized_piece_edges=[str(v) for v in edges],
        exact_relative_central_intervals=[[str(v) for v in pair] for pair in central],
        exact_relative_central_each_length=str(central[0][1]-central[0][0]),
        exact_relative_physical_piece_edges=[
            [str(a+(b-a)*v) for v in edges] for a,b in central],
        signs_in_radial_discovery_order=[1,-1],
        physical_profile="sign[index]*h_delta(t/2); t=(s-a)/(b-a)",
        radial_derivative_chain_factor="1/2",
        combined_cosine_mean="Lc*A_delta(lambda)*d",
        combined_transverse_mean="zero by equal complete central lengths and opposite signs",
        transverse_mean_zero_in_each_individual_interval=False,
        old_per_interval_odd_physical_profile_inherited=False)


class SupportedUnitMeridianJet:
    """Fixed reference; every requested angle uses one cached complete mean root."""

    def __init__(self, problem, prepared, *, expected_bundle_sha256=None,
                 seed_parameters=None, mean_kernel_module=None, cache_directory=None):
        require_actions()
        c = problem.axisymmetric_reference_context
        if (c.model.get("schema") != ORIGINAL_REFERENCE_SCHEMA
                or c.model.get("source_sha256") != ORIGINAL_REFERENCE_SHA
                or canonical(c.model) != c.identity
                or expected_bundle_sha256 != c.input_records["reference_bundle"]["sha256"]
                or sha(inspect.getfile(type(c))) != ORIGINAL_REFERENCE_SHA
                or sha(inspect.getfile(type(c.law))) != ORIGINAL_REFERENCE_SHA
                or sha(c.reference_at.__func__.__code__.co_filename) != ORIGINAL_REFERENCE_SHA
                or not np.array_equal(prepared.core, c.core)
                or float(prepared.height).hex() != float(c.height).hex()
                or c.scalar_identity != c.model["fixed_scalar_metric_identity_sha256"]
                or canonical(c.scalar_definition) != c.scalar_identity):
            raise ValueError("Bind the complete actual original reference, scalar, chart, core and H")
        if (mean_kernel_module is None
                or sha(mean_kernel_module.__file__) != MEAN_KERNEL_SHA
                or mean_kernel_module.SCHEMA != MEAN_KERNEL_SCHEMA
                or sha(mean_kernel_module.solve_mean_jets.__code__.co_filename) != MEAN_KERNEL_SHA
                or sha(mean_kernel_module.smooth_triangle_value_and_derivative.__code__.co_filename) != MEAN_KERNEL_SHA
                or sha(mean_kernel_module.spherical_boundary_jets.__code__.co_filename) != MEAN_KERNEL_SHA
                or sha(mean_kernel_module.spherical_boundary_definition.__code__.co_filename) != MEAN_KERNEL_SHA):
            raise ValueError("Bind the complete declared working mean and angle-jet source")
        if seed_parameters is None:
            seed_parameters = SeedParameters()
        if type(seed_parameters) is not SeedParameters:
            raise ValueError("Use this source's complete SeedParameters value")
        (support, central, boundary, delta, profile_delta, ints,
         tolerance, armijo) = seed_parameters.definitions()
        self.context, self.kernel, self.parameters = c, mean_kernel_module, seed_parameters
        self.support, self.central = support, central
        self.boundary, self.delta, self.profile_delta = boundary, delta, profile_delta
        self.physical_profile_definition = paired_halfwave_definition(central, profile_delta)
        self.boundary_cutoff_definition = boundary_cutoff_definition(support, central)
        self.spherical_boundary_definition = mean_kernel_module.spherical_boundary_definition()
        self.boundary_cutoff_epsilon = F(seed_parameters.boundary_cutoff_epsilon)
        self.boundary_cutoff_breakpoints = tuple(F(v) for v in
            self.boundary_cutoff_definition["exact_normalized_piece_edges"])
        self.profile_breakpoints = tuple(F(v) for v in
            self.physical_profile_definition["exact_normalized_piece_edges"])
        self.integer_parameters, self.tolerance, self.armijo = ints, tolerance, armijo
        self.core, self.height = np.array(c.core, copy=True), float(c.height)
        self.core.setflags(write=False)
        self.freq = 2*np.arange(1, c.M+1, dtype=float)
        self.qfreq = 1-self.freq*self.freq
        self.freq.setflags(write=False)
        self.qfreq.setflags(write=False)
        self.cache_directory = None if cache_directory is None else Path(cache_directory)
        self._plan = None
        self._radial_cache = {}
        self._mean_cache = {}
        self._mean_batches = []
        self.last_failure = None
        self.maximum_scalar_errors = np.zeros(4)
        self.counts = dict(reference_evaluations=0, requested_points=0,
            radial_query_batches=0, original_scalar_queries=0, exact_split_scalar_queries=0,
            mean_angle_requests=0, new_mean_angles=0, mean_batches=0,
            mean_cache_hits=0, completed_mean_angles=0)
        self.working_definition = dict(
            schema="R726-spherical-boundary-paired-halfwave-reference-working-definition-v1",
            spherical_boundary_definition=self.spherical_boundary_definition,
            mean_and_field_use_same_raw_v_and_full_two_angular_jet_graph=True,
            old_R709_potential_or_R722_posterior_formula_inherited=False,
            R726_acute_domain_and_existence_hypotheses_certified=False,
            radial_rule="all original exact-affine cells split at every support/boundary edge, both internal cuts in every R725 boundary layer and all six physical halfwave pieces per central interval; complete positive Gauss on every outside and boundary piece",
            physical_boundary_cutoff_definition=self.boundary_cutoff_definition,
            exact_boundary_cutoff_epsilon=str(self.boundary_cutoff_epsilon),
            old_boundary_quadrature_mean_root_or_cache_inherited=False,
            original_outer_whole_cell_Gauss_and_partial_rule_is_separate=True,
            radial_quadrature_order=ints["radial_quadrature_order"],
            central_profile_rule="the auxiliary A_delta and its two lambda derivatives retain all twelve original exact R711 pieces with positive Gauss and no weight renormalization; physical sine means cancel only across the two equal opposite halfwaves",
            physical_central_profile_definition=self.physical_profile_definition,
            auxiliary_mean_metadata_describes_original_full_R711_rule=True,
            physical_profile_is_not_the_auxiliary_full_period_on_each_interval=True,
            actual_field_quadrature_or_closure_words_inherited_from_original_seed=False,
            profile_quadrature_order=ints["profile_quadrature_order"],
            scalar_carriers="complete bound 4e scalar law and saved point carriers; normalize (b,c), differentiate the same normalization",
            mean_algorithm="complete three-component residual-backtracked Newton",
            mean_maxiter=ints["mean_maxiter"], mean_backtracks=ints["mean_backtracks"],
            mean_armijo_hex=armijo.hex(), mean_physical_tolerance_hex=tolerance.hex(),
            scalar_iterations=ints["scalar_iterations"],
            common_exact_support_and_boundary_lengths=True,
            mean_unknowns=3, scalar_amplitude_unknowns=1,
            fixed_root_cache_key="literal fixed-chart angle binary64 hex; full mean and two angular jets at the same point",
            current_outer_free_point_is_not_an_input=True,
            exact_S_and_affine_nodes_inherited=True,
            scalar_normalization_trigonometric_quadrature_and_root_errors_enclosed=False,
            full_outer_field_quadrature_is_separate=True,
            no_q_less_than_one_numerical_gate=True,
            uniform_R708_or_R709_hypotheses_certified=False,
            exact_seed_or_full_field_geometry_certified=False)
        self.model = dict(
            schema=SCHEMA, source_sha256=sha(__file__),
            original_reference_source_sha256=ORIGINAL_REFERENCE_SHA,
            mean_kernel_source_sha256=MEAN_KERNEL_SHA,
            initial_reference_bundle_sha256=c.input_records["reference_bundle"]["sha256"],
            initial_reference_model_identity_sha256=c.identity,
            complete_axisymmetric_reference_model=c.model,
            fixed_scalar_metric_identity_sha256=c.scalar_identity,
            fixed_scalar_profile_definition=c.scalar_definition,
            fixed_chart_core_sha256=array_sha(self.core),
            initial_height_hex=self.height.hex(),
            exact_relative_support_intervals=[[str(x) for x in pair] for pair in support],
            exact_relative_boundary_total_length=str(boundary),
            exact_profile_delta=str(profile_delta),
            exact_boundary_cutoff_epsilon=str(self.boundary_cutoff_epsilon),
            boundary_cutoff_definition=self.boundary_cutoff_definition,
            mathematical_amplitude_interval="(0,pi)",
            mathematical_profile_piece_count=6,
            mathematical_profile_piece_count_scope="one physical central interval",
            auxiliary_mean_profile_piece_count=12,
            complete_physical_pair_piece_count=12,
            paired_halfwave_definition=self.physical_profile_definition,
            old_five_piece_working_cache_or_geometry_inherited=False,
            exact_relative_boundary_each_end_length=str(delta),
            exact_relative_central_intervals=[[str(x) for x in pair] for pair in central],
            accurate_definition="fixed original unit T0 outside U; R726 S_chi(T0,d) on all boundary layers; cos(lambda*h_delta(t/2))*d+sign[index]*sin(lambda*h_delta(t/2))*w on the two equal central intervals",
            spherical_boundary_definition=self.spherical_boundary_definition,
            accurate_mean_definition="Lc*v+integral_E S_chi(T0,N(v))=P_original-Gamma_original-integral_complement_U T0; a_delta(lambda)=norm(v)",
            w_definition="normalized(er(theta0)-(er(theta0).d)*d)",
            boundary_cutoff="R725 fixed epsilon=1/8 three-piece C3 cutoff from original T0 to d at each support end; first three endpoint jets zero; two exact internal cuts per boundary layer",
            central_profile="paired opposite six-piece C3 halfwaves of the full R711 h_delta; first +h_delta(t/2), second -h_delta(t/2); all exact physical breakpoints retained",
            seed_is_frozen_from_original_initial_point=True,
            outer_current_core_height_and_all_rotation_variables_retained=True,
            working_definition=self.working_definition)
        self.model_identity = canonical(self.model)
        self.binding = dict(
            schema=SCHEMA, source_sha256=sha(__file__),
            reference_bundle=c.input_records["reference_bundle"],
            reference_model_identity_sha256=c.identity,
            supported_unit_seed_model_identity_sha256=self.model_identity,
            fixed_scalar_metric_identity_sha256=c.scalar_identity,
            complete_original_reference_input_records=c.input_records,
            original_reference_source_sha256=ORIGINAL_REFERENCE_SHA,
            mean_kernel_source_sha256=MEAN_KERNEL_SHA,
            original_optimized_q_field_used=False,
            seed_core_and_H_frozen_but_outer_free_variables_unchanged=True)

    def _fail(self, phase, reason, **details):
        record = dict(schema=SCHEMA, complete=False, failure_phase=phase, reason=str(reason),
            source_sha256=sha(__file__), seed_model_identity_sha256=self.model_identity,
            fixed_scalar_metric_identity_sha256=self.context.scalar_identity,
            counts=dict(self.counts), continuous_certificate=False, **details)
        self.last_failure = record
        if self.cache_directory is not None and self.cache_directory.is_dir():
            path = self.cache_directory/"supported-smooth-triangle-reference-last-failure.json"
            write_json(path, record)
            self.last_failure = dict(record, runner_raw_failure_file=file_record(path))
        raise SeedReferenceFailure(str(reason), self.last_failure)

    def _compare(self, a, b):
        if a == b:
            return 0
        box = self.context.full.affine_time(a[0]-b[0], a[1]-b[1])
        if box[1] < 0:
            return -1
        if box[0] > 0:
            return 1
        self._fail("exact_affine_partition",
            "The accurate scalar box does not order two distinct affine locations",
            left=[str(x) for x in a], right=[str(x) for x in b],
            difference_integer_box=[str(int(x)) for x in box],
            integer_scale=str(self.context.full.h.S))

    def _width(self, a, b):
        box = self.context.full.affine_time(b[0]-a[0], b[1]-a[1])
        if box[0] <= 0:
            self._fail("exact_affine_partition", "A complete exact piece lacks a positive lower width",
                left=[str(x) for x in a], right=[str(x) for x in b])
        value = self.context.full.carrier(box)
        if not math.isfinite(value) or value <= 0:
            self._fail("exact_affine_partition", "A positive exact width has no positive working carrier")
        return value

    def _carrier(self, a):
        return self.context.full.carrier(self.context.full.affine_time(*a))

    @staticmethod
    def _affine_point(a, b, u):
        u = F(float(u))
        return tuple((1-u)*x+u*y for x, y in zip(a, b))

    def _region(self, point):
        for index, ((left, right), (ca, cb)) in enumerate(zip(self.support, self.central)):
            lo, hi, a, b = tuple((v, F(0)) for v in (left, right, ca, cb))
            if self._compare(point, lo) < 0 or self._compare(point, hi) > 0:
                continue
            if self._compare(point, a) < 0:
                return "left", index
            if self._compare(point, b) > 0:
                return "right", index
            return "central", index
        return "outside", -1

    def _scaled_coordinate(self, point, lo, hi):
        if point == lo:
            return 0.
        if point == hi:
            return 1.
        numerator = self._carrier((point[0]-lo[0], point[1]-lo[1]))
        result = numerator/self._width(lo, hi)
        if not math.isfinite(result) or not 0. <= result <= 1.:
            self._fail("piece_coordinate", "An exact internal location has an unusable working piece coordinate",
                point=[str(x) for x in point], left=[str(x) for x in lo],
                right=[str(x) for x in hi], actual_coordinate=repr(result))
        return result

    def _cutoff_and_profile(self, point, kind, index):
        if kind == "outside":
            return 0., 0., 0., 0.
        left, right = self.support[index]
        ca, cb = self.central[index]
        if kind == "left":
            a, b = (left, F(0)), (ca, F(0))
            t = self._scaled_coordinate(point, a, b)
            cutoff = boundary_cutoff_working_jets(t)
            return cutoff[0], float(cutoff[1]/self._width(a, b)), 0., 0.
        if kind == "right":
            a, b = (cb, F(0)), (right, F(0))
            t = self._scaled_coordinate(point, a, b)
            cutoff = boundary_cutoff_working_jets(1.-t)
            return cutoff[0], float(-cutoff[1]/self._width(a, b)), 0., 0.
        a, b = (ca, F(0)), (cb, F(0))
        t = self._scaled_coordinate(point, a, b)
        h, ht = _profile(np.array([.5*t]), self.profile_delta, self.kernel)
        sign = 1. if index == 0 else -1.
        return 1., 0., float(sign*h[0]), float((.5*sign)*ht[0]/self._width(a, b))

    def _scalar(self, point, original=None):
        if original is None:
            values, errors = self.context.law.at(point)
            self.counts["exact_split_scalar_queries"] += 1
        else:
            values, errors = self.context.reference_at(*original)
            self.counts["original_scalar_queries"] += 1
        values, errors = np.asarray(values, dtype=float), np.asarray(errors, dtype=float)
        if (values.shape != (4,) or errors.shape != (4,)
                or not np.isfinite(values).all() or not np.isfinite(errors).all() or np.any(errors < 0)):
            self._fail("scalar_law", "The complete bound scalar returned unusable value/error carriers")
        self.maximum_scalar_errors = np.maximum(self.maximum_scalar_errors, errors)
        b, c, bs, cs = values
        norm = math.hypot(float(b), float(c))
        if not math.isfinite(norm) or norm <= 0:
            self._fail("scalar_normalization", "The full scalar meridian carrier is zero or nonfinite")
        B, C = b/norm, c/norm
        ns = B*bs+C*cs
        result = np.array((B, C, (bs-B*ns)/norm, (cs-C*ns)/norm))
        if not np.isfinite(result).all():
            self._fail("scalar_normalization", "A complete differentiated scalar normalization is nonfinite")
        return result

    def _prepare_plan(self):
        if self._plan is not None:
            return self._plan
        start = time.monotonic()
        c = self.context
        cuts = set(c.nodes)
        for (left, right), (ca, cb) in zip(self.support, self.central):
            cuts.update((v, F(0)) for v in (left, ca, cb, right))
            cuts.update((ca+(cb-ca)*v, F(0)) for v in self.profile_breakpoints)
            cuts.update((left+(ca-left)*v, F(0)) for v in self.boundary_cutoff_breakpoints)
            cuts.update((cb+(right-cb)*v, F(0)) for v in self.boundary_cutoff_breakpoints)
        ordered = sorted(cuts, key=cmp_to_key(self._compare))
        if ordered[0] != (F(0), F(0)) or ordered[-1] != (F(1), F(0)):
            self._fail("partition", "The complete original scalar domain is not retained")
        gx, gw = np.polynomial.legendre.leggauss(self.integer_parameters["radial_quadrature_order"])
        gu, weights0 = (gx+1.)/2., gw/2.
        if (not np.isfinite(gu).all() or not np.isfinite(weights0).all()
                or np.any(gu <= 0) or np.any(gu >= 1) or np.any(weights0 <= 0)):
            self._fail("quadrature", "Every complete positive radial Gauss node and weight is required")
        boundary_values, boundary_weights, boundary_chi = [], [], []
        outside_values, outside_weights = [], []
        point_records, piece_records = [], []
        original_cell = 0
        for piece, (left, right) in enumerate(zip(ordered, ordered[1:])):
            midpoint = tuple((x+y)/2 for x, y in zip(left, right))
            while (original_cell < c.J-2
                   and self._compare(midpoint, c.nodes[original_cell+1]) > 0):
                original_cell += 1
            if (self._compare(left, c.nodes[original_cell]) < 0
                    or self._compare(right, c.nodes[original_cell+1]) > 0):
                self._fail("partition", "Every split piece must remain in one true original affine cell")
            kind, region = self._region(midpoint)
            width = self._width(left, right)
            record = dict(index=piece, original_cell=original_cell, kind=kind,
                support_index=None if region < 0 else region,
                left=[str(v) for v in left], right=[str(v) for v in right],
                width_carrier_hex=width.hex(), node_count=0)
            if kind in ("left", "right"):
                layer = self.boundary_cutoff_definition["four_boundary_layers"][
                    2*region+(1 if kind == "right" else 0)]
                layer_edges = [F(v) for v in layer["exact_relative_piece_edges"]]
                cutoff_piece = next((j for j in range(3)
                    if self._compare(midpoint, (layer_edges[j+1], F(0))) < 0), None)
                if (cutoff_piece is None
                        or self._compare(left, (layer_edges[cutoff_piece], F(0))) < 0
                        or self._compare(right, (layer_edges[cutoff_piece+1], F(0))) > 0):
                    self._fail("boundary_cutoff_partition", "A boundary piece crosses an exact R725 internal cut")
                record.update(boundary_cutoff_piece_index=cutoff_piece,
                    boundary_cutoff_branch=layer["branches_in_increasing_material_order"][cutoff_piece],
                    odd_material_derivative_orientation=layer["odd_material_derivative_orientation"])
            if kind != "central":
                unchanged = left == c.nodes[original_cell] and right == c.nodes[original_cell+1]
                for u, weight0 in zip(gu, weights0):
                    point = self._affine_point(left, right, u)
                    original = (original_cell, float(u)) if unchanged else None
                    values = self._scalar(point, original)
                    weight = width*float(weight0)
                    if not math.isfinite(weight) or weight <= 0:
                        self._fail("quadrature", "A complete physical radial weight is nonpositive")
                    if kind == "outside":
                        outside_values.append(values)
                        outside_weights.append(weight)
                    else:
                        chi, _, _, _ = self._cutoff_and_profile(point, kind, region)
                        if not math.isfinite(chi) or not 0 <= chi <= 1:
                            self._fail("quadrature", "A boundary cutoff is not a usable actual carrier")
                        boundary_values.append(values)
                        boundary_weights.append(weight)
                        boundary_chi.append(chi)
                    point_records.append(dict(piece=piece, local_hex=float(u).hex(),
                        exact_affine_point=[str(v) for v in point], kind=kind,
                        original_cached_address=None if original is None else
                            dict(cell=original[0], local_hex=original[1].hex())))
                    record["node_count"] += 1
            piece_records.append(record)
        boundary_values = np.asarray(boundary_values, dtype=float).reshape(-1, 4)
        outside_values = np.asarray(outside_values, dtype=float).reshape(-1, 4)
        boundary_weights = np.asarray(boundary_weights, dtype=float)
        outside_weights = np.asarray(outside_weights, dtype=float)
        boundary_chi = np.asarray(boundary_chi, dtype=float)
        if not len(boundary_weights) or not len(outside_weights):
            self._fail("quadrature", "Retain the complete boundary layers and nonempty complement")
        outside_horizontal = float(np.dot(outside_weights, outside_values[:, 0]))
        outside_vertical = float(np.dot(outside_weights, outside_values[:, 1]))
        Lc_exact = sum((b-a for a, b in self.central), F(0))
        Lc = self._width((F(0), F(0)), (Lc_exact, F(0)))
        plan_arrays = dict(boundary_values=boundary_values, boundary_weights=boundary_weights,
            boundary_chi=boundary_chi, outside_values=outside_values,
            outside_weights=outside_weights, base_gauss_u=gu, base_gauss_w=weights0)
        for value in plan_arrays.values():
            value.setflags(write=False)
        record = dict(schema="complete-R726-spherical-boundary-paired-halfwave-seed-radial-plan-v1",
            source_sha256=sha(__file__), seed_model_identity_sha256=self.model_identity,
            complete_domain=True, original_cell_count=c.J-1,
            exact_partition_point_count=len(ordered), exact_piece_count=len(piece_records),
            complete_positive_boundary_node_count=len(boundary_weights),
            complete_positive_complement_node_count=len(outside_weights),
            central_profile_integral_is_separate=True,
            paired_halfwave_definition=self.physical_profile_definition,
            boundary_cutoff_definition=self.boundary_cutoff_definition,
            exact_boundary_cutoff_epsilon=str(self.boundary_cutoff_epsilon),
            every_internal_boundary_cut_in_complete_partition=True,
            complete_physical_boundary_piece_count=12,
            complete_internal_boundary_cut_count=8,
            every_physical_halfwave_breakpoint_in_complete_partition=True,
            complete_physical_pair_piece_count=12,
            auxiliary_mean_rule_piece_count=12,
            physical_sine_cancellation_scope="both equal complete central intervals together",
            complete_infinite_scalar_tail_in_complement=True,
            no_scalar_tail_or_radial_piece_dropped=True,
            exact_relative_central_total_length=str(Lc_exact),
            central_length_carrier_hex=Lc.hex(),
            outside_horizontal_integral_carrier_hex=outside_horizontal.hex(),
            outside_vertical_integral_carrier_hex=outside_vertical.hex(),
            boundary_weight_sum_hex=float(np.sum(boundary_weights)).hex(),
            complement_weight_sum_hex=float(np.sum(outside_weights)).hex(),
            arrays={key: array_record(value) for key, value in plan_arrays.items()},
            pieces_identity_sha256=canonical(piece_records),
            nodes_identity_sha256=canonical(point_records),
            scalar_errors_are_not_normalization_or_integration_errors=True,
            numerical_integral_error_enclosed=False,
            build_seconds=time.monotonic()-start)
        if self.cache_directory is not None:
            if not self.cache_directory.is_dir():
                self._fail("cache_directory", "The outer operator's fresh reference cache is absent")
            arrays_path = self.cache_directory/"supported-smooth-triangle-reference-radial-plan.npz"
            temporary = arrays_path.with_suffix(".partial.npz")
            np.savez(temporary, **plan_arrays,
                model_identity=np.array(self.model_identity),
                central_length=np.array(Lc),
                outside_integrals=np.array((outside_horizontal, outside_vertical)))
            temporary.replace(arrays_path)
            description = self.cache_directory/"supported-smooth-triangle-reference-radial-plan.json"
            write_json(description, dict(record, pieces=piece_records, nodes=point_records))
            record["runner_raw_arrays"] = file_record(arrays_path)
            record["runner_raw_description"] = file_record(description)
        self._plan = dict(arrays=plan_arrays, central_length=Lc,
            outside_horizontal=outside_horizontal, outside_vertical=outside_vertical,
            record=record)
        return self._plan

    def _chart(self, phi):
        phase = phi[:, None]*self.freq[None]
        cp, sp = np.cos(phase), np.sin(phase)
        theta = phi+sp@((self.qfreq/self.freq)*self.core)
        rho = 1.+cp@(self.qfreq*self.core)
        rhop = -sp@(self.freq*self.qfreq*self.core)
        if (not np.isfinite(theta).all() or not np.isfinite(rho).all()
                or not np.isfinite(rhop).all() or np.any(rho <= 0)):
            self._fail("fixed_chart", "The bound original chart is not positive at every requested angle",
                angle_hex=[float(v).hex() for v in phi])
        zeros = np.zeros_like(phi)
        er = np.column_stack((np.cos(theta), np.sin(theta), zeros))
        et = np.column_stack((-np.sin(theta), np.cos(theta), zeros))
        e1 = rho[:, None]*et
        e2 = rhop[:, None]*et-rho[:, None]**2*er
        normal = np.column_stack((np.cos(phi), np.sin(phi), zeros))
        tangent = np.column_stack((-np.sin(phi), np.cos(phi), zeros))
        support = 1.+cp@self.core
        support_phi = -sp@(self.freq*self.core)
        Gamma = support[:, None]*normal+support_phi[:, None]*tangent
        Gamma1 = rho[:, None]*tangent
        Gamma2 = rhop[:, None]*tangent-rho[:, None]*normal
        return dict(theta=theta, rho=rho, rhop=rhop, e0=er, e1=e1, e2=e2,
                    Gamma=Gamma, Gamma1=Gamma1, Gamma2=Gamma2)

    def _means(self, phi, chart):
        plan = self._prepare_plan()
        keys = [float(v).hex() for v in phi]
        self.counts["mean_angle_requests"] += len(keys)
        missing = []
        seen = set()
        for index, key in enumerate(keys):
            if key in self._mean_cache:
                self.counts["mean_cache_hits"] += 1
            elif key not in seen:
                missing.append(index)
                seen.add(key)
        if missing:
            indices = np.asarray(missing, dtype=np.int64)
            p = {name: value[indices] for name, value in chart.items()}
            ez = np.array((0., 0., 1.))
            horizontal = self.context.radius-plan["outside_horizontal"]
            vertical = self.height-plan["outside_vertical"]
            K0 = horizontal*p["e0"]+vertical*ez-p["Gamma"]
            K1 = horizontal*p["e1"]-p["Gamma1"]
            K2 = horizontal*p["e2"]-p["Gamma2"]
            values = plan["arrays"]["boundary_values"]
            B, C = values[:, 0], values[:, 1]
            T0 = B[:, None, None]*p["e0"][None]+C[:, None, None]*ez
            T1 = B[:, None, None]*p["e1"][None]
            T2 = B[:, None, None]*p["e2"][None]
            self.counts["new_mean_angles"] += len(indices)
            self.counts["mean_batches"] += 1
            try:
                result = self.kernel.solve_mean_jets(
                    K0, K1, K2, T0, T1, T2,
                    plan["arrays"]["boundary_chi"], plan["arrays"]["boundary_weights"],
                    plan["central_length"], p["e0"], p["e1"], p["e2"],
                    profile_delta=self.profile_delta,
                    profile_quadrature_order=self.integer_parameters["profile_quadrature_order"],
                    maxiter=self.integer_parameters["mean_maxiter"],
                    tolerance=self.tolerance,
                    scalar_iterations=self.integer_parameters["scalar_iterations"],
                    mean_backtracks=self.integer_parameters["mean_backtracks"],
                    mean_armijo=self.armijo)
            except self.kernel.SeedMeanFailure as error:
                self._fail("mean_and_amplitude", str(error),
                    actual_requested_angle_hex=[keys[i] for i in missing],
                    full_working_failure=error.record)
            needed = ("v", "v_phi", "v_phiphi", "d", "d_phi", "d_phiphi",
                      "w", "w_phi", "w_phiphi", "lambda", "lambda_phi", "lambda_phiphi")
            for name in needed:
                expected = (len(indices),) if name.startswith("lambda") else (len(indices), 3)
                if name not in result or result[name].shape != expected or not np.isfinite(result[name]).all():
                    self._fail("mean_result", "A complete successful mean/angle jet is missing: "+name)
            if result["metadata"].get("complete") is not True:
                self._fail("mean_result", "The working mean kernel did not return complete")
            batch_record = dict(
                literal_angle_hex=[keys[i] for i in missing],
                metadata=result["metadata"],
                seed_model_identity_sha256=self.model_identity,
                fixed_original_core_H_used=True,
                current_outer_free_point_not_used=True)
            for j, index in enumerate(missing):
                record = {}
                for name in needed:
                    value = np.array(result[name][j], copy=True)
                    value.setflags(write=False)
                    record[name] = value
                self._mean_cache[keys[index]] = record
            self.counts["completed_mean_angles"] += len(indices)
            if self.cache_directory is not None:
                digest = canonical(batch_record["literal_angle_hex"])
                path = self.cache_directory/("supported-smooth-triangle-mean-"+digest+".npz")
                temporary = path.with_suffix(".partial.npz")
                np.savez(temporary, phi=np.asarray(phi[indices]),
                    seed_model_identity=np.array(self.model_identity),
                    **{name: value for name, value in result.items() if isinstance(value, np.ndarray)})
                temporary.replace(path)
                report_path = self.cache_directory/("supported-smooth-triangle-mean-"+digest+".json")
                write_json(report_path, batch_record)
                batch_record["runner_raw_arrays"] = file_record(path)
                batch_record["runner_raw_report"] = file_record(report_path)
            self._mean_batches.append(batch_record)
        return {name: np.stack([self._mean_cache[key][name] for key in keys])
                for name in ("v", "v_phi", "v_phiphi", "d", "d_phi", "d_phiphi",
                             "w", "w_phi", "w_phiphi", "lambda", "lambda_phi", "lambda_phiphi")}

    def _radial(self, cells, local):
        key = (array_sha(cells), array_sha(local))
        if key in self._radial_cache:
            return self._radial_cache[key]
        self.counts["radial_query_batches"] += 1
        values, kinds, chi, chis, hs, hss = [], [], [], [], [], []
        names = {"outside": 0, "left": 1, "right": 1, "central": 2}
        for cell, u in zip(cells, local):
            point = self._affine_point(self.context.nodes[int(cell)],
                self.context.nodes[int(cell)+1], float(u))
            kind, index = self._region(point)
            values.append(self._scalar(point, (int(cell), float(u))))
            c0, c1, h0, h1 = self._cutoff_and_profile(point, kind, index)
            kinds.append(names[kind])
            chi.append(c0)
            chis.append(c1)
            hs.append(h0)
            hss.append(h1)
        result = dict(values=np.asarray(values), kinds=np.asarray(kinds),
            chi=np.asarray(chi), chi_s=np.asarray(chis),
            profile=np.asarray(hs), profile_s=np.asarray(hss))
        for value in result.values():
            value.setflags(write=False)
        self._radial_cache[key] = result
        return result

    def evaluate(self, cells, local, phi):
        require_actions()
        raw_cells, local, phi = np.asarray(cells), np.asarray(local), np.asarray(phi)
        if (raw_cells.ndim != 1 or local.shape != raw_cells.shape or phi.ndim != 1
                or not len(local) or not len(phi) or np.iscomplexobj(local) or np.iscomplexobj(phi)
                or not np.isfinite(raw_cells).all() or not np.isfinite(local).all()
                or not np.isfinite(phi).all()):
            raise ValueError("Use every complete finite radial row and fixed-chart angle")
        cells = raw_cells.astype(np.int64)
        if (not np.array_equal(cells, raw_cells) or np.any(cells < 0)
                or np.any(cells >= self.context.J-1) or np.any(local < 0) or np.any(local > 1)):
            raise ValueError("Use exact integer original cells and literal local coordinates in [0,1]")
        local, phi = np.asarray(local, dtype=float), np.asarray(phi, dtype=float)
        self.counts["reference_evaluations"] += 1
        self.counts["requested_points"] += len(cells)*len(phi)
        chart = self._chart(phi)
        mean = self._means(phi, chart)
        radial = self._radial(cells, local)
        B, C, Bs, Cs = radial["values"].T
        ez = np.array((0., 0., 1.))
        T = B[:, None, None]*chart["e0"][None]+C[:, None, None]*ez
        Ts = Bs[:, None, None]*chart["e0"][None]+Cs[:, None, None]*ez
        Tp = B[:, None, None]*chart["e1"][None]
        Tpp = B[:, None, None]*chart["e2"][None]
        d, dp, dpp = (mean[name][None] for name in ("d", "d_phi", "d_phiphi"))
        w, wp, wpp = (mean[name][None] for name in ("w", "w_phi", "w_phiphi"))
        boundary = radial["kinds"] == 1
        if np.any(boundary):
            try:
                actual = self.kernel.spherical_boundary_jets(
                    T[boundary], Tp[boundary], Tpp[boundary],
                    mean["v"], mean["v_phi"], mean["v_phiphi"],
                    radial["chi"][boundary], Ts=Ts[boundary],
                    chi_s=radial["chi_s"][boundary])
            except self.kernel.SeedMeanFailure as error:
                self._fail("spherical_boundary_jets", str(error),
                    literal_angle_hex=[float(v).hex() for v in phi],
                    full_working_failure=error.record)
            T[boundary], Tp[boundary], Tpp[boundary], Ts[boundary] = (
                actual["T0"], actual["T0_phi"], actual["T0_phiphi"], actual["T0_s"])
        central = radial["kinds"] == 2
        if np.any(central):
            h = radial["profile"][central, None]
            hs = radial["profile_s"][central, None]
            alpha = h*mean["lambda"][None]
            ap = h*mean["lambda_phi"][None]
            app = h*mean["lambda_phiphi"][None]
            sn, co = np.sin(alpha)[..., None], np.cos(alpha)[..., None]
            ap, app = ap[..., None], app[..., None]
            unit = co*d+sn*w
            tangent = -sn*d+co*w
            up = co*dp+sn*wp+ap*tangent
            upp = (co*dpp+sn*wpp+2.*ap*(-sn*dp+co*wp)
                   +app*tangent-ap*ap*unit)
            us = (hs*mean["lambda"][None])[..., None]*tangent
            T[central], Tp[central], Tpp[central], Ts[central] = unit, up, upp, us
        result = dict(T0=T, T0_s=Ts, T0_phi=Tp, T0_phiphi=Tpp,
            norm=np.linalg.norm(T, axis=-1),
            theta_parent=chart["theta"], rho_parent=chart["rho"], rho_phi_parent=chart["rhop"],
            metadata=dict(schema=SCHEMA, source_sha256=sha(__file__),
                seed_model_identity_sha256=self.model_identity,
                reference_model_identity_sha256=self.context.identity,
                complete_fixed_supported_reference=True,
                all_current_outer_variables_preserved=True,
                exact_definition_has_unit_speed_under_stated_hypotheses=True,
                accurate_mean_root_and_continuous_geometry_certified=False,
                spherical_boundary_source_sha256=MEAN_KERNEL_SHA,
                R726_acute_domain_existence_or_global_branch_verified=False,
                old_R709_or_R722_mean_certificate_inherited=False,
                working_mean_reused_for_every_radial_query_at_literal_angle=True,
                scalar_normalization_trigonometric_quadrature_root_errors_enclosed=False))
        for value in result.values():
            if isinstance(value, np.ndarray):
                if not np.isfinite(value).all():
                    self._fail("complete_reference_jets", "A complete supported reference jet is nonfinite")
                value.setflags(write=False)
        return result

    def metadata(self):
        return dict(schema=SCHEMA, source_sha256=sha(__file__), model=self.model,
            model_identity_sha256=self.model_identity, binding=self.binding,
            counts=dict(self.counts), working_definition=self.working_definition,
            radial_plan=None if self._plan is None else self._plan["record"],
            completed_literal_angle_count=len(self._mean_cache),
            mean_batch_records=self._mean_batches,
            last_failure=self.last_failure,
            maximum_original_scalar_carrier_errors=self.maximum_scalar_errors.tolist(),
            exact_seed_global_existence_hypotheses_certified=False,
            seed_physical_field_or_normal_control_rank_inherited=False,
            continuous_metric_geometry_or_full_phase_certificate=False)

