#!/usr/bin/env python3
"""Continue the paid R582 actual-mouth seed into the undivided core return.

The three completed inner/outward transfers in run 45800483161 are immutable
small numerical input. This scope executes only the previously unreached
compact mean controls and linear core-return representation refinements.
"""
import hashlib
from pathlib import Path

ORIGINAL_SOURCE_SHA256 = "fd4bd864c3e9e96d741b7bc896a1bf6f9d50ba54eda0c02bd898f21bd42427a4"
if hashlib.sha256(Path(__file__).with_name("r582_actual_circle_seed_and_return_20261126.py").read_bytes()).hexdigest() != ORIGINAL_SOURCE_SHA256:
    raise RuntimeError("the paid seed and unchanged return operator require the original R582 source")
from r582_actual_circle_seed_and_return_20261126 import (
    argparse, json, time, np, minimize, COUNTS, FIRST_PEAK, SOURCE_Q,
    LENGTH, ELL, CORE_END, CONTROL_LEFT, CONTROL_RIGHT,
    ActualTail, MeanProfile, UndividedReturn, ClockCheckpoint,
    emit, source_input, full_geometry_report,
)

SCHEMA = "r582-paid-actual-mouth-to-undivided-core-return-v1"
PAID_INPUT_SHA256 = "517c1f85592434ed015f2eca6de235fc5750b42a035471df2d4e10c178eb33a7"


