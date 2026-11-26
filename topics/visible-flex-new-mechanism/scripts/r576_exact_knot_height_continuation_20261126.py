#!/usr/bin/env python3
"""Continue the paid R576 height by exact radial knot insertion.

Scientific execution only in the declared public Actions job. The background
metric remains a design variable; no fixed-g convergence or reach is claimed.
"""
import argparse
from dataclasses import asdict
import hashlib
import importlib.util
import json
from pathlib import Path
import time
import numpy as np
from scipy.interpolate import BSpline

HERE = Path(__file__).resolve().parent
PARENT_FILE = "r576_function_space_continuation_20261126.py"
PARENT_SHA = "0e65a0140d0401d91f19381fffab791eb289de3c905c4aa5674735e322ea85fe"
SCHEMA = "r576-paid-height-exact-knot-insertion-v1"
SOURCE_RUN, SOURCE_JOB = 45798904133, 139836640637
SOURCE_COMMIT = "cbb89051c7fa84b902e29962dace81970da12b73"
SOURCE_LOG_SHA = "d4e3791acf70c017b3d0f22706c4805bcdb16764e3bd504c013fda2278ceacbe"
SOURCE_FINAL_SHA = "6f8ac00dd26ca122bd80f7f445f3536fd0e63cb508fe339580906aff90e61d60"
SOURCE_Q_SHA = "01b81f7f6a2764c5bc61d38ef00be86f6ad8164a350b2e642df1302276e9fd85"
PAID_ACTIVE_ETA = 1.6990646878250555e-6
INITIAL_KNOTS = (.55, .555, .56, .565, .57, .575, .58,
                 .585, .59, .60, .61, .63, .65)
RAW_Q_JSON = "[0.5188573152696206,-0.0001921541060127462,-9.068825480050256e-08,1.8734623098817277e-09,150052096.39933854,-37316.00314341096,0.2230715256171491,-0.005817267458314043,0.004534700337483398,-0.00012081974649658834,0.001619975856360685,-0.0016660312791175731,0.0012232883870837649,0.0005653828411048532,0.011774996014566606,0.021435658518070437,-8.058869413911455e-05,-6.011661069975683e-05,-6.378021952462724e-05,1.3216932771422758e-05,69.45218860912559,-12.15711203812903,3.0824539114980674,-1.1072429988031047,0.20537732410621215,-0.13878226606888514,0.25927798249336287,-0.19992048760332667,0.17714797482672173,0.72450584520915,2.075035206786145,4.3054578740199005,-0.00491349065555527,0.0018971949911123491,0.012007096866344375,-0.008700273882380264,149342094.58572006,-32065.800487028588,1.7054367682175184,0.08920452290970288,-0.00023376687671127047,-0.0014026505038607622,0.0031074237908176308,-0.004214145701995019,0.005930370818234232,-0.015536780699939941,0.012717025463721563,0.007067821611344358,-0.00013221137540527026,-0.00032803809306560324,6.390086971349848e-05,-0.0005225402303544088,0.8320452225959147,6.694324484647849,-0.49303008798596093,0.005142567413301793,-0.00045804171172543956,0.00023595484938288857,-0.0001967365147965445,0.0001608109968552057,-0.00018233439846459257,0.00016650694673211037,-0.0005763404691872392,-0.0008480839314728789,7.087237330759549e-06,1.2725790123423373e-05,-1.905884758252586e-05,3.2507812576382495e-05]"

def import_parent():
    path = HERE / PARENT_FILE
    if hashlib.sha256(path.read_bytes()).hexdigest() != PARENT_SHA:
        raise RuntimeError("paid continuation dependency changed")
    spec = importlib.util.spec_from_file_location("r576_paid_function_parent", path)
    module = importlib.util.module_from_spec(spec)
    import sys
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module

