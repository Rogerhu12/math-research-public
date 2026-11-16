#!/usr/bin/env python3
"""R442: every original C-root choice, all explicit finite-M deep-port rows.

This independent producer evaluates the proved complete finite-mode deep
enclosure. It does not choose a root, run a head ODE, reuse an old zero-J,
or infer a cut DN map from a deep-port graph. All scientific arithmetic is
restricted to the named public Actions repository. The actual original
config and both ready inputs are read by the frozen convention-C binder.
Raw rows are request-owned temporary recomputable output under Rule15.
"""
from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
import os
from pathlib import Path
import sys
import time

REPOSITORY = "Rogerhu12/math-research-public"
SCHEMA = "R442-original-C-root-family-complete-M-deep-far-enclosure-v1"
BINDING_SCHEMA = "R442-original-C-root-family-complete-M-deep-far-input-binding-v1"
ROW_SCHEMA = "R442-original-C-one-mode-deep-far-enclosure-v1"
MODEL_SCHEMA = "R286-original-stored-continuous-model-convention-C-v1"
BINDER_NAME = "geometry_20261115_stored_continuous_E_cover_v3.py"
BINDER_SHA256 = "f12f747041783dbb54b16ac2bdb0c3aeeade93e6bc7f276bde9dd81f424df7df"
PROOF_NAME = "R312-continuous-C-complete112-zero-tail-and-head-connection.md"
PROOF_SHA256 = "036289ed624b59456cfee700217f442d26104cae76bf33d9affd8ec618c9ac73"
EXTENSION_PROOF_NAME = "R442-fixed-accurate-C-finite-M-modes-and-deep-tail-range.md"
EXTENSION_PROOF_SHA256 = "535118e0403bdf10af73f7b47d35e607121c298c12a077b76e20337a3a6c2013"
SUMMARY_LIMIT = 90000


def require_actions():
    if (os.environ.get("GITHUB_ACTIONS") != "true"
            or os.environ.get("GITHUB_REPOSITORY") != REPOSITORY):
        raise RuntimeError("Scientific arithmetic only in the named public Actions repository")


def sha(raw):
    return hashlib.sha256(raw).hexdigest()


def file_receipt(path):
    path = Path(path)
    digest = hashlib.sha256()
    count = 0
    with path.open("rb") as stream:
        for raw in iter(lambda: stream.read(1048576), b""):
            digest.update(raw)
            count += len(raw)
    return dict(file=path.name, bytes=count, sha256=digest.hexdigest())


def canonical(value):
    return (json.dumps(value, ensure_ascii=False, sort_keys=True,
        separators=(",", ":"), allow_nan=False)+"\n").encode()


def write_json(path, value):
    raw = canonical(value)
    with Path(path).open("xb") as stream:
        stream.write(raw)
        stream.flush()
        os.fsync(stream.fileno())
    return dict(file=Path(path).name, bytes=len(raw), sha256=sha(raw))


