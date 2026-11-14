#!/usr/bin/env python3
"""An explicit C2 core-to-tail material chart and actual accepted-field probes.

The chart changes representation of the same physical metric. Projection of
the transformed finite field is measured, never called an exact seam. The
full tail problem must use an identity chart at its actual cut and retain the
complete physical tail solve, means, reflection and Cartesian jet audit.
"""
import os
for name in ('OPENBLAS_NUM_THREADS', 'OMP_NUM_THREADS', 'MKL_NUM_THREADS'):
    os.environ[name] = '1'
import argparse
import hashlib
import importlib.util
import json
from pathlib import Path
import numpy as np

P = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location('adaptive_material_reader', P/'geometry_20261114_material_quintic_readout.py')
reader = importlib.util.module_from_spec(spec)
spec.loader.exec_module(reader)
base = reader.base


class QuinticMaterialChart:
    def __init__(self, start, end):
        self.start, self.end = float(start), float(end)
        if not self.end > self.start:
            raise ValueError('A nonempty physical transition interval is required')

    def taper(self, s):
        s = np.asarray(s)
        length = self.end-self.start
        u = np.clip((s-self.start)/length, 0, 1)
        b = 1-10*u**3+15*u**4-6*u**5
        bp = (-30*u**2+60*u**3-30*u**4)/length
        bpp = (-60*u+180*u**2-120*u**3)/length**2
        return b, bp, bpp

    def angle(self, s, psi, coefficients):
        c = np.asarray(coefficients)
        freq = 2*np.arange(1, len(c)+1)
        density = (1-freq*freq)*c
        arg = freq[:, None]*np.asarray(psi)
        Q = (density/freq)@np.sin(arg)
        Qp = density@np.cos(arg)
        Qpp = -(freq*density)@np.sin(arg)
        b, bp, bpp = self.taper(s)
        theta = psi+b*Q
        rho = 1+b*Qp
        rho_p = b*Qpp
        theta_s, theta_ss = bp*Q, bpp*Q
        rho_s = bp*Qp
        v = theta_s/rho
        vp = (rho_s*rho-theta_s*rho_p)/rho**2
        vs = (theta_ss*rho-theta_s*rho_s)/rho**2
        return dict(theta=theta, rho=rho, rho_p=rho_p, theta_s=theta_s,
                    theta_ss=theta_ss, rho_s=rho_s, v=v, vp=vp, vs=vs,
                    b=float(b), bp=float(bp), bpp=float(bpp))

    def rhs(self, q, s, state, coefficients, strict=True):
        frame = q.frame(s, state, strict=strict)
        chart = self.angle(s, q.phi, coefficients)
        if strict and np.min(chart['rho'].real) <= 0:
            raise FloatingPointError('The adaptive material chart is not invertible')
        return q.project(frame['V']+chart['v'][:, None]*frame['d'])


def inverse_core_angle(theta, coefficients):
    c = np.asarray(coefficients)
    freq = 2*np.arange(1, len(c)+1)
    density = (1-freq*freq)*c
    phi = np.asarray(theta).copy()
    low, high = np.zeros_like(phi), np.full_like(phi, 2*np.pi)
    for iteration in range(80):
        arg = freq[:, None]*phi
        rho = 1+density@np.cos(arg)
        value = phi+(density/freq)@np.sin(arg)
        error = value-theta
        active = abs(error) > 2e-14
        if not np.any(active):
            return phi, rho, -(freq*density)@np.sin(arg), float(abs(error).max())
        low = np.where(active & (error < 0), phi, low)
        high = np.where(active & (error > 0), phi, high)
        proposed = phi-error/rho
        bad = (proposed <= low) | (proposed >= high) | ~np.isfinite(proposed)
        phi = np.where(active, np.where(bad, (low+high)/2, proposed), phi)
    raise RuntimeError('Core material-angle inversion did not converge')


def rotate_polar(values, difference):
    c, s = np.cos(difference), np.sin(difference)
    return np.stack([c*values[..., 0]-s*values[..., 1],
                     s*values[..., 0]+c*values[..., 1], values[..., 2]], axis=-1)


