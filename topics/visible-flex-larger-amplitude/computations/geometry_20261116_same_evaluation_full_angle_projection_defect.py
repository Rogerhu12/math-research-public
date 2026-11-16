#!/usr/bin/env python3
"""R575: complete-angle exact-reference Fourier projection defect.

This is an optional observer beside the original R553 prefix-tube observer.
It consumes that same evaluation and that same DFS retirement.  It does not
sample a second angular grid, run an FFT/BVP/native solve, split a cell, choose
a C root or sigma, change a scientific acceptance predicate, start a clock,
or delete data.  All arithmetic is restricted to the named public Actions.
The exact DFT reference and actual floating FFT formation remain separate.
Author: geometry agent (AI), 2026-11-16.
"""
from __future__ import annotations
import copy
from fractions import Fraction as Q
import hashlib
import json
import os
from pathlib import Path
import sys

REPOSITORY = "Rogerhu12/math-research-public"
HERE = Path(__file__).resolve().parent
SCHEMA = "R575-same-evaluation-complete-angle-projection-defect-v1"
TUBE_NAME = "geometry_20261116_actual_prefix_coefficient_tube_majorants.py"
TUBE_SHA = "81d33e7135eeba50b7d0b372d82cbcd656f0da34cf3f2691792f865e2dada96b"
TUBE_SCHEMA = "R553-actual-complete-prefix-coefficient-tube-majorants-v1"
MAJORANT_NAME = "geometry_20261116_finite_frenet_tube_residual_majorants.py"
MAJORANT_SHA = "4217bf9a30ade1934c473146131067de2ff778ea62bc0b7811b55356a7cd71ad"
MAJORANT_SCHEMA = "R521-complete-finite-frenet-tube-majorants-v1"
PHYSICAL_LAYOUT = "r0..rM,t1..tM,z0..zM"
REFERENCE_SOURCE_PINS = {
    "alternative-outward-probe.py":
        "cf163a5c42cff95137a78eefda058b6a18f5f226b4261b686a42e645f4002fcb",
    "geometry_20261114_r225_outward_probe.py":
        "64a3fd482f6ee01f4d149971dff1212b2c2ca3bdb00f1b733c7b119b458bab5f",
    "geometry_20261114_r225_high_core_bvp.py":
        "e12916dcf30dd2088ad59d2059647c8a03bed446aeee693b88f423730fa5a530",
    "geometry_20261114_r225_free_core_bvp.py":
        "a1e5486a3b5bfa4e8a52923335e7d7cb507f372c399cf6aaa72bde58fa1f8b08",
    "geometry_20261114_fft_frenet.py":
        "973898fcea1e8706d0ff9f87bbe72cde3576bc0055149af0a2e2058b144ac401",
}


def require(ok, message):
    if not ok:
        raise ValueError(message)


def actions():
    require(os.environ.get("GITHUB_ACTIONS") == "true"
            and os.environ.get("GITHUB_REPOSITORY") == REPOSITORY,
            "Evaluate this observer only in the named public Actions")


def exact(value):
    if isinstance(value, bool) or isinstance(value, float):
        raise TypeError("Use original exact rational lifts, not bool or float")
    if isinstance(value, (Q, int, str)):
        return Q(value)
    raise TypeError("Expected an exact rational")


def encode(value):
    if isinstance(value, Q):
        return str(value)
    if isinstance(value, dict):
        return {key: encode(item) for key, item in value.items()}
    if isinstance(value, (tuple, list)):
        return [encode(item) for item in value]
    return value


def canonical(value):
    return (json.dumps(encode(value), sort_keys=True, separators=(",", ":"),
        ensure_ascii=False, allow_nan=False)+"\n").encode("utf-8")


def value_identity(value):
    raw = canonical(value)
    return dict(bytes=len(raw), sha256=hashlib.sha256(raw).hexdigest())


def source_identity(path):
    path = Path(path).resolve()
    raw = path.read_bytes()
    return dict(file=str(path), bytes=len(raw), sha256=hashlib.sha256(raw).hexdigest())


