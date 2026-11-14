#!/usr/bin/env python3
"""Actual moving-turn principal return and actual mean derivatives.

This is a floating diagnostic, NOT a PDE inverse or a turning/scattering
certificate. The turn graph is recomputed from the actual spline at every
ray angle. A periodic interpolant provides only a Newton initial guess.
All characteristic derivatives include moving endpoints.
"""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

import numpy as np
from scipy.integrate import solve_ivp
from scipy.interpolate import CubicSpline
from scipy.optimize import linprog

from fourfold_characteristic_diagnostic import load


def evaluate_pairs(candidate, x, theta):
    """The actual Fourier spline's Cartesian jets in its cylindrical basis.

    Unlike evaluate_candidate, x and theta are paired, not a tensor grid.
    Output order: F,Fx,Ft,Fxx,Fxt,Ftt,Fxxx,Fxxt,Fxtt,Fttt.
    """
    x, theta = np.broadcast_arrays(
        np.asarray(x, dtype=float), np.asarray(theta, dtype=float))
    shape = x.shape
    x, theta = x.ravel(), theta.ravel()
    out = [np.zeros((x.size, 3)) for _ in range(10)]
    base_cache = {}
    for frequency, spline in candidate["splines"].items():
        if hasattr(spline, "spline") and hasattr(spline, "solver"):
            key = id(spline.solver)
            if key not in base_cache:
                base_cache[key] = [
                    spline.solver.base_spline(x, nu=j)[:, 0, None]
                    for j in range(4)]
            a, ap, app, appp = base_cache[key]
            power = np.array([4, 4, 3])
            w0 = a**power
            w1 = power * a**(power-1) * ap
            w2 = (power*(power-1)*a**(power-2)*ap**2
                  + power*a**(power-1)*app)
            w3 = (power*(power-1)*(power-2)*a**(power-3)*ap**3
                  + 3*power*(power-1)*a**(power-2)*ap*app
                  + power*a**(power-1)*appp)
            c, c1, c2, c3 = [spline.spline(x, nu=j) for j in range(4)]
            fields = [w0*c, w0*c1+w1*c,
                      w0*c2+2*w1*c1+w2*c,
                      w0*c3+3*w1*c2+3*w2*c1+w3*c]
        else:
            fields = [spline(x, nu=j) for j in range(4)]
        m = frequency
        co, si = np.cos(m*theta), np.sin(m*theta)
        (u, v, w), (ux, vx, wx), (uxx, vxx, wxx), (
            uxxx, vxxx, wxxx) = [field.T for field in fields]
        out[0] += np.stack((u*co, v*si, w*co), axis=-1)
        out[1] += np.stack((ux*co, vx*si, wx*co), axis=-1)
        out[2] += np.stack((-(m*u+v)*si, (u+m*v)*co, -m*w*si), axis=-1)
        out[3] += np.stack((uxx*co, vxx*si, wxx*co), axis=-1)
        out[4] += np.stack((-(m*ux+vx)*si, (ux+m*vx)*co, -m*wx*si), axis=-1)
        out[5] += np.stack((-((m*m+1)*u+2*m*v)*co,
                           -(2*m*u+(m*m+1)*v)*si, -m*m*w*co), axis=-1)
        out[6] += np.stack((uxxx*co, vxxx*si, wxxx*co), axis=-1)
        out[7] += np.stack((-(m*uxx+vxx)*si, (uxx+m*vxx)*co,
                           -m*wxx*si), axis=-1)
        out[8] += np.stack((-((m*m+1)*ux+2*m*vx)*co,
                           -(2*m*ux+(m*m+1)*vx)*si, -m*m*wx*co), axis=-1)
        out[9] += np.stack(((m*(m*m+3)*u+(3*m*m+1)*v)*si,
                           -((3*m*m+1)*u+m*(m*m+3)*v)*co,
                           m**3*w*si), axis=-1)
    return tuple(field.reshape(shape+(3,)) for field in out)


