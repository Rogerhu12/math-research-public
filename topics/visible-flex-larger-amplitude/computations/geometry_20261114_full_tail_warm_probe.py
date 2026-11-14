#!/usr/bin/env python3
"""Actual full-curve warm-field probes from the accepted prefix to a tail cut.

These are explicit approximate fields for a future global BVP. Their metric,
Cartesian curvature, Frenet domain, sphere clearance and full spectrum are
measured. No ODE solution or nonlinear tail acceptance is asserted.
"""
import os
for name in ('OPENBLAS_NUM_THREADS', 'OMP_NUM_THREADS', 'MKL_NUM_THREADS'):
    os.environ[name] = '1'
import argparse
import gzip
import hashlib
import importlib.util
import json
import math
from pathlib import Path
import numpy as np

P = Path(__file__).resolve().parent


def load(name, filename):
    spec = importlib.util.spec_from_file_location(name, P/filename)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


chartmod = load('warm_material_chart', 'geometry_20261114_adaptive_material_chart.py')
base = chartmod.base
connector = load('warm_angle_connector', 'strong_20261114_scaled_core_tail_connector.py')
provider = load('warm_original_bridge', 'alternative-neck-provider.py')


class FullScalarProfile:
    def __init__(self, fixed, port, K=2.2, ramp_in=.08, ramp_out=.08):
        self.fixed = fixed
        self.start = fixed.end
        incoming = fixed.profile(self.start)
        self.connector = connector.AngleConnector(incoming, K, ramp_in=ramp_in, ramp_out=ramp_out)
        self.turn_end = self.start+self.connector.length
        self.coast_length = (self.connector.end_radius-.35)/.985
        if self.coast_length <= 0:
            raise ValueError('The proposed connector has no positive coast to the original bridge')
        self.coast_end = self.turn_end+self.coast_length
        tagged = provider.tagged_port(port, dict(loop_radius=.35, loop_speed=.985,
                                                 loop_curvature=7.5, terminal_peak_fraction=.1))
        self.port = tagged
        self.bridge = provider.NeckTerminalBridge(tagged['cut'])
        self.end = self.coast_end+self.bridge.end
        self.parameter_values = [K, ramp_in, ramp_out]

    def profile(self, s):
        if s <= self.start:
            return self.fixed.profile(s)
        if s <= self.turn_end:
            return tuple(float(v) for v in self.connector.profile(s-self.start))
        if s <= self.coast_end:
            return self.connector.end_radius-.985*(s-self.turn_end), -.985, 0.
        if s <= self.end+1e-13:
            return tuple(float(np.ravel(v)[0]) for v in self.bridge.profile(s-self.coast_end))
        raise ValueError('Outside the complete fixed-cut scalar profile')

    def height(self, s):
        if s < self.start-1e-14:
            raise ValueError('The background increment is defined after the accepted endpoint')
        if s <= self.turn_end:
            return float(self.connector.height_at(s-self.start))
        value = self.connector.height
        if s <= self.coast_end:
            return value+(s-self.turn_end)*math.sqrt(1-.985**2)
        value += self.coast_length*math.sqrt(1-.985**2)
        local = s-self.coast_end
        for seg in self.bridge.segments:
            if local <= seg['s1']+1e-13:
                u = np.clip((local-seg['s0'])/seg['length'], 0., 1.)
                return value+seg['h0']+seg['length']*float(provider.fl.integral(seg, u, 'cos'))
        return value+self.bridge.height

    def breakpoints(self):
        c = self.connector
        return np.unique(np.r_[self.start, self.start+c.length*c.ei,
                               self.start+c.length*(1-c.eo), self.turn_end, self.coast_end,
                               self.coast_end+self.bridge.breakpoints, self.end])


def blend_weights(s, length):
    if s >= length:
        return np.zeros(3), np.zeros(3), np.zeros(3)
    u = s/length
    w = np.array([1-10*u**3+15*u**4-6*u**5,
                  length*(u-6*u**3+8*u**4-3*u**5),
                  length**2*(u*u-3*u**3+3*u**4-u**5)/2])
    wp = np.array([(-30*u*u+60*u**3-30*u**4)/length,
                   1-18*u*u+32*u**3-15*u**4,
                   length*(2*u-9*u*u+12*u**3-5*u**4)/2])
    wpp = np.array([(-60*u+180*u*u-120*u**3)/length**2,
                    (-36*u+96*u*u-60*u**3)/length,
                    (2-18*u+36*u*u-20*u**3)/2])
    return w, wp, wpp