parent = import_parent()
base = parent.base
emit = base.emit
COUNTS = {"svd_factorizations": 0, "accepted_steps": 0,
          "model_directions": 0, "knot_insertions": 0,
          "same_height_mapping_observations": 0,
          "radial_space_enlargements": 0}
REJECTIONS = {}

def reject(key, local):
    local[key] = local.get(key, 0) + 1
    REJECTIONS[key] = REJECTIONS.get(key, 0) + 1

def q_identity(q):
    raw = json.dumps(q.tolist(), separators=(",", ":")).encode()
    return {"parameters": int(q.size), "JSON_bytes": len(raw),
            "sha256": hashlib.sha256(raw).hexdigest(),
            "norm": parent.stable_norm(q), "H": float(q[0])}

def insert_one(t, coefficient, degree, knot):
    """Boehm's exact simple-knot map, applied to all four angular blocks."""
    t = np.asarray(t, dtype=float)
    coefficient = np.asarray(coefficient, dtype=float)
    n = coefficient.shape[0]
    if len(t) != n + degree + 1 or coefficient.ndim != 2:
        raise ValueError("inconsistent spline coefficient dimensions")
    if not t[degree] < knot < t[n]:
        raise ValueError("new knot is not strictly interior")
    if np.min(abs(t - knot)) <= 1e-13:
        raise ValueError("this declared insertion accepts only new simple knots")
    span = int(np.searchsorted(t, knot, side="right") - 1)
    result = np.zeros((n + 1, coefficient.shape[1]))
    result[:span - degree + 1] = coefficient[:span - degree + 1]
    result[span + 1:] = coefficient[span:]
    for i in range(span - degree + 1, span + 1):
        alpha = (knot - t[i]) / (t[i + degree] - t[i])
        result[i] = alpha * coefficient[i] + (1 - alpha) * coefficient[i - 1]
    COUNTS["knot_insertions"] += 1
    return np.insert(t, span + 1, knot), result

def refine_model(old, q, knots):
    """Preserve every mode's entire pre-tanh height, including local extras."""
    old_base_count = len(old.bs.t) - old.bs.k - 1
    if old.nb != old_base_count + 4:
        raise ValueError("paid model must retain exactly its four local extras")
    blocks = q[len(base.MODES):].reshape(len(base.MODES), old.nb)
    spline_coefficients = blocks[:, :old_base_count].T.copy()
    t = old.bs.t.copy()
    for knot in sorted(knots):
        t, spline_coefficients = insert_one(t, spline_coefficients,
                                           old.bs.k, float(knot))
    new_base_count = spline_coefficients.shape[0]
    new = parent.LocalHeightDesign.__new__(parent.LocalHeightDesign)
    new.__dict__.update(old.__dict__)
    new.cache = {}
    new.bs = BSpline(t, np.eye(new_base_count), old.bs.k, extrapolate=False)
    new.nb = new_base_count + 4
    new.nq = len(base.MODES) * (1 + new.nb)
    mapped = np.zeros(new.nq)
    mapped[:len(base.MODES)] = q[:len(base.MODES)]
    new_blocks = mapped[len(base.MODES):].reshape(len(base.MODES), new.nb)
    new_blocks[:, :new_base_count] = spline_coefficients.T
    new_blocks[:, new_base_count:] = blocks[:, old_base_count:]
    COUNTS["radial_space_enlargements"] += 1
    return new, mapped

def radial_grid(model, density):
    inherited = base.radial_nodes(model.minimum * (1 + 1e-10),
                                  model.par.R, density)
    knots = np.unique(model.bs.t)
    # Every current spline span has an actual interior grid, in addition to
    # the existing phase-aware tail and regular-core observations.
    pieces = []
    for left, right in zip(knots[:-1], knots[1:]):
        pieces.append(np.linspace(left, right, 6 * density + 1))
    values = np.unique(np.r_[inherited, *pieces])
    return values[(values >= model.minimum * (1 + 1e-10))
                  & (values <= model.par.R - 1e-7)]

