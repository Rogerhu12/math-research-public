#!/usr/bin/env python3
"""Read-only spectra of the same complete core in three numerical angle charts.

The original chart is compared with material angle and a frozen exact
normal-angle chart u=arc_core(psi). No BVP, geometry, tail, or acceptance gate
is changed. The lambda-one row is an unsolved candidate with the same actual
physical controls. Fourier tails are sampled diagnostics, not certificates.
"""
import os
for key in ('OPENBLAS_NUM_THREADS', 'OMP_NUM_THREADS', 'MKL_NUM_THREADS'):
    os.environ[key] = '1'
import argparse
import hashlib
import json
from pathlib import Path
import sys
import time
import numpy as np


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def curve_normal_jets(core, phi):
    ng = core.normal_geometry(phi)
    # Independently evaluated material jets provide the same normal angle.
    material = core.rho_material_jets(core.arc(phi))
    inverse_error = float(abs(material['phi'] - phi).max())
    rho = ng['rho']
    rp = material['rho_phi']
    return (ng['F'], rho[:, None] * ng['et'],
            rp[:, None] * ng['et'] - rho[:, None] * ng['er']), rho, rp, inverse_error


def circle_jets(u, du, ddu):
    er = np.c_[np.cos(u), np.sin(u), np.zeros(len(u))]
    et = np.c_[-np.sin(u), np.cos(u), np.zeros(len(u))]
    return er, du[:, None] * et, ddu[:, None] * et - du[:, None] ** 2 * er


