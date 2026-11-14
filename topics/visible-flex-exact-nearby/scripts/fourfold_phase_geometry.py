#!/usr/bin/env python3
"""Consistent finite-primitive phase geometry through three physical jets.

The checkpoint defines the infinite R33 unit tangent. This evaluator keeps
the same Q-point quarter FFT primitive as PhaseNewton.geometry and
differentiates that ONE finite primitive consistently in x and theta.
Strip budgets compare it with the infinite definition; ordinary floating
rounding is not included. No PDE, cap, or reach certificate is asserted.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import math
from pathlib import Path

import numpy as np
from scipy.interpolate import BSpline

from fourfold_phase_newton import PhaseNewton
from fourfold_unit_tangent import primitive_error_bounds


def reflected_spline(solver, coefficients):
    full = np.concatenate((coefficients[:, :, ::-1], coefficients), axis=2)
    full = full.transpose(2, 0, 1).copy()
    full[:solver.points, :, 1] *= -1
    return BSpline(solver.knots, full, 5)


def phase_jets(solver, spline, x, order=3):
    """Actual weighted beta/gamma coefficients, including radial third jet."""
    x = np.atleast_1d(x)
    base = [solver.base_spline(x, nu=j)[:, 0, None, None]
            for j in range(order+1)]
    a = base[0]
    power = np.array([3, 2])[None, None, :]
    weights = [a**power]
    if order:
        ap = base[1]
        weights.append(power*a**(power-1)*ap)
    if order >= 2:
        app = base[2]
        weights.append(power*(power-1)*a**(power-2)*ap**2
                       +power*a**(power-1)*app)
    if order >= 3:
        appp = base[3]
        # The p(p-1)(p-2) term vanishes at p=2. No zero/negative-radius
        # extrapolation is used in the finite body under consideration.
        weights.append(
            power*(power-1)*(power-2)*a**(power-3)*ap**3
            +3*power*(power-1)*a**(power-2)*ap*app
            +power*a**(power-1)*appp)
    raw = [spline(x, nu=j) for j in range(order+1)]
    return np.stack([
        sum(math.comb(j, k)*weights[k]*raw[j-k] for k in range(j+1))
        for j in range(order+1)])


def tangent_radial_jets(phase, sine):
    """Analytic T,T_x,T_xx,T_xxx in the cylindrical basis."""
    fields = np.einsum("rxmc,mq->rxqc", phase, sine)
    b, p = fields[0, ..., 0], fields[0, ..., 1]
    sb, cb, sp, cp = np.sin(b), np.cos(b), np.sin(p), np.cos(p)
    z = np.zeros_like(b)
    t = np.stack((-cp*sb, cp*cb, sp), axis=-1)
    tb = np.stack((-cp*cb, -cp*sb, z), axis=-1)
    tp = np.stack((sp*sb, -sp*cb, cp), axis=-1)
    tbb = np.stack((cp*sb, -cp*cb, z), axis=-1)
    tbp = np.stack((sp*cb, sp*sb, z), axis=-1)
    tbbp = np.stack((-sp*sb, sp*cb, z), axis=-1)
    bx, px = fields[1, ..., 0], fields[1, ..., 1]
    bxx, pxx = fields[2, ..., 0], fields[2, ..., 1]
    tx = tb*bx[..., None]+tp*px[..., None]
    txx = (tb*bxx[..., None]+tp*pxx[..., None]+tbb*bx[..., None]**2
           +2*tbp*(bx*px)[..., None]-t*px[..., None]**2)
    result = [t, tx, txx]
    if len(phase) > 3:
        bxxx, pxxx = fields[3, ..., 0], fields[3, ..., 1]
        txxx = (
            tb*(bxxx-bx**3-3*bx*px**2)[..., None]
            +tp*(pxxx-px**3)[..., None]
            +3*tbb*(bx*bxx)[..., None]
            +3*tbp*(bxx*px+bx*pxx)[..., None]
            -3*t*(px*pxx)[..., None]
            +3*tbbp*(bx**2*px)[..., None])
        result.append(txxx)
    auxiliaries = dict(fields=fields, T=t, Tb=tb, Tp=tp,
                       Tbb=tbb, Tbp=tbp, Tbbp=tbbp)
    return np.stack(result), auxiliaries


def tangent_variation_jets(aux, variation, sine):
    """Exact differential of T,T_x,T_xx with respect to finite phase jets."""
    d = np.einsum("rxmc,mq->rxqc", variation, sine)
    field = aux["fields"]
    b1, p1 = field[1, ..., 0], field[1, ..., 1]
    b2, p2 = field[2, ..., 0], field[2, ..., 1]
    db, dp = d[0, ..., 0], d[0, ..., 1]
    db1, dp1 = d[1, ..., 0], d[1, ..., 1]
    db2, dp2 = d[2, ..., 0], d[2, ..., 1]
    t, tb, tp, tbb, tbp, tbbp = [
        aux[key] for key in ("T", "Tb", "Tp", "Tbb", "Tbp", "Tbbp")]
    dt = tb*db[..., None]+tp*dp[..., None]
    dtb = tbb*db[..., None]+tbp*dp[..., None]
    dtp = tbp*db[..., None]-t*dp[..., None]
    dtbb = -tb*db[..., None]+tbbp*dp[..., None]
    dtbp = tbbp*db[..., None]-tb*dp[..., None]
    dtx = (dtb*b1[..., None]+tb*db1[..., None]
           +dtp*p1[..., None]+tp*dp1[..., None])
    dtxx = (
        dtb*b2[..., None]+tb*db2[..., None]
        +dtp*p2[..., None]+tp*dp2[..., None]
        +dtbb*b1[..., None]**2+2*tbb*(b1*db1)[..., None]
        +2*dtbp*(b1*p1)[..., None]
        +2*tbp*(db1*p1+b1*dp1)[..., None]
        -dt*p1[..., None]**2-2*t*(p1*dp1)[..., None])
    return np.stack((dt, dtx, dtxx))


class PhaseGeometry:
    def __init__(self, solver, vector, quarter_nodes=256, directions=None):
        self.solver = solver
        self.vector = np.asarray(vector).copy()
        self.coefficients, self.alpha = solver.unpack(self.vector)
        self.spline = reflected_spline(solver, self.coefficients)
        self.nodes = int(quarter_nodes)
        if self.nodes % 4 or self.nodes < 4*solver.modes+8:
            raise ValueError("quarter nodes must be a multiple of 4 >= 4M+8")
        self.frequency = 4*np.fft.fftfreq(self.nodes, 1/self.nodes)
        angles = np.arange(self.nodes)*(np.pi/2)/self.nodes
        self.sine = np.sin(4*np.arange(1, solver.modes+1)[:, None]*angles)
        self._cache = {}
        self.directions = directions
        if directions is not None:
            self.direction_splines, self.direction_means = [], []
            for direction in directions:
                coeff, mean = solver.unpack(direction)
                self.direction_splines.append(reflected_spline(solver, coeff))
                self.direction_means.append(mean)
            if len(directions) != solver.mean_count:
                raise ValueError("return adapter expects one column per mean parameter")

    def primitive_coefficients(self, samples):
        coefficient = np.fft.fft(samples, axis=-2)/self.nodes
        n = self.frequency
        out = np.zeros_like(coefficient)
        out[..., 0] = (1j*n*coefficient[..., 0]+coefficient[..., 1])/(1-n*n)
        out[..., 1] = (-coefficient[..., 0]+1j*n*coefficient[..., 1])/(1-n*n)
        nonzero = n != 0
        out[..., nonzero, 2] = coefficient[..., nonzero, 2]/(1j*n[nonzero])
        out[..., self.nodes//2, :] = 0.
        # Odd cylindrical radial tangent and odd vertical tangent have
        # exact zero means in this symmetry class.
        out[..., 0, 1] = 0.
        return out

    def angular(self, coefficients, order=1):
        result = coefficients
        n = self.frequency[..., None]
        for _ in range(order):
            changed = 1j*n*result
            changed[..., 0] -= result[..., 1]
            changed[..., 1] += result[..., 0]
            result = changed
        return result

    def radial_coefficients(self, x):
        x = np.atleast_1d(x)
        key = x.tobytes()
        if key in self._cache:
            return self._cache[key]
        phase = phase_jets(self.solver, self.spline, x)
        tangent, aux = tangent_radial_jets(phase, self.sine)
        primitive = self.primitive_coefficients(tangent)
        mean = np.stack([self.solver.mean(x, self.alpha, j) for j in range(4)])
        radial = []
        for j in range(4):
            coefficient = sum(
                math.comb(j, k)*mean[k, :, 0, None, None]*primitive[j-k]
                for k in range(j+1))
            coefficient[:, 0, 2] += mean[j, :, 2]
            radial.append(coefficient)
        answer = dict(radial=radial, primitive=primitive, mean=mean,
                      phase=phase, auxiliary=aux)
        if len(self._cache) >= 3:
            self._cache.pop(next(iter(self._cache)))
        self._cache[key] = answer
        return answer

    def evaluate_coefficients(self, coefficients, inverse, theta):
        wave = np.exp(1j*theta[:, None]*self.frequency)
        return np.real(np.sum(coefficients[inverse]*wave[..., None], axis=1))

    def paired_jets(self, x, theta):
        x, theta = np.broadcast_arrays(np.asarray(x), np.asarray(theta))
        shape = x.shape
        x, theta = x.ravel(), theta.ravel()
        unique, inverse = np.unique(x, return_inverse=True)
        radial = self.radial_coefficients(unique)["radial"]
        fields = (
            radial[0], radial[1], self.angular(radial[0]),
            radial[2], self.angular(radial[1]), self.angular(radial[0], 2),
            radial[3], self.angular(radial[2]), self.angular(radial[1], 2),
            self.angular(radial[0], 3))
        return tuple(self.evaluate_coefficients(field, inverse, theta).reshape(shape+(3,))
                     for field in fields)

    def variation_jets(self, x, theta):
        x, theta = np.broadcast_arrays(np.asarray(x), np.asarray(theta))
        shape = x.shape
        x, theta = x.ravel(), theta.ravel()
        unique, inverse = np.unique(x, return_inverse=True)
        results = []
        for value in self.variation_radial_coefficients(unique):
            radial = value["radial"]
            fields = (radial[0], radial[1], self.angular(radial[0]),
                      radial[2], self.angular(radial[1]), self.angular(radial[0], 2))
            results.append(tuple(
                self.evaluate_coefficients(field, inverse, theta).reshape(shape+(3,))
                for field in fields))
        return results

    def variation_radial_coefficients(self, x):
        data = self.radial_coefficients(x)
        if "variation_radial" in data:
            return data["variation_radial"]
        unique = np.atleast_1d(x)
        z, mean, aux = data["primitive"], data["mean"], data["auxiliary"]
        results = []
        for index in range(self.solver.mean_count):
            if self.directions is None:
                variation_mean = np.stack([
                    self.solver.mean_splines[index](unique, nu=j)
                    for j in range(3)])
                dz = np.zeros_like(z[:3])
            else:
                variation_mean = np.stack([
                    sum((coefficient*sp(unique, nu=j) for coefficient, sp in
                         zip(self.direction_means[index], self.solver.mean_splines)),
                        np.zeros((len(unique), 3))) for j in range(3)])
                dphase = phase_jets(self.solver, self.direction_splines[index],
                                    unique, order=2)
                dz = self.primitive_coefficients(
                    tangent_variation_jets(aux, dphase, self.sine))
            radial = []
            for j in range(3):
                coefficient = sum(math.comb(j, k)*(
                    variation_mean[k, :, 0, None, None]*z[j-k]
                    +mean[k, :, 0, None, None]*dz[j-k]) for k in range(j+1))
                coefficient[:, 0, 2] += variation_mean[j, :, 2]
                radial.append(coefficient)
            results.append(dict(radial=radial, mean=variation_mean))
        data["variation_radial"] = results
        return results

    def strip_budget(self, x, sigma):
        """Third-order analytic tail+alias budgets, excluding all rounding."""
        x = float(x)
        data = self.radial_coefficients(np.array([x]))
        phase = data["phase"][:, 0]
        weight = np.cosh(4*np.arange(1, self.solver.modes+1)*sigma)
        size = np.sum(np.abs(phase)*weight[None, :, None], axis=1)
        b, p = size[0]
        tangent_bound = math.exp(p)*(2*math.exp(sigma+b)+1)
        d1, d2, d3 = (float(value) for value in size[1:].sum(axis=1))
        bounds = [tangent_bound, tangent_bound*d1,
                  tangent_bound*(d2+d1*d1),
                  tangent_bound*(d3+3*d1*d2+d1**3)]
        full_nodes, cutoff = 4*self.nodes, 2*self.nodes-3
        q, denominator = math.exp(-sigma), -math.expm1(-sigma)
        frequencies = np.arange(1, cutoff+1, dtype=float)
        primitive_budgets = []
        for bound in bounds:
            first = primitive_error_bounds(bound, sigma, full_nodes, cutoff)["total"]
            tail3 = 2*bound*math.exp(-sigma*(cutoff+1))*(
                (cutoff+1)**2/denominator
                +2*(cutoff+1)*q/denominator**2
                +q*(1+q)/denominator**3)
            alias3 = 4*bound*float(np.sum(
                frequencies**2*np.exp(-sigma*(full_nodes-frequencies))
            ))/(-math.expm1(-sigma*full_nodes))
            primitive_budgets.append(first+[tail3+alias3])
        primitive_budgets = np.array(primitive_budgets)
        radius = np.abs(data["mean"][:, 0, 0])
        pairs = [(0, 0), (1, 0), (0, 1), (2, 0), (1, 1),
                 (0, 2), (3, 0), (2, 1), (1, 2), (0, 3)]
        names = ["F", "Fx", "Ftheta", "Fxx", "Fxtheta", "Fthetatheta",
                 "Fxxx", "Fxxtheta", "Fxthetatheta", "Fthetathetatheta"]
        geometry_budgets = {
            name: float(sum(math.comb(r, k)*radius[k]*primitive_budgets[r-k, t]
                            for k in range(r+1)))
            for name, (r, t) in zip(names, pairs)}
        if not all(math.isfinite(value) for value in geometry_budgets.values()):
            raise ValueError("nonfinite strip budget")
        return dict(x=x, sigma=sigma, quarter_nodes=self.nodes,
                    equivalent_full_circle_nodes=full_nodes, cutoff=cutoff,
                    tangent_radial_bounds=[float(v) for v in bounds],
                    geometry_tail_alias_bounds=geometry_budgets,
                    roundoff_included=False)

    def radial_target_metric(self, x, with_variations=False):
        """Exact finite-primitive angular averages via Fourier Parseval.

        E=<|Fx|^2> and a are the output radial metric data, not the actual
        metric of a nonzero-residual candidate. K is that target metric's
        curvature and must not replace the candidate's actual det(II).
        """
        x = np.atleast_1d(x)
        unique, inverse = np.unique(x.ravel(), return_inverse=True)
        data = self.radial_coefficients(unique)
        fx, fxx, fxxx = data["radial"][1:]
        E = np.sum(np.abs(fx)**2, axis=(-2, -1))
        Ex = 2*np.real(np.sum(fxx*np.conj(fx), axis=(-2, -1)))
        Exx = 2*np.real(np.sum(fxxx*np.conj(fx)+fxx*np.conj(fxx), axis=(-2, -1)))
        a, ap, app, appp = data["mean"][:, :, 0]
        K = -app/(a*E)+ap*Ex/(2*a*E**2)
        discriminant = a*app-a*ap*Ex/(2*E)
        derivative = (ap*app+a*appp-(ap*ap+a*app)*Ex/(2*E)
                      -a*ap*Exx/(2*E)+a*ap*Ex**2/(2*E**2))
        G0 = E*a*a
        G0x = Ex*a*a+2*E*a*ap
        result = dict(E=E, E_x=Ex, E_xx=Exx, a=a, a_x=ap, a_xx=app,
                      a_xxx=appp, K=K, target_discriminant=discriminant,
                      target_discriminant_x=derivative, G0=G0, G0_x=G0x,
                      minus_K=discriminant/G0,
                      minus_K_x=derivative/G0-discriminant*G0x/G0**2)
        result = {key: value[inverse].reshape(x.shape) for key, value in result.items()}
        if with_variations:
            columns, curvature_columns = [], []
            for variation in self.variation_radial_coefficients(unique):
                vx, vxx = variation["radial"][1:]
                dE = 2*np.real(np.sum(vx*np.conj(fx), axis=(-2, -1)))
                dEx = 2*np.real(np.sum(
                    vxx*np.conj(fx)+fxx*np.conj(vx), axis=(-2, -1)))
                da, dap, dapp = variation["mean"][:, :, 0]
                ddisc = (da*app+a*dapp
                         -((da*ap+a*dap)*Ex+a*ap*dEx)/(2*E)
                         +a*ap*Ex*dE/(2*E**2))
                columns.append(ddisc[inverse].reshape(x.shape))
                dG0 = dE*a*a+2*E*a*da
                dmK = ddisc/G0-discriminant*dG0/G0**2
                curvature_columns.append(dmK[inverse].reshape(x.shape))
            result["discriminant_columns"] = np.array(columns)
            result["minus_K_columns"] = np.array(curvature_columns)
        return result


def raw_phase_data(geometry, solver, x, theta, columns=False):
    _, fx, ft, fxx, fxt, ftt, fxxx, fxxt, fxtt, fttt = geometry.paired_jets(x, theta)
    cross = np.cross(ft, fx)
    cx = np.cross(fxt, fx)+np.cross(ft, fxx)
    ct = np.cross(ftt, fx)+np.cross(ft, fxt)
    dot = lambda a, b: np.sum(a*b, axis=-1)
    l, m, n = [dot(cross, field) for field in (fxx, fxt, ftt)]
    lx, mx, nx = [dot(cx, a)+dot(cross, b)
                  for a, b in ((fxx, fxxx), (fxt, fxxt), (ftt, fxtt))]
    lt, mt, nt = [dot(ct, a)+dot(cross, b)
                  for a, b in ((fxx, fxxt), (fxt, fxtt), (ftt, fttt))]
    area = np.linalg.norm(cross, axis=-1)
    result = dict(l=l, m=m, n=n, delta=m*m-l*n, area=area,
                  area_x=dot(cross, cx)/area, area_theta=dot(cross, ct)/area,
                  delta_x=2*m*mx-lx*n-l*nx,
                  delta_theta=2*m*mt-lt*n-l*nt, m_theta=mt, n_theta=nt)
    if columns:
        dm_list, dn_list, dd_list, area_list = [], [], [], []
        for _, vx, vt, vxx, vxt, vtt in geometry.variation_jets(x, theta):
            dcross = np.cross(vt, fx)+np.cross(ft, vx)
            dl = dot(dcross, fxx)+dot(cross, vxx)
            dm = dot(dcross, fxt)+dot(cross, vxt)
            dn = dot(dcross, ftt)+dot(cross, vtt)
            dm_list.append(dm)
            dn_list.append(dn)
            dd_list.append(2*m*dm-n*dl-l*dn)
            area_list.append(dot(cross, dcross)/area)
        result.update(m_columns=np.array(dm_list), n_columns=np.array(dn_list),
                      delta_columns=np.array(dd_list), area_columns=np.array(area_list))
    return result


def raw_modified_phase_data(geometry, solver, x, theta, columns=False):
    """Principal symbol of R37 with this candidate's radial mean target metric.

    R37 uses G_actual=area(F)^2, NOT G0=E*a^2 in its density. Its exact
    raw discriminant is (-K_target)*G_actual^2=area(F)^4*(-K_target).
    The velocities are -M/N +/- sqrt(-K_target*G_actual)/abs(N).

    Parameter derivatives here belong to the synchronous target family
    g0(p)=E(p)dx^2+a(p)^2dtheta^2 and include delta K_target. They are NOT
    derivatives with a single target metric frozen. At a selected parameter
    one may then freeze g0 for the subsequent modified Newton correction.
    This is not the actual second fundamental form determinant.
    """
    result = raw_phase_data(geometry, solver, x, theta, columns)
    target = geometry.radial_target_metric(x, with_variations=columns)
    area, d = result["area"], target["minus_K"]
    result["true_delta"] = result["delta"]
    result["delta"] = area**4*d
    result["delta_x"] = (4*area**3*result["area_x"]*d
                         +area**4*target["minus_K_x"])
    result["delta_theta"] = 4*area**3*result["area_theta"]*d
    if columns:
        result["true_delta_columns"] = result["delta_columns"]
        result["delta_columns"] = (
            4*area[None, :]**3*result["area_columns"]*d[None, :]
            +area[None, :]**4*target["minus_K_columns"])
    return result


def load_phase(path, quarter_nodes=None, directions=None):
    with np.load(path, allow_pickle=False) as saved:
        metadata = json.loads(str(saved["metadata"]))
        solver = PhaseNewton(**metadata["parameters"])
        vector = saved["vector"]
        if "radius_shift_knots" in saved:
            solver.radius_shift = BSpline(
                saved["radius_shift_knots"], saved["radius_shift_coefficients"],
                int(saved["radius_shift_degree"]))
    nodes = metadata["quarter_period_angles"] if quarter_nodes is None else quarter_nodes
    geometry = PhaseGeometry(solver, vector, nodes, directions)
    return geometry, solver, vector, metadata


def preflight(geometry, solver, vector):
    x = np.array([0., .071, .13, .224])
    indices = np.array([0, 11, 43, 97]) % geometry.nodes
    theta = indices*(np.pi/2)/geometry.nodes
    actual = geometry.paired_jets(x, theta)
    reference = solver.geometry(vector, x, angles=geometry.nodes)[0]
    twojet = max(float(np.max(np.abs(
        actual[j]-reference[j][np.arange(len(x)), indices]))) for j in range(6))
    h = 2e-6
    plus, minus = geometry.paired_jets(x+h, theta), geometry.paired_jets(x-h, theta)
    third = {
        str(j): float(np.max(np.abs((plus[k]-minus[k])/(2*h)-actual[j])))
        for j, k in ((6, 3), (7, 4), (8, 5))}
    data = raw_phase_data(geometry, solver, x, theta, columns=True)
    modified = raw_modified_phase_data(geometry, solver, x, theta, columns=True)
    modified_x_fd = (
        raw_modified_phase_data(geometry, solver, x+h, theta)["delta"]
        -raw_modified_phase_data(geometry, solver, x-h, theta)["delta"])/(2*h)
    variation_errors, modified_errors = [], []
    for index in range(solver.mean_count):
        direction = (geometry.directions[index] if geometry.directions is not None
                     else np.r_[np.zeros(len(vector)-solver.mean_count),
                                np.eye(solver.mean_count)[index]])
        plus_geometry = PhaseGeometry(solver, vector+h*direction, geometry.nodes)
        minus_geometry = PhaseGeometry(solver, vector-h*direction, geometry.nodes)
        delta = (raw_phase_data(plus_geometry, solver, x, theta)["delta"]
                 -raw_phase_data(minus_geometry, solver, x, theta)["delta"])/(2*h)
        variation_errors.append(float(np.max(abs(delta-data["delta_columns"][index]))))
        modified_delta = (
            raw_modified_phase_data(plus_geometry, solver, x, theta)["delta"]
            -raw_modified_phase_data(minus_geometry, solver, x, theta)["delta"])/(2*h)
        modified_errors.append(float(np.max(
            abs(modified_delta-modified["delta_columns"][index]))))
    return dict(existing_finite_twojet_max_difference=twojet,
                radial_third_jet_finite_difference_errors=third,
                actual_parameter_discriminant_derivative_errors=variation_errors,
                actual_parameter_discriminant_derivative_scales=[
                    float(np.max(abs(column))) for column in data["delta_columns"]],
                actual_parameter_discriminant_derivative_relative_errors=[
                    error/max(1., float(np.max(abs(column))))
                    for error, column in zip(variation_errors, data["delta_columns"])],
                R37_synchronous_target_discriminant_derivative_errors=modified_errors,
                R37_synchronous_target_discriminant_derivative_relative_errors=[
                    error/max(1., float(np.max(abs(column))))
                    for error, column in zip(modified_errors, modified["delta_columns"])],
                R37_discriminant_x_derivative_error=float(
                    np.max(abs(modified_x_fd-modified["delta_x"]))),
                finite_difference_step=h,
                limitations="ordinary floating comparison, not error bounds")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--checkpoint", type=Path, required=True)
    parser.add_argument("--out", type=Path, required=True)
    parser.add_argument("--quarter-nodes", type=int)
    args = parser.parse_args()
    geometry, solver, vector, metadata = load_phase(
        args.checkpoint, args.quarter_nodes)
    result = dict(kind="floating_phase_geometry_threejet_preflight",
                  checkpoint=args.checkpoint.name,
                  sha256=hashlib.sha256(args.checkpoint.read_bytes()).hexdigest(),
                  quarter_nodes=geometry.nodes, checks=preflight(geometry, solver, vector))
    args.out.write_text(json.dumps(result, indent=2)+"\n")
    print(json.dumps(result), flush=True)


if __name__ == "__main__":
    main()