def compact_report(q, amplitude, data, g):
    where = np.unravel_index(int(np.argmax(g["eta"])), g["eta"].shape)
    return {"amplitude": amplitude, "gain_height": float(q[0]),
            "eta_max": float(np.max(g["eta"])),
            "eta_attainer": [float(data["r"][where[0]]),
                             float(data["theta"][where[1]])],
            "Darboux_R_max": float(np.max(abs(g["R"]))),
            "b_over_r_min": float(np.min(g["b"] / data["r"][:, None])),
            "N_min": float(np.min(g["N"])), "u_min": float(np.min(g["u"])),
            "identity_outward_ratio_min": float(np.min(g["identity_outward_ratio"])),
            "turning_error_max": float(np.max(abs(g["turning_error"]))),
            "angular_closure_error_max": float(np.max(abs(g["closure_error"]))),
            "sampled_ball_max": float(np.max(np.sqrt(
                np.sum(g["Y"] ** 2, axis=2) + g["Z"] ** 2))),
            "sampled_height_min": float(np.min(g["Z"])),
            "sampled_abs_y_max": float(np.max(abs(g["Y"][:, :, 1]))),
            "r_nodes": int(len(data["r"])), "theta_nodes": int(len(data["theta"]))}

def mapping_observation(old, oldq, new, newq, amplitude, r, ntheta):
    old_data, new_data = old.prepare(r, ntheta), new.prepare(r, ntheta)
    old_jets = old.height_jets(oldq, amplitude, old_data)
    new_jets = new.height_jets(newq, amplitude, new_data)
    differences = [float(np.max(abs(a - b))) for a, b in zip(old_jets, new_jets)]
    residual_difference = float(np.max(abs(old.geometry(oldq, amplitude, old_data)
                                               - new.geometry(newq, amplitude, new_data))))
    COUNTS["same_height_mapping_observations"] += 1
    emit("HEIGHT_KNOT_EXACT_MAPPING", {
        "inserted_space_preserves_the_polynomial_function_in_exact_arithmetic": True,
        "six_height_jet_maximum_differences": differences,
        "complete_normalized_residual_maximum_difference": residual_difference,
        "old_q": q_identity(oldq), "new_q": q_identity(newq),
        "same_reference_profile_and_envelope_normalization": True})
    if max(differences) > 1e-7 or residual_difference > 1e-7:
        raise ArithmeticError("floating knot map failed its declared same-height observation")

