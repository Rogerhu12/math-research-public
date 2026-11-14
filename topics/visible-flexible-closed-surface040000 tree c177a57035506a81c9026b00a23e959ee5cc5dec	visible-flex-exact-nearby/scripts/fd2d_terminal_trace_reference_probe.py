#!/usr/bin/env python3
"""Two explicit positive-Gauss terminal references on one actual tail input.

Finite pointwise comparison only. No BVP, body, new metric, or acceptance
decision; both references retain their actual nonzero Codazzi residual.
"""
import os
for key in ('OPENBLAS_NUM_THREADS', 'OMP_NUM_THREADS', 'MKL_NUM_THREADS'):
    os.environ[key] = '1'
import argparse
import hashlib
import json
import resource
import time
from pathlib import Path
import numpy as np
from fd2d_positive_flat_developable_family import PositiveFlatDevelopableFamily
from fd2d_gc_raw_native_field import curvature_second_y


def identity(path):
    path = Path(path)
    body = path.read_bytes()
    return dict(path=str(path.resolve()), bytes=len(body),
                sha256=hashlib.sha256(body).hexdigest())


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--input', type=Path, required=True)
    parser.add_argument('--candidate', type=Path, required=True)
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args()
    started = time.monotonic()
    input_identity = identity(args.input)
    with np.load(args.input, allow_pickle=False) as state:
        parameters = state['parameters'].copy()
        assert parameters.shape == (38,)
        tail_controls = parameters[15:31]
    data = json.loads(args.candidate.read_text())
    piece = data['segments'][-1]
    assert piece['kind'] == 'phase_bridge' and piece['label'] == 'cut_second_jet_brake'
    assert piece['exact_endpoint_phase'] == '-pi/2'
    L, D, ac = float(piece['L']), np.pi/2+float(piece['p0']), .8
    assert .0259 < L < .0261 and 0 < D < .125
    assert np.all((tail_controls >= 0) & (tail_controls <= 1.2))
    tail = PositiveFlatDevelopableFamily(tail_controls)
    u = 2*np.pi*np.arange(1024)/1024
    su, cu = np.sin(u), np.cos(u)
    curve = tail.curve(ac*su, integrate=False)
    k, ky = curve['kappa'], curve['kappa_y']
    kyy = curvature_second_y(tail, ac*su, 'positive_bernstein')
    ku, kuu = ky*ac*cu, kyy*(ac*cu)**2-ky*ac*su
    dT, m = k*np.cos(2*u), -.5*k*np.sin(2*u)
    du = ku*np.cos(2*u)-2*k*np.sin(2*u)
    duu = kuu*np.cos(2*u)-4*ku*np.sin(2*u)-4*k*np.cos(2*u)
    mu = -.5*ku*np.sin(2*u)-k*np.cos(2*u)
    muu = -.5*kuu*np.sin(2*u)-2*ku*np.cos(2*u)+2*k*np.sin(2*u)
    radii = np.unique(np.r_[np.geomspace(1e-10, .02, 48), np.linspace(.0005, .02, 40)])
    nodes, weights = np.polynomial.legendre.leggauss(40)
    result = {}
    for kind in ('tail_plus_isotropic', 'round_anisotropy_plus_tail'):
        maximum = {name:0. for name in ('Gauss', 'Codazzi_n', 'Codazzi_m',
                   'principal_curvature', 'flat_arc_Codazzi_n', 'flat_arc_Codazzi_m',
                   'trace_endpoint_bound_excess')}
        minimum_ratio = float('inf')
        witnesses = {}
        for r in radii:
            z = r*(nodes+1)/2
            epsq = D*(3*(z/L)**2-2*(z/L)**3)
            a = ac+r/2*np.dot(weights, np.cos(epsq))
            eps = D*(3*(r/L)**2-2*(r/L)**3)
            lr = 6*D*r/L**2*(1-r/L)
            lr_s = -6*D/L**2*(1-2*r/L)
            nr = np.sin(eps)/a
            nr_s = -np.cos(eps)*(lr-nr)/a
            K, Ks, c = nr*lr, nr_s*lr+nr*lr_s, -np.cos(eps)/a
            d = dT+(nr-lr if kind == 'round_anisotropy_plus_tail' else 0.)
            ds = nr_s-lr_s if kind == 'round_anisotropy_plus_tail' else 0.
            h = np.hypot(d, np.hypot(2*m, 2*np.sqrt(K)))
            hu = (d*du+4*m*mu)/h
            huu = (du*du+d*duu+4*mu*mu+4*m*muu-hu*hu)/h
            hs = (d*ds+2*Ks)/h
            # Stable eigenvalue-side evaluations; no small-difference loss.
            n = np.where(d >= 0, (h+d)/2, 2*(m*m+K)/(h-d))
            ell = np.where(d <= 0, (h-d)/2, 2*(m*m+K)/(h+d))
            ns, lu = (hs+ds)/2, (hu-du)/2
            gauss = n*ell-m*m-K
            rn, rm = ns-mu/a-c*(ell-n), -lu/a+2*c*m
            curvature = (h+np.hypot(d,2*m))/2
            flat = np.abs(ac*su) < .34
            values = dict(Gauss=np.abs(gauss), Codazzi_n=np.abs(rn),
                Codazzi_m=np.abs(rm), principal_curvature=curvature,
                flat_arc_Codazzi_n=np.abs(rn[flat]),
                flat_arc_Codazzi_m=np.abs(rm[flat]),
                trace_endpoint_bound_excess=np.maximum(np.abs(h-k)-(nr+lr),0.)
                    if kind == 'round_anisotropy_plus_tail' else np.zeros_like(h))
            for name, value in values.items():
                local = float(np.max(value))
                if local > maximum[name]:
                    maximum[name] = local
                    if value.shape == u.shape:
                        index = int(np.argmax(value))
                        witnesses[name] = dict(r=float(r), u=float(u[index]),
                            n=float(n[index]), m=float(m[index]), l=float(ell[index]),
                            K=float(K), k_tail=float(k[index]))
            ratio = h/(k+nr+lr)
            minimum_ratio = min(minimum_ratio, float(np.min(ratio)))
            assert np.all(np.isfinite(huu))
        result[kind] = dict(sampled_maxima=maximum,
            min_sampled_h_over_k_plus_round_trace=minimum_ratio,
            witnesses=witnesses)
    assert identity(args.input) == input_identity
    report = dict(schema='fd2d-terminal-positive-trace-reference-comparison-v1',
        input=input_identity, candidate=identity(args.candidate), source=identity(__file__),
        radial_samples=len(radii), angular_samples=len(u), tail_controls=tail_controls.tolist(),
        constants=dict(L=L,D=D,a_cut=ac,leading_K_over_r3=18*D*D/(ac*L**4)),
        results=result, seconds=time.monotonic()-started,
        peak_rss_kib=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,
        pointwise_finite_comparison_only=True, nonlinear_solve=False,
        body_integration=False, input_modified=False,
        proof_references=['R156','R157'])
    args.output.write_text(json.dumps(report, indent=2)+'\n')
    print(json.dumps({key:value['sampled_maxima'] for key,value in result.items()}))


if __name__ == '__main__':
    main()
