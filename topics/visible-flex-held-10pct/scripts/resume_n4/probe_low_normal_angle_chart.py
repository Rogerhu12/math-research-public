#!/usr/bin/env python3
"""Read-only low-harmonic angle filters of one complete n4 core.

The recorded chart and the complete physical core stay unchanged. Candidate
angle coefficients are literal numerical choices, not asserted exact moments.
No finite BVP or tail is solved in a proposed chart.
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
from probe_full_core_normal_chart import circle_jets, spectrum, sha


def main():
    p = argparse.ArgumentParser(description=__doc__)
    for key in ('source-topic', 'checkpoint', 'out'):
        p.add_argument('--' + key, type=Path, required=True)
    p.add_argument('--samples', type=int, default=8192)
    a = p.parse_args()
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
    q, controls = obj.support_amplitude, obj.pscale * par[1:]
    Core = make_core_class(ReferenceCore, seed['core_projection_order'])
    flow = obj.flow(par[0])
    N = a.samples
    psi = 2*np.pi*np.arange(N)/N
    frequency = abs(np.rint(np.fft.fftfreq(N)*N).astype(int))
    number = 4*np.arange(1,9)
    sn, co = np.sin(psi[:,None]*number), np.cos(psi[:,None]*number)
    result = dict(scope=__doc__, command=sys.argv, script_sha256=sha(__file__),
                  source_root=str(Path(__file__).parent.resolve()),
                  helper_sha256=sha(Path(__file__).with_name('probe_full_core_normal_chart.py')),
                  input_checkpoint_sha256=sha(a.checkpoint), actual_q=q, gauge_q=obj.q,
                  physical_control_sha256=hashlib.sha256(
                      np.asarray(controls, '<f8').tobytes()).hexdigest(),
                  settings=seed['settings'], samples=N, rows=[])
    started = time.monotonic()
    for lam in [seed['settings']['homotopy'], 1.]:
        core = Core(q,controls,4,arc_nodes=2048,**dict(seed['settings'],homotopy=lam))
        rho = core.normal_geometry(psi)['rho']
        coefficient = 2/N*((rho-1)@co)
        original = np.zeros(8)
        original[:2] = [-flow.warp_e*(1+seed['eta']),flow.warp_e*seed['eta']]
        cases = [('original',original)]
        for K in [1,2,4,8]:
            b = coefficient.copy()
            b[K:] = 0
            cases.append(('filtered_'+str(K),b))
        for label,b in cases:
            u = psi+sn@(b/number)
            du = 1+co@b
            ddu = -(sn@(number*b))
            lower = float(np.nextafter(1-sum(abs(b)), -np.inf))
            if lower <= 0:
                raise ValueError('Candidate has no simple positive derivative certificate')
            g = core.evaluate(u)
            first = (g['F'],g['Ft']*du[:,None],
                     g['Ftt']*du[:,None]**2+g['Ft']*ddu[:,None])
            base = circle_jets(u,du,ddu)
            values = spectrum(dict(F_psipsi_perturbation=first[2]-base[2]),frequency)
            row=dict(homotopy=lam,chart=label,literal_cosine_derivative_coefficients=b.tolist(),
                     chart_derivative_triangle_lower=lower,
                     second_reference_jet=values['F_psipsi_perturbation'],
                     accepted_chart=label=='original' and lam==seed['settings']['homotopy'],
                     same_solved_core=lam==seed['settings']['homotopy'])
            result['rows'].append(row)
            print(json.dumps(row),flush=True)
    result['seconds']=time.monotonic()-started
    a.out.write_text(json.dumps(result,indent=2)+'\n')


if __name__ == '__main__':
    main()