def spectrum(fields, freq):
    out = {}
    for name, field in fields.items():
        c = np.fft.fft(field, axis=0) / len(freq)
        mag = np.linalg.norm(c, axis=1)
        out[name] = {str(M): float(mag[freq > 4 * M + 1].sum())
                     for M in (16, 20, 24, 32)}
        out[name]['above_N_over_4'] = float(mag[freq > len(freq) // 4].sum())
    return out


def main():
    p = argparse.ArgumentParser(description=__doc__)
    for key in ('source-topic', 'checkpoint', 'out'):
        p.add_argument('--' + key, type=Path, required=True)
    p.add_argument('--samples', type=int, default=8192)
    a = p.parse_args()
    sys.path.insert(0, str(Path(__file__).parent))
    from refine_fixed_raw_n4 import build_seed
    from raw_fixed_core import make_core_class
    from run_large_radius_circle import ReferenceCore
    source = a.source_topic.resolve()
    sys.path[:0] = [str(source / 'notes'), str(
        source / 'repro/source-root/topics/large-amplitude-twist-flex/scripts')]
    from curve_stable_prefix_bvp import load_checkpoint
    rec = load_checkpoint(a.checkpoint)
    seed = build_seed(source, a.checkpoint, rec['config']['modes'], rec['config']['angular'])
    obj, par = seed['obj'], seed['par']
    obj.initial(par)
    flow = obj.flow(par[0])
    q, controls = obj.support_amplitude, obj.pscale * par[1:]
    Core = make_core_class(ReferenceCore, seed['core_projection_order'])
    N = a.samples
    angle = flow.angular(N)
    psi = angle[0]
    freq = abs(np.rint(np.fft.fftfreq(N) * N).astype(int))
    result = dict(scope=__doc__, command=sys.argv,
                  input_checkpoint_sha256=sha(a.checkpoint),
                  script_sha256=sha(__file__),
                  source_root=str(Path(__file__).parent.resolve()),
                  source_sha256={name: sha(Path(__file__).with_name(name))
                                 for name in ('refine_fixed_raw_n4.py',
                                              'refine_fixed_large_radius.py',
                                              'raw_fixed_core.py',
                                              'raw_n4_free_complementary.py',
                                              'raw_n4_complementary.py',
                                              'large_radius_local_core.py',
                                              'bimodal_chart_loader.py')},
                  actual_q=q, gauge_q=obj.q, controls=len(controls),
                  physical_control_sha256=hashlib.sha256(
                      np.asarray(controls, '<f8').tobytes()).hexdigest(),
                  settings=seed['settings'], physical_profile=seed['cfg'],
                  samples=N, original_chart_warp_e=flow.warp_e, rows=[])
    began = time.monotonic()
    for lam in [seed['settings']['homotopy'], 1.]:
        settings = dict(seed['settings'], homotopy=lam)
        core = Core(q, controls, 4, arc_nodes=2048, **settings)
        normal, rho, rp, inverse_error = curve_normal_jets(core, psi)
        for chart in ('original_bimodal', 'material', 'frozen_full_normal'):
            if chart == 'original_bimodal':
                u, du, ddu = angle[1:4]
            elif chart == 'material':
                u, du, ddu = psi, np.ones_like(psi), np.zeros_like(psi)
            else:
                u, du, ddu = core.arc(psi), rho, rp
            m = core.evaluate(u)
            complete = (m['F'], m['Ft'] * du[:, None],
                        m['Ftt'] * du[:, None] ** 2 + m['Ft'] * ddu[:, None])
            base = circle_jets(u, du, ddu)
            perturbation = tuple(v - b for v, b in zip(complete, base))
            row = dict(homotopy=lam, chart=chart,
                       same_solved_core=(lam == seed['settings']['homotopy']),
                       solved_chart=(lam == seed['settings']['homotopy']
                                     and chart == 'original_bimodal'),
                       minimum_sampled_du=float(du.min()),
                       maximum_sampled_du=float(du.max()),
                       core_rho_lower=core.rho_lower,
                       spectra=spectrum(
                           dict(F=complete[0], F_psipsi=complete[2],
                                F_perturbation=perturbation[0],
                                F_psipsi_perturbation=perturbation[2]), freq))
            if chart == 'frozen_full_normal':
                row['direct_normal_chain_identity'] = {
                    name: float(abs(direct - transformed).max())
                    for name, direct, transformed in
                    zip(('F', 'F_psi', 'F_psipsi'), normal, complete)}
                row['normal_arc_inverse_error'] = inverse_error
            result['rows'].append(row)
            print(json.dumps(row), flush=True)
        # Check the frozen spatial chart jets independently of a solver.
        # theta = psi + c(s)D(psi), D=arc(psi)-psi, with the old C2 end fade.
        length = flow.end
        sample_phi = np.linspace(.013, 2*np.pi-.019, 73)
        _, local_rho, local_rp, _ = curve_normal_jets(core, sample_phi)
        D = core.arc(sample_phi) - sample_phi
        xx = .82
        z = (xx-.75)/.25
        c = 1-z**3*(10-15*z+6*z*z)
        cp = -30*z*z*(1-z)**2/(.25*length)
        cpp = -60*z*(1-z)*(1-2*z)/(.25*length)**2
        theta = sample_phi+c*D
        theta_s, theta_ss = cp*D, cpp*D
        theta_p = 1+c*(local_rho-1)
        theta_pp = c*local_rp
        theta_sp, theta_spp = cp*(local_rho-1), cp*local_rp
        chart_data = dict(
            homotopy=lam,
            analytic_continuous_du_lower=min(1., core.rho_lower),
            identity_at_cut_through_second_order=True,
            theta_s_max=float(abs(theta_s).max()),
            theta_ss_max=float(abs(theta_ss).max()),
            theta_p_min=float(theta_p.min()),
            theta_pp_max=float(abs(theta_pp).max()),
            theta_sp_max=float(abs(theta_sp).max()),
            theta_spp_max=float(abs(theta_spp).max()),
            scope='Exact chain formulas for the proposed frozen chart; no flow or BVP executed.')
        result.setdefault('spatial_chain', []).append(chart_data)
    result['seconds'] = time.monotonic() - began
    a.out.write_text(json.dumps(result, indent=2) + '\n')


if __name__ == '__main__':
    main()