def core_endpoint_material(theta, data, jets):
    c = np.array(data['core']['coefficients'])
    M = len(c)
    phi, rho, rhop, error = chartmod.inverse_core_angle(theta, c)
    v, first, second = chartmod.reader.angular_jet(None, M, phi)(np.array([
        data['states'][-1], data['rhs'][-1], jets['second_jets_binary64'][-1]]))
    value = np.array([chartmod.rotate_polar(z, phi) for z in v])
    angular = np.array([chartmod.rotate_polar(z/rho[:, None], phi) for z in first])
    angular2 = np.array([chartmod.rotate_polar(z/rho[:, None]**2-f*(rhop/rho**3)[:, None], phi)
                         for z, f in zip(second, first)])
    return value, angular, angular2, error


def seed_jet(s, damping_length, data, jets, scalar, chart, psi):
    g = chart.angle(s, psi, np.array(data['core']['coefficients']))
    theta = g['theta']
    er = np.c_[np.cos(theta), np.sin(theta), np.zeros_like(theta)]
    et = np.c_[-np.sin(theta), np.cos(theta), np.zeros_like(theta)]
    a, ap, app = scalar.profile(s)
    a0, ap0, app0 = scalar.profile(scalar.start)
    z0 = float(data['states'][-1][2*data['M']+1])
    zp = math.sqrt(1-ap*ap)
    zpp = -ap*app/zp
    zp0 = math.sqrt(1-ap0*ap0)
    zpp0 = -ap0*app0/zp0
    old, old_t, old_tt, error = core_endpoint_material(theta, data, jets)
    background0 = np.array([a0*er, ap0*er, app0*er])
    background0[:, :, 2] = np.array([z0, zp0, zpp0])[:, None]
    background_t0 = np.array([a0*et, ap0*et, app0*et])
    background_tt0 = -np.array([a0*er, ap0*er, app0*er])
    D, Dt, Dtt = old-background0, old_t-background_t0, old_tt-background_tt0
    w, wp, wpp = blend_weights(s-scalar.start, damping_length)
    F = a*er+np.einsum('i,ijk->jk', w, D)
    F[:, 2] += z0+scalar.height(s)
    Fs = ap*er+np.einsum('i,ijk->jk', wp, D)
    Fs[:, 2] += zp
    Fss = app*er+np.einsum('i,ijk->jk', wpp, D)
    Fss[:, 2] += zpp
    Ft = a*et+np.einsum('i,ijk->jk', w, Dt)
    Fst = ap*et+np.einsum('i,ijk->jk', wp, Dt)
    Ftt = -a*er+np.einsum('i,ijk->jk', w, Dtt)
    coordinate_s = Fs+g['theta_s'][:, None]*Ft
    coordinate_ss = Fss+2*g['theta_s'][:, None]*Fst+g['theta_s'][:, None]**2*Ftt+g['theta_ss'][:, None]*Ft
    return np.array([chartmod.rotate_polar(v, -psi) for v in (F, coordinate_s, coordinate_ss)]), g, error