def raw_data(candidate, solver, x, theta, columns=False):
    x, theta = np.broadcast_arrays(
        np.asarray(x, dtype=float), np.asarray(theta, dtype=float))
    fields = evaluate_pairs(candidate, x, theta)
    _, fx, ft, fxx, fxt, ftt, fxxx, fxxt, fxtt, fttt = fields
    cross = np.cross(ft, fx)
    cross_x = np.cross(fxt, fx)+np.cross(ft, fxx)
    cross_t = np.cross(ftt, fx)+np.cross(ft, fxt)
    dot = lambda a, b: np.sum(a*b, axis=-1)
    l, m, n = [dot(cross, field) for field in (fxx, fxt, ftt)]
    lx, mx, nx = [dot(cross_x, a)+dot(cross, b)
                  for a, b in ((fxx, fxxx), (fxt, fxxt), (ftt, fxtt))]
    lt, mt, nt = [dot(cross_t, a)+dot(cross, b)
                  for a, b in ((fxx, fxxt), (fxt, fxtt), (ftt, fttt))]
    result = dict(l=l, m=m, n=n, delta=m*m-l*n,
                  delta_x=2*m*mx-lx*n-l*nx,
                  delta_theta=2*m*mt-lt*n-l*nt,
                  m_theta=mt, n_theta=nt)
    if columns:
        x = np.asarray(x, dtype=float)
        shape = x.shape
        delta_columns, m_columns, n_columns = [], [], []
        for mean in solver.mean_splines:
            v, vx, vxx = [mean(x.ravel(), nu=j).reshape(shape+(3,))
                           for j in range(3)]
            vt, vxt, vtt = [np.zeros_like(v) for _ in range(3)]
            vt[..., 1] = v[..., 0]
            vxt[..., 1] = vx[..., 0]
            vtt[..., 0] = -v[..., 0]
            dcross = np.cross(vt, fx)+np.cross(ft, vx)
            dl = dot(dcross, fxx)+dot(cross, vxx)
            dm = dot(dcross, fxt)+dot(cross, vxt)
            dn = dot(dcross, ftt)+dot(cross, vtt)
            delta_columns.append(2*m*dm-n*dl-l*dn)
            m_columns.append(dm)
            n_columns.append(dn)
        result.update(delta_columns=np.array(delta_columns),
                      m_columns=np.array(m_columns),
                      n_columns=np.array(n_columns))
    return result


