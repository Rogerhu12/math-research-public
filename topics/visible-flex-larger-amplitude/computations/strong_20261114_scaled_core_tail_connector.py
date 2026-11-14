#!/usr/bin/env python3
"""A scalar C2 continuation from the new large-core prefix to the original tail.

Only the metric profile and axisymmetric continuation budget are computed.
No nonaxisymmetric Frenet solution, core response, tail solution, full closed
surface, diameter bound, reach bound, or amplitude certificate is created.
The old complete physical tail cut and original finite bridge are retained.
"""
from __future__ import annotations
import os
for _k in ('OPENBLAS_NUM_THREADS', 'OMP_NUM_THREADS', 'MKL_NUM_THREADS'):
    os.environ[_k] = '1'
import argparse
import gzip
import hashlib
import importlib.util
import json
import math
from pathlib import Path
import numpy as np


def read(path):
    path = Path(path)
    raw = path.read_bytes()
    return json.loads(gzip.decompress(raw) if path.suffix == '.gz' else raw)


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


class AngleConnector:
    """Exact angle formula, with numerical quadrature only for a and height.

    The incoming (a,a',a'') is retained. Curvature starts at its actual value,
    changes by a cubic smoothstep to K, stays flat, then falls to zero.
    The normalization makes the terminal radial speed exactly -speed.
    """
    def __init__(self, incoming, K, speed=.985, ramp_in=.08, ramp_out=.08,
                 quadrature=48):
        self.a0, self.ap0, self.app0 = map(float, incoming)
        if not self.a0 > 0 or not -1 < self.ap0 < 1 or not self.app0 < 0:
            raise ValueError('This connector requires positive radius and a genuine incoming inward bend')
        self.phi0, self.phi1 = math.asin(self.ap0), -math.asin(speed)
        self.k0 = -self.app0/math.sqrt(1-self.ap0*self.ap0)
        self.K, self.ei, self.eo = float(K), float(ramp_in), float(ramp_out)
        if not self.K >= self.k0 or not 0 < self.ei or not 0 < self.eo or not self.ei+self.eo < 1:
            raise ValueError('The positive peak and two disjoint ramps must retain the incoming curvature')
        self.integrated_K = self.K*(1-(self.ei+self.eo)/2)+self.k0*self.ei/2
        self.length = (self.phi0-self.phi1)/self.integrated_K
        self.gx, self.gw = np.polynomial.legendre.leggauss(quadrature)
        self.gx, self.gw = (self.gx+1)/2, self.gw/2
        self.end_radius, _, _ = self.profile(self.length)
        self.height = float(self.integral(1., 'cos')*self.length)

    def phase_and_k(self, u):
        u = np.asarray(u, float)
        if np.any(u < -1e-13) or np.any(u > 1+1e-13):
            raise ValueError('Angle connector point is outside its interval')
        u = np.clip(u, 0., 1.)
        first = self.ei*(self.k0+self.K)/2
        last0 = first+self.K*(1-self.eo-self.ei)
        t = u/self.ei
        ramp = 3*t*t-2*t*t*t
        integral = self.k0*u+(self.K-self.k0)*self.ei*(t**3-t**4/2)
        k = self.k0+(self.K-self.k0)*ramp
        middle = (u >= self.ei) & (u <= 1-self.eo)
        integral = np.where(middle, first+self.K*(u-self.ei), integral)
        k = np.where(middle, self.K, k)
        t = (u-(1-self.eo))/self.eo
        last = u > 1-self.eo
        integral = np.where(last, last0+self.K*self.eo*(t-t**3+t**4/2), integral)
        k = np.where(last, self.K*(1-3*t*t+2*t*t*t), k)
        return self.phi0-self.length*integral, k

    def integral(self, u, component='sin'):
        u = np.asarray(u, float)
        shape = u.shape
        values = u.reshape(-1)
        answer = np.zeros_like(values)
        f = np.sin if component == 'sin' else np.cos
        for lo, hi in zip((0., self.ei, 1-self.eo), (self.ei, 1-self.eo, 1.)):
            widths = np.maximum(0., np.minimum(values, hi)-lo)
            points = lo+widths[:, None]*self.gx[None, :]
            phase, _ = self.phase_and_k(points)
            answer += widths*np.sum(f(phase)*self.gw[None, :], axis=1)
        return answer.reshape(shape)

    def profile(self, s):
        u = np.asarray(s, float)/self.length
        phase, k = self.phase_and_k(u)
        return self.a0+self.length*self.integral(u), np.sin(phase), -k*np.cos(phase)

    def height_at(self, s):
        return self.length*self.integral(np.asarray(s, float)/self.length, 'cos')


