#!/usr/bin/env python3
"""R609: actual h/k curves with all fifteen histories integrated, not fitted.

The only scientific executor is this repository's public GitHub Actions.
The R598 mother, both R590 ruling equations and the entire positive potential
are unchanged. Four odd center moments and zeta0 are dependent functions of
the actual curve. No independent state can absorb a history equation defect.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
import time

import numpy as np
from scipy.optimize import least_squares

import r598_wide_mother_prepared_mass_bvp_agent as base

previous, paid = base.previous, base.paid
LD, Jet, constant, emit = base.LD, base.Jet, base.constant, base.emit
ODD, EVEN, JPAR = base.ODD, base.EVEN, base.JPAR


def jtanh(jet):
    value = np.tanh(jet.value)
    return Jet(value, (1-value*value)*jet.derivative)


def jets_values(jets):
    return np.asarray([v.value for v in jets], dtype=LD)


class IntegralGrid:
    """Composite Gauss collocation, with the exact polynomial prefix map.

    The finite rule approximates the continuous integrals in R609. Integrals
    of the within-panel interpolation polynomial are evaluated in Legendre
    coordinates. No triangular trapezoid/sampled-prefix surrogate is used.
    Both endpoints are included as observations but have zero Gauss weight.
    """
    def __init__(self, panels, order):
        self.panels, self.order = panels, order
        nodes, weights = np.polynomial.legendre.leggauss(order)
        leg = np.polynomial.legendre.legvander(nodes, order)
        integrated = np.zeros((order, order))
        integrated[:, 0] = nodes+1
        for degree in range(1, order):
            integrated[:, degree] = (leg[:, degree+1]-leg[:, degree-1])/(2*degree+1)
        coefficients = ((2*np.arange(order)+1)[:, None]/2
                        *leg[:, :order].T*weights[None, :])
        local_prefix = integrated@coefficients/(2*panels)
        self.x = np.r_[0., np.concatenate([(i+(nodes+1)/2)/panels
                                          for i in range(panels)]), 1.]
        self.weights = np.r_[0., np.tile(weights/(2*panels), panels), 0.]
        self.prefix = np.zeros((len(self.x), len(self.x)), dtype=LD)
        for panel in range(panels):
            current = slice(1+panel*order, 1+(panel+1)*order)
            self.prefix[current, :1+panel*order] = self.weights[:1+panel*order]
            self.prefix[current, current] = local_prefix
        self.prefix[-1] = self.weights

    def integrate(self, rows):
        """All derivatives pass through the same linear quadrature map."""
        count, width, dimension = len(rows), len(rows[0]), len(rows[0][0].derivative)
        values = np.asarray([[v.value for v in row] for row in rows], dtype=LD)
        derivatives = np.asarray([[v.derivative for v in row] for row in rows], dtype=LD)
        integrated = self.prefix@values
        chain = (self.prefix@derivatives.reshape(count, width*dimension)
                 ).reshape(count, width, dimension)
        return [[Jet(integrated[i, j], chain[i, j]) for j in range(width)]
                for i in range(count)]


class Curves:
    def __init__(self, modes, grid):
        self.modes, self.grid = modes, grid
        self.dimension = 2*modes+3
        self.evaluations = self.jet_evaluations = self.shape_points = 0

    def shape(self, parameters, x, derivatives=False):
        x = np.asarray(x, dtype=float).reshape(-1)
        self.shape_points += len(x)
        m, dimension = self.modes, self.dimension if derivatives else 0
        identity = np.eye(self.dimension, dtype=LD) if derivatives else None
        length = Jet(parameters[2*m], identity[2*m] if derivatives else np.zeros(0))
        hf = np.pi*np.arange(m)
        kf = np.pi*(2*np.arange(m)+1)/2
        hc, hs = np.cos(x[:, None]*hf), np.sin(x[:, None]*hf)
        ks, kc = np.sin(x[:, None]*kf), np.cos(x[:, None]*kf)
        # These are exact analytic endpoint identities of the declared basis.
        hs[(x == 0.) | (x == 1.)] = 0.
        ks[x == 0.] = 0.
        kc[x == 1.] = 0.
        result = []
        for i in range(len(x)):
            rows = [hc[i], -hf*hs[i], -hf*hf*hc[i],
                    ks[i], kf*kc[i], -kf*kf*ks[i]]
            latent = []
            for j, row in enumerate(rows):
                offset = 0 if j < 3 else m
                derivative = np.zeros(dimension, dtype=LD)
                if derivatives:
                    derivative[offset:offset+m] = row
                latent.append(Jet(row@parameters[offset:offset+m], derivative))
            hv, hxv, hxxv, kv, kxv, kxxv = latent
            ht, kt = jtanh(hv), jtanh(kv)
            h, k = LD('1.9')+ht, LD('1.95')*kt
            hx, kx = (1-ht*ht)*hxv, LD('1.95')*(1-kt*kt)*kxv
            hxx = (1-ht*ht)*(hxxv-2*ht*hxv*hxv)
            kxx = LD('1.95')*(1-kt*kt)*(kxxv-2*kt*kxv*kxv)
            result.append([h, k, hx, kx, hxx, kxx])
        return result, length

    def evaluate(self, parameters, derivatives=False):
        self.evaluations += 1
        self.jet_evaluations += int(derivatives)
        shape, length = self.shape(parameters, self.grid.x, derivatives)
        eta = self.grid.integrate([[row[3]/(2*row[0])] for row in shape])
        geometry, acceleration = [], []
        for i, (h, k, hx, kx, hxx, kxx) in enumerate(shape):
            geometry.append([h, k, eta[i][0], hx/length, kx/length])
            acceleration.append([hxx/length**2, kxx/length**2])
        density = [[length*v for v in paid.density(row)] for row in geometry]
        primitive = self.grid.integrate(density)
        total = primitive[-1]
        history = [[row[j]-total[j] if j in ODD else row[j] for j in range(8)]
                   for row in primitive]
        height = geometry[0][0]
        end = [total[1]/length, (8*total[3]+2*total[1])/length,
               8*height**2*total[4]/length, 4*height**2*total[6]/length]
        return {"parameters":np.asarray(parameters, dtype=float).copy(),
                "geometry":geometry, "acceleration":acceleration,
                "history":history, "total_integral":total, "end":end,
                "length":length, "grid":self.grid}

    @staticmethod
    def box(curve, margin=False):
        geometry = np.asarray([[v.value for v in row] for row in curve["geometry"]], dtype=LD)
        eta, speed = (.98, 5.8) if margin else (.999, 5.99)
        violations = [np.max(np.abs(geometry[:, 2]))/eta-1,
                      np.max(np.abs(geometry[:, 3:5]))/speed-1]
        return float(max(0., *violations))

    def fit_rows(self, parameters):
        curve = self.evaluate(parameters, True)
        rows = list(curve["end"])
        for row in curve["geometry"]:
            for value, bound in ((row[2], .98), (row[3], 5.8), (row[4], 5.8)):
                # A fixed-size soft guard is used only to find a legal seed.
                if value.value > bound:
                    rows.append((value-bound)/bound)
                elif value.value < -bound:
                    rows.append((-value-bound)/bound)
                else:
                    rows.append(value*0)
        values, jac = paid.values_and_jacobian(rows)
        return curve, np.asarray(values, dtype=float), np.asarray(jac, dtype=float)


def valid_parameters(parameters, modes):
    return bool(np.all(np.isfinite(parameters))
                and np.max(np.abs(parameters[:2*modes])) <= 6.
                and 2.1 <= parameters[2*modes] <= 7.9
                and np.max(np.abs(parameters[-2:])) <= 1.e6)


def embed(parameters, old_modes, modes):
    out = np.zeros(2*modes+3)
    out[:old_modes] = parameters[:old_modes]
    out[modes:modes+old_modes] = parameters[old_modes:2*old_modes]
    out[2*modes:] = parameters[2*old_modes:]
    return out


def moment_fit(model, parameters, max_nfev):
    started = time.monotonic()
    n = 2*model.modes+1
    cached = {"x":None}
    def evaluate(x):
        if cached["x"] is None or not np.array_equal(x, cached["x"]):
            p = np.r_[x, parameters[-2:]]
            curve, residual, jac = model.fit_rows(p)
            cached.update(x=x.copy(), curve=curve, residual=residual, jac=jac[:, :n])
        return cached
    lower, upper = np.r_[np.full(n-1, -6.), 2.1], np.r_[np.full(n-1, 6.), 7.9]
    result = least_squares(lambda x:evaluate(x)["residual"], parameters[:n],
                           jac=lambda x:evaluate(x)["jac"], bounds=(lower, upper),
                           max_nfev=max_nfev, xtol=1.e-12, ftol=1.e-12,
                           gtol=1.e-12, x_scale="jac", verbose=0)
    final = np.r_[result.x, parameters[-2:]]
    data = evaluate(result.x)
    emit("R609_TRUE_MOMENT_SEED", {"modes":model.modes,
         "parameters":final.tolist(), "nfev":int(result.nfev),
         "njev":int(result.njev or 0), "optimizer_status":int(result.status),
         "optimizer_message":str(result.message), "seconds":time.monotonic()-started,
         "four_actual_transformed_end_integrals":data["residual"][:4].tolist(),
         "sampled_box_violation":model.box(data["curve"]),
         "continuous_moment_or_ruling_root_claim":False})
    return final


def restore_moments(model, parameters, tolerance, maximum=12):
    """Only the actual shape changes; no A or rho field is adjusted."""
    p = parameters.copy()
    count = 0
    for iteration in range(maximum+1):
        curve = model.evaluate(p, True)
        count += 1
        ev, ej = paid.values_and_jacobian(curve["end"])
        ev, ej = np.asarray(ev, float), np.asarray(ej, float)
        if np.max(np.abs(ev)) <= tolerance and model.box(curve) == 0:
            return p, curve, {"success":True, "evaluations":count, "iterations":iteration}
        if iteration == maximum:
            break
        direction, _, rank, _ = np.linalg.lstsq(ej[:, :-2], -ev, rcond=1.e-11)
        if rank < 4 or not np.all(np.isfinite(direction)):
            break
        direction *= min(1., .5/max(1.e-30, np.linalg.norm(direction)))
        accepted = False
        for level in range(10):
            trial = p.copy()
            trial[:-2] += (2.**-level)*direction
            if not valid_parameters(trial, model.modes):
                continue
            candidate = model.evaluate(trial, False)
            count += 1
            ce = np.asarray(jets_values(candidate["end"]), float)
            if model.box(candidate) == 0 and np.linalg.norm(ce) < np.linalg.norm(ev):
                p, accepted = trial, True
                break
        if not accepted:
            break
    return p, curve, {"success":False, "evaluations":count, "iterations":iteration,
                      "end_max":float(np.max(np.abs(ev))), "sampled_box_violation":model.box(curve)}


class FullHistory:
    def __init__(self, coefficients, potential):
        self.coefficients, self.potential = coefficients, potential
        self.evaluations = self.jet_evaluations = 0
        self.seconds = 0.

    def evaluate(self, curve):
        started = time.monotonic()
        self.evaluations += 1
        self.jet_evaluations += int(len(curve["geometry"][0][0].derivative)>0)
        geometry, history, accel = curve["geometry"], curve["history"], curve["acceleration"]
        center, ca = geometry[0], history[0]
        sides, outputs, rates = [], [], []
        for geo, aa, (acc, bcc) in zip(geometry, history, accel):
            neg = [geo[0], -geo[1], -geo[2], -geo[3], geo[4]]
            aneg = [sign*v for sign, v in zip(JPAR, aa)]
            op = self.coefficients.evaluate_jets(geo, aa)
            om = self.coefficients.evaluate_jets(neg, aneg)
            if not (op[1].value<0 and om[1].value<0 and op[2].value>0 and om[2].value>0):
                raise FloatingPointError("actual_R598_Ch_Ck_domain")
            qg = 1+(geo[0]*geo[2]-geo[1])**2
            plus = [(op[3+3*j]+acc*op[4+3*j]+bcc*op[5+3*j])/qg**2 for j in range(3)]
            minus = [-(om[3+3*j]+acc*om[4+3*j]-bcc*om[5+3*j])/qg**2 for j in range(3)]
            rates.append([curve["length"]*v for v in plus+minus])
            sides.append(((geo, aa), (neg, aneg)))
            outputs.append((op, om))
        rho = curve["grid"].integrate(rates)
        zeta0 = (outputs[0][0][0]+outputs[0][0][1]*accel[0][0])/(2*paid.weights(center)[0])
        zero = zeta0*0
        ruling, designs = [], []
        for i, ((acc, bcc), pair, pair_outputs) in enumerate(zip(accel, sides, outputs)):
            for side, ((geo, aa), op) in enumerate(zip(pair, pair_outputs)):
                sign = 1 if side == 0 else -1
                rr = rho[i][3*side:3*side+3]
                wp = paid.weights(geo)
                difference = self.potential.center_difference(geo, aa, center, ca)
                residual = (op[0]+op[1]*acc+sign*op[2]*bcc
                            -4*paid.dot(wp, rr)-4*difference
                            -2*previous.center_pairing(geo, center, [zeta0, zero, zero]))
                h, k, eta, _, _ = geo
                height, d = center[0], h*eta-k
                ruling.append(residual)
                designs.append([d, ((h-height)*(h+height)-height*height*d*d)/(2*h)])
        self.seconds += time.monotonic()-started
        return {"curve":curve, "base_ruling":ruling, "design":designs,
                "rho":rho, "outputs":outputs, "zeta0":zeta0}


def assemble(data, parameters, unit, optimize_gauge=True):
    """Two constants are solved globally; their shape derivatives stay live."""
    p = parameters.copy()
    rhs = np.asarray(jets_values(data["base_ruling"]), float)
    design = np.asarray([[v.value for v in row] for row in data["design"]], float)
    gauge_rank = None
    if optimize_gauge:
        gauge, _, gauge_rank, _ = np.linalg.lstsq(design, rhs/unit, rcond=1.e-12)
        if np.all(np.isfinite(gauge)) and np.max(np.abs(gauge)) <= 1.e6:
            p[-2:] = gauge
    dimension = len(data["base_ruling"][0].derivative)
    free = []
    for index in (-2, -1):
        derivative = np.zeros(dimension)
        if dimension:
            derivative[index] = unit
        free.append(Jet(unit*p[index], derivative))
    rows = [value-paid.dot(row, free) for value, row in zip(data["base_ruling"], data["design"])]
    original, jacobian = paid.values_and_jacobian(rows)
    original, jacobian = np.asarray(original, float), np.asarray(jacobian, float)
    normalization = unit*np.sqrt(len(rows))
    end, end_jac = paid.values_and_jacobian(data["curve"]["end"])
    return {"parameters":p, "original":original,
            "residual":original/normalization, "jacobian":jacobian/normalization,
            "end":np.asarray(end, float), "end_jacobian":np.asarray(end_jac, float),
            "gauge_rank":None if gauge_rank is None else int(gauge_rank),
            "data":data, "unit":float(unit)}


def checkpoint(evaluation, level, iteration, reason, trust, damping):
    data, p = evaluation["data"], evaluation["parameters"]
    curve = data["curve"]
    geometry = np.asarray([[v.value for v in row] for row in curve["geometry"]], float)
    history = np.asarray([[v.value for v in row] for row in curve["history"]], float)
    rho = np.asarray([[v.value for v in row] for row in data["rho"]], float)
    canonical = json.dumps(p.tolist(), separators=(",", ":"), allow_nan=False).encode()
    emit("R609_ACTUAL_FUNCTION_STATE", {
        "level":level, "iteration":iteration, "reason":reason,
        "modes":(len(p)-3)//2, "panels":curve["grid"].panels,
        "gauss_order":curve["grid"].order, "ruling_observation_points":len(geometry),
        "parameters":p.tolist(), "parameter_json_sha256":hashlib.sha256(canonical).hexdigest(),
        "fixed_ruling_and_free_gauge_unit":evaluation["unit"],
        "actual_zeta":[float(data["zeta0"].value), *(evaluation["unit"]*p[-2:]).tolist()],
        "true_discrete_odd_center":history[0, ODD].tolist(),
        "all_eight_discrete_end_integrals":np.asarray(jets_values(curve["total_integral"]), float).tolist(),
        "actual_eight_terminal_A":history[-1].tolist(),
        "actual_six_terminal_rho":rho[-1].tolist(),
        "four_transformed_end_rows":evaluation["end"].tolist(),
        "actual_original_ruling_max":float(np.max(np.abs(evaluation["original"]))),
        "normalized_ruling_rms":float(np.linalg.norm(evaluation["residual"])),
        "geometry_ranges":[[float(v.min()), float(v.max())] for v in geometry.T],
        "sampled_original_box_violation":Curves.box(curve),
        "global_two_constant_gauge_rank":evaluation["gauge_rank"],
        "trust":float(trust), "damping":float(damping),
        "independent_history_parameters":0, "full_positive_potential_coefficient":1,
        "continuous_integral_root_pose_reach_or_README_completion_claim":False})


def solve_level(model, full, parameters, unit, args, level):
    started = time.monotonic()
    p, curve, restoration = restore_moments(model, parameters, args.end_tol)
    if not restoration["success"]:
        emit("R609_MOMENT_RESTORATION_FAILED", {"level":level, "modes":model.modes,
             "parameters":p.tolist(), "report":restoration})
        return p, unit, None, "four_even_integrals_not_restored"
    data = full.evaluate(curve)
    if unit is None:
        unit = max(1., float(np.max(np.abs(jets_values(data["base_ruling"])))))
    current = assemble(data, p, unit)
    trust, damping, accepted, rejected = args.trust, args.damping, 0, 0
    checkpoint(current, level, 0, "initial_true_integrals_and_global_gauge", trust, damping)
    status = "iteration_limit_with_finite_actual_curve"
    for iteration in range(1, args.iterations+1):
        if (np.max(np.abs(current["original"])) <= args.ruling_tol
                and np.max(np.abs(current["end"])) <= args.end_tol):
            status = "actual_discrete_original_equations_converged"
            break
        p = current["parameters"]
        _, singular, vh = np.linalg.svd(current["end_jacobian"], full_matrices=True)
        rank = int(np.sum(singular > max(1.e-13, singular[0]*1.e-11)))
        if rank < 4:
            status = "actual_four_end_map_rank_loss"
            break
        tangent = vh[rank:].T
        jtan = current["jacobian"]@tangent
        augmented = np.vstack((jtan, np.sqrt(damping)*np.eye(tangent.shape[1])))
        target = np.r_[-current["residual"], np.zeros(tangent.shape[1])]
        restricted, _, _, _ = np.linalg.lstsq(augmented, target, rcond=1.e-12)
        direction = tangent@restricted
        direction *= min(1., trust/max(np.linalg.norm(direction), 1.e-30))
        found = False
        for backtrack in range(args.trials):
            trial_parameters = p+(2.**-backtrack)*direction
            if not valid_parameters(trial_parameters, model.modes):
                rejected += 1
                continue
            trial_parameters, trial_curve, report = restore_moments(
                model, trial_parameters, args.end_tol)
            if not report["success"]:
                rejected += 1
                continue
            try:
                trial_data = full.evaluate(trial_curve)
                trial = assemble(trial_data, trial_parameters, unit)
            except (FloatingPointError, OverflowError, ValueError) as error:
                rejected += 1
                emit("R609_FUNCTION_TRIAL", {"level":level, "iteration":iteration,
                     "backtrack":backtrack, "accepted":False,
                     "actual_error":type(error).__name__+":"+str(error)})
                continue
            old_cost = float(current["residual"]@current["residual"])/2
            new_cost = float(trial["residual"]@trial["residual"])/2
            delta = trial["parameters"]-p
            predicted = old_cost-float(np.linalg.norm(current["residual"]+current["jacobian"]@delta)**2)/2
            gain = old_cost-new_cost
            ratio = gain/max(abs(predicted), 1.e-30)
            chosen = bool(np.isfinite(new_cost) and gain>max(1.e-24, 1.e-12*old_cost)
                          and np.max(np.abs(trial["end"])) <= args.end_tol)
            emit("R609_FUNCTION_TRIAL", {"level":level, "iteration":iteration,
                 "backtrack":backtrack, "accepted":chosen, "cost":new_cost,
                 "actual_gain":gain, "model_ratio":ratio, "moment_restoration":report,
                 "original_ruling_max":float(np.max(np.abs(trial["original"]))),
                 "true_end_max":float(np.max(np.abs(trial["end"]))),
                 "end_map_singular_values":singular.tolist()})
            if chosen:
                current, found = trial, True
                accepted += 1
                if ratio>.5 and backtrack==0:
                    trust, damping = min(args.maximum_trust, 1.5*trust), max(1.e-14, damping/3)
                else:
                    damping = max(1.e-14, damping/1.2)
                checkpoint(current, level, iteration, "accepted_actual_curve", trust, damping)
                break
            rejected += 1
        if not found:
            trust, damping = trust/2, min(1.e12, 10*damping)
            if trust < 1.e-7:
                status = "current_finite_function_space_stalled"
                break
    checkpoint(current, level, iteration, status, trust, damping)
    emit("R609_FUNCTION_LEVEL_FINAL", {"level":level, "status":status,
         "modes":model.modes, "accepted":accepted, "rejected":rejected,
         "seconds":time.monotonic()-started,
         "curve_evaluations":model.evaluations,
         "curve_jet_evaluations":model.jet_evaluations,
         "shape_points":model.shape_points,
         "full_history_evaluations_cumulative":full.evaluations,
         "full_history_seconds_cumulative":full.seconds})
    return current["parameters"], unit, current, status


class PhysicalCurve:
    """The same analytic h/k and a point-independent quadrature for eta."""
    def __init__(self, modes, quadrature_order=128):
        self.modes = modes
        nodes, weights = np.polynomial.legendre.leggauss(quadrature_order)
        self.qx, self.qw = (nodes+1)/2, weights/2
        self.geometry_calls = self.shape_points = 0

    def fields(self, parameters, x, unused=None):
        x = np.asarray(x, float).reshape(-1)
        self.shape_points += len(x)
        m = self.modes
        hf, kf = np.pi*np.arange(m), np.pi*(2*np.arange(m)+1)/2
        hc, hs = np.cos(hf[:, None]*x), np.sin(hf[:, None]*x)
        ks, kc = np.sin(kf[:, None]*x), np.cos(kf[:, None]*x)
        hs[:, (x == 0.) | (x == 1.)] = 0.
        ks[:, x == 0.] = 0.
        kc[:, x == 1.] = 0.
        aa, bb = parameters[:m], parameters[m:2*m]
        hv, hxv, hxxv = aa@hc, (-hf*aa)@hs, (-hf*hf*aa)@hc
        kv, kxv, kxxv = bb@ks, (kf*bb)@kc, (-kf*kf*bb)@ks
        ht, kt = np.tanh(hv), np.tanh(kv)
        return (1.9+ht, 1.95*kt, (1-ht*ht)*hxv, 1.95*(1-kt*kt)*kxv,
                (1-ht*ht)*(hxxv-2*ht*hxv*hxv),
                1.95*(1-kt*kt)*(kxxv-2*kt*kxv*kxv), parameters[2*m])

    def geometry(self, parameters, x, unused=None):
        self.geometry_calls += 1
        x = np.asarray(x, float).reshape(-1)
        h, k, hx, kx, hxx, kxx, length = self.fields(parameters, x)
        integration = self.qx[:, None]*x[None, :]
        qh, _, _, qkx, _, _, _ = self.fields(parameters, integration.ravel())
        eta = x*np.sum(self.qw[:, None]*(qkx/(2*qh)).reshape(integration.shape), axis=0)
        return np.array([h, k, eta, hx/length, kx/length]), hxx/length**2, kxx/length**2, None


def physical_readout(parameters, unit, data, grid):
    started = time.monotonic()
    curve, modes = data["curve"], (len(parameters)-3)//2
    center = tuple(v.value for v in curve["geometry"][0])
    ca = np.asarray(jets_values(curve["history"][0]), dtype=LD)
    center_outputs = np.asarray(jets_values(data["outputs"][0][0]), dtype=LD)
    center_e = center_outputs[16:19]
    # The cached coefficient outputs give the original shift without a second
    # coefficient evaluation: r=op[12:15]/4, r0-=op[15]/(4*w0).
    rc = center_outputs[12:15].copy()/4
    rc[0] -= center_outputs[15]*center[0]
    actual_zeta = np.r_[float(data["zeta0"].value), unit*parameters[-2:]]
    nubar = actual_zeta.copy()
    nubar[0] -= center[0]**2*nubar[2]
    ending, end_shifts = [], []
    for side in range(2):
        op = np.asarray(jets_values(data["outputs"][-1][side]), dtype=LD)
        geo = curve["geometry"][-1]
        qg = 1+(geo[0].value*geo[2].value-geo[1].value)**2
        rho = np.asarray(jets_values(data["rho"][-1][3*side:3*side+3]), dtype=LD)
        ending.append(np.asarray(rho+op[16:19]/qg-center_e, float))
        shift = op[12:15].copy()/4
        shift[0] -= op[15]*geo[0].value/qg
        end_shifts.append(np.asarray(shift, float))
    physical = PhysicalCurve(modes)
    # The legacy geometry helper takes physical L in its last coordinate.
    geometry_parameters = np.r_[parameters[:2*modes], parameters[2*modes]]
    report = base.guide_geometry_budget(physical, geometry_parameters, None, grid)
    emit("R609_ACTUAL_CURVE_PHYSICAL_READOUT", {
         "parameters":parameters.tolist(), "fixed_free_gauge_unit":float(unit),
         "actual_nubar":nubar.tolist(), "actual_center_E":np.asarray(center_e, float).tolist(),
         "actual_center_r":np.asarray(rc, float).tolist(),
         "actual_original_nu":np.asarray(nubar-2*rc, float).tolist(),
         "actual_nuhat":np.asarray(nubar-2*center_e, float).tolist(),
         "actual_terminal_sigma_plus_minus":[v.tolist() for v in ending],
         "actual_terminal_original_shift_plus_minus":[v.tolist() for v in end_shifts],
         "actual_terminal_Tproj":(ending[0]-ending[1]-end_shifts[0]+end_shifts[1]).tolist(),
         "actual_reanchored_gauge":(nubar+2*ending[1]-2*end_shifts[1]).tolist(),
         "base_geometry":report, "physical_geometry_calls":physical.geometry_calls,
         "physical_shape_points":physical.shape_points,
         "seconds":time.monotonic()-started,
         "full_closed_pose_or_finite_flex_claim":False})


def main():
    if (os.environ.get("GITHUB_ACTIONS") != "true"
            or os.environ.get("GITHUB_REPOSITORY") != "Rogerhu12/math-research-public"):
        raise SystemExit("Science is authorized only in this public repository's Actions.")
    parser = argparse.ArgumentParser()
    parser.add_argument("--modes", default="9,13,17")
    parser.add_argument("--panels", type=int, default=8)
    parser.add_argument("--quadrature-order", type=int, default=16)
    parser.add_argument("--mother-order", type=int, default=192)
    parser.add_argument("--gap-order", type=int, default=8)
    parser.add_argument("--seed-nfev", type=int, default=240)
    parser.add_argument("--iterations", type=int, default=35)
    parser.add_argument("--trials", type=int, default=8)
    parser.add_argument("--trust", type=float, default=.2)
    parser.add_argument("--maximum-trust", type=float, default=1.)
    parser.add_argument("--damping", type=float, default=1.e-4)
    parser.add_argument("--end-tol", type=float, default=1.e-9)
    parser.add_argument("--ruling-tol", type=float, default=1.e-7)
    args = parser.parse_args()
    modes = [int(v) for v in args.modes.split(",")]
    if modes != [9, 13, 17] or args.panels != 8 or args.quadrature_order != 16:
        raise ValueError("A changed physical function/grid scope needs an explicit new request.")
    started = time.monotonic()
    coefficients = full = grid = final = None
    parameters, old_modes, unit = np.r_[.4, -.6, -1.2, 0., 0., -2., 2., 0., 0., 0., 4.5, 0., 0.], 5, None
    status = "not_initialized"
    try:
        initial = Curves(5, IntegralGrid(args.panels, args.quadrature_order))
        parameters = moment_fit(initial, parameters, args.seed_nfev)
        labels, rows = previous.rebuild_known_rows()
        grid = base.WideReferenceGrid(args.mother_order, args.gap_order, 5.)
        coefficients = base.CountedCoefficients(labels, rows, grid)
        potential = previous.FactoredPotential(grid)
        full = FullHistory(coefficients, potential)
        emit("R609_FIXED_PHYSICAL_MOTHER", {
             "graph":grid.graph_info, "coefficients":coefficients.stats,
             "positive_Gram":potential.stats, "same_R598_mother":True,
             "full_positive_potential_coefficient":1,
             "necessary_rebuild_counted":True, "old_identity_or_derivative_gate_replayed":False})
        for level, count in enumerate(modes):
            parameters = embed(parameters, old_modes, count)
            old_modes = count
            model = Curves(count, IntegralGrid(args.panels, args.quadrature_order))
            parameters, _, report = restore_moments(model, parameters, args.end_tol)
            if not report["success"]:
                parameters = moment_fit(model, parameters, args.seed_nfev)
            parameters, unit, final, status = solve_level(model, full, parameters, unit, args, level)
            if final is not None and status == "actual_discrete_original_equations_converged":
                break
        if final is not None:
            # Same h/k coefficients, L and two constant gauges: no refit here.
            refined = Curves(old_modes, IntegralGrid(2*args.panels, args.quadrature_order))
            finer_curve = refined.evaluate(parameters, True)
            finer_data = full.evaluate(finer_curve)
            fine = assemble(finer_data, parameters, unit, optimize_gauge=False)
            checkpoint(fine, "fixed_curve_finer_integrals", 0,
                       "same_curve_and_two_free_gauges_no_refit", 0., 0.)
            emit("R609_FIXED_CURVE_REFINEMENT", {
                 "coarse_original_ruling_max":float(np.max(np.abs(final["original"]))),
                 "fine_original_ruling_max":float(np.max(np.abs(fine["original"]))),
                 "coarse_end":final["end"].tolist(), "fine_end":fine["end"].tolist(),
                 "same_parameters":True, "same_free_gauge_unit":True,
                 "dependent_center_and_zeta0_reintegrated":True,
                 "continuous_error_certificate":False})
            physical_readout(parameters, unit, finer_data, grid)
    except Exception as error:
        status = "exception_with_actual_scope_recorded"
        emit("R609_ACTUAL_EXCEPTION", {"type":type(error).__name__, "message":str(error)})
        raise
    finally:
        emit("R609_FUNCTION_FINAL", {"status":status, "seconds":time.monotonic()-started,
             "parameters":parameters.tolist(), "modes":old_modes, "fixed_unit":unit,
             "coefficient_value_calls":None if coefficients is None else coefficients.value_calls,
             "coefficient_jet_calls":None if coefficients is None else coefficients.jet_calls,
             "full_history_calls":None if full is None else full.evaluations,
             "full_history_jet_calls":None if full is None else full.jet_evaluations,
             "full_history_seconds":None if full is None else full.seconds,
             "root_or_README_completion_claim":False})


if __name__ == "__main__":
    main()