class TurnGeometry:
    def __init__(self, candidate, solver, bracket=(.22, .25), guess_nodes=128,
                 with_variations=True, raw_evaluator=None):
        self.candidate, self.solver = candidate, solver
        self.with_variations = with_variations
        self.raw = raw_data if raw_evaluator is None else raw_evaluator
        self.bracket = bracket
        self.guess = None
        self.minimum_denominator = float("inf")
        self.minimum_qbar = float("inf")
        self.maximum_root_residual = 0.
        self.calls = 0
        angles = np.arange(guess_nodes)*(np.pi/2)/guess_nodes
        lo = self.raw(candidate, solver, np.full_like(angles, bracket[0]), angles)
        hi = self.raw(candidate, solver, np.full_like(angles, bracket[1]), angles)
        if np.min(lo["delta"]) <= 0 or np.max(hi["delta"]) >= 0:
            raise ValueError("initial angle sample does not bracket the desired actual turn")
        roots, _ = self.turn(angles)
        self.guess = CubicSpline(
            np.r_[angles, np.pi/2], np.r_[roots, roots[0]], bc_type="periodic")
        self.initial_turn_range = [float(roots.min()), float(roots.max())]

    def turn(self, theta):
        theta = np.asarray(theta, dtype=float)
        if self.guess is None:
            root = np.full_like(theta, sum(self.bracket)/2)
        else:
            root = self.guess(np.mod(theta, np.pi/2))
        lo = np.full_like(theta, self.bracket[0])
        hi = np.full_like(theta, self.bracket[1])
        for _ in range(50):
            data = self.raw(self.candidate, self.solver, root, theta)
            positive = data["delta"] > 0
            lo = np.where(positive, root, lo)
            hi = np.where(positive, hi, root)
            step = data["delta"]/data["delta_x"]
            proposed = root-step
            outside = (proposed <= lo) | (proposed >= hi)
            proposed = np.where(outside & (np.abs(step) > 2e-13),
                                (lo+hi)/2, proposed)
            move = proposed-root
            root = proposed
            if np.max(np.abs(move)) < 2e-13:
                break
        else:
            raise RuntimeError("actual turning root did not converge")
        data = self.raw(self.candidate, self.solver, root, theta,
                       columns=self.with_variations)
        residual = float(np.max(np.abs(data["delta"])))
        self.maximum_root_residual = max(self.maximum_root_residual, residual)
        data["t_theta"] = -data["delta_theta"]/data["delta_x"]
        if self.with_variations:
            data["t_columns"] = -data["delta_columns"]/data["delta_x"][None, :]
        return root, data

    def branch(self, theta, sign, start, finish, tolerance):
        count, means = len(theta), self.solver.mean_count
        rows = means+2 if self.with_variations else 1
        value = np.zeros((rows, count))
        value[0] = theta
        if self.with_variations:
            value[1] = 1.
        start_side = -1 if start < 0 else 1
        finish_side = -1 if finish < 0 else 1
        if self.with_variations:
            _, start_data = self.turn(theta)

        def fun(tau, flat):
            self.calls += 1
            val = flat.reshape(rows, count)
            angle = val[0]
            root, turn = self.turn(angle)
            s = np.sin(tau)
            cosine = max(0., float(np.cos(tau)))
            if abs(abs(tau)-np.pi/2) < 1e-13:
                s = 1. if tau > 0 else -1.
                cosine = 0.
            x = s*root
            data = self.raw(self.candidate, self.solver, x, angle,
                            columns=self.with_variations)
            if abs(s) < .999:
                qbar = data["delta"]/(1-s*s)
            else:
                # Stable divided difference using the exact identity
                # D(st)/(1-s²)=-t/(1+|s|) int_0^1 D_x(t-lambda*t*(1-|s|)) dlambda.
                # Three-point Gaussian integration is a floating diagnostic.
                nodes = (np.array([-np.sqrt(3/5), 0., np.sqrt(3/5)])+1)/2
                weights = np.array([5/18, 4/9, 5/18])
                derivative = np.zeros_like(root)
                for node, weight in zip(nodes, weights):
                    xx = root*(1-node*(1-abs(s)))
                    derivative += weight*self.raw(
                        self.candidate, self.solver, xx, angle)["delta_x"]
                qbar = -root*derivative/(1+abs(s))
            if np.min(qbar) <= 0 or np.max(data["n"]) >= 0:
                raise ValueError("actual principal flow left its hyperbolic N<0 chart")
            qroot = np.sqrt(qbar)
            q = cosine*qroot
            m, n = data["m"], data["n"]
            speed = (-m+sign*q)/n
            denominator = 1-s*turn["t_theta"]*speed
            self.minimum_denominator = min(self.minimum_denominator,
                                           float(denominator.min()))
            self.minimum_qbar = min(self.minimum_qbar, float(qbar.min()))
            if np.min(denominator) <= 0:
                raise ValueError("actual turning graph is not transverse in this chart")
            x_tau = root*cosine/denominator
            if not self.with_variations:
                return speed*x_tau
            scaled_theta = (
                x_tau*(-data["m_theta"]/n
                       +(m-sign*q)*data["n_theta"]/n**2)
                + sign*root*data["delta_theta"]
                /(2*n*denominator*qroot))
            scaled_columns = (
                x_tau[None, :]*(
                    -data["m_columns"]/n[None, :]
                    +(m-sign*q)[None, :]*data["n_columns"]/n[None, :]**2)
                + sign*root[None, :]*data["delta_columns"]
                /(2*n*denominator*qroot)[None, :])
            answer = np.empty_like(val)
            answer[0] = speed*x_tau
            answer[1] = scaled_theta*val[1]
            answer[2:] = scaled_theta[None, :]*val[2:]+scaled_columns
            return answer.ravel()

        solved = solve_ivp(fun, (start, finish), value.ravel(), method="DOP853",
                          rtol=tolerance, atol=tolerance/20,
                          max_step=abs(finish-start)/48)
        if not solved.success:
            raise RuntimeError(solved.message)
        result = solved.y[:, -1].reshape(rows, count)
        if not self.with_variations:
            return result[0], None, None
        _, end_data = self.turn(result[0])
        c_start = -start_side*start_data["m"]/start_data["n"]
        c_finish = -finish_side*end_data["m"]/end_data["n"]
        start_factor = 1-c_start*start_side*start_data["t_theta"]
        end_factor = 1-c_finish*finish_side*end_data["t_theta"]
        jacobian = result[1]*start_factor/end_factor
        columns = (
            -result[1][None, :]*c_start[None, :]*start_side*start_data["t_columns"]
            + result[2:]
            + c_finish[None, :]*finish_side*end_data["t_columns"]
        )/end_factor[None, :]
        return result[0], jacobian, columns

    def round_trip(self, theta, tolerance):
        middle, jac1, col1 = self.branch(
            theta, -1., -np.pi/2, np.pi/2, tolerance)
        print(json.dumps({"progress": "first actual moving-turn branch finished",
                          "rhs_calls": self.calls}), flush=True)
        final, jac2, col2 = self.branch(
            middle, 1., np.pi/2, -np.pi/2, tolerance)
        if not self.with_variations:
            return final, None, None
        return final, jac2*jac1, jac2[None, :]*col1+col2