def solve_stage(model, initial, amplitude, data, args, deadline):
    q = initial.copy()
    damping = 1e-5
    history = []
    status = "declared_iteration_limit"
    for iteration in range(args.iterations):
        if time.monotonic() >= deadline:
            status = "declared_scientific_budget"
            break
        try:
            g = model.geometry(q, amplitude, data, details=True)
        except base.DomainError as error:
            status = "actual_initial_domain_failure"
            emit("HEIGHT_KNOT_INITIAL_DOMAIN", {"message": str(error),
                 "amplitude": amplitude, "actual_q": q_identity(q)})
            break
        residual = g["residual_vector"]
        if not np.all(np.isfinite(residual)):
            status = "nonfinite_actual_residual"
            break
        objective = float(np.dot(residual, residual) / residual.size)
        report = compact_report(q, amplitude, data, g)
        report.update({"iteration": iteration, "objective": objective,
                       "damping": damping, "actual_q": q_identity(q)})
        history.append(report)
        emit("HEIGHT_KNOT_ITERATION", report)
        if report["eta_max"] <= args.target_eta:
            status = "sampled_metric_target"
            break
        J = base.jacobian(model, q, amplitude, data)
        if not np.all(np.isfinite(J)):
            status = "nonfinite_actual_jacobian"
            break
        norms = np.linalg.norm(J, axis=0)
        scales = np.maximum(norms, 1e-12)
        Js = J / scales
        U, singular, Vh = np.linalg.svd(Js, full_matrices=False)
        COUNTS["svd_factorizations"] += 1
        projected = U.T @ residual
        # Damped SVD uses every computed singular direction; the rank threshold
        # below is reported only and does not silently discard directions.
        threshold = max(Js.shape) * np.finfo(float).eps * singular[0]
        rank = int(np.sum(singular > threshold))
        gradient = Js.T @ residual
        spectrum = {"reported_numerical_rank": rank,
                    "rank_threshold": float(threshold),
                    "singular_min": float(singular[-1]),
                    "singular_max": float(singular[0]),
                    "columns_below_scale_floor": int(np.sum(norms < 1e-12)),
                    "column_norm_min": float(np.min(norms)),
                    "column_norm_max": float(np.max(norms)),
                    "scaled_gradient_inf": float(np.max(abs(gradient))),
                    "normal_equations_not_formed": True}
        accepted = False
        local_rejections = {}
        last_direction = None
        for trial in range(8):
            if time.monotonic() >= deadline:
                status = "declared_scientific_budget"
                break
            base.COUNTS["linear_solves"] += 1
            COUNTS["model_directions"] += 1
            scaled_direction = -Vh.T @ (
                singular * projected / (singular * singular + damping))
            direction = scaled_direction / scales
            if not np.all(np.isfinite(direction)):
                reject("nonfinite_direction", local_rejections)
                damping = min(1e12, damping * 10)
                continue
            raw_norm = parent.stable_norm(direction)
            factor, jet_measures = parent.function_trial_limit(
                model, q, direction, amplitude, data, g)
            direction *= factor
            Jdirection = J @ direction
            cross = float(np.dot(residual, Jdirection))
            square = float(np.dot(Jdirection, Jdirection))
            last_direction = {"raw_parameter_direction_norm": raw_norm,
                "scaled_direction_norm": parent.stable_norm(scaled_direction),
                "function_factor": factor, "height_jet_measures": jet_measures,
                "damping": damping}
            for fraction in (1., .5, .25, .125, .0625, .03125,
                             .015625, .0078125, .00390625):
                predicted = -(2 * fraction * cross + fraction * fraction * square) / residual.size
                if predicted <= 0:
                    reject("nonpositive_predicted_decrease", local_rejections)
                    continue
                base.COUNTS["line_search_trials"] += 1
                proposed = q + fraction * direction
                if not .02 <= proposed[0] <= 4:
                    reject("H_bounds", local_rejections)
                    continue
                try:
                    rr = model.geometry(proposed, amplitude, data)
                except base.DomainError as error:
                    reject("domain: " + str(error), local_rejections)
                    continue
                if not np.all(np.isfinite(rr)):
                    reject("nonfinite_trial_residual", local_rejections)
                    continue
                new_objective = float(np.dot(rr, rr) / rr.size)
                actual = objective - new_objective
                ratio = actual / predicted
                resolvable = 32 * np.finfo(float).eps * max(objective, 1e-30)
                if actual <= resolvable:
                    reject("no_resolvable_actual_decrease", local_rejections)
                    continue
                if ratio < 1e-4:
                    reject("actual_over_predicted_below_1e-4", local_rejections)
                    continue
                q = proposed
                accepted = True
                COUNTS["accepted_steps"] += 1
                emit("HEIGHT_KNOT_ACCEPTED", {
                    "amplitude": amplitude, "iteration": iteration, "LM_trial": trial,
                    "actual_q": q_identity(q), "fraction": fraction,
                    "predicted_decrease": predicted, "actual_decrease": actual,
                    "actual_over_predicted": ratio, "spectrum": spectrum,
                    "direction": last_direction,
                    "rejected_trials_before_acceptance": local_rejections})
                if ratio > .75:
                    damping = max(1e-16, damping / 3)
                elif ratio < .25:
                    damping = min(1e12, damping * 2)
                break
            if accepted:
                break
            damping = min(1e12, damping * 10)
        if not accepted:
            if status != "declared_scientific_budget":
                status = "finite_space_no_resolvable_accepted_step"
            emit("HEIGHT_KNOT_STALL", {
                "amplitude": amplitude, "iteration": iteration, "status": status,
                "actual_q": q_identity(q), "spectrum": spectrum,
                "last_direction": last_direction, "rejection_reasons": local_rejections,
                "geometric_failure_not_inferred_from_optimizer_status": True})
            break
    return q, status, history

