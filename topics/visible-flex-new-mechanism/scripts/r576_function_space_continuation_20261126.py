#!/usr/bin/env python3
"""Continue the paid R576 height state with a function-space trial limit.

The old inner Riccati chains and background shooting are not repeated.
All science belongs to public Actions.  The complete old geometry source is
hash-bound; only the continuation driver and trial metric are new.
"""
import argparse
from dataclasses import asdict
import hashlib
import importlib.util
import json
import math
from pathlib import Path
import sys
import time
import numpy as np

HERE = Path(__file__).resolve().parent
BASE_FILE = "r576_finite_height_turning_20261126.py"
BASE_SHA = "40d70b729664a8d59dc653ce30315ea356ce09c461bd4d108fc0a78d05517ad9"
SOURCE_RUN = 45795351410
SOURCE_JOB = 139824473317
SOURCE_COMMIT = "6d1b3233cf6e174cff53e75b96207e1bed29bf82"
SOURCE_LOG_SHA = "38668b1831fdb92a902c88146efefbc926164d34e4d18ba30616c77941a4d729"
SOURCE_FINAL_SHA = "73663bc20f8fa6908fbe108ce977b9ff5d7a96568ebba62ecb201e6471aa1caa"
SOURCE_Q_SHA = "3312fb30ebf6fa9ddcb44fc281e055ce51da7ea1eb201f804a23b88e9124dd37"
PAID_REFERENCE_H = .5188880921515537
PAID_ACTIVE_ETA = 5.2037331962617675e-6
RAW_Q_JSON = "[0.5188880894107396,-4.83138568674759e-07,-2.906594007475052e-09,1.610871812152455e-11,48.90224017709697,-47.302690438568185,0.00067857378280848,-6.210666527431936e-06,5.9642250969504734e-06,-6.5767133385462795e-06,4.738769546135226e-06,-9.603031029215345e-06,1.516133245884239e-05,-6.799451270288086e-05,-9.983073947771269e-05,-0.0002087577910505998,2.003796943346312e-05,-0.048709761428430656,0.011710321965706523,0.00020432108967986302,0.00018581439042997743,-0.00021248095291757465,0.0005572218795174203,-0.0005002309457287324,0.0007654248666881296,0.0018390881996249834,0.005208013733744809,0.01030935844305025,48.66472152002968,-75.20471356974763,0.027310556365572097,0.0006244490609000711,-4.2474326620954757e-05,1.5221535932214718e-05,1.7070111806748015e-06,-2.9787618669421497e-05,7.392658696756411e-05,-0.0002419745839861336,0.00012510324737350162,-3.3096232730247735e-05,1.156450210541192e-07,7.41925196963687e-05,0.00011596058408711507,-3.7715461077809223e-06,-5.873509350833634e-07,5.165978301879732e-07,-6.572226414954843e-07,8.934717657063385e-07,-1.5452850770007535e-06,2.665440743334575e-06,-6.53980111594457e-06,-8.653509714821982e-06]"
PAID_SEEDS = json.loads("{\"2\":{\"M\":25,\"alpha_first\":108.37588351522939,\"z_at_alpha_first\":0.12009089235212347,\"rho_first_plus_one\":8.985323950640713e-88,\"display_log_scale\":1559.1449362672672},\"4\":{\"M\":25,\"alpha_first\":108.3758665138987,\"z_at_alpha_first\":0.12009089735559321,\"rho_first_plus_one\":4.5163366370167665e-89,\"display_log_scale\":1594.3750375063262},\"6\":{\"M\":25,\"alpha_first\":108.37583817830033,\"z_at_alpha_first\":0.12009090861745494,\"rho_first_plus_one\":8.678234870257888e-90,\"display_log_scale\":1594.7026336454442},\"8\":{\"M\":25,\"alpha_first\":108.37579850836339,\"z_at_alpha_first\":0.12009093052188517,\"rho_first_plus_one\":2.7454140125273373e-90,\"display_log_scale\":1574.4014615001925}}")
SCHEMA = "r576-paid-state-function-space-height-continuation-v2"
EXTRA = {"height_direction_evaluations": 0, "height_direction_points": 0,
         "physical_trial_limits": 0, "accepted_steps": 0,
         "rejected_model_steps": 0}

