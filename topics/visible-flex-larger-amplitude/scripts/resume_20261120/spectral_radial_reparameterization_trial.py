#!/usr/bin/env python3
"""One positive spectral-Lp same-image radial direction; full original rows.

Consumes the complete radial-composition evaluator and positive 3x3 Gram
blocks. This is a small mechanism trial, separate from the full-space and
coarse-QP consumers of the same Blocks/NativeLinearization interface.
"""
import argparse
import hashlib
import importlib.util
import json
from pathlib import Path
import sys
import time
import numpy as np


def sha(path): return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def load(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module; spec.loader.exec_module(module)
    return module


def make_trial(base, spectral, args):
    class SpectralTrial(base.Trial):
        def __init__(self, args):
            super().__init__(args)
            self.parameters = spectral.Parameters(p=args.p, epsilon=args.epsilon, scale=args.scale)
            self.normalization = float(self.weights.sum()*self.o.full_N)
            self.w_min = float(self.weights.min()*self.o.multiplicity.min()/self.normalization)

        @staticmethod
        def stats_init():
            state = base.Trial.stats_init()
            state['spectral_power_sum'] = 0.
            return state

        def accumulate(self, state, residual, start, moved=None):
            super().accumulate(state, residual, start, moved)
            powers = spectral.point_loss(residual, self.parameters)@self.o.multiplicity
            state['spectral_power_sum'] += float(self.weights[start:start+len(residual)]@powers)

        def finish_spectral(self, state):
            p = self.parameters; phi = state['spectral_power_sum']/self.normalization
            state.update(phi_normalized=phi, smoothed_spectral_lp=p.scale*phi**(1/p.p),
                minimum_normalized_orbit_weight=self.w_min,
                finite_max_formula_lower=float(np.sqrt(max(0., p.scale**2*(phi/2)**(1/p.k)-p.epsilon**2))),
                finite_max_formula_upper=float(np.sqrt(max(0., p.scale**2*(phi/self.w_min)**(1/p.k)-p.epsilon**2))),
                formula_evaluation_outward=False)
            return state

        def baseline_and_direction(self):
            o, p, b = self.o, self.p, self.basis
            state = self.stats_init(); normal = np.zeros((b.dimension, b.dimension)); gradient = np.zeros(b.dimension)
            min_block, max_block, base_quadratic = float('inf'), 0., 0.
            for start in range(0, o.P, o.stage_block):
                stop = min(start+o.stage_block, o.P)
                z = o.physical_jet_batch(p, start, stop)
                V, T, AA, VT = [z[k] for k in ('Fs', 'Fphi', 'Fss', 'Fsphi')]
                residual = self.relative(V, T, start)
                self.accumulate(state, residual, start)
                ar = o.a[start:stop, None]*p.rho[None]
                E, cross = o._bdot(V, V), o._bdot(V, T)
                shift = np.stack((2*o._bdot(V, AA), (o._bdot(AA, T)+o._bdot(V, VT))/ar,
                                  2*o._bdot(T, VT)/(ar*ar)), axis=-1)
                stretch = np.stack((2*E, cross/ar, np.zeros_like(E)), axis=-1)
                blocks = spectral.Blocks(residual, self.parameters)
                min_block, max_block = min(min_block, blocks.minimum_eigenweight), max(max_block, blocks.maximum_eigenweight)
                point_weights = self.weights[start:stop, None]*o.multiplicity[None]
                cc, cd, dd, gc, gd = blocks.contractions(residual, shift, stretch, point_weights)
                Y, U = self.Y[start:stop], self.U[start:stop]
                normal += Y.T@(cc[:, None]*Y)+Y.T@(cd[:, None]*U)+U.T@(cd[:, None]*Y)+U.T@(dd[:, None]*U)
                gradient += Y.T@gc+U.T@gd
                base_quadratic += float(np.sum(point_weights*np.sum(residual*blocks.apply(residual), axis=-1)))
            scale = np.sqrt(np.diag(normal))
            if np.any(scale <= 0): raise ValueError('Unsupported original radial column')
            scaled = normal/scale[:, None]/scale[None, :]
            values, vectors = np.linalg.eigh((scaled+scaled.T)/2)
            keep = values > 1e-12*values[-1]
            step = -(vectors[:, keep]@((vectors[:, keep].T@(gradient/scale))/values[keep]))/scale
            state['weighted_mean_sse'] = state['weighted_sse']/self.normalization
            self.finish_spectral(state)
            return state, step, dict(dimension=b.dimension, retained_rank=int(keep.sum()),
                normalized_gram_smallest_eigenvalue=float(values[0]), normalized_gram_largest_eigenvalue=float(values[-1]),
                block_minimum_eigenweight=min_block, block_maximum_eigenweight=max_block,
                base_frozen_quadratic=base_quadratic,
                predicted_frozen_quadratic=base_quadratic+2*float(gradient@step)+float(step@normal@step),
                actual_phi_directional_derivative=2*self.parameters.k/(self.parameters.scale**2*self.normalization)*float(gradient@step),
                frozen_quadratic_is_MM_majorant=False,
                direction_maximum_abs_coefficient=float(np.max(np.abs(step))))

        def exact_composition_trial(self, coefficients):
            return self.finish_spectral(super().exact_composition_trial(coefficients))

    return SpectralTrial(args)


def main():
    p = argparse.ArgumentParser(description=__doc__)
    for key in ('bundle', 'carrier', 'node-report', 'operator', 'batch-source', 'observed-source', 'radial-source', 'spectral-source', 'out'):
        p.add_argument('--'+key, type=Path, required=True)
    p.add_argument('--angles', type=int, default=2048)
    p.add_argument('--stage-block', type=int, default=64)
    p.add_argument('--line-trials', type=int, default=8)
    p.add_argument('--p', type=int, default=8)
    p.add_argument('--epsilon', type=float, default=.001)
    p.add_argument('--scale', type=float, default=.05)
    args = p.parse_args()
    if args.out.exists(): raise FileExistsError('Keep earlier trial results')
    np.seterr(over='raise', invalid='raise', divide='raise', under='ignore')
    start = time.monotonic()
    base = load('spectral_trial_radial_base', args.radial_source)
    spectral = load('spectral_trial_blocks', args.spectral_source)
    t = make_trial(base, spectral, args)
    before, direction, fit = t.baseline_and_direction()
    print(json.dumps(dict(event='spectral_radial_direction', baseline=before, fit=fit)), flush=True)
    report = dict(schema='positive-spectral-Lp-one-radial-map-trial-20261120-v1',
        source_sha256=sha(__file__), radial_source_sha256=sha(args.radial_source), spectral_source_sha256=sha(args.spectral_source),
        parent_sha256=sha(args.bundle), carrier_sha256=sha(args.carrier),
        parameters=t.parameters.as_dict(), minimum_normalized_orbit_weight=t.w_min,
        full_angles=t.o.full_N, evaluated_angles=t.o.N, stages=t.o.P,
        original_rows_retained=True, original_same_g_preserved=True,
        basis_centers=t.basis.centers.tolist(), basis_halfwidths=t.basis.widths.tolist(),
        before=before, linear_fit=fit, trials=[], accepted_trial=None,
        target_scope='Exact composition finite observed objective; no new quintic or geometry certificate',
        other_consumers='Same positive spectral Blocks and NativeLinearization available to complete-space and coarse-QP solvers')
    for j in range(args.line_trials):
        alpha = 2.**(-j); coefficients = alpha*direction
        proof = t.basis.monotonicity(coefficients, t.S_lower, float(t.data['width']))
        item = dict(alpha=alpha, coefficients=coefficients.tolist(), monotonicity=proof, accepted=False)
        if proof['strictly_increasing']:
            trial = t.exact_composition_trial(coefficients)
            item['statistics'] = trial
            item['actual_phi_decreased'] = bool(trial['phi_normalized'] < before['phi_normalized'])
            item['finite_max_decreased'] = bool(trial['max_gram'] < before['max_gram'])
            item['accepted'] = item['actual_phi_decreased'] and item['finite_max_decreased']
        report['trials'].append(item)
        print(json.dumps(dict(event='spectral_radial_trial', alpha=alpha,
            derivative_lower=proof['derivative_lower_approximate'], accepted=item['accepted'], statistics=item.get('statistics'))), flush=True)
        if item['accepted']:
            report['accepted_trial'] = len(report['trials'])-1; break
    report['elapsed_seconds'] = time.monotonic()-start
    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text(json.dumps(report, indent=2)+'\n')
    print(json.dumps(dict(event='spectral_radial_complete', report_sha256=sha(args.out),
        elapsed_seconds=report['elapsed_seconds'], accepted_trial=report['accepted_trial'])), flush=True)


if __name__ == '__main__': main()