def assess(model, q, amplitude, data, density, args):
    try:
        record = {"actual": base.small_report(model, q, amplitude, data)}
    except base.DomainError as error:
        return {"actual_domain_error": str(error),
                "fine_observation_passed": False}, None, None
    fine_r = radial_grid(model, 2 * density)
    fine_data = model.prepare(fine_r, 2 * len(data["theta"]))
    row_eta = None
    try:
        gg = model.geometry(q, amplitude, fine_data, details=True)
        row_eta = np.max(gg["eta"], axis=1)
        record["same_q_fine"] = compact_report(q, amplitude, fine_data, gg)
        r = fine_r[(fine_r > model.minimum + 1e-5)
                   & (fine_r < model.par.R - 1e-6)]
        record["direct_step"] = base.actual_curvature_observation(
            model, q, amplitude, r, len(fine_data["theta"]))
        record["direct_half_step"] = base.actual_curvature_observation(
            model, q, amplitude, r, len(fine_data["theta"]), .5)
    except base.DomainError as error:
        record["fine_or_direct_domain_error"] = str(error)
    record["fine_observation_passed"] = (
        "same_q_fine" in record and row_eta is not None
        and record["same_q_fine"]["eta_max"] <= args.target_eta
        and "direct_half_step" in record
        and max(record["direct_step"]["direct_reconstructed_metric_eta"],
                record["direct_half_step"]["direct_reconstructed_metric_eta"])
              <= 8 * args.target_eta
        and min(record["direct_step"]["direct_position_outward_ratio_min"],
                record["direct_half_step"]["direct_position_outward_ratio_min"]) > 0)
    return record, fine_data, row_eta