def xyz_jet(jet, z):
    a, ap, app = map(float, jet)
    zp = math.sqrt(1-ap*ap)
    return np.array([[a, 0., z], [ap, 0., zp], [app, 0., -ap*app/zp]])


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--profile', type=Path, required=True)
    p.add_argument('--endpoint', type=Path, required=True)
    p.add_argument('--port', type=Path, required=True)
    p.add_argument('--out', type=Path, required=True)
    a = p.parse_args()
    profile, endpoint, port = read(a.profile), read(a.endpoint), read(a.port)
    g, row = profile['geometry'], endpoint['row']
    if g != endpoint['fixed_metric_profile'] or endpoint['reached_s'] != g['knots'][-1]['s']:
        raise ValueError('The actual endpoint and complete fixed scalar profile differ')
    last = g['knots'][-1]
    incoming = tuple(last[k] for k in ('a', 'ap', 'app'))
    if incoming != tuple(row[k] for k in ('a', 'ap', 'app')):
        raise ValueError('Endpoint physical scalar jets differ')
    path = Path(__file__).with_name('alternative-neck-provider.py')
    spec = importlib.util.spec_from_file_location('large_core_connector_provider', path)
    provider = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(provider)
    # This is exactly A's physical infinite tail; only its unchanged finite
    # connector is selected explicitly with the already used K=7.5 design.
    tagged = provider.tagged_port(port, dict(loop_radius=.35, loop_speed=.985,
        loop_curvature=7.5, terminal_peak_fraction=.1))
    bridge = provider.NeckTerminalBridge(tagged['cut'])
    k0 = -incoming[2]/math.sqrt(1-incoming[1]**2)
    results = []
    for K in (k0, 2.5, 3.):
        c = AngleConnector(incoming, K)
        fine = AngleConnector(incoming, K, quadrature=80)
        coast_length = (c.end_radius-.35)/.985
        if coast_length <= 0:
            raise ValueError('The full scalar extension has a negative coast')
        u = np.linspace(0, 1, 2001)
        cr, cv, ca = c.profile(c.length*u)
        cz = row['height_mean']+c.height_at(c.length*u)
        coast_z0 = row['height_mean']+c.height
        coast_height = coast_length*math.sqrt(1-.985**2)
        coast_z1 = coast_z0+coast_height
        end_jet = np.array([float(z) for z in c.profile(c.length)])
        bridge_start = np.array([float(z[0]) for z in bridge.profile(0.)])
        bridge_end = np.array([float(z[0]) for z in bridge.profile(bridge.end)])
        tail_jet = np.array([tagged['cut']['radius'],
            -1/math.sqrt(tagged['cut']['E']),
            -tagged['cut']['Ep']/(2*tagged['cut']['E']**2)])
        jumps = [
            xyz_jet(c.profile(0.), row['height_mean'])-xyz_jet(incoming, row['height_mean']),
            xyz_jet(end_jet, coast_z0)-xyz_jet((c.end_radius, -.985, 0.), coast_z0),
            xyz_jet((.35, -.985, 0.), coast_z1)-xyz_jet(bridge_start, coast_z1),
            xyz_jet(bridge_end, coast_z1+bridge.height)-xyz_jet(tail_jet, coast_z1+bridge.height),
        ]
        for left, right in zip(bridge.segments[:-1], bridge.segments[1:]):
            jumps.append(xyz_jet(provider.piece_jet(left, 1.), coast_z1+left['h1'])-
                         xyz_jet(provider.piece_jet(right, 0.), coast_z1+right['h0']))
        error = max(float(abs(j).max()) for j in jumps)
        if error > 5e-12:
            raise ValueError('A complete scalar/background Cartesian C2 join failed')
        bs = np.linspace(0, bridge.end, 401)
        ba, bap, bapp = bridge.profile(bs)
        # Original bridge height is integrated piece by piece on the same
        # scalar geometry. This still is not a nonaxisymmetric mean height.
        bz = np.zeros_like(bs)
        for seg in bridge.segments:
            ix = bs >= seg['s0']
            uu = np.clip((bs[ix]-seg['s0'])/seg['length'], 0., 1.)
            bz[ix] = seg['h0']+seg['length']*provider.fl.integral(seg, uu, 'cos')
        bz += coast_z1
        norms = np.r_[np.sqrt(cr*cr+cz*cz),
            np.hypot(np.linspace(c.end_radius,.35,201), np.linspace(coast_z0,coast_z1,201)),
            np.sqrt(ba*ba+bz*bz)]
        results.append(dict(peak_turn_curvature=K, incoming_turn_curvature=k0,
            ramp_in=.08, ramp_out=.08, turn_length=c.length,
            turn_radius_end=c.end_radius, turn_height=c.height,
            coast_length=coast_length, coast_height=coast_height,
            bridge_length=bridge.end, bridge_height=bridge.height,
            physical_cut_s=endpoint['reached_s']+c.length+coast_length+bridge.end,
            mean_anchored_background_cut_height=coast_z1+bridge.height,
            scalar_min_radius=float(min(cr.min(), ba.min(), .35)),
            scalar_max_abs_ap=float(max(abs(cv).max(), abs(bap).max(), .985)),
            added_axisymmetric_background_kappa_sample=float(max(
                np.max(np.maximum(abs(ca)/np.sqrt(1-cv*cv), np.sqrt(1-cv*cv)/cr)),
                bridge.summary()['background_kappa_sample'])),
            mean_anchored_extension_radial_norm_max=float(norms.max()),
            extension_reflection_D_proxy=float(2*norms.max()),
            incoming_endpoint_ball_norm=float(row['ball_radius_max']),
            max_scalar_and_background_XYZ_012_join_error=error,
            all_join_matrices=[j.tolist() for j in jumps],
            quadrature48to80_max_radius_height_difference=float(max(
                abs(np.array(c.profile(c.length*u)[0])-np.array(fine.profile(fine.length*u)[0])).max(),
                abs(c.height_at(c.length*u)-fine.height_at(fine.length*u)).max())),
            physical_tail_cut_and_parameters_unchanged=True,
            current_nonaxis_endpoint_was_not_replaced_by_a_circle=True,
            only_new_scalar_profile_was_computed=True))
    record = dict(scope=__doc__, schema='large-core-C2-to-original-tail-profile-v1',
        source_sha256=sha(__file__), provider_sha256=sha(path),
        inputs=[dict(file=str(q),sha256=sha(q)) for q in (a.profile,a.endpoint,a.port)],
        complete_original_fixed_prefix_geometry=g, original_endpoint_s=endpoint['reached_s'],
        original_endpoint_scalar_jet=list(incoming),
        original_endpoint_nonaxis_mean_height=row['height_mean'],
        original_endpoint_nonaxis_height_range=[row['height_min'],row['height_max']],
        physical_tail_parameters=port['parameters'], physical_tail_cut=tagged['cut'],
        results=results,
        limitations=['No Frenet flow has been evaluated on these added segments.',
            'Background norm and mean-anchored height are design proxies, not actual D or G.',
            'The nonaxisymmetric Cartesian 0/1/2 interface still requires an actual global solution.',
            'No tail solve, closed assembly, nonlocal reach, or final criterion is claimed.'])
    a.out.parent.mkdir(parents=True,exist_ok=True)
    a.out.write_text(json.dumps(record,indent=2)+'\n')
    print(json.dumps(dict(out=str(a.out),results=[{k:r[k] for k in
        ('peak_turn_curvature','physical_cut_s','mean_anchored_background_cut_height',
         'extension_reflection_D_proxy','max_scalar_and_background_XYZ_012_join_error',
         'quadrature48to80_max_radius_height_difference')} for r in results])))


if __name__ == '__main__':
    main()