def paid_seed_input(raw, args):
    if hashlib.sha256(raw.encode()).hexdigest() != PAID_INPUT_SHA256:
        raise ValueError("the original completed seed input bytes changed")
    paid = json.loads(raw)
    if paid.get("schema") != "identified-r582-paid-three-actual-mouth-seeds-v1":
        raise ValueError("paid actual-mouth input schema changed")
    origin = paid["origin"]
    if (origin["run_id"] != 45800483161 or origin["job_id"] != 139842104318
            or origin["source_commit"] != "f473b765b70c44e68090f022df0bd8c1c08737a4"
            or origin["executed_source_sha256"] != ORIGINAL_SOURCE_SHA256):
        raise ValueError("a different or unexecuted tail seed cannot replace the paid actual background")
    expected_arguments = {key: getattr(args, key) for key in
        ("M", "rtol", "atol", "max_step", "tolerance_refinement")}
    if paid["source_arguments"] != expected_arguments:
        raise ValueError("the paid M/tolerance identity differs from the declared source")
    seeds = paid["compact_seed_inputs"]
    if [(row["M"], row["tolerance_factor"]) for row in seeds] != [(168, 1), (169, 1), (169, 8)]:
        raise ValueError("all three original completed seed readouts must remain identifiable")
    for row in seeds:
        outer = row["outer"]
        if (outer["mouth_s"] != .82 or not outer["requested_mouth_reached"]
                or outer["chart_checkpoint_before_requested_mouth"] is not None
                or len(outer["normalized_jets_A_As_Ass_C_Cs_Css"]) != 6
                or not np.all(np.isfinite(outer["normalized_jets_A_As_Ass_C_Cs_Css"]))):
            raise ValueError("the original complete actual mouth is not recoverable")
    return paid


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source-state-json", required=True)
    parser.add_argument("--paid-seed-json", required=True)
    parser.add_argument("--M", type=int, default=168)
    parser.add_argument("--rtol", type=float, default=2e-11)
    parser.add_argument("--atol", type=float, default=2e-13)
    parser.add_argument("--max-step", type=float, default=.15)
    parser.add_argument("--tolerance-refinement", type=float, default=8.)
    parser.add_argument("--return-basis", type=int, default=24)
    parser.add_argument("--return-radial-nodes", type=int, default=257)
    parser.add_argument("--geometry-radial-nodes", type=int, default=513)
    parser.add_argument("--maximum-control-iterations", type=int, default=60)
    parser.add_argument("--maximum-control-exchanges", type=int, default=4)
    parser.add_argument("--maximum-log-radius-control", type=float, default=.04)
    parser.add_argument("--maximum-height-control", type=float, default=.06)
    parser.add_argument("--maximum-seconds", type=float, default=1800.)
    args = parser.parse_args()
    if (not FIRST_PEAK < args.M <= 300 or args.tolerance_refinement <= 1
            or args.return_basis < 6 or args.return_radial_nodes < 33
            or args.geometry_radial_nodes < 65 or args.maximum_control_iterations < 1
            or args.maximum_control_exchanges < 1 or not 30 < args.maximum_seconds <= 2400
            or min(args.rtol, args.atol, args.max_step, args.maximum_log_radius_control,
                   args.maximum_height_control) <= 0):
        raise ValueError("invalid actual-circle seed and control scope")
    source, original_nodes = source_input(args.source_state_json)
    paid = paid_seed_input(args.paid_seed_json, args)
    started = time.monotonic()
    deadline = started + args.maximum_seconds - 20
    actual = ActualTail(SOURCE_Q, deadline)
    definition = {"schema": SCHEMA, "source": source,
        "arguments": {k: v for k, v in vars(args).items() if k not in ("source_state_json", "paid_seed_json")},
        "source_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "paid_seed_input": paid,
        "paid_seed_input_sha256": hashlib.sha256(args.paid_seed_json.encode()).hexdigest(),
        "new_inner_or_outer_seed_transfers_executed": 0,
        "original_source_sha256": ORIGINAL_SOURCE_SHA256,
        "actual_positive_weight": "P=z_s*a^8/(a_s^2*s_u), epsilon=12*(a_s*s_u)^2/a^2",
        "R582_proved_cell_start": 160,
        "compact_controls": {"support": [CONTROL_LEFT, CONTROL_RIGHT],
            "bump": "exp(4-1/t-1/(1-t)); exact zero outside 0<t<1",
            "radius": "a_actual*exp(mu*bump)", "height": "z_actual+nu*bump",
            "tail_seed_independent_of_controls": True},
        "linear_return": "a_s*A_s+z_s*C_s=0; a*A_s+3*a_s*A+4*z_s*C=0",
        "no_division_by_z_s_in_return_collocation": True,
        "conservative_angular_spectral_upper_bound": True,
        "true_continuous_angular_maximum_computed": False,
        "reduced_control_gradient_is_certified": False,
        "reduced_control_gradient_scope": "explicit field-held derivative, conditionally the variable-projection derivative at differentiable full least-squares stationarity; rcond truncation and rank changes are reported, not certified away",
        "C2_core_and_actual_tail_jets_enforced": True,
        "mean_profile_changes_the_design_metric": True,
        "fixed_metric_refinement_claim": False, "README_completion_claim": False}
    emit("ACTUAL_CIRCLE_DEFINITION", definition)
    latest_control, latest_linear, latest_scan = np.zeros(2), None, None
    seeds, comparisons, refinements = [], [], []
    seed, overall_best, overall_best_score = None, None, np.inf
    natural_results, accepted, outer_records = [], 0, []
    geometry_nodes = np.array([], dtype=float)
    actual_geometry_nodes = np.array([], dtype=float)
    actual_fine_geometry_nodes = np.array([], dtype=float)
    coarse_return_s = np.array([], dtype=float)
    fine_return_s = np.array([], dtype=float)
    pending = []

    def best_snapshot():
        return None if overall_best is None else {
            **overall_best, "control": overall_best["control"].tolist(),
            "coefficients": overall_best["coefficients"].tolist()}

    try:
        seeds = paid["compact_seed_inputs"]
        emit("ACTUAL_CIRCLE_PAID_SEED_INPUT", {
            "schema": SCHEMA, "origin": paid["origin"],
            "compact_seed_inputs": seeds,
            "seed_record_identities": paid["seed_record_identities"],
            "paid_cost": paid["paid_cost"],
            "new_inner_or_outer_seed_transfers_executed": 0})
        actual.last_completed = {"phase": "reused_complete_paid_actual_mouth",
            "origin": paid["origin"], "mouth": seeds[-1]["outer"],
            "not_a_complete_core_return": True}
        seed = seeds[-1]["outer"]
        for left, right in zip(seeds[:-1], seeds[1:]):
            same_mouth = bool(left["outer"]["mouth_s"] == right["outer"]["mouth_s"])
            comparisons.append({"left_M": left["M"], "right_M": right["M"],
                "left_factor": left["tolerance_factor"], "right_factor": right["tolerance_factor"],
                "inner_balanced_slope_difference": right["inner"]["z_alpha160"] - left["inner"]["z_alpha160"],
                "same_actual_mouth": same_mouth,
                "C2_mouth_normalized_difference": (np.asarray(right["outer"]["normalized_jets_A_As_Ass_C_Cs_Css"])
                    - np.asarray(left["outer"]["normalized_jets_A_As_Ass_C_Cs_Css"])).tolist() if same_mouth else None,
                "comparison_is_not_a_numerical_error_certificate": True})
        emit("ACTUAL_CIRCLE_SEED_COMPARISONS", {"comparisons": comparisons,
            "new_inner_or_outer_seed_transfers_executed": 0,
            "comparison_cost_is_new_only_the_scalar_paid_record_readout": True,
            "original_seed_cost_retained_in_paid_input": paid["paid_cost"]})
        mouth = float(seed["mouth_s"])
        if mouth <= CONTROL_RIGHT:
            raise ArithmeticError("actual seed mouth would overlap the fixed compact-control support")
        coarse_return_s = np.unique(np.r_[0., LENGTH, CORE_END, mouth,
                                          np.linspace(CORE_END, mouth, args.return_radial_nodes)])
        fine_return_s = np.unique(np.r_[coarse_return_s,
                                        (coarse_return_s[:-1] + coarse_return_s[1:]) / 2])
        return_profile = MeanProfile(coarse_return_s)
        fine_return_profile = MeanProfile(fine_return_s)
        return_operator = UndividedReturn(return_profile, seed, args.return_basis)
        fine_return_operator = UndividedReturn(fine_return_profile, seed, args.return_basis)
        phases = np.arange(4, 640) * (np.pi / 2)
        tail_points = LENGTH - ELL / np.sqrt(phases)
        geometry_nodes = np.unique(np.r_[original_nodes, np.linspace(0, LENGTH, args.geometry_radial_nodes),
                                         tail_points, CORE_END, .324, .612, .82, mouth])
        control = np.zeros(2)
        termination = "declared_compact_control_exchanges_returned"
        for outer_index in range(args.maximum_control_exchanges):
            actual.check_clock()
            geometry_profile = MeanProfile(geometry_nodes)
            fine_geometry_nodes = np.unique(np.r_[geometry_nodes,
                (geometry_nodes[:-1] + geometry_nodes[1:]) / 2])
            fine_geometry_profile = MeanProfile(fine_geometry_nodes)
            actual_geometry_nodes = geometry_nodes.copy()
            actual_fine_geometry_nodes = fine_geometry_nodes.copy()
            if overall_best is not None:
                carried = full_geometry_report(fine_geometry_profile, overall_best["control"])
                if carried["geometry_violation_max"] > 1e-8:
                    emit("ACTUAL_CIRCLE_REQUALIFICATION", {"outer": outer_index,
                        "previous_finite_candidate_lost_new_grid_qualification": True,
                        "control": overall_best["control"].tolist(), "new_fine_geometry": carried})
                    overall_best, overall_best_score = None, np.inf
                else:
                    overall_best["fine_geometry"] = carried
                    overall_best["qualified_fine_geometry_nodes"] = fine_geometry_nodes.tolist()
            cache = {}
            pending = []

            def candidate(value):
                actual.check_clock()
                key = np.asarray(value, dtype=float).tobytes()
                if key not in cache:
                    COUNTS["mean_control_candidates"] += 1
                    coefficients, linear = return_operator.solve(value)
                    score, gradient, report = return_operator.evaluate(value, coefficients)
                    fields, _ = geometry_profile.geometry_fields(value)
                    cache[key] = {"coefficients": coefficients, "linear": linear,
                        "score": score, "gradient": gradient, "report": report,
                        "geometry_values": np.concatenate([f.v for f in fields.values()]),
                        "geometry_jacobian": np.concatenate([f.d for f in fields.values()])}
                return cache[key]

            def assess(value, *, terminal=False):
                nonlocal overall_best, overall_best_score, accepted
                nonlocal latest_control, latest_linear, latest_scan
                item = candidate(value)
                _, _, fine_linear = fine_return_operator.evaluate(value, item["coefficients"])
                full = full_geometry_report(fine_geometry_profile, value)
                field_values, _ = fine_geometry_profile.geometry_fields(value)
                for name, field in field_values.items():
                    worst = int(np.argmin(field.v))
                    s = float(fine_geometry_profile.s[worst])
                    if field.v[worst] < -1e-8 and np.min(abs(geometry_nodes - s)) > 1e-12:
                        pending.append(s)
                feasible = full["geometry_violation_max"] <= 1e-8
                fine_score = fine_linear["first_variation_eta_max"]
                take = feasible and fine_score < overall_best_score
                if take:
                    overall_best = {"control": np.asarray(value, dtype=float).copy(),
                        "coefficients": item["coefficients"].copy(), "fine_linear": fine_linear,
                        "fine_geometry": full, "coarse_linear": item["linear"],
                        "qualified_fine_geometry_nodes": fine_geometry_nodes.tolist()}
                    overall_best_score = fine_score
                    accepted += 1
                latest_control, latest_linear, latest_scan = np.asarray(value, dtype=float).copy(), fine_linear, full
                emit("ACTUAL_CIRCLE_CONTROL_ITERATE", {
                    "outer": outer_index, "control": np.asarray(value).tolist(),
                    "terminal_OptimizeResult_point": terminal, "linear_fit": item["linear"],
                    "coarse_objective": item["score"], "fine_linear": fine_linear,
                    "fine_geometry": full, "accepted_finite_geometry_and_linear_improvement": take,
                    "pending_radial_geometry_positions": sorted(set(pending)),
                    "elapsed_seconds": time.monotonic() - started})

            assess(control)
            outcome = minimize(lambda v: candidate(v)["score"], control,
                jac=lambda v: candidate(v)["gradient"], method="SLSQP",
                bounds=[(-args.maximum_log_radius_control, args.maximum_log_radius_control),
                        (-args.maximum_height_control, args.maximum_height_control)],
                constraints={"type": "ineq", "fun": lambda v: candidate(v)["geometry_values"],
                             "jac": lambda v: candidate(v)["geometry_jacobian"]},
                callback=lambda v: assess(v),
                options={"maxiter": args.maximum_control_iterations, "ftol": 1e-13, "disp": False})
            natural = {"status": int(outcome.status), "success": bool(outcome.success),
                "message": str(outcome.message), "nit": int(outcome.nit),
                "nfev": int(outcome.nfev), "njev": int(outcome.njev),
                "control": outcome.x.tolist(), "not_an_exact_resonance_certificate": True}
            natural_results.append(natural)
            assess(outcome.x, terminal=True)
            outer_records.append({"outer": outer_index, "actual_geometry_nodes": geometry_nodes.tolist(),
                "actual_return_basis": args.return_basis, "natural_backend": natural,
                "pending_geometry_nodes": sorted(set(pending))})
            control = (overall_best["control"].copy() if overall_best is not None else outcome.x.copy())
            if not pending:
                termination = "natural_control_backend_returned_without_new_fine_geometry_points"
                break
            geometry_nodes = np.unique(np.r_[geometry_nodes, pending])
        if overall_best is not None:
            # Freeze this mean profile before enlarging only the linear field
            # representation. This is a linear-return observation, not a
            # finite nonlinear fixed-metric convergence claim.
            for count in (2 * args.return_basis, 4 * args.return_basis):
                actual.check_clock()
                refined = UndividedReturn(return_profile, seed, count)
                refined_fine = UndividedReturn(fine_return_profile, seed, count)
                coeff, linear = refined.solve(overall_best["control"])
                _, _, report = refined_fine.evaluate(overall_best["control"], coeff)
                refinements.append({"basis_count": count, "linear_fit": linear,
                    "report": report, "coefficients": coeff.tolist(),
                    "fit_radial_nodes": len(refined.s),
                    "independent_fine_radial_nodes": len(refined_fine.s),
                    "same_frozen_mean_controls": overall_best["control"].tolist(),
                    "finite_nonlinear_isometry_not_claimed": True})
        final = {"schema": SCHEMA, "termination": termination,
            "definition": definition, "actual_seed_mouth": seed,
            "prior_paid_seed_cost": paid["paid_cost"],
            "new_inner_or_outer_seed_transfers_executed": 0,
            "different_scientific_and_child_wall_clocks_not_added_as_exact_seconds": True,
            "mean_control_scope": [CONTROL_LEFT, CONTROL_RIGHT],
            "best_finite_geometry_qualified_linear_candidate": best_snapshot(),
            "last_trial_control": latest_control.tolist(), "last_trial_linear": latest_linear,
            "last_trial_geometry": latest_scan, "natural_OptimizeResults": natural_results,
            "accepted_finite_linear_improvements": accepted, "outer_records": outer_records,
            "last_constructed_geometry_nodes": actual_geometry_nodes.tolist(),
            "last_constructed_fine_geometry_nodes": actual_fine_geometry_nodes.tolist(),
            "pending_geometry_nodes": sorted(set(pending)),
            "next_geometry_node_proposal": np.unique(np.r_[geometry_nodes, pending]).tolist(),
            "proposal_is_not_an_already_optimized_grid": True,
            "fixed_mean_linear_representation_refinements": refinements,
            "counts": dict(COUNTS), "total_new_scientific_seconds": time.monotonic() - started,
            "actual_complete_linear_return_proved": False,
            "finite_isometric_family_constructed": False, "README_completion_claim": False}
        emit("ACTUAL_CIRCLE_FINAL", final)
        raw = json.dumps(final, sort_keys=True, separators=(",", ":"), allow_nan=False).encode()
        emit("ACTUAL_CIRCLE_FINAL_IDENTITY", {"JSON_bytes": len(raw), "sha256": hashlib.sha256(raw).hexdigest()})
    except ClockCheckpoint as error:
        emit("ACTUAL_CIRCLE_CLOCK_CHECKPOINT", {"schema": SCHEMA, "message": str(error),
            "definition": definition,
            "actual_seed_last_completed": actual.last_completed,
            "completed_seed_evaluations": seeds,
            "completed_seed_comparisons": comparisons,
            "actual_seed_mouth": seed,
            "best_finite_geometry_qualified_linear_candidate": best_snapshot(),
            "accepted_finite_linear_improvements": accepted,
            "last_constructed_geometry_nodes": actual_geometry_nodes.tolist(),
            "last_constructed_fine_geometry_nodes": actual_fine_geometry_nodes.tolist(),
            "fit_return_nodes": coarse_return_s.tolist(),
            "fine_return_nodes": fine_return_s.tolist(),
            "pending_geometry_nodes": sorted(set(pending)),
            "next_geometry_node_proposal": np.unique(np.r_[geometry_nodes, pending]).tolist(),
            "proposal_is_not_an_already_optimized_grid": True,
            "natural_OptimizeResults": natural_results, "outer_records": outer_records,
            "fixed_mean_linear_representation_refinements": refinements,
            "last_trial_control": latest_control.tolist(), "last_trial_linear": latest_linear,
            "last_trial_geometry": latest_scan, "counts": dict(COUNTS),
            "total_new_scientific_seconds": time.monotonic() - started,
            "README_completion_claim": False})


if __name__ == "__main__":
    main()