def load_binder(directory):
    require_actions()
    path = Path(directory)/BINDER_NAME
    description = file_receipt(path)
    if description["sha256"] != BINDER_SHA256:
        raise ValueError("The exact original C metadata binder source differs")
    spec = importlib.util.spec_from_file_location("_R312_frozen_C_metadata", path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module, description


def proof_receipt(path):
    description = file_receipt(path)
    if description["sha256"] != PROOF_SHA256:
        raise ValueError("Use the complete frozen R312 theorem")
    return description


def requested_modes(value):
    if isinstance(value, bool) or not isinstance(value, int) or value < 112:
        raise ValueError("An explicit finite integer M>=112 is required")
    return tuple(range(2, 2*value+1, 2))


def extension_proof_receipt(path):
    description = file_receipt(path)
    if description["sha256"] != EXTENSION_PROOF_SHA256:
        raise ValueError("Use the complete frozen R442 finite-M extension")
    return description


class TheoremRangeUnpaid(RuntimeError):
    """The stated finite-M theorem range has not been paid, not BVP refusal."""


def finite_mode_bound(B, field_modes):
    """R442 rational certificate; evaluated only inside the Actions producer."""
    requested_modes(field_modes)
    m = 2*field_modes
    numerator = m*m*(m*m-1)
    if numerator % 12:
        raise ArithmeticError("Even-mode nu integer identity differs")
    nu = numerator//12
    b = m*m
    A = 2*nu+b+64
    c = B.Q(1, 2**84)
    delta = B.Q(1, 2**163)
    ell = 6*A*c
    e = b*delta+(2*nu+b)*delta*delta
    v = ell+3*e
    epsilon = (780*nu*v+130*nu*(2**14*c+2**11*delta*delta))/32
    certificate = dict(
        field_modes=field_modes, largest_physical_frequency=m,
        far_port=159, physical_node=160,
        exact_nu_upper=str(nu), exact_beta_and_kappa_squared_upper=str(b),
        exact_short_matrix_coefficient=str(A),
        exact_c_upper=str(c), exact_delta_upper=str(delta),
        exact_short_integral_bound=str(ell), exact_platform_relative_error=str(e),
        exact_product_exponent_bound=str(v), exact_normalized_perturbation_bound=str(epsilon),
        product_exponent_at_most_one_half=v <= B.Q(1, 2),
        normalized_perturbation_at_most_one_sixty_fourth=epsilon <= B.Q(1, 64),
        scope_is_all_original_root_choices=True,
        no_new_BVP_or_native_acceptance_condition=True)
    certificate["proved_theorem_range"] = (
        certificate["product_exponent_at_most_one_half"]
        and certificate["normalized_perturbation_at_most_one_sixty_fourth"])
    return epsilon, certificate


def original_binding(B, args, binder_receipt, theorem_receipt, extension_receipt):
    # This calls only the frozen original byte/metadata binder, not its
    # ContinuousHead, SixPrimitiveIntegrator, inverse cover or main().
    original_args = argparse.Namespace(
        config=args.config, config_sha256=args.config_sha256,
        ledger_ready=args.ledger_ready,
        ledger_ready_sha256=args.ledger_ready_sha256,
        stored_ready=args.stored_ready,
        stored_ready_sha256=args.stored_ready_sha256,
        runtime_computations=args.runtime_computations,
        source_topic=args.source_topic, proof=args.proof,
        queries=None, queries_sha256=None,
        deep_definition="original-exact-root-family")
    p, rows, lam, requested, original = B.bind_inputs(original_args)
    if original["convention"]["schema"] != MODEL_SCHEMA:
        raise ValueError("The exact declared continuous target model differs")
    if original["convention"]["root_existence_proved"] is not True:
        raise ValueError("The complete R286 original-root existence range is unpaid")
    if requested is not None:
        raise ValueError("This producer does not substitute an E query for a far boundary")
    binding = dict(schema=BINDING_SCHEMA,
        source_sha256=sha(Path(__file__).read_bytes()),
        actual_original_metadata_binder=binder_receipt,
        original_C_input_binding=original,
        original_binder_was_used_only_for_input_metadata=True,
        binder_integral_strategy_not_executed=True,
        actual_R312_proof=theorem_receipt,
        actual_R442_proof=extension_receipt,
        target_model_schema=MODEL_SCHEMA,
        exact_model_layer_choice_remains_explicit=True,
        deep_root_scope="every-fixed-original-mode2-exact-root-sequence",
        shared_one_root_per_source_cell_for_all_modes=True,
        original_root_choice_or_RK_calibration_not_executed=True,
        actual_unique_infinite_background_selected=False,
        original_shallow_table_recalibrated=False,
        finite_head_source_identity_bound_but_no_head_value_or_matrix_created=True,
        far_port=args.far_port,
        physical_node=args.far_port+1,
        source_cells_strictly_deeper_than_far_port=dict(
            first=args.far_port+1, last="infinity"),
        complete_physical_modes=list(requested_modes(args.field_modes)),
        mode_count=args.field_modes,
        field_modes=args.field_modes,
        balanced_state="(Q_m,Pi_m/nu_m)",
        normalized_state="(-1)^n*delta_n^(-11/2)*(Q_m,Pi_m/nu_m)",
        cell_direction="U_(n-1)=T_n*U_n; outward",
        port_Pi_factor="2^(-11/4)",
        no_angular_strip_growth_used=True,
        old_finite_zero_J_or_readylineargraph_used=False,
        output_is_deep_port_not_requested_physical_cut=True)
    return p, binding


def deep_geometry(B, p, far_port):
    """Exact R286 real expressions with outward Arb enclosures."""
    sqrt12 = B.exact(12).sqrt()
    delta = B.exact(p["delta0"])*B.p2(-far_port)
    short_ratio = B.p2(-3).sqrt()
    s = (3*B.exact(p["delta0"])*B.p2(-far_port)
        +6*B.exact(p["etaRatioAtN0"])*B.exact(p["delta0"])
        *B.p2(-3*(far_port+1)).sqrt()/(1-short_ratio))
    radius = B.exact(p["rCuff"])*(s/sqrt12).exp()
    mu = B.exact(p["epsilonScale"])*(delta.log()*B.exact(B.Q(11, 4))).exp()
    w = mu/radius**7
    if not (radius.is_finite() and radius > 0
            and mu.is_finite() and mu > 0
            and w.is_finite() and w > 0):
        raise ArithmeticError("The actual deep-port positive geometry was not enclosed")
    return dict(radius=radius, log_length=s, delta=delta, mu=mu, w=w,
                sqrt12=sqrt12)


def one_mode(B, m, far_port, epsilon, geom):
    """A proved original-root family enclosure, never a point-selected root."""
    nu_integer = m*m*(m*m-1)//12
    if 12*nu_integer != m*m*(m*m-1):
        raise ArithmeticError("The complete even-mode exact integer nu identity differs")
    nu = B.exact(nu_integer)
    d = B.p2(-11).sqrt().sqrt()
    normalized_scale = B.p2(-11).sqrt()
    alpha0 = B.exact(B.Q(65, 64))
    trace_magnitude = 65*nu*(1+d/64)-1-d
    discriminant = trace_magnitude**2-4*d
    if not (discriminant.is_finite() and discriminant > 0):
        raise ArithmeticError("The exact ideal real spectral split was not enclosed")
    large = (trace_magnitude+discriminant.sqrt())/2
    if not (large.is_finite() and large > 0):
        raise ArithmeticError("The positive large ideal eigenvalue was not enclosed")
    small = d/large
    # This form avoids subtracting two large almost equal high-mode values.
    ideal = B.exact(0) if m == 2 else -d+(d+small)/(alpha0*nu)
    radius = 20*epsilon
    if m == 2:
        graph = B.exact(0)
        reason = "exact-mode2-calibration-and-R442-bounded-solution-uniqueness"
        graph_error = B.exact(0)
    else:
        graph = ideal+(-radius).union(radius)
        reason = "R442-(442.10)-uniform-over-every-original-exact-root-sequence"
        graph_error = radius
    if not graph.is_finite():
        raise ArithmeticError("A finite complete root-family far interval is required")
    raw_ratio = nu*graph
    # R312 physical slope is dH/dr at this deep port only, where p=1.
    slope_per_height = (m*m+geom["sqrt12"]*raw_ratio)/geom["radius"]
    if not slope_per_height.is_finite():
        raise ArithmeticError("The complete physical deep-port row is nonfinite")
    return dict(schema=ROW_SCHEMA, mode_index=m//2-1, physical_frequency=m,
        exact_nu=str(nu_integer), far_port=far_port, physical_node=far_port+1,
        ideal_reference_only_alpha="65/64",
        actual_root_replaced_by_ideal_alpha=False,
        ideal_large_eigenvalue=B.record(large),
        ideal_small_eigenvalue=B.record(small),
        normalized_outward_large_eigenvalue=B.record(normalized_scale*large),
        normalized_outward_small_eigenvalue=B.record(normalized_scale*small),
        ideal_balanced_graph=B.record(ideal),
        theorem_graph_error_bound=B.record(graph_error),
        actual_balanced_Pi_over_nu_Q=B.record(graph),
        actual_original_Pi_over_Q=B.record(raw_ratio),
        actual_deep_port_slope_per_unit_physical_height=B.record(slope_per_height),
        graph_inclusion_reason=reason,
        original_Robin_row=dict(order=["Q_m", "Pi_m"],
            coefficient_Q=B.record(-raw_ratio), coefficient_Pi=B.record(B.exact(1))),
        physical_Robin_row=dict(order=["u_m", "k_m=dH_m/dr"],
            coefficient_u=B.record(-slope_per_height), coefficient_k=B.record(B.exact(1))),
        every_actual_original_root_choice_included=True,
        finite_head_propagation_or_cut_DN_claimed=False,
        arbitrary_finite_pivot_not_used_as_nonresonance_proof=True)


def argument_parser():
    parser = argparse.ArgumentParser(description=__doc__)
    for name in ("config", "ledger-ready", "stored-ready"):
        parser.add_argument("--"+name, type=Path, required=True)
        parser.add_argument("--"+name+"-sha256", required=True)
    parser.add_argument("--runtime-computations", type=Path, required=True)
    parser.add_argument("--source-topic", type=Path, required=True)
    parser.add_argument("--proof", type=Path, required=True,
                        help="Original complete R286 proof, checked by its frozen binder")
    parser.add_argument("--tail-proof", type=Path, required=True,
                        help="The complete R312 proof")
    parser.add_argument("--mode-extension-proof", type=Path, required=True,
                        help="Complete R442 finite-M theorem and fixed-F159 scope")
    parser.add_argument("--field-modes", type=int, required=True)
    parser.add_argument("--far-port", type=int, default=159)
    parser.add_argument("--precision-bits", type=int, default=256)
    parser.add_argument("--out", type=Path, required=True)
    return parser


def main(argv=None):
    args = argument_parser().parse_args(argv)
    require_actions()
    modes = requested_modes(args.field_modes)
    if args.far_port != 159 or not 128 <= args.precision_bits <= 8192:
        raise ValueError("This R442 complete finite-head route uses F159 and explicit interval precision")
    if args.out.exists():
        raise ValueError("Use a fresh request-owned temporary output directory")
    for path in (args.config, args.ledger_ready, args.stored_ready, args.proof, args.tail_proof, args.mode_extension_proof):
        if path.resolve().is_relative_to(args.out.resolve()):
            raise ValueError("The output directory cannot own an original input")
    B, binder_receipt = load_binder(args.runtime_computations)
    theorem_receipt = proof_receipt(args.tail_proof)
    extension_receipt = extension_proof_receipt(args.mode_extension_proof)
    p, binding = original_binding(B, args, binder_receipt, theorem_receipt, extension_receipt)
    args.out.mkdir(parents=True)
    large_dir = args.out/"large-arrays"
    large_dir.mkdir()
    runtime = B.initialise_math(args.precision_bits)
    binding["runtime"] = runtime
    binding_receipt = write_json(args.out/"input-binding.json", binding)
    journal = B.Journal(large_dir/"complete-M-deep-far-rows.jsonl", args.out)
    started = time.monotonic()
    completed = []
    error = None
    geometrical_values = None
    epsilon = None
    theorem_applicability = None
    try:
        epsilon_q, theorem_applicability = finite_mode_bound(B, args.field_modes)
        if not theorem_applicability["proved_theorem_range"]:
            raise TheoremRangeUnpaid("The exact R442 finite-M perturbation conditions are unpaid at F159")
        epsilon = B.exact(epsilon_q)
        geom = deep_geometry(B, p, args.far_port)
        geometrical_values = {key:B.record(geom[key])
            for key in ("radius", "log_length", "delta", "mu", "w")}
        for m in modes:
            row = one_mode(B, m, args.far_port, epsilon, geom)
            journal.add(row)
            completed.append(m)
    except Exception as failure:
        error = dict(type=type(failure).__name__, message=str(failure))
    finally:
        rows_receipt = journal.finish()
    all_rows = len(completed) == len(modes) and error is None
    pending = list(modes[len(completed):])
    report = dict(schema=SCHEMA,
        source_sha256=sha(Path(__file__).read_bytes()),
        repository=REPOSITORY, run_id=os.environ.get("GITHUB_RUN_ID"),
        source_commit=os.environ.get("GITHUB_SHA"),
        runtime=runtime, input_binding=binding_receipt,
        actual_original_metadata_binder=binder_receipt,
        actual_R312_proof=theorem_receipt,
        actual_R442_proof=extension_receipt,
        target_model_schema=MODEL_SCHEMA,
        target_scope="declared-C-background-family-with-original-exact-mode2-roots",
        original_C_model_choice_is_explicit=True,
        root_choice_resolved=False,
        deep_root_values_computed=0,
        finite_root_calibration_calls=0,
        finite_ODE_or_RHS_calls=0,
        old_zero_J_or_stored_far_graph_used=False,
        far_port=args.far_port, physical_node=args.far_port+1,
        included_source_cells=dict(first=args.far_port+1,last="infinity"),
        field_modes=args.field_modes,
        complete_requested_modes=list(modes),
        exact_theorem_applicability=theorem_applicability,
        completed_modes=completed, unpaid_mode_suffix=pending,
        all_complete_M_deep_far_rows_enclosed=all_rows,
        all_original_root_choices_uniformly_included=all_rows,
        deep_graph_existence_is_theorem_not_zero_unresolved_assumption=True,
        interval_precision_is_numerical_work_not_new_BVP_gate=True,
        original_R286_deep_geometry=geometrical_values,
        normalization_exponent="11/2",
        theorem_uniform_matrix_perturbation_bound=(
            B.record(epsilon) if epsilon is not None else None),
        theorem_Green_operator_upper_bound="9",
        numerical_pivot_or_sampled_spectrum_used=False,
        exact_original_mode2_graph_is_zero=bool(all_rows),
        complete_rows=rows_receipt,
        finite_head_C_source_only_bound=True,
        finite_head_propagation_performed=False,
        protected_head_join_verified_by_this_producer=False,
        natural_outer_radius_computed=False,
        requested_cut_domain_verified=False,
        cut_height_denominators_verified=False,
        cut_DN_matrix=None,
        actual_nonlinear_DN_existence_or_differentiability_proved=False,
        actual_nonlinear_solve=False,
        full_BVP_or_closed_surface_accepted=False,
        full_angular_infinite_frequency_claim=False,
        declared_C_frozen_parameters_or_scalar_controls_changed=False,
        old_finite_selector_reinterpreted_as_certified_continuous_C=False,
        complete_unpaid_scope=[
            "actual protected finite-head two-jet join",
            "same-C finite-head R*/w coefficients and all requested M transfers",
            "actual cut inverse/domain within natural Rout",
            "all requested cut-height nonzero denominators, if a DN graph is requested",
            "nonzero nonlinear tail and full prefix/native/final audit",
            "complete closed-field/metric/embedding/reach responsibilities"],
        error=error, elapsed_seconds=time.monotonic()-started,
        raw_outputs_are_request_owned_temporary_recomputable_data=True)
    result_receipt = write_json(args.out/"result.json", report)
    summary = dict(report, actual_result_file=result_receipt)
    raw = canonical(summary)
    if len(raw) > SUMMARY_LIMIT:
        print(json.dumps(dict(event="R442-M-summary-metadata-too-large", bytes=len(raw),
            sha256=sha(raw), actual_result_file=result_receipt,
            complete_result_written=True, scientific_acceptance_not_inferred=True)), flush=True)
        return 70
    print("BEGIN_R442_CONTINUOUS_C_M_DEEP_FAR_SUMMARY", flush=True)
    print(raw.decode(), end="", flush=True)
    print("END_R442_CONTINUOUS_C_M_DEEP_FAR_SUMMARY", flush=True)
    print(json.dumps(dict(event="R442-M-deep-far-summary-identity",
        bytes=len(raw), sha256=sha(raw), actual_result_file=result_receipt)), flush=True)
    return 0 if all_rows else 2


if __name__ == "__main__":
    raise SystemExit(main())