def emit(tag, value):
    print(tag + " " + json.dumps(value, sort_keys=True, separators=(",", ":"),
                                 allow_nan=False), flush=True)

def load_base():
    path = HERE / BASE_FILE
    if hashlib.sha256(path.read_bytes()).hexdigest() != BASE_SHA:
        raise RuntimeError("bound R576 geometry source changed")
    spec = importlib.util.spec_from_file_location("r576_paid_geometry", path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module

base = load_base()

class PaidFlatSeed(base.FlatSeed):
    """Reuse the actual alpha17 Cauchy direction; rebuild only needed dense data."""
    def __init__(self, mode, args):
        self.mode, self.args = mode, args
        paid = PAID_SEEDS[str(mode)]
        if args.M != paid["M"]:
            raise ValueError("paid finite-tail identity has a different M")
        inner = dict(paid)
        inner["nfev_inner"] = 0
        self.inner = inner
        self.alpha = inner["alpha_first"]
        self.minimum_radius = base.RC + base.ELL / self.alpha
        base.seed.ANGULAR_MODE, base.seed.PHASE = mode, 0.
        last_u = base.ELL / (base.R0 - base.RC)
        centers = np.pi / 2 + 2 * np.pi * np.arange(base.seed.FIRST_PEAK + 1)
        breaks = np.r_[self.alpha,
                       np.sort(centers[(centers < self.alpha) & (centers > last_u)])[::-1],
                       last_u]
        state = np.array([1., inner["z_at_alpha_first"]])
        log_scale = 0.
        self.segments = []
        for high, low in zip(breaks[:-1], breaks[1:]):
            sol = base.seed.integrate(float(high), float(low), state,
                                      args.rtol, args.atol, .1, dense=True)
            base.COUNTS["seed_RHS"] += int(sol.nfev)
            self.segments.append((float(low), float(high), sol.sol, log_scale))
            outgoing = sol.y[:, -1]
            scale = float(np.max(np.abs(outgoing)))
            if not (scale > 0 and np.isfinite(scale)):
                raise ArithmeticError("outward paid-state normalization failed")
            log_scale += math.log(scale)
            state = outgoing / scale
        outer = base.seed.scaled_jets(last_u, state)
        # Preserve the old common display convention, also for the higher modes.
        self.display_log = paid["display_log_scale"]
        self.outer = base.scaled_values(outer, log_scale - self.display_log)
        self.finite_inner_data = {
            "mode": mode, "M": args.M, "alpha_first": self.alpha,
            "z_alpha_first": inner["z_at_alpha_first"],
            "source_run": SOURCE_RUN, "source_job": SOURCE_JOB,
            "inner_Riccati_RHS_this_run": 0,
            "old_inner_ODE_error_not_erased_by_reuse": True,
            "outer_jets": self.outer.tolist(),
            "minimum_numerically_evaluated_radius": self.minimum_radius,
        }

def stable_norm(value):
    scale = float(np.max(np.abs(value)))
    return 0. if scale == 0 else scale * float(np.linalg.norm(value / scale))

def function_trial_limit(model, q, direction, amplitude, data, current_geometry):
    """Limit changes in height jets, invariant under rescaling parameter columns."""
    EXTRA["height_direction_evaluations"] += 1
    EXTRA["height_direction_points"] += int(data["r"].size * data["theta"].size)
    direction_scale = max(1., float(np.max(np.abs(direction))))
    jets = model.height_jets(q.astype(complex) + 1e-25j * (direction / direction_scale), amplitude, data)
    df, dfr, dfrr, dft, dftt, dfrt = [np.imag(a) / 1e-25 * direction_scale for a in jets]
    Hstep = direction[0]
    dZ = Hstep * data["gain_height"][:, None] + df
    dZr = -Hstep * data["gain_w"][:, None] + dfr
    dZrr = -Hstep * data["gain_wr"][:, None] + dfrr
    r = data["r"][:, None]
    E = current_geometry["E"]
    sqrtE = np.sqrt(E)
    measures = {
        "height_over_002": float(np.max(np.abs(dZ)) / .02),
        "meridian_slope_over_01": float(np.max(np.abs(dZr) / sqrtE) / .1),
        "angular_slope_over_01": float(np.max(np.abs(dft) / r) / .1),
        "radial_second_jet_over_2": float(np.max(np.abs(dZrr) / E) / 2.),
        "mixed_second_jet_over_2": float(np.max(np.abs(dfrt) / (r * sqrtE)) / 2.),
        "angular_second_jet_over_2": float(np.max(np.abs(dftt) / (r * r)) / 2.),
    }
    maximum = max(measures.values())
    if not np.isfinite(maximum):
        raise ArithmeticError("nonfinite function-space trial direction")
    factor = min(1., 1. / maximum) if maximum > 0 else 1.
    if factor < 1:
        EXTRA["physical_trial_limits"] += 1
    return factor, measures

def solve_stage(model, initial, amplitude, data, args, started):
    q = initial.copy()
    damping = 1e-5
    history = []
    status = "iteration_limit"
    for iteration in range(args.iterations):
        if time.monotonic() - started > args.maximum_seconds:
            status = "declared_run_budget"
            break
        try:
            geom = model.geometry(q, amplitude, data, details=True)
        except base.DomainError as error:
            status = "initial_domain_failure: " + str(error)
            break
        residual = geom["residual_vector"]
        if not np.all(np.isfinite(residual)):
            status = "nonfinite_residual"
            break
        objective = float(np.dot(residual, residual) / residual.size)
        report = base.small_report(model, q, amplitude, data)
        report.update({"iteration": iteration, "objective": objective, "damping": damping})
        history.append(report)
        emit("HEIGHT_FUNCTION_ITERATION", report)
        if report["eta_max"] <= args.target_eta:
            status = "sampled_metric_target"
            break
        J = base.jacobian(model, q, amplitude, data)
        if not np.all(np.isfinite(J)):
            status = "nonfinite_jacobian"
            break
        norms = np.linalg.norm(J, axis=0)
        column_scale = np.maximum(norms, 1e-12)
        Js = J / column_scale
        accepted = False
        for trial in range(8):
            base.COUNTS["linear_solves"] += 1
            scaled_direction = np.linalg.solve(
                Js.T @ Js + damping * np.eye(q.size), -Js.T @ residual)
            direction = scaled_direction / column_scale
            if not np.all(np.isfinite(direction)):
                damping = min(1e12, damping * 10)
                EXTRA["rejected_model_steps"] += 1
                continue
            raw_norm = stable_norm(direction)
            function_factor, jet_measures = function_trial_limit(
                model, q, direction, amplitude, data, geom)
            direction *= function_factor
            Jdirection = J @ direction
            accepted_record = None
            for fraction in (1., .5, .25, .125, .0625, .03125, .015625, .0078125, .00390625):
                linear = residual + fraction * Jdirection
                predicted = objective - float(np.dot(linear, linear) / residual.size)
                if predicted <= 0:
                    continue
                base.COUNTS["line_search_trials"] += 1
                proposed = q + fraction * direction
                if not (.02 <= proposed[0] <= 4):
                    continue
                try:
                    new_residual = model.geometry(proposed, amplitude, data)
                except base.DomainError:
                    continue
                if not np.all(np.isfinite(new_residual)):
                    continue
                new_objective = float(np.dot(new_residual, new_residual) / new_residual.size)
                actual = objective - new_objective
                ratio = actual / predicted
                if actual > 0 and ratio >= 1e-4:
                    q = proposed
                    accepted = True
                    EXTRA["accepted_steps"] += 1
                    accepted_record = {
                        "amplitude": amplitude, "iteration": iteration, "LM_trial": trial,
                        "actual_parameter_direction_norm_before_function_limit": raw_norm,
                        "column_scaled_direction_norm": stable_norm(scaled_direction),
                        "unscaled_parameter_ball_used": False,
                        "function_limit_factor": function_factor,
                        "height_jet_trial_measures": jet_measures,
                        "accepted_backtracking_fraction": fraction,
                        "predicted_reduction": predicted, "actual_reduction": actual,
                        "actual_over_predicted": ratio,
                        "column_norm_min": float(np.min(norms)),
                        "column_norm_max": float(np.max(norms)),
                        "columns_below_scale_floor": int(np.sum(norms < 1e-12)),
                        "accepted_q_sha256": hashlib.sha256(json.dumps(q.tolist(), separators=(",", ":")).encode()).hexdigest(),
                        "accepted_q_norm": stable_norm(q), "accepted_gain_H": float(q[0]),
                    }
                    if ratio > .75:
                        damping = max(1e-12, damping / 3)
                    elif ratio < .25:
                        damping = min(1e12, damping * 2)
                    emit("HEIGHT_FUNCTION_ACCEPTED", accepted_record)
                    break
            if accepted:
                break
            damping = min(1e12, damping * 10)
            EXTRA["rejected_model_steps"] += 1
        if not accepted:
            status = "no_domain_preserving_function_step"
            break
    return q, status, history

class LocalHeightDesign(base.HeightDesign):
    """One declared compact enrichment, with the old height function unchanged."""
    def prepare(self, r, ntheta):
        data = super().prepare(r, ntheta)
        if data.get("local_enrichment_added", False):
            return data
        rr = data["r"]
        env = self.envelope(rr, data["fields"])
        width = .10
        t = (rr - .53) / width
        chi, chit, chitt = base.step2(t)
        beta = 4 * chi * (1 - chi)
        betar = 4 * chit * (1 - 2 * chi) / width
        betarr = (4 * chitt * (1 - 2 * chi) - 8 * chit * chit) / width ** 2
        v = 2 * t - 1
        P = np.stack([np.ones_like(v), v, (3 * v * v - 1) / 2,
                      (5 * v ** 3 - 3 * v) / 2], axis=1)
        Pr = np.stack([np.zeros_like(v), np.ones_like(v), 3 * v,
                       (15 * v * v - 3) / 2], axis=1) * (2 / width)
        Prr = np.stack([np.zeros_like(v), np.zeros_like(v), 3 * np.ones_like(v),
                        15 * v], axis=1) * (2 / width) ** 2
        L = beta[:, None] * P
        Lr = betar[:, None] * P + beta[:, None] * Pr
        Lrr = betarr[:, None] * P + 2 * betar[:, None] * Pr + beta[:, None] * Prr
        extra = np.stack([env[:, 0, None] * L,
                          env[:, 1, None] * L + env[:, 0, None] * Lr,
                          env[:, 2, None] * L + 2 * env[:, 1, None] * Lr + env[:, 0, None] * Lrr], axis=2)
        data["bulk"] = np.concatenate([data["bulk"], extra], axis=1)
        data["local_enrichment_added"] = True
        return data

def enrich_same_state(old, q):
    new = LocalHeightDesign.__new__(LocalHeightDesign)
    new.__dict__.update(old.__dict__)
    new.cache = {}
    new.nb = old.nb + 4
    new.nq = len(base.MODES) + len(base.MODES) * new.nb
    mapped = np.zeros(new.nq)
    mapped[:len(base.MODES)] = q[:len(base.MODES)]
    mapped[len(base.MODES):].reshape(len(base.MODES), new.nb)[:, :old.nb] = q[len(base.MODES):].reshape(len(base.MODES), old.nb)
    return new, mapped

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--maximum-seconds", type=float, default=2400)
    parser.add_argument("--M", type=int, choices=[25], default=25)
    parser.add_argument("--rtol", type=float, default=2e-11)
    parser.add_argument("--atol", type=float, default=2e-13)
    parser.add_argument("--iterations", type=int, default=100)
    parser.add_argument("--theta-nodes", type=int, default=64)
    parser.add_argument("--target-eta", type=float, default=2e-9)
    parser.add_argument("--height-saturation", type=float, choices=[.15], default=.15)
    args = parser.parse_args()
    started = time.monotonic()
    if hashlib.sha256(RAW_Q_JSON.encode()).hexdigest() != SOURCE_Q_SHA:
        raise RuntimeError("paid actual q payload changed")
    q = np.asarray(json.loads(RAW_Q_JSON), dtype=float)
    if q.size != 52:
        raise RuntimeError("paid q dimension mismatch")
    profile = base.gain.Profile(R=.85, log_suppression=6., core_scale=.5,
                                gain_height=PAID_REFERENCE_H)
    amplitudes = [1e-5, 3e-5, 1e-4, 3e-4, .001, .003, .01, .03, .1, .2]
    knots = [.235, .27, .34, .48, .64, .78]
    emit("HEIGHT_FUNCTION_DEFINITION", {
        "schema": SCHEMA, "arguments": vars(args),
        "source_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "base_source_sha256": BASE_SHA, "paid_run": SOURCE_RUN, "paid_job": SOURCE_JOB,
        "paid_source_commit": SOURCE_COMMIT, "paid_raw_log_sha256": SOURCE_LOG_SHA,
        "paid_final_sha256": SOURCE_FINAL_SHA, "paid_actual_q_sha256": SOURCE_Q_SHA,
        "reference_profile": asdict(profile), "amplitudes": amplitudes,
        "old_inner_Riccati_repeated": False, "old_gain_shooting_repeated": False,
        "trial_limit": "actual first variation of height and its spatial jets; no Euclidean q ball",
        "acceptance": "positive actual objective reduction and actual/predicted >= 1e-4",
        "optional_single_enrichment": "after actual same-space stall, append four compact radial functions on [.53,.63] per mode; zero new coefficients exactly preserve paid height",
        "direct_metric_observation_tolerance": 8 * args.target_eta,
        "fixed_metric_refinement": False, "complete_finite_family": False})
    flats = [PaidFlatSeed(j, args) for j in base.MODES]
    for f in flats:
        emit("HEIGHT_FUNCTION_PAID_SEED", f.finite_inner_data)
    modes = [base.AdmissibleMode(f, profile, args) for f in flats]
    for mode in modes:
        emit("HEIGHT_FUNCTION_CORE_REBUILD", mode.receipt())
    model = base.HeightDesign(profile, modes, knots, args)
    active_density = 1
    r = base.radial_nodes(model.minimum * (1 + 1e-10), profile.R, active_density)
    data = model.prepare(r, args.theta_nodes)
    baseline = base.small_report(model, q, amplitudes[0], data)
    baseline["paid_previous_active_eta"] = PAID_ACTIVE_ETA
    baseline["eta_difference"] = baseline["eta_max"] - PAID_ACTIVE_ETA
    emit("HEIGHT_FUNCTION_PAID_BASELINE", baseline)
    if abs(baseline["eta_difference"]) > max(1e-11, 1e-5 * PAID_ACTIVE_ETA):
        raise ArithmeticError("reconstructed paid state does not match its original active observation")
    stages = []
    enriched = False
    for amplitude in amplitudes:
        exchanges = []
        while True:
            q, status, history = solve_stage(model, q, amplitude, data, args, started)
            exchange = {"active_density": active_density, "status": status,
                        "iterations": len(history), "same_q_active": None, "same_q_fine": None}
            try:
                exchange["same_q_active"] = base.small_report(model, q, amplitude, data)
                fine_density = 2 * active_density
                fine_r = base.radial_nodes(model.minimum * (1 + 1e-10), profile.R, fine_density)
                fine_data = model.prepare(fine_r, fine_density * args.theta_nodes)
                exchange["same_q_fine"] = base.small_report(model, q, amplitude, fine_data)
                probe_r = fine_r[(fine_r > model.minimum + 1e-5) & (fine_r < profile.R - 1e-6)]
                exchange["direct_reconstruction_step"] = base.actual_curvature_observation(
                    model, q, amplitude, probe_r, fine_density * args.theta_nodes)
                exchange["direct_reconstruction_half_step"] = base.actual_curvature_observation(
                    model, q, amplitude, probe_r, fine_density * args.theta_nodes, .5)
            except base.DomainError as error:
                exchange["fine_domain_failure"] = str(error)
            exchanges.append(exchange)
            emit("HEIGHT_FUNCTION_GRID_EXCHANGE", exchange)
            if (status in ("iteration_limit", "no_domain_preserving_function_step")
                    and not enriched and time.monotonic() - started < args.maximum_seconds - 60):
                old_residual = model.geometry(q, amplitude, data)
                old_nq = model.nq
                model, q = enrich_same_state(model, q)
                data = model.prepare(data["r"], data["theta"].size)
                new_residual = model.geometry(q, amplitude, data)
                difference = float(np.max(np.abs(new_residual - old_residual)))
                emit("HEIGHT_FUNCTION_LOCAL_ENRICHMENT", {
                    "amplitude": amplitude, "old_unknown_count": old_nq,
                    "new_unknown_count": model.nq, "support": [.53, .63],
                    "new_coefficients_all_zero_at_mapping": True,
                    "same_height_residual_difference_observation": difference})
                if difference > 1e-8:
                    raise ArithmeticError("zero-column embedding did not preserve the current height state")
                enriched = True
                continue
            fine_ok = (exchange["same_q_fine"] is not None
                       and exchange["same_q_fine"]["eta_max"] <= args.target_eta
                       and "direct_reconstruction_half_step" in exchange
                       and max(exchange["direct_reconstruction_step"]["direct_reconstructed_metric_eta"],
                               exchange["direct_reconstruction_half_step"]["direct_reconstructed_metric_eta"])
                           <= 8 * args.target_eta
                       and exchange["direct_reconstruction_step"]["direct_position_outward_ratio_min"] > 0
                       and exchange["direct_reconstruction_half_step"]["direct_position_outward_ratio_min"] > 0)
            if status != "sampled_metric_target" or fine_ok:
                break
            if active_density >= 2 or time.monotonic() - started > args.maximum_seconds:
                status = "fine_grid_target_unresolved"
                break
            active_density = fine_density
            data = fine_data
        record = {"amplitude": amplitude, "status": status, "actual_accepted_q": q.tolist(),
                  "grid_exchanges": exchanges}
        stages.append(record)
        emit("HEIGHT_FUNCTION_STAGE", record)
        if status != "sampled_metric_target" or time.monotonic() - started > args.maximum_seconds:
            break
    emit("HEIGHT_FUNCTION_FINAL", {
        "schema": SCHEMA, "elapsed_seconds": time.monotonic() - started,
        "counts": base.COUNTS, "additional_counts": EXTRA,
        "imported_gain_counters": base.gain.COUNTS, "stages": stages,
        "mode_height_scales": model.mode_height_scales.tolist(),
        "free_envelope_scale": model.envelope_scale, "local_enrichment_executed": enriched,
        "old_inner_Riccati_repeated": False, "old_gain_shooting_repeated": False,
        "uncomputed_inner_tail_not_certified": True, "same_metric_refinement": False,
        "continuous_reach_certificate": False, "complete_finite_family": False,
        "raw_arrays_tables_artifacts_releases_or_git_writes": False})

if __name__ == "__main__":
    main()