def actual_defining_module(function, name, sha):
    function = getattr(function, "__func__", function)
    module = sys.modules.get(getattr(function, "__module__", ""))
    require(module is not None and getattr(module, "__file__", None) is not None,
            "The actual defining module is unavailable")
    row = source_identity(module.__file__)
    require(Path(row["file"]).parent == HERE and Path(row["file"]).name == name
            and row["sha256"] == sha,
            "The actual defining source differs")
    return module, row


def validate_reference_grid(field_modes, angular_count):
    require(type(field_modes) is int and field_modes >= 1,
            "Use the actual positive integer field mode count")
    require(type(angular_count) is int and angular_count % 2 == 0
            and angular_count >= 4*field_modes+4,
            "Use the original even grid with every retained bin strictly below Nyquist")
    return tuple(2*j for j in range(field_modes+1))


def conditional_uniform_projection_bound(B2, field_modes, angular_count):
    """A conditional exact-reference bound, never a floating FFT certificate.

    B2 must bound the Euclidean norm of the second PHYSICAL-angle derivative
    of the actually projected rotating-frame vector over the entire circle.
    Its components must have parity (even, odd, even) and period pi.  The
    complete bound is not justified by a single angular leaf or samples.
    """
    actions()
    validate_reference_grid(field_modes, angular_count)
    B2 = exact(B2)
    require(B2 >= 0, "The complete second derivative bound must be nonnegative")
    m, n = field_modes, angular_count
    tail = B2/(2*m)
    alias_each = 4*B2/((n-2*m)**2)
    alias = (2*m+1)*alias_each
    # Since N>4M, the retained residue classes are disjoint.  Every alias
    # frequency is an omitted even frequency, counted at most once.
    alias_used = min(alias, tail)
    return encode(dict(schema=SCHEMA+"-conditional-uniform-bound",
        field_modes=m, angular_count=n, physical_size=3*m+2,
        physical_layout=PHYSICAL_LAYOUT,
        physical_angle_period="2*pi; the three component functions also have period pi",
        derivative_coordinate="phi, not q=phi/(2*pi) and not a material angle",
        component_frame="rotating cylindrical orthonormal frame",
        component_parity=["even", "odd", "even"],
        retained_signed_frequencies=list(range(-2*m, 2*m+1, 2)),
        retained_frequency_count=2*m+1,
        reference_grid=dict(count=n, first_index=0, last_index=n-1,
            formula="phi_l=2*pi*l/N", repeated_endpoint_included=False,
            Nyquist_index=n//2, largest_retained_index=2*m,
            retained_Nyquist=False),
        actual_complete_B2=B2,
        continuous_Fourier_tail_upper=tail,
        alias_per_retained_complex_vector_coefficient_upper=alias_each,
        all_retained_alias_sum_upper=alias,
        alternative_alias_upper_from_disjoint_tail=tail,
        alias_upper_used=alias_used,
        uniform_reconstructed_projection_defect_upper=tail+alias_used,
        vector_norm="Euclidean norm of the full three-vector; complex coefficients use C^3 norm",
        full_infinite_tail_and_all_integer_aliases_included=True,
        both_R_and_Z_means_retained=True,
        omitted_T_mean_exactly_zero_only_by_the_stated_parity=True,
        finite_N_fft_roundoff_table_and_RHS_formation_bound=False,
        original_solver_residual_or_metric_floor_bound=False,
        conditional_full_circle_and_fixed_sigma_requirements_not_inferred_from_B2_word=True))


