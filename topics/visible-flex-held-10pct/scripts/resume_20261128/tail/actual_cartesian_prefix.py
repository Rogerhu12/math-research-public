#!/usr/bin/env python3
"""Explicit common-C2 Cartesian prefix from an actual positive-lambda R53 field.

Retain the entire analytical core lift, not merely its Fourier projection.
The radial coefficients and mean are declared shared-jet finite functions.
The mean samples use the source's literal angular count and GL6 rule, but
their shared-Hermite interpolant is explicitly a NEW finite map. It is not
the source primitive and does not inherit R59/R62 metric or geometry bounds.
This module does not solve a BVP or assert a closed surface.
"""
import os
for _key in ('OPENBLAS_NUM_THREADS', 'OMP_NUM_THREADS', 'MKL_NUM_THREADS'):
    os.environ[_key] = '1'
import argparse
import hashlib
import importlib.util
import json
from pathlib import Path
import sys
from types import SimpleNamespace

import numpy as np
from scipy.interpolate import PPoly

HERE = Path(__file__).resolve().parent
SCRIPTS = HERE.parents[1]
CLOSED = SCRIPTS/'finite_closure/m3_m8_closed_map'
sys.path.insert(0, str(CLOSED))
from shared_jet import SharedJetQuintic, build_mean
from m3_shared_prefix import M3SharedPrefix, M3CartesianPrefix, circle
from phase_angle_chart import PhaseAngleChart


