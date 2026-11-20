"""Finite core-only diagnostics for the material-curvature family.

All reported Fourier tails are finite sampled diagnostics, not bounds on an
infinite tail.  The held ratios are conditional on a complete surface with
the declared D budget.  No BVP or complete-surface validation is performed.
"""
import argparse
import hashlib
import json
import math
from pathlib import Path
import time

import numpy as np

from material_curvature_core import MaterialCurvatureCore


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def diagnostics(n, material_halfwidth, transition, kappa, nodes, diameter):
    q = (1-kappa)/(n*n-1)
    core = MaterialCurvatureCore(q=q, base_mode=n, halfwidth=material_halfwidth,
                                 transition=transition, arc_nodes=1024)
    theta = 2*np.pi*np.arange(nodes)/nodes
    g = core.evaluate(theta)
    circle = np.c_[np.cos(theta), np.sin(theta), np.zeros(nodes)]
    diff2 = g['Ftt']+circle
    spectrum = np.fft.fft(diff2, axis=0)/nodes
    frequency = np.abs(np.fft.fftfreq(nodes)*nodes)
    tail = {str(M): float(np.linalg.norm(spectrum[frequency > n*M+1], axis=1).sum())
            for M in (8, 12, 16, 24, 32, 48, 64)}
    normals = np.c_[np.cos(g['phi']), np.sin(g['phi']), np.zeros(nodes)]
    support = np.sum(g['F']*normals, axis=1)
    support_Q = float(2*np.mean(support*np.cos(n*g['phi'])*g['kappa']))
    support_coefficients = [float(2*np.mean(support*np.cos(n*j*g['phi'])*g['kappa']))
                            for j in range(1, 9)]
    center = np.asarray(core.summary()['circle_center'])
    cc = float(np.linalg.norm(center))
    alpha = 2*(material_halfwidth-1e-4)
    factor = math.sqrt(3) if n == 3 else 2.
    held = factor*cc*math.sin(kappa*alpha/2)
    # Same physical core, different declared quadrature resolution.
    refined = MaterialCurvatureCore(q=q, base_mode=n, halfwidth=material_halfwidth,
                                    transition=transition, arc_nodes=128,
                                    quadrature_order=24, integration_cells=96)
    probe = theta[::max(1, nodes//1000)]
    a, b = core.evaluate(probe), refined.evaluate(probe)
    refinement = {key: float(np.max(abs(a[key]-b[key]))) for key in ('F', 'Ft', 'Ftt')}
    return dict(n=n, q_curvature_parameter=q, target_kappa=kappa,
                material_halfwidth=material_halfwidth, transition=transition,
                core_summary=core.summary(), support_Q_sample=support_Q,
                support_cosine_coefficients_sample=support_coefficients,
                support_range_sample=[float(support.min()), float(support.max())],
                radial_perturbation_sample=float(np.max(np.linalg.norm(g['F']-circle, axis=1))),
                material_second_jet_sampled_tail_l1=tail,
                conditional_held=held, conditional_held_over_D=held/diameter,
                assumed_complete_D=diameter, phase_range=[0., alpha],
                same_physical_core_quadrature_difference=refinement,
                metric_identity_sample=float(np.max(abs(np.sum(g['Ft']**2, axis=1)-1))))


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--out', required=True)
    parser.add_argument('--nodes', type=int, default=16384)
    parser.add_argument('--diameter', type=float, default=2.65)
    args = parser.parse_args()
    records = []
    start = time.time()
    for n in (3, 4):
        for halfwidth, transition in ((.18, .25), (.20, .25), (.20, .40), (.23, .30)):
            for kappa in (.5, .3, .2, .1):
                row = diagnostics(n, halfwidth, transition, kappa, args.nodes, args.diameter)
                records.append(row)
                print(json.dumps(dict(n=n, S=halfwidth, transition=transition, kappa=kappa,
                                      Q=row['support_Q_sample'], held_D=row['conditional_held_over_D'],
                                      M16=row['material_second_jet_sampled_tail_l1']['16'],
                                      M32=row['material_second_jet_sampled_tail_l1']['32'])), flush=True)
    out = dict(scope='New physical core designs only; no BVP, complete geometry or infinite-spectrum certificate',
               nodes=args.nodes, seconds=time.time()-start,
               source_sha256={p.name: sha(p) for p in (Path(__file__), Path(__file__).with_name('material_curvature_core.py'))},
               records=records)
    Path(args.out).parent.mkdir(parents=True, exist_ok=True)
    Path(args.out).write_text(json.dumps(out, indent=2)+'\n')


if __name__ == '__main__':
    main()