def angular_component_derivative_majorants(tube_module, api, coefficient_box,
                                           field_modes, sqrt_bits, budget_check):
    """Actual finite angular derivatives of d_rot and e_rot, through order 2.

    This is NOT the identity e_rot=d(d_rot)/dphi.  The latter is false in a
    rotating frame.  Every expression below differentiates the actual finite
    component trigonometric polynomials.  r0 and z0 remain in the full input;
    their angular derivatives are exactly zero, not deleted state columns.
    """
    actions()
    m = field_modes
    require(len(coefficient_box) == 3*m+2,
            "Keep all actual physical coefficients and both means")
    bounds = [tube_module.absolute(tube_module.pair(row)) for row in coefficient_box]
    d1 = [Q(0), Q(0), Q(0)]
    d2 = [Q(0), Q(0), Q(0)]
    e1 = [Q(0), Q(0), Q(0)]
    e2 = [Q(0), Q(0), Q(0)]
    for j in range(1, m+1):
        budget_check()
        n = 2*j
        r, t, z = bounds[j], bounds[m+j], bounds[2*m+1+j]
        dc = (n*r+t, n*t+r, n*z)
        ec = ((n*n+1)*r+2*n*t, (n*n+1)*t+2*n*r, n*n*z)
        for k in range(3):
            d1[k] += n*dc[k]
            d2[k] += n*n*dc[k]
            e1[k] += n*ec[k]
            e2[k] += n*n*ec[k]
    return dict(
        physical_layout=PHYSICAL_LAYOUT, physical_size=3*m+2,
        complete_frequency_count=m, frequencies=[2*j for j in range(1,m+1)],
        actual_complete_coefficient_box_identity=value_identity(coefficient_box),
        d_rot_phi_component_upper=d1, e_rot_phi_component_upper=e1,
        d_rot_phiphi_component_upper=d2, e_rot_phiphi_component_upper=e2,
        d_rot_phi_upper=api.norm_upper(d1, sqrt_bits),
        e_rot_phi_upper=api.norm_upper(e1, sqrt_bits),
        d_rot_phiphi_upper=api.norm_upper(d2, sqrt_bits),
        e_rot_phiphi_upper=api.norm_upper(e2, sqrt_bits),
        derivative_variable="the original physical angle phi",
        world_frame_derivative_not_substituted=True,
        scalar_A_nu_mu_angular_derivatives_exactly_zero_for_this_reference=True)