def inspect(s, coefficients, scalar, chart, core, N, q):
    y, yp, ypp = coefficients
    M = len(core)
    values, first, second = chartmod.uniform_jet(coefficients, M, N)
    F, Fs, Fss = values
    Ft, Fst = first[:2]
    Ftt = second[0]
    g = chart.angle(s, q.phi, core)
    a, ap, app = scalar.profile(s)
    metric = chartmod.metric(Fs, Ft, a, g)
    E = np.sum(Fs*Fs, axis=-1)
    mix = np.sum(Fs*Ft, axis=-1)
    G = np.sum(Ft*Ft, axis=-1)
    cross = np.cross(Fs, Ft)
    det = E*G-mix*mix
    normal = cross/np.linalg.norm(cross, axis=-1)[:, None]
    e = np.sum(Fss*normal, axis=-1)
    f = np.sum(Fst*normal, axis=-1)
    gg = np.sum(Ftt*normal, axis=-1)
    trace = (e*G+gg*E-2*f*mix)/det
    kdet = (e*gg-f*f)/det
    kappa = float(np.max((abs(trace)+np.sqrt(np.maximum(0, trace*trace-4*kdet)))/2))
    fr = q.frame(s, y, strict=False)
    domain = float(fr['margin'].real.min())
    residual = None
    if domain > 0 and g['rho'].min() > 0:
        actual = chart.rhs(q, s, y, core)
        residual = float(abs(actual-yp).max())
    xyz = chartmod.rotate_polar(F, q.phi)
    witness = np.array([0., 1+sum(core), 0.])
    return dict(s=float(s), a=a, ap=ap, app=app, metric_sample=metric,
                curvature_sample=kappa, actual_frenet_domain_min=domain,
                seed_derivative_vs_actual_rhs_max=residual,
                D_prefix_proxy=2*float(np.linalg.norm(xyz, axis=-1).max()),
                witness_distance_min=float(np.linalg.norm(xyz-witness, axis=-1).min()),
                chart_density_min=float(g['rho'].min()),
                target_H_nonmean_max=float(abs(y[2*M+2:]).max()),
                tail_coefficient_max=float(max(abs(y[M]), abs(y[2*M]), abs(y[-1]))))


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--input', type=Path, required=True)
    p.add_argument('--second-jets', type=Path, required=True)
    p.add_argument('--port', type=Path, required=True)
    p.add_argument('--damping-lengths', type=float, nargs='+', default=[.15, .25, .4, .6])
    p.add_argument('--angular', type=int, default=1024)
    p.add_argument('--projection-angular', type=int, default=2048)
    p.add_argument('--radial', type=int, default=81)
    p.add_argument('--K', type=float, default=2.2)
    p.add_argument('--out', type=Path, required=True)
    args = p.parse_args()
    data = base.fixed.read(args.input)
    jets = base.fixed.read(args.second_jets)
    port = base.fixed.read(args.port)
    fixed = base.fixed.FixedProfile(data['fixed_scalar_profile']['geometry'])
    scalar = FullScalarProfile(fixed, port, K=args.K)
    chart = chartmod.QuinticMaterialChart(scalar.start, scalar.end)
    M = data['M']
    c = np.array(data['core']['coefficients'])
    law = data['original_metric_identity']['law']
    q = base.native.outward.FullCoreProbe(c, M, args.angular, law['velocity'], law['length'], law['k0'])
    q.profile = scalar.profile
    base.fixed.fft.enable_fft(q)
    psi = 2*np.pi*np.arange(args.projection_angular)/args.projection_angular
    all_rows = []
    for damping in args.damping_lengths:
        stations = np.unique(np.r_[np.linspace(scalar.start, min(scalar.end, scalar.start+damping), args.radial),
                                    np.linspace(min(scalar.end, scalar.start+damping), scalar.end, 41),
                                    scalar.breakpoints()])
        rows, states, derivatives, second = [], [], [], []
        for s in stations:
            values, ignored, error = seed_jet(float(s), damping, data, jets, scalar, chart, psi)
            coefficients = np.array([chartmod.project(v, M) for v in values])
            rows.append(inspect(float(s), coefficients, scalar, chart, c, args.angular, q))
            states.append(coefficients[0].tolist())
            derivatives.append(coefficients[1].tolist())
            second.append(coefficients[2].tolist())
        record = dict(damping_length=damping, rows=rows, mesh=stations.tolist(), states=states,
                      actual_seed_first_jets=derivatives, actual_seed_second_jets=second,
                      summary=dict(metric_sample=max(r['metric_sample'] for r in rows),
                                   curvature_sample=max(r['curvature_sample'] for r in rows),
                                   minimum_frenet_domain=min(r['actual_frenet_domain_min'] for r in rows),
                                   D_proxy=max(r['D_prefix_proxy'] for r in rows),
                                   witness_distance=min(r['witness_distance_min'] for r in rows),
                                   maximum_ODE_residual=max((r['seed_derivative_vs_actual_rhs_max'] or 0) for r in rows)))
        all_rows.append(record)
        print(json.dumps(dict(event='full_tail_warm_probe', damping_length=damping, **record['summary'])), flush=True)
    report = dict(scope=__doc__, actual_new_solution=False, physical_tail_cut=scalar.port['cut'],
                  source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
                  inputs={str(p):hashlib.sha256(p.read_bytes()).hexdigest() for p in (args.input, args.second_jets, args.port)},
                  M=M, angular=args.angular, projection_angular=args.projection_angular,
                  scalar_controls=scalar.parameter_values, physical_cut_s=scalar.end,
                  scalar_breakpoints=scalar.breakpoints().tolist(), chart_start=chart.start, chart_end=chart.end,
                  complete_original_fixed_prefix=data['fixed_scalar_profile'], probes=all_rows)
    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_bytes(gzip.compress((json.dumps(report)+'\n').encode(), mtime=0))
    print(json.dumps(dict(out=str(args.out), physical_cut_s=scalar.end,
                         summaries=[v['summary'] for v in all_rows])), flush=True)


if __name__ == '__main__':
    main()