def mean_directions(solver, columns):
    height = np.array([sp(np.array([solver.length]))[0, 2]
                       for sp in solver.mean_splines])
    waist = np.array([sp(np.array([0.]))[0, 0] for sp in solver.mean_splines])
    result = {"mean_height_column": height.tolist(),
              "mean_waist_radius_column": waist.tolist()}
    for label, rows in (("unconstrained", []), ("fixed_mean_height", [height]),
                        ("fixed_height_and_radius", [height, waist])):
        constraints = None if not rows else np.column_stack(
            [np.array(rows), np.zeros(len(rows))])
        solved = linprog(
            np.r_[np.zeros(solver.mean_count), -1.],
            A_ub=np.column_stack([-columns, np.ones(len(columns))]),
            b_ub=np.zeros(len(columns)), A_eq=constraints,
            b_eq=None if constraints is None else np.zeros(len(rows)),
            bounds=[(-1., 1.)]*solver.mean_count+[(None, None)], method="highs")
        if solved.success:
            direction = solved.x[:-1]
            result[label] = dict(
                direction=direction.tolist(),
                sampled_pointwise_min=float((columns@direction).min()),
                sampled_pointwise_max=float((columns@direction).max()),
                constraint_residual=[] if not rows else
                (np.array(rows)@direction).tolist())
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--candidate", type=Path, required=True)
    parser.add_argument("--out", type=Path, required=True)
    parser.add_argument("--rays", type=int, default=16)
    parser.add_argument("--tolerance", type=float, default=2e-7)
    parser.add_argument("--turn-bracket", type=float, nargs=2, default=[.22, .25])
    parser.add_argument("--guess-nodes", type=int, default=128)
    args = parser.parse_args()
    candidate, solver, _ = load(args.candidate)
    if solver is None:
        raise ValueError("this diagnostic needs an actual SplineNewton checkpoint")
    print(json.dumps({"progress": "actual spline loaded"}), flush=True)
    geometry = TurnGeometry(candidate, solver, args.turn_bracket, args.guess_nodes)
    print(json.dumps({"progress": "turn graph initialized",
                      "turn_range": geometry.initial_turn_range}), flush=True)
    theta = np.arange(args.rays)*(np.pi/2)/args.rays
    returned, jacobian, columns = geometry.round_trip(theta, args.tolerance)
    columns = columns.T
    displacement = returned-theta
    report = dict(
        kind="floating_actual_moving_turn_principal_return_not_pde_certificate",
        candidate=args.candidate.name,
        sha256=hashlib.sha256(args.candidate.read_bytes()).hexdigest(),
        angular_period=float(np.pi/2),
        actual_initial_turn_range=geometry.initial_turn_range,
        initial_angles=theta.tolist(), returned_angles=returned.tolist(),
        displacement_min=float(displacement.min()),
        displacement_max=float(displacement.max()),
        jacobian_min=float(jacobian.min()), jacobian_max=float(jacobian.max()),
        jacobian=jacobian.tolist(), mean_columns=columns.tolist(),
        mean_column_min=columns.min(axis=0).tolist(),
        mean_column_max=columns.max(axis=0).tolist(),
        minimum_sampled_transversality=geometry.minimum_denominator,
        minimum_sampled_qbar=geometry.minimum_qbar,
        maximum_float_turn_residual=geometry.maximum_root_residual,
        ode_rtol=args.tolerance, rhs_calls=geometry.calls,
        limitations=[
            "ordinary floating arithmetic and finite ray samples",
            "actual turn roots recomputed, but uniqueness is not certified",
            "endpoint divided differences use three-point Gaussian quadrature",
            "principal geometric return excludes amplitudes and elliptic DtN",
            "mean columns do not preserve nonlinear PDE or n4 compatibility",
            "no rotation number derivative, inverse, closed surface, or reach proof"],
    )
    report.update(mean_directions(solver, columns))
    args.out.write_text(json.dumps(report, indent=2)+"\n")
    print(json.dumps({k: v for k, v in report.items()
                      if k not in ("initial_angles", "returned_angles", "jacobian",
                                   "mean_columns")}), flush=True)


if __name__ == "__main__":
    main()