class BoundProjectionDefect:
    """Consumes the actual R553 observer; original DFS retains all authority."""

    def __init__(self, prefix_tubes):
        actions()
        module = sys.modules.get(type(prefix_tubes).__module__)
        require(module is not None and getattr(module, "__file__", None) is not None,
                "The actual R553 class owner is unavailable")
        row = source_identity(module.__file__)
        require(Path(row["file"]).parent == HERE and Path(row["file"]).name == TUBE_NAME
                and row["sha256"] == TUBE_SHA
                and module.SCHEMA == TUBE_SCHEMA
                and getattr(module, "BoundPrefixTubes", None) is type(prefix_tubes),
                "Use the actual frozen R553 observer, not a same-name replacement")
        self.tubes, self.T = prefix_tubes, module
        self.field, self.current = prefix_tubes.field, prefix_tubes.current
        self.api = prefix_tubes.api
        self.budget_check = prefix_tubes.budget_check
        self.sqrt_bits = prefix_tubes.sqrt_bits
        self.M, self.N = prefix_tubes.M, prefix_tubes.N
        validate_reference_grid(self.M, self.N)
        require(type(self.field.saved.N) is int and self.field.saved.N == self.N,
                "Use the actual checkpoint's original angular quadrature")
        require(self.field.M == self.M and self.api.SCHEMA == MAJORANT_SCHEMA,
                "Actual finite dimensions or R521 schema differ")
        _, majorant_source = actual_defining_module(
            self.api.frenet_directional_majorants, MAJORANT_NAME, MAJORANT_SHA)
        references = {}
        for name, sha in REFERENCE_SOURCE_PINS.items():
            self.budget_check()
            actual = source_identity(HERE/name)
            require(actual["sha256"] == sha, "The original DFT reference source differs: "+name)
            references[name] = actual
        self.binding = dict(schema=SCHEMA+"-binding", source=source_identity(__file__),
            actual_R553_source=row, actual_R521_source=majorant_source,
            actual_R553_binding=copy.deepcopy(prefix_tubes.binding),
            original_DFT_reference_sources=references,
            field_modes=self.M, angular_count=self.N, physical_size=3*self.M+2,
            physical_layout=PHYSICAL_LAYOUT,
            input="the same returned R553 cell record, before its original ledger write",
            reference="exact-trigonometric synthesis and exact unnormalized-forward/normalized-inverse DFT",
            actual_rounded_FFT_was_not_executed_or_certified_here=True,
            whole_prefix_physical_circle_required_before_global_bound=True,
            original_clock_callback_reused=True,
            no_new_BVP_metric_or_DFS_predicate=True)
        self.observed = self.committed = self.split = self.terminal = self.paid = self.unpaid = 0
        self.max_B1 = self.max_B2 = Q(0)
        self.min_P = None
        self.first_unpaid = self.last_unpaid = self.last_observed = None

    def describe(self):
        return encode(copy.deepcopy(self.binding))

    def inspect(self, cell, actual_tube_record):
        """Read the already computed full coefficient/P box; no new field query."""
        self.budget_check()
        piece = self.field.pieces[cell["piece_index"]]
        if piece["kind"] != "prefix":
            return None
        self.observed += 1
        self.last_observed = copy.deepcopy(cell)
        result = dict(schema=SCHEMA+"-cell", original_cell=copy.deepcopy(cell),
            available=False, source_tube_record_identity=(
                value_identity(actual_tube_record) if isinstance(actual_tube_record, dict) else None),
            actual_scalar_and_P_record=None, component_derivative_bounds=None,
            first_affine_direction_record=None, angular_acceleration_direction_record=None,
            V_rot_phi_upper=None, V_rot_phiphi_upper=None, reasons=[], error=None,
            local_cell_is_not_a_complete_Fourier_projection_certificate=True,
            original_metric_split_and_acceptance_not_changed=True)
        try:
            require(isinstance(actual_tube_record, dict)
                    and actual_tube_record.get("schema") == TUBE_SCHEMA+"-cell"
                    and actual_tube_record.get("original_cell") == cell,
                    "The actual same-cell R553 return is absent")
            if actual_tube_record.get("available") is not True:
                result["reasons"].append("same_cell_R553_complete_positive_tube_unpaid")
                result["R553_reasons"] = copy.deepcopy(actual_tube_record.get("reasons"))
                result["R553_error"] = copy.deepcopy(actual_tube_record.get("error"))
                return encode(result)
            tube = actual_tube_record["coefficient_tube"]
            angular = actual_tube_record["angular_box"]
            scalar = actual_tube_record["scalar_box"]
            invariants = actual_tube_record["joint_invariants"]
            require(tube["field_modes"] == self.M and tube["physical_size"] == 3*self.M+2
                    and self.T.pair(tube["radial"]) == self.T.pair(cell["radial"])
                    and tube["prefix_span"] == piece["prefix_span"],
                    "The actual complete radial coefficient owner differs")
            require(self.T.pair(angular["angular"]) == self.T.pair(cell["angular"])
                    and angular["complete_frequency_count"] == self.M
                    and angular["frequencies"] == [2*j for j in range(1,self.M+1)],
                    "The original complete closed angular cell differs")
            lo, hi = self.T.pair(angular["angular"])
            require(Q(0) <= lo <= hi <= Q(1),
                    "Use the original complete closed physical-angle address")
            A, mu, nu = (self.T.pair(scalar[key]) for key in ("A", "mu", "nu"))
            P, W = (self.T.pair(invariants[key]) for key in ("P", "W"))
            require(A[0] > 0 and mu[0] > 0 and P[0] > 0,
                    "The same actual complete positive Frenet domain remains unpaid")
            require(len(angular["d"]) == 3 and len(angular["e"]) == 3,
                    "Both complete rotating-frame three-vectors are required")
            d_upper = self.api.norm_upper(
                [self.T.absolute(self.T.pair(v)) for v in angular["d"]], self.sqrt_bits)
            e_upper = self.api.norm_upper(
                [self.T.absolute(self.T.pair(v)) for v in angular["e"]], self.sqrt_bits)
            domain = dict(A_lower=A[0], A_upper=A[1],
                mu_lower=mu[0], mu_upper=mu[1], nu_abs_upper=self.T.absolute(nu),
                P_lower=P[0], W_lower=max(Q(0), W[0]),
                d_upper=d_upper, e_upper=e_upper)
            derivatives = angular_component_derivative_majorants(self.T, self.api,
                tube["complete_coefficient_box"], self.M, self.sqrt_bits, self.budget_check)
            first_direction = dict(d=derivatives["d_rot_phi_upper"],
                e=derivatives["e_rot_phi_upper"], A=Q(0), nu=Q(0), mu=Q(0))
            acceleration_direction = dict(d=derivatives["d_rot_phiphi_upper"],
                e=derivatives["e_rot_phiphi_upper"], A=Q(0), nu=Q(0), mu=Q(0))
            self.budget_check()
            first = self.api.frenet_directional_majorants(domain, first_direction, self.sqrt_bits)
            self.budget_check()
            acceleration = self.api.frenet_directional_majorants(
                domain, acceleration_direction, self.sqrt_bits)
            B1 = exact(first["first_upper"])
            B2 = exact(first["second_upper"])+exact(acceleration["first_upper"])
            require(B1 >= 0 and B2 >= 0, "Original nonnegative majorants were not returned")
            result.update(available=True,
                actual_scalar_and_P_record=dict(domain=domain,
                    same_C_return_identity=value_identity(scalar["actual_same_target_return"]),
                    complete_coefficient_owner_identity=value_identity(tube),
                    angular_box_identity=value_identity(angular),
                    fixed_sigma_required=True, same_bounds_for_both_fixed_signs=True,
                    sigma_may_not_change_from_leaf_to_leaf=True),
                component_derivative_bounds=derivatives,
                first_affine_direction_record=first,
                angular_acceleration_direction_record=acceleration,
                V_rot_phi_upper=B1, V_rot_phiphi_upper=B2,
                chain_rule="D^2 F[x_phi,x_phi]+DF[x_phiphi], with A_phi=nu_phi=mu_phi=0",
                actual_worker_root_or_sigma_selection_not_identified=True,
                actual_FFT_scalar_table_and_rhs_formation_bound=False)
            return encode(result)
        except (ArithmeticError, ValueError, TypeError, KeyError, IndexError) as error:
            result["error"] = dict(type=type(error).__name__, message=str(error))
            result["reasons"].append("actual_full_angle_projection_ingredient_unpaid")
            return encode(result)

    def commit_original_retirement(self, cell, diagnostic, *, split):
        """Call beside R553 retirement; never replaces the original decision."""
        piece = self.field.pieces[cell["piece_index"]]
        if piece["kind"] != "prefix":
            return None
        self.committed += 1
        if split:
            self.split += 1
            return dict(original_prefix_cell_split=True,
                all_original_children_keep_the_full_projection_responsibility=True)
        self.terminal += 1
        available = (isinstance(diagnostic, dict)
            and diagnostic.get("schema") == SCHEMA+"-cell"
            and diagnostic.get("original_cell") == cell
            and diagnostic.get("available") is True)
        commit_error = None
        if available:
            try:
                B1 = exact(diagnostic["V_rot_phi_upper"])
                B2 = exact(diagnostic["V_rot_phiphi_upper"])
                P = exact(diagnostic["actual_scalar_and_P_record"]["domain"]["P_lower"])
                require(B1 >= 0 and B2 >= 0 and P > 0,
                        "The actual complete-angle local record is inconsistent")
            except (ArithmeticError, ValueError, TypeError, KeyError, IndexError) as error:
                available = False
                commit_error = dict(type=type(error).__name__, message=str(error))
        if not available:
            self.unpaid += 1
            row = dict(original_cell=copy.deepcopy(cell),
                reasons=(["same_cell_projection_record_not_returned"]
                    if not isinstance(diagnostic, dict) else copy.deepcopy(diagnostic.get("reasons"))),
                evaluation_error=(None if not isinstance(diagnostic, dict)
                    else copy.deepcopy(diagnostic.get("error"))),
                retirement_record_error=commit_error,
                terminal_projection_ingredient_paid=False)
            if self.first_unpaid is None:
                self.first_unpaid = row
            self.last_unpaid = row
            return row
        self.paid += 1
        self.max_B1, self.max_B2 = max(self.max_B1,B1), max(self.max_B2,B2)
        self.min_P = P if self.min_P is None else min(self.min_P,P)
        return dict(original_cell=copy.deepcopy(cell),
            terminal_projection_ingredient_paid=True,
            actual_complete_local_projection_record_identity=value_identity(diagnostic),
            local_ingredient_not_relabelled_full_circle_bound=True)

    def summary(self, *, original_coverage, complete_cell_ledger, original_error,
                original_stop, close_errors):
        # R553 computes metadata from its actual in-memory retirement counters.
        # Calling it here does not reevaluate a field/target/interval or rerun DFS.
        tube = self.tubes.summary(original_coverage=original_coverage,
            complete_cell_ledger=complete_cell_ledger, original_error=original_error,
            original_stop=original_stop, close_errors=close_errors)
        counters_match = (
            self.observed == self.tubes.observed_prefix_cells
            and self.committed == self.tubes.committed_prefix_cells
            and self.split == self.tubes.split_prefix_cells
            and self.terminal == self.tubes.terminal_prefix_leaves
            and self.paid == self.terminal and self.unpaid == 0)
        complete = (tube.get("complete_prefix_constant_cover") is True
                    and counters_match and self.terminal > 0)
        bound = (conditional_uniform_projection_bound(self.max_B2,self.M,self.N)
                 if complete else None)
        return encode(dict(schema=SCHEMA+"-necessary", binding=self.binding,
            actual_R553_complete_summary_identity=value_identity(tube),
            complete_original_cell_ledger=copy.deepcopy(complete_cell_ledger),
            original_coverage_object_in_same_result="coverage",
            original_all_DFS_and_R553_complete=tube.get("complete_prefix_constant_cover") is True,
            observed_prefix_cells=self.observed, committed_prefix_cells=self.committed,
            split_prefix_cells=self.split, terminal_prefix_leaves=self.terminal,
            paid_terminal_projection_ingredients=self.paid,
            unpaid_terminal_projection_ingredients=self.unpaid,
            exact_original_retirement_counters_match=counters_match,
            complete_prefix_physical_angle_projection_bound=complete,
            global_prefix_exact_reference_projection_bound=bound,
            global_prefix_V_rot_phi_upper=(self.max_B1 if complete else None),
            global_prefix_positive_P_lower=(self.min_P if complete else None),
            observed_paid_leaf_extrema=dict(V_rot_phi_upper=self.max_B1,
                V_rot_phiphi_upper=self.max_B2, P_lower=self.min_P,
                these_are_not_global_without_complete_original_cover=True),
            first_unpaid_terminal=self.first_unpaid, last_unpaid_terminal=self.last_unpaid,
            last_observed_cell=self.last_observed,
            complete_per_cell_input_error_and_result_remains_in_original_ledger=True,
            ledger_rows_not_claimed_fully_returned_by_this_summary=True,
            current_frontier_and_all_unvisited_roots_remain_original_coverage=True,
            both_reflected_sheets_and_all_original_prefix_pieces_retained=True,
            phase_scope=dict(
                base_complete_circle_supremum_invariant_under_exact_angle_translation=True,
                orthogonal_world_registration_and_reflection_preserve_vector_norm=True,
                actual_common_material_pullback_requires_original_accurate_phase_contract=True,
                fixed_grid_parity_projection_not_claimed_to_commute_with_arbitrary_translation=True,
                allowed_phase_reference="pull back the already constructed base-field defect, or use the explicitly conjugated projection"),
            unpaid=["actual floating FFT and table/RHS formation difference",
                "nominal scalar versus the same accurate target RHS difference",
                "actual solver literal cubic and complete residual",
                "comparison-curve membership beyond the actual R553 box",
                "actual worker root/sigma identification",
                "tail/collar/cut-patch/cap coefficient reference",
                "boundary-anchor/angular metric error and full relative-metric floor"],
            original_BVP_native_FD_fullDN_metric_acceptance_and_DFS_decisions_changed=False,
            new_angular_grid_time_grid_clock_child_or_cleanup_started=False))


def bind_loaded_projection_defect(prefix_tubes):
    """Bind only the actual R553 owner; future caller registration is explicit."""
    return BoundProjectionDefect(prefix_tubes)