def module(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    value = importlib.util.module_from_spec(spec)
    sys.modules[name] = value
    spec.loader.exec_module(value)
    return value


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


class ActualR53CartesianPrefix(M3CartesianPrefix):
    """Finite Cartesian base plus the complete exact-core reference lift.

    Values returned by core.evaluate use its original numerical integral
    oracle. The mathematical core is the R53 true phase/position integral;
    rigorous bounds for oracle error are a separate obligation.
    """
    def __init__(self, obj, flow, physical, mean_nodes, side_modes=None,
                 center_width=.04):
        if flow.exact_lift_core is not obj._core:
            raise ValueError('The source must retain its actual exact-core lift')
        if not hasattr(obj._core, 'homotopy') or not 0 < obj._core.homotopy <= 1:
            raise ValueError('This adapter is for the declared positive-lambda R53 core')
        shared = SharedJetQuintic.from_ppoly(physical.sol)
        sol = SimpleNamespace(x=shared.x, y=shared(shared.x), p=physical.p.copy(), sol=shared)
        # Deliberately explicit: source N and GL6, never build_mean defaults.
        sol.mean_spline = build_mean(flow, sol, int(mean_nodes), 6)
        old = M3SharedPrefix(obj, flow, sol, center_width)
        super().__init__(old, max(int(obj.M), 32) if side_modes is None else side_modes)
        self.source_physical = physical
        self.mean_nodes = int(mean_nodes)
        self.source_initial = np.asarray(flow.exact_lift_initial, float).copy()
        knots = self.rep.x
        a, ap, app = (np.asarray(v, float) for v in flow.profile(knots))
        low, high = .5*flow.prefix_end, .9*flow.prefix_end
        width = high-low
        u = np.clip((knots-low)/width, 0., 1.)
        chi = 1-u**3*(10-15*u+6*u*u)
        chip = -30*u*u*(1-u)**2/width
        chipp = -60*u*(1-u)*(1-2*u)/width**2
        h = np.stack((a*chi, ap*chi+a*chip,
                      app*chi+2*ap*chip+a*chipp))[:, None, :]
        self.core_lift_radial = SharedJetQuintic(knots, h)

    def complete_core_lift_jets(self, psi):
        psi = np.atleast_1d(np.asarray(psi, float))
        theta = psi-self.E0*np.sin(3*psi)/3
        rho = 1-self.E0*np.cos(3*psi)
        rhop = 3*self.E0*np.sin(3*psi)
        core = self.core.evaluate(theta)
        er, et = circle(theta), circle(theta, 1)
        return (
            core['F']-er-self.q*self.coefficient_value(self.source_initial, psi, 0),
            rho[:, None]*(core['Ft']-et)
                -self.q*self.coefficient_value(self.source_initial, psi, 1),
            rho[:, None]**2*(core['Ftt']+er)
                +rhop[:, None]*(core['Ft']-et)
                -self.q*self.coefficient_value(self.source_initial, psi, 2),
        )

    def raw_cartesian_jets(self, s, psi):
        s = np.atleast_1d(np.asarray(s, float))
        psi = np.atleast_1d(np.asarray(psi, float))
        coefficients = [self.rep(s, order) for order in range(3)]
        radial = [self.core_lift_radial(s, order)[0] for order in range(3)]
        angular = self.complete_core_lift_jets(psi)
        pairs = ((0, 0), (1, 0), (2, 0), (0, 1), (0, 2), (1, 1))
        return [self.tensor_values(coefficients[i], psi, j)
                +radial[i][:, None, None]*angular[j][None, :, :] for i, j in pairs]

    def center_delta(self, psi):
        psi = np.atleast_1d(np.asarray(psi, float))
        theta = psi-self.E0*np.sin(3*psi)/3
        rho, rhop = 1-self.E0*np.cos(3*psi), 3*self.E0*np.sin(3*psi)
        b, bp, bpp = (-self.Epp*np.sin(3*psi)/3,
                     -self.Epp*np.cos(3*psi), 3*self.Epp*np.sin(3*psi))
        core = self.core.evaluate(theta)
        if any(key not in core for key in ('phi', 'kappa', 'kappa_u')):
            raise ValueError('Use actual material curvature derivatives, not support Fourier labels')
        gt, gtt = core['Ft'], core['Ftt']
        gttt = (-core['kappa_u'][:, None]*circle(core['phi'])
                 -core['kappa'][:, None]**2*circle(core['phi'], 1))
        angular = self.complete_core_lift_jets(psi)
        radial = self.core_lift_radial.jets[:, 0, 0]
        data = self.rep.jets[:, :, 0]
        result = []
        for j in range(3):
            before = (self.tensor_values(data.T, psi, j)
                      +radial[:, None, None]*angular[j][None, :, :])
            target = np.zeros_like(before)
            if j == 0:
                target[0], target[1, :, 2], target[2] = core['F'], 1., b[:, None]*gt
            elif j == 1:
                target[0] = rho[:, None]*gt
                target[2] = bp[:, None]*gt+(b*rho)[:, None]*gtt
            else:
                target[0] = rho[:, None]**2*gtt+rhop[:, None]*gt
                target[2] = (bpp[:, None]*gt+(2*bp*rho+b*rhop)[:, None]*gtt
                             +(b*rho*rho)[:, None]*gttt)
            result.append(target-before)
        return result

    def raw_endpoint_angular_jets(self, psi):
        data = self.rep.jets[:, :, -1]
        radial = self.core_lift_radial.jets[:, 0, -1]
        angular = self.complete_core_lift_jets(psi)
        return [self.tensor_values(data.T, psi, j)
                +radial[:, None, None]*angular[j][None, :, :] for j in range(3)]

    def evaluate(self, s, psi):
        s, psi = np.atleast_1d(np.asarray(s, float)), np.atleast_1d(np.asarray(psi, float))
        jets = self.raw_cartesian_jets(s, psi)
        pairs = ((0, 0), (1, 0), (2, 0), (0, 1), (0, 2), (1, 1))
        if np.any(s <= self.center_width):
            differences = self.center_delta(psi)
            weights = [self.center_weights(s, order) for order in range(3)]
            for value, (i, j) in zip(jets, pairs):
                value += np.einsum('sj,juk->suk', weights[i], differences[j])
        if self.end_lift is not None:
            for value, correction in zip(jets, self.end_lift.correction(s, psi)):
                value += correction
        return jets


def load_actual_prefix(source_run, *, side_modes=None, center_width=.04):
    source_run = Path(source_run).resolve()
    gate = module('_actual_c2_original_gate', SCRIPTS/'resume_20261126/material_design_secant_predictor.py')
    repo = SCRIPTS.parents[2]
    record, arrays = gate.accepted_original(source_run, repo)
    del arrays
    loader = module('_actual_c2_original_model', SCRIPTS/'resume_m3/actual_m3_metric_model.py')
    obj = loader.load_model({'source_run': str(source_run)})
    with np.load(source_run.parent/'physical.npz', allow_pickle=False) as data:
        physical = SimpleNamespace(x=data['x'].copy(), p=data['p'].copy(),
            sol=PPoly.construct_fast(data['c'].copy(), data['x'].copy(),
                                     extrapolate=False, axis=1))
    obj.initial(physical.p)
    flow = obj.flow(physical.p[0])
    count = int(record['prefix_audit']['samples_psi'])
    value = ActualR53CartesianPrefix(obj, flow, physical, count, side_modes, center_width)
    return record, value


def sampled_diagnostics(prefix, *, block=16):
    """Sample the same new map; no continuous bounds are inherited."""
    chart = PhaseAngleChart(prefix)
    s = np.unique(np.r_[prefix.rep.x, (prefix.rep.x[:-1]+prefix.rep.x[1:])/2,
                        prefix.center_width, prefix.flow.prefix_end])
    s = s[(s >= 0)&(s <= prefix.flow.end)]
    psi = 2*np.pi*np.arange(prefix.mean_nodes)/prefix.mean_nodes
    result = dict(sampled_radial_count=len(s), sampled_angle_count=len(psi),
        metric_relative_operator_max=0., metric_normalized_entry_max=0.,
        principal_curvature_absolute_max=0., support_min=float('inf'),
        norm_max=0., area_factor_min=float('inf'), angular_rho_min=float('inf'),
        finite_values=True, immersed_at_samples=True,
        curvature_discriminant_min=float('inf'))
    for start in range(0, len(s), block):
        ss = s[start:start+block]
        X, Xs, Xss, Xp, Xpp, Xsp = prefix.evaluate(ss, psi)
        if not all(np.all(np.isfinite(v)) for v in (X, Xs, Xss, Xp, Xpp, Xsp)):
            raise FloatingPointError('The explicit new Cartesian map has a nonfinite sampled jet')
        _, rho, _, theta_s, _, _ = chart.angular(ss[:, None], psi[None, :])
        a = np.asarray(prefix.flow.profile(ss)[0], float)[:, None]
        F_s = Xs-(theta_s/rho)[:, :, None]*Xp
        F_t_normalized = Xp/(a*rho)[:, :, None]
        q0 = np.sum(F_s*F_s, axis=-1)-1
        q1 = np.sum(F_s*F_t_normalized, axis=-1)
        q2 = np.sum(F_t_normalized*F_t_normalized, axis=-1)-1
        relative = np.abs(q0+q2)/2+np.sqrt(((q0-q2)/2)**2+q1*q1)
        E, F, G = (np.sum(v*w, axis=-1) for v, w in ((Xs, Xs), (Xs, Xp), (Xp, Xp)))
        normal = np.cross(Xp, Xs)
        area = np.linalg.norm(normal, axis=-1)
        determinant = E*G-F*F
        if np.any(area <= 0) or np.any(determinant <= 0) or np.any(rho <= 0):
            raise FloatingPointError('The explicit new Cartesian map loses sampled immersion or angle invertibility')
        normal /= area[:, :, None]
        e, f, g = (np.sum(normal*v, axis=-1) for v in (Xss, Xsp, Xpp))
        trace = (e*G+g*E-2*f*F)/determinant
        gaussian = (e*g-f*f)/determinant
        disc = trace*trace-4*gaussian
        if np.min(disc) < -1e-8:
            raise FloatingPointError('A sampled curvature discriminant exceeds its floating consistency allowance')
        K = (np.abs(trace)+np.sqrt(np.maximum(disc, 0)))/2
        result['metric_relative_operator_max'] = max(result['metric_relative_operator_max'], float(relative.max()))
        result['metric_normalized_entry_max'] = max(result['metric_normalized_entry_max'],
            float(np.max(np.abs(q0))), float(np.max(np.abs(q1))), float(np.max(np.abs(q2))))
        result['principal_curvature_absolute_max'] = max(result['principal_curvature_absolute_max'], float(K.max()))
        result['support_min'] = min(result['support_min'], float(np.sum(X*normal, axis=-1).min()))
        result['norm_max'] = max(result['norm_max'], float(np.linalg.norm(X, axis=-1).max()))
        result['area_factor_min'] = min(result['area_factor_min'], float(area.min()))
        result['angular_rho_min'] = min(result['angular_rho_min'], float(rho.min()))
        result['curvature_discriminant_min'] = min(result['curvature_discriminant_min'], float(disc.min()))
    mean_s = np.unique(np.r_[np.linspace(0., prefix.flow.end, 33),
                            prefix.center_width, prefix.flow.prefix_end, prefix.flow.end])
    flow, physical = prefix.flow, prefix.source_physical
    source_height = flow.height_integral(physical, mean_s, prefix.mean_nodes, 6)
    _, B1, B2 = flow.basis(prefix.mean_nodes)
    mean_first, mean_second = [], []
    for start in range(0, len(mean_s), block):
        ss = mean_s[start:start+block]
        velocity, _, derivative = flow.velocity_s(ss, physical.sol(ss), physical.sol(ss, 1), B1, B2)
        mean_first.extend(np.mean(velocity['V'][:, :, 2], axis=1))
        mean_second.extend(np.mean(derivative[:, :, 2], axis=1))
    source_mean = np.stack((source_height, mean_first, mean_second))
    new_mean = np.stack([prefix.sol.mean_spline(mean_s, order)[0] for order in range(3)])
    result['source_mean_oracle_comparison'] = dict(
        definition='Original physical PPoly; source literal N, source GL6 position oracle, original mean velocity/acceleration',
        radial_samples=len(mean_s), angular=prefix.mean_nodes, height_quadrature_order=6,
        new_shared_mean_minus_source_orders_0_1_2_absolute_max=np.max(np.abs(new_mean-source_mean), axis=1).tolist(),
        same_mean_function_asserted=False)
    result['sampled_budget_checks'] = dict(
        metric_at_most_1e_6=result['metric_relative_operator_max'] <= 1e-6,
        curvature_at_most_12p3=result['principal_curvature_absolute_max'] <= 12.3,
        norm_at_most_1p34=result['norm_max'] <= 1.34,
        support_at_least_p087=result['support_min'] >= .087)
    result['scope'] = 'Sampled new prefix only, before tail/end-lift; no all-angle/all-radius, reach, or full-surface assertion'
    result['phase_chart'] = chart.report()
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--source-run', type=Path, required=True)
    parser.add_argument('--out', type=Path, required=True)
    parser.add_argument('--side-modes', type=int)
    args = parser.parse_args()
    record, prefix = load_actual_prefix(args.source_run, side_modes=args.side_modes)
    angles = 2*np.pi*np.arange(prefix.mean_nodes)/prefix.mean_nodes
    sample_s = np.unique(np.r_[0., prefix.center_width,
        np.linspace(0., prefix.flow.end, 21), prefix.flow.prefix_end, prefix.flow.end])
    sample_s = sample_s[(sample_s >= 0)&(sample_s <= prefix.flow.end)]
    fields = prefix.evaluate(sample_s, angles)
    maxima = [float(np.max(np.abs(value))) for value in fields]
    core = prefix.core.evaluate(angles-prefix.E0*np.sin(3*angles)/3)
    center = prefix.evaluate([0.], angles)
    target_ss = (-prefix.Epp*np.sin(3*angles)/3)[:, None]*core['Ft']
    errors = [float(np.max(np.abs(center[0][0]-core['F']))),
              float(np.max(np.abs(center[1][0]-np.array([0., 0., 1.])))),
              float(np.max(np.abs(center[2][0]-target_ss)))]
    report = dict(scope=__doc__, source_run=str(args.source_run.resolve()),
        source_run_sha256=sha(args.source_run), source_sha256=sha(__file__),
        source_homotopy=record['core_settings']['homotopy'], modes=prefix.M,
        source_literal_mean_nodes=prefix.mean_nodes, mean_height_quadrature_order=6,
        mean_definition='New finite shared-Hermite interpolant of source-N/GL6 oracle samples',
        source_primitive_preserved_as_same_function=False,
        original_R62_or_other_geometry_bounds_inherited=False,
        complete_analytic_core_lift_retained=True,
        radial_knots=len(prefix.rep.x), sampled_radial_count=len(sample_s),
        sampled_angle_count=len(angles), six_cartesian_jet_absolute_maxima=maxima,
        center_shared_position_first_second_numeric_errors=errors,
        finite_queries_all_finite=all(np.all(np.isfinite(value)) for value in fields),
        actual_cut_correction_applied=False, tail_attached=False, complete_surface=False,
        metric_or_C2_convergence_asserted=False)
    report['new_map_sampled_diagnostics'] = sampled_diagnostics(prefix)
    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text(json.dumps(report, indent=2, allow_nan=False)+'\n')
    print(json.dumps(report, indent=2, allow_nan=False))


if __name__ == '__main__':
    main()