def pullback_jet(y, dy, ddy, coefficients, chart, s, psi):
    info = chart.angle(s, psi, coefficients)
    phi, rho0, rho0p, residual = inverse_core_angle(info['theta'], coefficients)
    values, angular, angular2 = reader.angular_jet(None, len(coefficients), phi)(np.array([y, dy, ddy]))
    F, Fs, Fss = values
    Fp, Fsp = angular[:2]
    Fpp = angular2[0]
    eta_p = info['rho']/rho0
    eta_s = info['theta_s']/rho0
    eta_pp = (info['rho_p']-rho0p*eta_p**2)/rho0
    eta_sp = (info['rho_s']-rho0p*eta_s*eta_p)/rho0
    eta_ss = (info['theta_ss']-rho0p*eta_s**2)/rho0
    new = dict(position=F,
               s1=Fs+Fp*eta_s[:, None],
               s2=Fss+2*Fsp*eta_s[:, None]+Fpp*eta_s[:, None]**2+Fp*eta_ss[:, None],
               p1=Fp*eta_p[:, None],
               p2=Fpp*eta_p[:, None]**2+Fp*eta_pp[:, None],
               sp=Fsp*eta_p[:, None]+Fpp*(eta_s*eta_p)[:, None]+Fp*eta_sp[:, None])
    new = {key: rotate_polar(value, phi-psi) for key, value in new.items()}
    old_physical = rotate_polar(Fs, phi-psi)
    physical = new['s1']-info['v'][:, None]*new['p1']
    info['inversion_residual'] = residual
    info['physical_s_chain_rule_max'] = float(np.max(abs(physical-old_physical)))
    return new, info


def project(values, M):
    N = len(values)
    modes = 2*np.arange(M+1)
    fourier = np.fft.rfft(values, axis=0)
    rr = 2/N*fourier[modes, 0].real
    rr[0] *= .5
    tt = -2/N*fourier[modes[1:], 1].imag
    zz = 2/N*fourier[modes, 2].real
    zz[0] *= .5
    return np.r_[rr, tt, zz]


def metric(Fs, Fp, a, chart):
    physical_s = Fs-chart['v'][:, None]*Fp
    physical_theta = Fp/chart['rho'][:, None]
    E = np.sum(physical_s*physical_s, axis=-1)
    FF = np.sum(physical_s*physical_theta, axis=-1)
    G = np.sum(physical_theta*physical_theta, axis=-1)
    return float(max(abs(E-1).max(), abs(FF/a).max(), abs(G/(a*a)-1).max()))