def select_new_knots(model, data, row_eta, args):
    knots = np.unique(model.bs.t)
    candidates = []
    for left, right in zip(knots[:-1], knots[1:]):
        if right - left <= 2 * args.minimum_knot_spacing:
            continue
        selected = ((data["r"] >= max(left, model.minimum))
                    & (data["r"] <= right))
        if not np.any(selected):
            continue
        score = float(np.max(row_eta[selected]))
        if score <= args.target_eta:
            continue
        mid = float((left + right) / 2)
        if not model.minimum < mid < model.par.R - 1e-6:
            continue
        candidates.append((score, float(left), float(right), mid))
    candidates.sort(reverse=True)
    chosen = candidates[:args.knots_per_refinement]
    return [item[3] for item in chosen], [
        {"observed_eta": a, "span": [b, c], "inserted_knot": d}
        for a, b, c, d in chosen]

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--maximum-seconds", type=float, default=2400.)
    parser.add_argument("--M", type=int, choices=[25], default=25)
    parser.add_argument("--rtol", type=float, default=2e-11)
    parser.add_argument("--atol", type=float, default=2e-13)
    parser.add_argument("--iterations", type=int, default=60)
    parser.add_argument("--theta-nodes", type=int, default=64)
    parser.add_argument("--target-eta", type=float, default=2e-9)
    parser.add_argument("--height-saturation", type=float, choices=[.15], default=.15)
    parser.add_argument("--maximum-refinements", type=int, default=6)
    parser.add_argument("--knots-per-refinement", type=int, default=6)
    parser.add_argument("--minimum-knot-spacing", type=float, default=1e-5)
    args = parser.parse_args()
    if (not 60 < args.maximum_seconds <= 2400 or args.iterations < 1
            or not 0 <= args.maximum_refinements <= 6
            or not 1 <= args.knots_per_refinement <= 6
            or args.theta_nodes < 32 or args.theta_nodes % 4
            or min(args.target_eta, args.rtol, args.atol, args.minimum_knot_spacing) <= 0):
        raise ValueError("outside declared knot-insertion scope")
    started = time.monotonic()
    deadline = started + args.maximum_seconds
    if hashlib.sha256(RAW_Q_JSON.encode()).hexdigest() != SOURCE_Q_SHA:
        raise RuntimeError("paid 68-dimensional state identity changed")
    q = np.asarray(json.loads(RAW_Q_JSON), dtype=float)
    profile = base.gain.Profile(R=.85, log_suppression=6., core_scale=.5,
                                gain_height=parent.PAID_REFERENCE_H)
    amplitudes = [1e-5, 3e-5, 1e-4, 3e-4, .001, .003, .01, .03, .1, .2]
    emit("HEIGHT_KNOT_DEFINITION", {
        "schema": SCHEMA, "arguments": vars(args),
        "source_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "parent_sha256": PARENT_SHA, "paid_run": SOURCE_RUN, "paid_job": SOURCE_JOB,
        "paid_commit": SOURCE_COMMIT, "paid_raw_log_sha256": SOURCE_LOG_SHA,
        "paid_final_sha256": SOURCE_FINAL_SHA, "paid_q_sha256": SOURCE_Q_SHA,
        "reference_profile": asdict(profile), "initial_knots": list(INITIAL_KNOTS),
        "amplitudes": amplitudes, "old_inner_Riccati_repeated": False,
        "old_gain_shooting_repeated": False,
        "knot_map": "simple-knot Boehm map, separately for four spline blocks; preserve four local extras",
        "trial_solver": "column-scaled damped SVD, all singular directions; stable predicted decrease",
        "exact_or_fixed_metric_convergence_claim": False,
        "continuous_reach_or_README_completion_claim": False})
    flats = [parent.PaidFlatSeed(j, args) for j in base.MODES]
    modes = [base.AdmissibleMode(f, profile, args) for f in flats]
    for flat, mode in zip(flats, modes):
        emit("HEIGHT_KNOT_PAID_BASIS", {"flat": flat.finite_inner_data,
                                      "mode": mode.receipt()})
    original = base.HeightDesign(profile, modes, [.235, .27, .34, .48, .64, .78], args)
    model, _ = parent.enrich_same_state(original, np.zeros(original.nq))
    if q.size != model.nq:
        raise ValueError("paid q is not the exact retained local-enrichment space")
    old_r = base.radial_nodes(model.minimum * (1 + 1e-10), profile.R, 1)
    old_data = model.prepare(old_r, args.theta_nodes)
    baseline = base.small_report(model, q, amplitudes[0], old_data)
    baseline.update({"paid_active_eta": PAID_ACTIVE_ETA,
                     "eta_difference": baseline["eta_max"] - PAID_ACTIVE_ETA,
                     "actual_q": q_identity(q)})
    emit("HEIGHT_KNOT_PAID_BASELINE", baseline)
    if abs(baseline["eta_difference"]) > max(1e-11, 1e-5 * PAID_ACTIVE_ETA):
        raise ArithmeticError("paid 68-dimensional height reconstruction changed")
    old, oldq = model, q
    model, q = refine_model(model, q, INITIAL_KNOTS)
    mapping_observation(old, oldq, model, q, amplitudes[0], old_r, args.theta_nodes)
    density, angular = 1, args.theta_nodes
    data = model.prepare(radial_grid(model, density), angular)
    stages = []
    refinements = 0
    final_status = "declared_amplitude_list_complete"
    for amplitude in amplitudes:
        exchanges = []
        while True:
            q, status, history = solve_stage(model, q, amplitude, data, args, deadline)
            observation, fine_data, row_eta = assess(model, q, amplitude, data, density, args)
            exchange = {"status": status, "iterations": len(history),
                        "spline_interior_knots": np.unique(model.bs.t[model.bs.k + 1:-model.bs.k - 1]).tolist(),
                        "actual_q_identity": q_identity(q), **observation}
            exchanges.append(exchange)
            emit("HEIGHT_KNOT_EXCHANGE", exchange)
            if status == "sampled_metric_target" and observation["fine_observation_passed"]:
                break
            if "actual_domain_error" in observation:
                status = "actual_current_amplitude_domain_failure"
                break
            if time.monotonic() >= deadline:
                status = "declared_scientific_budget"
                break
            # A missed independent observation first changes the actual grid,
            # while preserving the same model and q.
            if status == "sampled_metric_target" and density < 2:
                density *= 2
                angular *= 2
                data = fine_data
                emit("HEIGHT_KNOT_GRID_PROMOTION", {
                    "density": density, "theta_nodes": angular,
                    "same_q": q_identity(q), "same_height_basis": True})
                continue
            if refinements >= args.maximum_refinements:
                status = "declared_radial_refinement_capacity"
                break
            if row_eta is None:
                gg = model.geometry(q, amplitude, data, details=True)
                knot_data, row_eta = data, np.max(gg["eta"], axis=1)
            else:
                knot_data = fine_data
            new_knots, selection = select_new_knots(model, knot_data, row_eta, args)
            if not new_knots:
                status = "no_unresolved_refinable_radial_span"
                break
            if time.monotonic() > deadline - 20:
                status = "declared_scientific_budget_before_new_space"
                break
            old, oldq = model, q
            model, q = refine_model(model, q, new_knots)
            refinements += 1
            mapping_observation(old, oldq, model, q, amplitude, data["r"], len(data["theta"]))
            data = model.prepare(radial_grid(model, density), angular)
            emit("HEIGHT_KNOT_RADIAL_ENLARGEMENT", {
                "index": refinements, "amplitude": amplitude, "selection": selection,
                "actual_new_q": q_identity(q), "actual_new_r_nodes": len(data["r"]),
                "actual_theta_nodes": len(data["theta"]),
                "new_space_is_only_optimized_after_this_record": True})
        stage = {"amplitude": amplitude, "status": status,
                 "actual_retained_q": q.tolist(), "actual_q_identity": q_identity(q),
                 "metric_observation_accepted_at_this_amplitude": status == "sampled_metric_target",
                 "actual_spline_knot_vector": model.bs.t.tolist(),
                 "actual_local_extra_count": 4, "exchanges": exchanges}
        stages.append(stage)
        emit("HEIGHT_KNOT_STAGE", stage)
        if status != "sampled_metric_target":
            final_status = status
            break
    final = {"schema": SCHEMA, "status": final_status, "stages": stages,
        "elapsed_seconds": time.monotonic() - started,
        "new_counts": COUNTS, "rejection_reasons": REJECTIONS,
        "base_counts": dict(base.COUNTS), "function_trial_counts": dict(parent.EXTRA),
        "gain_import_counts": dict(base.gain.COUNTS),
        "adaptive_refinements_executed": refinements,
        "mode_height_scales": model.mode_height_scales.tolist(),
        "envelope_scale": model.envelope_scale,
        "old_inner_Riccati_repeated": False, "old_gain_shooting_repeated": False,
        "finite_input_ODE_errors_certified": False,
        "actual_exact_isometry_or_continuous_reach_proved": False,
        "same_metric_refinement_claim": False, "README_completion_claim": False,
        "raw_arrays_tables_artifacts_releases_or_git_writes": False}
    emit("HEIGHT_KNOT_FINAL", final)
    raw = json.dumps(final, sort_keys=True, separators=(",", ":"), allow_nan=False).encode()
    emit("HEIGHT_KNOT_FINAL_IDENTITY", {"JSON_bytes": len(raw),
                                       "sha256": hashlib.sha256(raw).hexdigest()})

if __name__ == "__main__":
    main()