def uniform_jet(coefficients, M, N):
    """The same polar Fourier field, evaluated on a uniform grid with FFTs."""
    rows = len(coefficients)
    modes = 2*np.arange(M+1)
    spectrum = np.zeros((rows, 3, N//2+1), complex)
    spectrum[:, 0, modes] = N/2*coefficients[:, :M+1]
    spectrum[:, 0, 0] *= 2
    spectrum[:, 1, modes[1:]] = -1j*N/2*coefficients[:, M+1:2*M+1]
    spectrum[:, 2, modes] = N/2*coefficients[:, 2*M+1:]
    spectrum[:, 2, 0] *= 2
    frequency = np.arange(N//2+1)
    value = np.fft.irfft(spectrum, n=N, axis=-1).transpose(0, 2, 1)
    first = np.fft.irfft(spectrum*(1j*frequency), n=N, axis=-1).transpose(0, 2, 1)
    second = np.fft.irfft(spectrum*(-frequency*frequency), n=N, axis=-1).transpose(0, 2, 1)
    d = np.stack([first[..., 0]-value[..., 1], first[..., 1]+value[..., 0], first[..., 2]], axis=-1)
    dd = np.stack([second[..., 0]-2*first[..., 1]-value[..., 0],
                   second[..., 1]+2*first[..., 0]-value[..., 1], second[..., 2]], axis=-1)
    return value, d, dd


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--input', type=Path, required=True)
    p.add_argument('--second-jets', type=Path, required=True)
    p.add_argument('--transition-start', type=float, default=.984)
    p.add_argument('--transition-end', type=float, default=2.32948)
    p.add_argument('--angular', type=int, default=2048)
    p.add_argument('--modes', type=int, nargs='+', default=[96, 128, 192])
    p.add_argument('--fractions', type=float, nargs='+', default=[0., .25, .5, .75, 1.])
    p.add_argument('--out', type=Path, required=True)
    args = p.parse_args()
    data = base.fixed.read(args.input)
    jets = base.fixed.read(args.second_jets)
    sha = hashlib.sha256(args.input.read_bytes()).hexdigest()
    if jets['accepted_input_sha256'] != sha:
        raise ValueError('The second jets belong to a different accepted field')
    if not data['success']:
        raise ValueError('Use an actually accepted complete finite prefix')
    M = data['M']
    c = np.array(data['core']['coefficients'])
    chart = QuinticMaterialChart(args.transition_start, args.transition_end)
    scalar = base.fixed.FixedProfile(data['fixed_scalar_profile']['geometry'])
    actual_s = data['mesh'][-1]
    a, ap, app = scalar.profile(actual_s)
    psi = 2*np.pi*np.arange(args.angular)/args.angular
    y, dy, ddy = data['states'][-1], data['rhs'][-1], jets['second_jets_binary64'][-1]
    probes = []
    for fraction in args.fractions:
        if not 0 <= fraction <= 1:
            raise ValueError('A chart probe fraction must lie in [0,1]')
        station = chart.start+fraction*(chart.end-chart.start)
        exact, info = pullback_jet(y, dy, ddy, c, chart, station, psi)
        levels = []
        for modes in args.modes:
            coefficients = np.array([project(exact[key], modes) for key in ('position', 's1', 's2')])
            values, first, second = uniform_jet(coefficients, modes, args.angular)
            errors = dict(position=float(np.max(np.linalg.norm(values[0]-exact['position'], axis=-1))),
                          s1=float(np.max(np.linalg.norm(values[1]-exact['s1'], axis=-1))),
                          s2=float(np.max(np.linalg.norm(values[2]-exact['s2'], axis=-1))),
                          p1=float(np.max(np.linalg.norm(first[0]-exact['p1'], axis=-1))),
                          p2=float(np.max(np.linalg.norm(second[0]-exact['p2'], axis=-1))),
                          sp=float(np.max(np.linalg.norm(first[1]-exact['sp'], axis=-1))))
            levels.append(dict(modes=modes, reconstructed_material_metric_sample=metric(values[1], first[0], a, info),
                               physical_twojet_projection_errors=errors,
                               last_height_coefficient=float(coefficients[0, -1])))
        probes.append(dict(virtual_transition_fraction=fraction, chart_station=station,
                           actual_field_station=actual_s,
                           scope='Coordinate/projection probe of the same accepted endpoint jet; no physical continuation to the chart station.',
                           taper=[info['b'], info['bp'], info['bpp']],
                           rho_min=float(info['rho'].min()),
                           inverse_residual=info['inversion_residual'],
                           exact_chain_rule_max=info['physical_s_chain_rule_max'],
                           exact_pulled_back_material_metric_sample=metric(exact['s1'], exact['p1'], a, info), levels=levels))
    report = dict(scope=__doc__, accepted_input_sha256=sha,
                  second_jets_sha256=hashlib.sha256(args.second_jets.read_bytes()).hexdigest(),
                  source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
                  angular=args.angular, complete_core_modes=M,
                  chart=dict(start=chart.start, end=chart.end,
                             b='1-10u^3+15u^4-6u^5 on u=(s-start)/(end-start), clamped to 1/0 outside.',
                             theta='psi+b(s)*sum((1-4m^2)c_m*sin(2m psi)/(2m))',
                             rhs='physical_Frenet_velocity+(theta_s/theta_psi)*F_psi',
                             positive_density_identity='theta_psi=(1-b)+b*rho_core',
                             end_identity_through_order_two=True),
                  full_tail_dimension_count=dict(physical_states=3*M+2, constant_core_states=M,
                       constant_profile_states=3, total=4*M+5,
                       left_constraints=3*M+5, right_actual_tail_constraints=M,
                       fixed_low_core_modes=3, free_high_core_modes=M-3),
                  scalar_metric_not_changed_by_chart=True,
                  full_tail_DN_evaluated=False, closed_surface=False, probes=probes)
    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text(json.dumps(report, indent=2)+'\n')
    print(json.dumps(dict(out=str(args.out),probes=[dict(fraction=r['virtual_transition_fraction'],
        exact_metric=r['exact_pulled_back_material_metric_sample'],
        levels=[dict(modes=v['modes'],metric=v['reconstructed_material_metric_sample'],
                     position=v['physical_twojet_projection_errors']['position']) for v in r['levels']]) for r in probes])), flush=True)


if __name__ == '__main__':
    main()
